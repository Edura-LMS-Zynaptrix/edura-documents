# Test Coverage Report

Guideline reference: §6.4 (test coverage requirements), §7.2 (Unit Tests stage generates a coverage report), §8.2 (quality gates), §10.1 item 6.

- **Report date:** 2026-10-27
- **Source:** coverage reports produced by the CI pipelines, not measured by hand.
  - Backend lines: [Backend CI run 40474889384](https://github.com/Edura-LMS-Zynaptrix/edura-backend/actions/runs/40474889384) on `develop` (commit `3778203`), artifacts `coverage-<service>` (`coverage.xml`).
  - Backend branches: [Backend CI run 40614773460](https://github.com/danindu2024/edura-backend/actions/runs/40614773460) on the `feature/DDP-63-backend-branch-coverage` branch, the first run with `--cov-branch` (DDP-#63). The line figures in that run are identical to the `develop` run, so the two sets of numbers describe the same code. Re-export both from `develop` once DDP-#63 is merged.
  - Frontend: [Frontend CI run 40475255079](https://github.com/Edura-LMS-Zynaptrix/edura-frontend/actions/runs/40475255079) (commit `574e385`), artifact `coverage-report` (`lcov.info`).
- **Test inventory:** see `test-register.md` (every test case) and `endpoint-register.md` (every API endpoint).

## Targets (§6.4, §8.2)

| Layer | Required | Measured by |
|---|---|---|
| Unit tests, all new code | 80% (lines / branches) | pytest-cov, Jest |
| API endpoints | 100% have at least one integration test | `endpoint-register.md` |
| Critical business logic | 90% branch coverage | defined in the SDS |

## Backend (pytest-cov, lines and branches)

| Service | Lines covered | Lines total | Line coverage | Branches covered | Branches total | Branch coverage | Test cases |
|---|---|---|---|---|---|---|---|
| admin_service | 910 | 925 | 98.4% | 50 | 56 | 89.3% | 66 |
| analytics_service | 1,610 | 1,631 | 98.7% | 143 | 160 | 89.4% | 97 |
| assessment_service | 2,892 | 2,914 | 99.2% | 308 | 324 | 95.1% | 141 |
| auth_service | 1,486 | 1,505 | 98.7% | 133 | 142 | 93.7% | 88 |
| content_service | 626 | 639 | 98.0% | 51 | 60 | 85.0% | 37 |
| course_service | 1,800 | 1,822 | 98.8% | 174 | 188 | 92.6% | 81 |
| enrollment_service | 1,221 | 1,269 | 96.2% | 145 | 158 | 91.8% | 65 |
| notification_service | 807 | 827 | 97.6% | 44 | 52 | 84.6% | 38 |
| payment_service | 1,017 | 1,028 | 98.9% | 51 | 58 | 87.9% | 44 |
| progress_service | 960 | 977 | 98.3% | 103 | 110 | 93.6% | 36 |
| user_service | 1,445 | 1,463 | 98.8% | 143 | 156 | 91.7% | 85 |
| **Total** | **14,774** | **15,000** | **98.5%** | **1,345** | **1,464** | **91.9%** | **778** |

Every service is above the 80% target for lines and for branches.

**Critical business logic (§6.4: 90% branch coverage).** `auth_service` reaches **93.7%**. `payment_service` reaches **87.9%**, which is **below the 90% target**: 7 of its 58 branches are not exercised. Overall backend branch coverage is 91.9%. `content_service` (85.0%) and `notification_service` (84.6%) are the lowest services but are not named as critical logic.

## Frontend (Jest)

| Metric | Covered | Total | Coverage |
|---|---|---|---|
| Lines | 7,187 | 7,315 | 98.3% |
| Branches | 4,078 | 4,455 | 91.5% |
| Functions | 2,097 | 2,161 | 97.0% |

The frontend has 854 test cases in 31 test files. Lines, branches and functions are all above 80%, and branches (91.5%) are above the 90% branch target.

## Other suites

| Suite | Test cases | What it checks |
|---|---|---|
| `edura-tests/integration` | 5 | Payment and enrolment flow, against an in-process mock gateway |
| `edura-tests/smoke` | 1 | End-to-end critical path on staging, run after each staging deploy |
| `edura-infra` | 12 | Nginx configuration and RabbitMQ topology |
| **Total, all suites** | **1,650** | |

## How coverage is enforced in CI

| Repository | Gate | Where |
|---|---|---|
| edura-backend | Coverage on changed lines of a pull request must be at least 80% (`diff-cover`); the report is uploaded as an artifact | `ci.yml`, job `verify-service` |
| edura-frontend | Overall coverage must be at least 80% (Jest `coverageThreshold`); changed lines of a pull request must be at least 80% (`diff-cover`) | `jest.config.js`, `ci.yml` (DDP-#58, pending merge when this report was written) |

## Test results

All test jobs in the two runs linked above passed (every `Verify <service>` job in the backend run and the Unit Tests job in the frontend run). The test register's `Status` column stays blank because it is generated from source; the execution record is the CI run history.

## Gaps

| # | Gap | Suggested action |
|---|---|---|
| 1 | `payment_service` branch coverage is 87.9%, below the 90% target for critical logic | Add tests for the 7 uncovered payment branches (new tests only, no code change) |
| 1a | Branch coverage is collected from the DDP-#63 branch, not yet from `develop` | Merge DDP-#63, then re-export both runs from `develop` |
| 2 | No performance test results (guideline §10.1 item 9) and no load tests in the repositories | Run a load test against staging and add `performance-report` |
| 3 | The report is a snapshot of one CI run | Re-export after the last merge before submission |
| 4 | Report is Markdown; the deliverable list asks for HTML or PDF | Export to PDF as `coverage-sprint8.pdf` for the final submission |
