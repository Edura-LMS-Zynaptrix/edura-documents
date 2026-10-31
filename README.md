# EDURA Documents — Requirements, Designs & Project Evidence

This repository contains the specifications, design documents, architectural decisions, and test, security and project evidence for the EDURA LMS project. The source code is in `edura-backend`, `edura-frontend`, `edura-infra` and `edura-tests`.

## Contents

| Location | Contents |
|---|---|
| [srs/](srs/) | Final Software Requirements Specification |
| [sds/](sds/) | Final Software Design Specification (as implemented) |
| [erd/](erd/) | Entity-relationship diagrams, one per service |
| [ADR-12](ADR-12-event-driven-service-communication.md) | Event-driven service communication |
| [ADR-13](ADR-13-azure-deployment-adjustments.md) | Azure deployment adjustments |
| [ADR-14](ADR-14-accepted-dependency-vulnerabilities.md) | Accepted dependency vulnerabilities |
| [ADR-15](ADR-15-documents-repository-single-branch.md) | The documents repository uses `main` only |
| [ADR-16](ADR-16-sprint-scope-and-issue-tracking.md) | Sprint backlog scope, untracked demo activities and sprint capacity |
| [ADR-17](ADR-17-known-security-and-quality-limitations.md) | Known security and quality limitations accepted in the release |
| [standards/](standards/coding-standards.md) | Coding standards: principles, linters and formatters, git workflow, commit convention and code review rules |
| [security/](security/) | OWASP Top 10 checklist and STRIDE threat model |
| [testing/](testing/) | Test register, test case table, endpoint register, test results, coverage report and performance report |
| [retrospectives/](retrospectives/) | Sprint retrospectives |
| [final-report/](final-report/) | Final development report |

## Branching

`main` is the only long-lived branch in this repository (see [ADR-15](ADR-15-documents-repository-single-branch.md)); there is no `develop` branch because the repository holds no code and nothing is deployed from it.

- Work happens on short-lived branches named `feature/<ticket-id>-<slug>` or `fix/<ticket-id>-<slug>`.
- Every change reaches `main` through a pull request with at least one approving review.
- Commit messages follow Conventional Commits and reference the issue, for example `docs(adr): add ADR-15`.
