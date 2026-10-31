# EDURA Documents — Requirements, Designs & Project Evidence

This repository contains the specifications, design documents, architectural decisions, and test, security and project evidence for the EDURA LMS project. The source code is in `edura-backend`, `edura-frontend`, `edura-infra` and `edura-tests`.

## Deployed application

| Environment | URL |
|---|---|
| Staging | https://staging.eduralms.com |
| Production | https://eduralms.com |

The application is built from four code repositories: [edura-backend](https://github.com/Edura-LMS-Zynaptrix/edura-backend), [edura-frontend](https://github.com/Edura-LMS-Zynaptrix/edura-frontend), [edura-infra](https://github.com/Edura-LMS-Zynaptrix/edura-infra) and [edura-tests](https://github.com/Edura-LMS-Zynaptrix/edura-tests).

## CI, coverage and setup

This repository holds documents only: no code, no pipeline and no deployment (see ADR-15), so it has no CI or coverage badge. The badges are on the [edura-backend](https://github.com/Edura-LMS-Zynaptrix/edura-backend#readme) and [edura-frontend](https://github.com/Edura-LMS-Zynaptrix/edura-frontend#readme) READMEs, and the coverage results are in [testing/coverage-report.md](testing/coverage-report.md).

Nothing needs to be installed or run to read the documents. They are Markdown files; the PDF versions are regenerated with `testing/tools/export_pdfs.py`.

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
