#!/usr/bin/env python3
"""Export the evidence documents to PDF (guideline 10.1 items 6 to 9).

Usage (from edura-documents):

    pip install markdown
    CHROME=/path/to/chrome-or-headless_shell python3 testing/tools/export_pdfs.py

Converts each Markdown file to HTML with a print stylesheet and prints it to PDF
with headless Chromium (`--print-to-pdf`). Set CHROME to a Chrome, Chromium or
Playwright `headless_shell` binary. Re-run it after the last merge, so the PDFs
match the Markdown.
"""

import os
import pathlib
import subprocess
import sys
import tempfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parents[2]
# (Markdown source, PDF name required by the deliverables list, or a supporting document)
DOCUMENTS = [
    ("testing/coverage-report.md", "testing/coverage-sprint8.pdf"),
    ("testing/test-register.md", "testing/test-register.pdf"),
    ("security/owasp-checklist.md", "security/owasp-checklist.pdf"),
    ("testing/performance-report.md", "testing/performance-report.pdf"),
    ("testing/test-case-table.md", "testing/test-case-table.pdf"),
    ("testing/test-results.md", "testing/test-results.pdf"),
    ("security/threat-model.md", "security/threat-model.pdf"),
]

CSS = """
@page { size: A4 landscape; margin: 14mm; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 9.5pt; line-height: 1.4; color: #1a1a1a; }
h1 { font-size: 18pt; border-bottom: 2px solid #0f766e; padding-bottom: 4px; }
h2 { font-size: 13pt; margin-top: 18px; color: #0f766e; }
h3 { font-size: 11pt; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #c9c9c9; padding: 3px 6px; vertical-align: top; text-align: left; overflow-wrap: break-word; }
th { background: #eef6f5; }
td:first-child, th:first-child { white-space: nowrap; }
code { font-family: Consolas, monospace; font-size: 8.5pt; background: #f3f3f3; padding: 0 2px; }
pre { background: #f3f3f3; padding: 6px; overflow-wrap: anywhere; white-space: pre-wrap; }
"""


def render(md_path, pdf_path, chrome):
    body = markdown.markdown(md_path.read_text(encoding="utf8"), extensions=["tables", "fenced_code"])
    html = f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>"
    with tempfile.TemporaryDirectory() as tmp:
        page = pathlib.Path(tmp) / "doc.html"
        page.write_text(html, encoding="utf8")
        subprocess.run(
            [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
             f"--print-to-pdf={pdf_path}", page.as_uri()],
            check=True, capture_output=True, timeout=300,
        )


def main():
    chrome = os.environ.get("CHROME")
    if not chrome:
        sys.exit("Set CHROME to a Chrome, Chromium or headless_shell binary.")
    for source, target in DOCUMENTS:
        if not (ROOT / source).exists():
            print(f"skipped {source} (not in this branch)")
            continue
        render(ROOT / source, ROOT / target, chrome)
        print(f"{source} -> {target}")


if __name__ == "__main__":
    main()
