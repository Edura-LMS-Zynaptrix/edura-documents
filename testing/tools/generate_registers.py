#!/usr/bin/env python3
"""Regenerate the test case register and the API endpoint register.

Usage (from the folder that holds all the edura-* clones):

    python3 edura-documents/testing/tools/generate_registers.py .

Reads the current source of edura-backend, edura-tests, edura-infra and
edura-frontend and writes, next to this script's parent folder:

    testing/test-register.md      every test case (guideline 6.3.3, index form)
    testing/endpoint-register.md  every API endpoint and the tests that call it
                                  (guideline 6.4)

Static analysis only: no tests are run, so Status / Actual Output stay blank
until a run is recorded. Standard library only.
"""

import ast
import collections
import datetime
import os
import re
import sys

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
# Endpoints whose test builds the whole URL in a helper, which static analysis cannot
# read. Each entry was checked by hand: (service, METHOD, route path) -> test name.
MANUAL_COVERAGE = {
    ("course_service", "DELETE", "/{course_id}/modules/{module_id}"):
        "test_delete_module_clears_its_children",
}
SKIP_DIRS = {"node_modules", ".git", ".next", "__pycache__", ".pytest_cache",
             ".ruff_cache", "alembic", ".venv"}


def walk(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            yield os.path.join(dirpath, name)


def humanise(name):
    text = re.sub(r"^test_?", "", name).replace("_", " ").strip()
    return text[:1].upper() + text[1:] if text else name


# --------------------------------------------------------------------------
# Python tests
# --------------------------------------------------------------------------
ANY_PREFIX = "\x00"  # marks a path that starts with an unresolved expression


def str_pattern(node, env, first=True):
    """Regex for a string / f-string / constant / concatenation, or None."""
    if isinstance(node, ast.Name):
        return str_pattern(env[node.id], env, first) if node.id in env else None
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return re.escape(node.value)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = str_pattern(node.left, env, first)
        right = str_pattern(node.right, env, False)
        if left is None:
            left = ANY_PREFIX if first else "[^/?]+"
        return left + right if right is not None else None
    if isinstance(node, ast.JoinedStr):
        parts = []
        for index, v in enumerate(node.values):
            if isinstance(v, ast.Constant):
                parts.append(re.escape(str(v.value)))
                continue
            resolved = str_pattern(v.value, env, first and index == 0) \
                if isinstance(v.value, (ast.Name, ast.Constant, ast.BinOp)) else None
            if resolved is not None:
                parts.append(resolved)
            elif first and index == 0:
                parts.append(ANY_PREFIX)
            else:
                parts.append("[^/?]+")
        return "".join(parts)
    return None


def http_calls(func, module_env):
    """(METHOD, path-regex) for every HTTP client call inside a function."""
    env = dict(module_env)
    for n in ast.walk(func):
        if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                and isinstance(n.targets[0], ast.Name) \
                and isinstance(n.value, (ast.Constant, ast.JoinedStr, ast.BinOp)):
            env[n.targets[0].id] = n.value
    calls = []
    for n in ast.walk(func):
        if not (isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)):
            continue
        attr = n.func.attr
        if attr in HTTP_METHODS and n.args:
            pattern = str_pattern(n.args[0], env)
            if pattern:
                calls.append((attr.upper(), pattern))
        elif attr == "request" and len(n.args) >= 2 \
                and isinstance(n.args[0], ast.Constant):
            pattern = str_pattern(n.args[1], env)
            if pattern:
                calls.append((str(n.args[0].value).upper(), pattern))
    # Test helpers such as _post("/upload-material", ...) or _upload_zip("/x", ...):
    # the HTTP method is guessed from the helper's name, so the match is "probable".
    for n in ast.walk(func):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name) \
                and n.func.id.startswith("_") and n.args:
            method = helper_method(n.func.id)
            pattern = str_pattern(n.args[0], env)
            if method and pattern and pattern.lstrip(ANY_PREFIX).startswith(("/", "\\/")):
                calls.append((method, pattern if pattern.startswith(ANY_PREFIX)
                              else ANY_PREFIX + pattern))
    return calls


def helper_method(name):
    lowered = name.lower()
    for word, method in (("upload", "POST"), ("post", "POST"), ("delete", "DELETE"),
                         ("patch", "PATCH"), ("put", "PUT"), ("get", "GET")):
        if word in lowered:
            return method
    return None


def scan_python_tests(path):
    """Yield dicts for each test function; also return all HTTP calls in file."""
    try:
        tree = ast.parse(open(path, encoding="utf8", errors="ignore").read())
    except SyntaxError:
        return [], []
    module_env = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                and isinstance(node.targets[0], ast.Name) \
                and isinstance(node.value, (ast.Constant, ast.JoinedStr, ast.BinOp)):
            module_env[node.targets[0].id] = node.value
    tests, file_calls = [], []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            file_calls.extend(http_calls(node, module_env))

    def visit(body, cls):
        for node in body:
            if isinstance(node, ast.ClassDef):
                visit(node.body, node.name)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                    and node.name.startswith("test_"):
                doc = ast.get_docstring(node)
                tests.append({
                    "class": cls or "–",
                    "name": node.name,
                    "desc": (doc.strip().splitlines()[0] if doc else humanise(node.name)),
                    "calls": http_calls(node, module_env),
                })

    visit(tree.body, None)
    return tests, file_calls


# --------------------------------------------------------------------------
# Frontend (Jest) tests
# --------------------------------------------------------------------------
JS_TITLE = r"""(['"`])((?:\\.|(?!\1).)*)\1"""


def scan_js_tests(path):
    tests, stack = [], []
    lines = open(path, encoding="utf8", errors="ignore").read().splitlines()
    for number, line in enumerate(lines):
        if re.match(r"\s*(?:it|test)\.each\(.*\)\(\s*$", line) and number + 1 < len(lines):
            m = re.match(r"\s*" + JS_TITLE, lines[number + 1])
            if m:
                tests.append({"class": stack[0][1] if stack else "–",
                              "name": m.group(2), "desc": m.group(2)})
            continue
        indent = len(line) - len(line.lstrip())
        while stack and stack[-1][0] >= indent:
            stack.pop()
        m = re.match(r"\s*describe(?:\.each\([^)]*\))?\(\s*" + JS_TITLE, line)
        if m:
            stack.append((indent, m.group(2)))
            continue
        m = re.match(r"\s*(?:it|test)(?:\.each\([^)]*\))?\(\s*" + JS_TITLE, line)
        if m:
            tests.append({
                "class": stack[0][1] if stack else "–",
                "name": m.group(2),
                "desc": m.group(2),
            })
    return tests


# --------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------
def kw_str(call, key):
    for kw in call.keywords:
        if kw.arg == key and isinstance(kw.value, ast.Constant):
            return str(kw.value.value)
    return ""


def service_routes(service_dir):
    """Return [(METHOD, path, handler)] for one backend service."""
    modules = {}
    for path in walk(service_dir):
        rel = os.path.relpath(path, service_dir)
        if not path.endswith(".py") or rel.startswith("tests") or "/tests/" in rel:
            continue
        try:
            modules[os.path.splitext(os.path.basename(path))[0]] = ast.parse(
                open(path, encoding="utf8", errors="ignore").read())
        except SyntaxError:
            continue

    own_prefix, routes_by_router = {}, collections.defaultdict(list)
    for mod, tree in modules.items():
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
                fn = node.value.func
                name = fn.id if isinstance(fn, ast.Name) else getattr(fn, "attr", "")
                if name in ("APIRouter", "FastAPI") and isinstance(node.targets[0], ast.Name):
                    own_prefix[(mod, node.targets[0].id)] = kw_str(node.value, "prefix")
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) \
                            and dec.func.attr in HTTP_METHODS \
                            and isinstance(dec.func.value, ast.Name) and dec.args \
                            and isinstance(dec.args[0], ast.Constant):
                        routes_by_router[(mod, dec.func.value.id)].append(
                            (dec.func.attr.upper(), str(dec.args[0].value), node.name))

    # include_router(prefix=...) in any module, resolving imported aliases
    include_prefix = {}
    for mod, tree in modules.items():
        alias = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module:
                for a in node.names:
                    alias[a.asname or a.name] = (node.module.split(".")[-1], a.name)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                    and node.func.attr == "include_router" and node.args \
                    and isinstance(node.args[0], ast.Name):
                name = node.args[0].id
                key = alias.get(name, (mod, name))
                include_prefix[key] = kw_str(node, "prefix")

    out = []
    for key, routes in routes_by_router.items():
        prefix = include_prefix.get(key, "") + own_prefix.get(key, "")
        for method, path, handler in routes:
            out.append((method, (prefix + path) or "/", handler))
    return sorted(set(out), key=lambda r: (r[1], r[0]))


def route_regex(path):
    """Regex for a route template such as /courses/{course_id}/lessons."""
    parts = re.split(r"(\{[^}]+\})", path.rstrip("/") or "/")
    pattern = ""
    for part in parts:
        if part.startswith("{"):
            pattern += ".+" if part.endswith(":path}") else "[^/]+"
        else:
            pattern += re.escape(part)
    return re.compile("^" + pattern + "/?$")


def concrete(pattern):
    """Turn a call's path regex back into a sample path (query string removed)."""
    path = pattern.replace("[^/?]+", "x")
    path = re.sub(r"\\(.)", r"\1", path)
    return path.split("?")[0]


def call_match(route_path, rx, method, call):
    """'exact', 'probable' (matched only by the path's tail) or None."""
    call_method, pattern = call
    if call_method != method:
        return None
    path = concrete(pattern)
    if path.startswith(ANY_PREFIX):
        tail = path[1:].rstrip("/")
        norm = re.sub(r"\{[^}]+\}", "x", route_path).rstrip("/")
        return "probable" if len(tail) > 1 and norm.endswith(tail) else None
    if rx.match(path):
        return "exact"
    if path.startswith("/api/"):  # tests that go through the gateway prefix
        for cut in (3, 2):
            if rx.match("/" + path.split("/", cut)[-1]):
                return "exact"
    return None


def best(route_path, rx, method, calls):
    states = {call_match(route_path, rx, method, c) for c in calls}
    return "exact" if "exact" in states else ("probable" if "probable" in states else None)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def md_escape(text):
    return text.replace("|", "\\|")


def main(base):
    docs_testing = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))
    today = datetime.date.today().isoformat()
    suites = []  # (title, [rows])

    backend = os.path.join(base, "edura-backend")
    services = sorted(d for d in os.listdir(backend)
                      if d.endswith("_service") and os.path.isdir(os.path.join(backend, d)))
    service_tests = {}
    for svc in services:
        rows, file_calls = [], {}
        tdir = os.path.join(backend, svc, "tests")
        for path in walk(tdir) if os.path.isdir(tdir) else []:
            if not path.endswith(".py") or not os.path.basename(path).startswith("test_"):
                continue
            rel = "edura-backend/" + os.path.relpath(path, backend)
            tests, calls = scan_python_tests(path)
            file_calls[rel] = calls
            is_api = bool(calls)
            base_name = os.path.basename(path)
            for t in tests:
                if base_name == "test_migrations.py":
                    kind, prio = "Migration", "P2"
                elif is_api:
                    kind, prio = "Integration (API)", "P1"
                else:
                    kind, prio = "Unit", "P2"
                rows.append({**t, "type": kind, "prio": prio, "file": rel})
        service_tests[svc] = (rows, file_calls)
        suites.append((f"Backend – {svc}", rows))

    cross = []
    for path in walk(os.path.join(base, "edura-tests", "integration")):
        if os.path.basename(path).startswith("test_") and path.endswith(".py"):
            tests, _ = scan_python_tests(path)
            rel = "edura-tests/" + os.path.relpath(path, os.path.join(base, "edura-tests"))
            cross += [{**t, "type": "Integration (cross-service)", "prio": "P1", "file": rel} for t in tests]
    suites.append(("Cross-service integration (edura-tests/integration)", cross))

    infra = []
    for path in walk(os.path.join(base, "edura-infra")):
        if path.endswith(".py") and os.path.basename(path).startswith("test_"):
            tests, _ = scan_python_tests(path)
            rel = "edura-infra/" + os.path.relpath(path, os.path.join(base, "edura-infra"))
            infra += [{**t, "type": "Config", "prio": "P2", "file": rel} for t in tests]
    suites.append(("Infrastructure (edura-infra)", infra))

    smoke = []
    for path in walk(os.path.join(base, "edura-tests", "smoke")):
        if path.endswith(".py"):
            tests, _ = scan_python_tests(path)
            rel = "edura-tests/" + os.path.relpath(path, os.path.join(base, "edura-tests"))
            smoke += [{**t, "type": "E2E", "prio": "P1", "file": rel} for t in tests]
    suites.append(("End-to-end smoke (edura-tests/smoke)", smoke))

    front = []
    fe_root = os.path.join(base, "edura-frontend")
    for path in walk(os.path.join(fe_root, "src")):
        if re.search(r"\.test\.(ts|tsx|js|jsx)$", path):
            rel = "edura-frontend/" + os.path.relpath(path, fe_root)
            front += [{**t, "type": "Unit", "prio": "P2", "file": rel} for t in scan_js_tests(path)]
    suites.append(("Frontend – Jest (edura-frontend)", front))

    # ---- test register ----
    total = sum(len(rows) for _, rows in suites)
    out = [
        "# Complete Test Case Register", "",
        f"Generated: {today} · Source: static scan of the test code in the repositories "
        "(`testing/tools/generate_registers.py`) · Guideline: development guideline §6.3.3 / §6.4", "",
        "## Summary", "", "| Layer / suite | Test cases |", "|---|---|",
    ]
    out += [f"| {title} | {len(rows)} |" for title, rows in suites]
    out += [f"| **Total** | **{total}** |", "", "Notes:", "",
            "- This register lists only tests that exist in the repositories on the date above. "
            "Re-run `testing/tools/generate_registers.py` after tests are added or removed.",
            "- Type: `test_migrations` → Migration; backend test files that send HTTP requests to the "
            "FastAPI app → Integration (API); other backend tests → Unit; `edura-tests/integration` → "
            "Integration (cross-service); `edura-infra` → Config; `edura-tests/smoke` → E2E; "
            "`edura-frontend` Jest tests → Unit.",
            "- Priority: P1 for integration and end-to-end tests, P2 for unit, migration and config tests.",
            "- **Description** is the test's docstring if present, otherwise its humanised name. For "
            "frontend tests it is the `it(...)` title and **Class** is the top-level `describe(...)`.",
            "- **Status** is blank until the suite is executed; this register was generated from source "
            "and no test run was done. Record *Actual Output* and *Status* per §6.3.3 after a run.",
            "- This register is the index of test cases. The fields it does not hold (related requirement, "
            "preconditions, input, expected and actual output) still have to be written, in the §6.3.3 "
            "format, for the key cases in the development report appendix.",
            "- The endpoint-level register is in `endpoint-register.md`.", ""]
    counter = 0
    for title, rows in suites:
        out += [f"## {title}", "",
                "| TC ID | Type | Priority | Class | Test | Description | Test file | Status |",
                "|---|---|---|---|---|---|---|---|"]
        for r in rows:
            counter += 1
            out.append(f"| TC-{counter:04d} | {r['type']} | {r['prio']} | {md_escape(r['class'])} | "
                       f"`{md_escape(r['name'])}` | {md_escape(r['desc'])} | `{r['file']}` | |")
        out.append("")
    with open(os.path.join(docs_testing, "test-register.md"), "w", encoding="utf8") as fh:
        fh.write("\n".join(out))

    # ---- endpoint register ----
    sections, summary = [], []
    grand = covered_total = 0
    for svc in services:
        routes = service_routes(os.path.join(backend, svc))
        rows, file_calls = service_tests[svc]
        lines = []
        counts = collections.Counter()
        for method, path, handler in routes:
            rx = route_regex(path)
            direct, probable = collections.Counter(), collections.Counter()
            for t in rows:
                state = best(path, rx, method, t["calls"])
                if state == "exact":
                    direct[t["file"]] += 1
                elif state == "probable":
                    probable[t["file"]] += 1
            helper = {rel for rel, calls in file_calls.items()
                      if rel not in direct and rel not in probable
                      and best(path, rx, method, calls)}
            if direct:
                state_text, files = "Yes", direct
            elif probable or helper:
                state_text, files = "Probable", probable or collections.Counter({f: 0 for f in helper})
            else:
                state_text, files = "**No**", collections.Counter()
            manual = MANUAL_COVERAGE.get((svc, method, path))
            if manual:
                state_text, files = "Yes", collections.Counter()
            counts[state_text] += 1
            where = (f"`{manual}` (checked by hand)" if manual else None) or ", ".join(
                f"`{f.split('/')[-1]}`" + (f" ({n})" if n else " (helper)")
                for f, n in files.most_common(3)) or "–"
            lines.append(f"| {method} | `{path}` | `{handler}` | {state_text} | {where} |")
        grand += len(routes)
        summary.append((svc, len(routes), counts["Yes"], counts["Probable"]))
        covered_total += counts["Yes"] + counts["Probable"]
        sections += [f"## {svc}", "", "| Method | Path | Handler | Tested | Test file (direct tests) |",
                     "|---|---|---|---|---|"] + lines + [""]
    pct = 100 * covered_total / grand if grand else 0
    head = ["# API Endpoint Register", "",
            f"Generated: {today} · Source: FastAPI routes in `edura-backend` and the HTTP calls in the "
            "service tests (`testing/tools/generate_registers.py`) · Guideline §6.4: every endpoint must "
            "have at least one integration test", "", "## Summary", "",
            "| Service | Endpoints | Tested | Probably tested | No test found |", "|---|---|---|---|---|"]
    head += [f"| {s} | {n} | {c} | {p} | {n - c - p} |" for s, n, c, p in summary]
    yes_total = sum(c for _, _, c, _ in summary)
    prob_total = sum(p for _, _, _, p in summary)
    head += [f"| **Total** | **{grand}** | **{yes_total}** | **{prob_total}** | **{grand - covered_total}** |", "",
             "Notes:", "",
             "- Paths are as defined in each service (the gateway adds its own `/api/...` prefix, see "
             "`edura-infra/nginx/nginx.conf`).",
             "- *Yes*: a test sends a request with that method to a matching path. *Probable*: the test "
             "builds the start of the path with a helper, so only the end of the path could be matched "
             "(or the call is made in a shared helper function); confirm these by hand. **No**: no "
             "matching call was found; this is a static match, so check each row by hand before "
             "concluding the endpoint is untested.",
             "- *Test file (direct tests)* shows the files whose tests call the endpoint, with the number "
             "of tests in brackets.", ""]
    with open(os.path.join(docs_testing, "endpoint-register.md"), "w", encoding="utf8") as fh:
        fh.write("\n".join(head + sections))

    print(f"test cases: {total}")
    for title, rows in suites:
        print(f"  {len(rows):4}  {title}")
    print(f"endpoints: {grand}, yes {yes_total}, probable {prob_total}, no {grand - covered_total}")
    for s, n, c, p in summary:
        print(f"  {s:22} yes {c:2} probable {p:2} no {n - c - p:2}  / {n}")


if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "."))
