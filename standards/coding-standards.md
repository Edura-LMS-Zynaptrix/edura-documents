# EDURA Coding Standards

Applies to all code in `edura-backend`, `edura-frontend`, `edura-infra` and `edura-tests`.
Source: Development Guideline (SENG 34213), Chapters 3 and 5.

## 1. Principles

All code must follow:

1. **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.
2. **DRY**: extract shared logic into utilities or services (for the backend, the `shared` package).
3. **YAGNI**: implement only what the current sprint's acceptance criteria require.
4. **Clean Code**: meaningful names, small single-purpose functions, minimal side effects, no magic numbers.

## 2. Language-Specific Standards

| Area | Language | Style guide | Linter / formatter | Config file (repo root) |
|---|---|---|---|---|
| `edura-backend` | Python 3.12 | PEP 8 | Ruff (lint) + Black (format) | `pyproject.toml` |
| `edura-frontend` | TypeScript / JavaScript | ESLint (`next/core-web-vitals`, `eslint:recommended`, `plugin:react/recommended`) + Prettier | ESLint + Prettier | `.eslintrc.json`, `.prettierrc` |
| `edura-tests` | Python | PEP 8 | Ruff + Black (same settings as backend) | follow backend `pyproject.toml` |
| `edura-infra` | YAML, Dockerfile, shell | Keep files small and commented | none mandated | n/a |

### 2.1 Python (backend, tests)

- Line length 88, target `py312`.
- Ruff rule sets enabled: `E`, `W`, `F`, `I` (isort), `C` (comprehensions), `B` (bugbear). `shared` is configured as first-party for import sorting.
- Ignored rules, kept as configured: `B008`, `E501`, `B904`, `E402`.
- Use type hints on public functions.
- Run before every commit: `ruff check .` and `black .`

### 2.2 TypeScript / JavaScript (frontend)

- Prettier: semicolons, single quotes, 2-space indent, print width 80, ES5 trailing commas.
- `no-unused-vars` is a warning; do not merge new warnings without a reason.
- Run before every commit: `npm run lint` and `npm run format:check`

### 2.3 Naming

| Item | Convention |
|---|---|
| Python modules, functions, variables | `snake_case` |
| Python classes | `PascalCase` |
| Constants | `UPPER_SNAKE_CASE` |
| React components and TS types | `PascalCase` |
| TS variables and functions | `camelCase` |
| Files (frontend) | match the component name for components, `kebab-case` otherwise |

## 3. Git Workflow

### 3.1 Branches

| Branch | Purpose |
|---|---|
| `main` | Production-ready, protected, tagged with a SemVer version on each release |
| `develop` | Integration branch; features merge here first |
| `feature/<ticket-id>-<slug>` | One branch per GitHub issue, e.g. `feature/42-user-auth` |
| `fix/<ticket-id>-<slug>` | Bug fixes, e.g. `fix/67-login-token-expiry` |
| `hotfix/<slug>` | Emergency fixes branched from `main` |
| `release/<version>` | Release preparation (version bump, changelog, smoke tests) |

- Feature branches are short-lived. A branch open for more than **5 working days** without a PR must be split into smaller issues.
- `edura-documents` uses a single `main` branch (see ADR-15).

### 3.2 Versioning

Releases are tagged `vMAJOR.MINOR.PATCH`: MAJOR for breaking API or data model changes, MINOR for backwards-compatible features, PATCH for backwards-compatible fixes.

| Sprint | Release |
|---|---|
| Sprint 5 | `v0.1.0` |
| Sprint 6 | `v0.2.0` |
| Sprint 7 | `v0.3.0` |
| Sprint 8 | `v1.0.0` |

### 3.3 Commit messages (Conventional Commits)

Format: `type(scope): short summary`, then an optional body and footer (`Closes #54`, `Refs ADR-07`).

| Type | Use when |
|---|---|
| `feat` | New feature (MINOR) |
| `fix` | Bug fix (PATCH) |
| `test` | Adding or updating tests |
| `ci` | CI/CD pipeline configuration |
| `build` | Build system or dependency changes |
| `perf` | Performance improvement |
| `refactor` | Restructuring without feature or fix |
| `docs` | Documentation |
| `chore` | Housekeeping (tooling, configs) |
| `style` | Formatting only |
| `revert` | Reverting a previous commit |

Example:

```
feat(auth): implement JWT refresh token rotation

Implements sliding-window refresh token strategy as specified in
SDS Section 4.3.2.

Closes #54
Refs ADR-07
```

## 4. Code Review

Every PR needs at least **one approving review** before merging. Reviewers assess:

| Dimension | Question |
|---|---|
| Correctness | Does the code do what the ticket specifies? Do all acceptance-criteria tests pass? |
| Readability | Can a new team member understand it without the author's help? |
| Architecture | Is it consistent with the SDS and agreed architecture? |
| Test quality | Do tests check behaviour rather than implementation? |
| Security | Hardcoded secrets? SQL injection risk? Unvalidated input? |
| Performance | N+1 queries? Blocking calls in async code? |
| Error handling | Are all error cases handled and surfaced meaningfully? |

### Comment etiquette

- Authors do not resolve a reviewer's comment; the reviewer resolves it after verifying the change.
- Reviewers prefix comments with:
  - `[blocker]:` must be fixed before merge
  - `[suggestion]:` recommended, not mandatory
  - `[question]:` asking for clarification
  - `[nit]:` minor style preference

## 5. Security Basics

- Never commit secrets. Commit `.env.example` with placeholder values; keep real `.env` files out of git.
- Validate all external input at the API boundary.
- Any significant deviation from the approved SDS needs a new ADR, reviewed with the supervisor within one sprint.

## 6. Definition of Done (code)

- Lint and format checks pass with no new warnings.
- CI is green on the PR.
- Tests are added or updated for the change.
- At least one approving review.
- Linked issue is referenced in the PR (`Closes #<n>`).
