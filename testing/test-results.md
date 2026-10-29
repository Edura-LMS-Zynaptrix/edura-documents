# Test Execution Record

Guideline reference: §6.3.3 (Actual Output / Status), §7.2 (Unit Tests stage), §10.1 item 7. The per-test Status is in `test-register.md`; this file records how and when the results were obtained.

- **Date of the runs:** 2026-10-28
- **Run by:** the team, on one developer machine (Python 3.14, Node 22) and against the staging environment.

## Runs

| Suite | Code state | Environment | Command | Result |
|---|---|---|---|---|
| Backend, 11 services | `edura-backend`, branch `feature/DDP-67-gwt-test-naming` | Local; PostgreSQL 16 in Docker (one database per service), as the CI job does | `pytest <service>` with `DATABASE_URL`, `PYTHONPATH=.:<service>` | 857 test results: 855 passed, 1 skipped (enrollment) and 1 expected failure (assessment, xfail); see Notes |
| Frontend | `edura-frontend`, branch `feature/DDP-58-frontend-coverage-gate` | Local, `npm ci` | `npx jest --ci --json` | 1,170 passed, 0 failed (31 files) |
| Infrastructure | `edura-infra`, branch `feature/DDP-64-security-headers` | Local | `pytest nginx/tests rabbitmq/tests` | 10 passed, 1 failed, 3 skipped (they need a live RabbitMQ) |
| Cross-service integration, payment and enrolment | `edura-tests`, branch `feature/DDP-66-staging-integration-tests` | In-process mock gateway (as in CI) | `pytest integration/test_payment_enrollment_flow.py` | 6 passed |
| Cross-service integration, all other services | same | **Staging**, `https://staging.eduralms.com` | `pytest integration/test_*_flow.py` with `STAGING_API_URL` | 197 passed, 1 skipped, 0 failed |
| Cross-service integration, all services including payment and enrolment | `edura-tests` `develop`, plus the payment and enrolment test files from open PR #11 | **Local throwaway stack** (see below) | `pytest integration` with `STAGING_API_URL=http://localhost:8080` | `develop` suite: 201 passed, 1 failed (needs Cloudinary, see Notes), 1 skipped. PR #11 files `test_payment_flow.py` and `test_enrollment_flow.py`: 68 passed |
| UI end-to-end (Playwright) | `edura-tests`, branch `feature/DDP-68-ui-e2e-tests` | **Staging** | `npx playwright test` | 6 passed |

The register counts test functions found in the source (1,850). The runs count every executed instance, so parametrised tests count more than once (for example Jest reports 1,170 results for 854 test definitions). Statuses in the register are matched by file and test name; a test with several instances shows Fail if any failed, otherwise Pass.

## Local throwaway stack (integration tests, payment and enrolment)

Guideline §6.3.2 asks for integration tests "against a test database", and the CI stage spins a test database up and tears it down (§7.2), so these tests were run on a disposable local stack instead of the shared staging database, which would keep payment records because `payment_service` has no delete endpoint.

- All 11 services were built from `edura-backend` `develop` and run in Docker with the gateway's Nginx configuration, a new PostgreSQL 16 container (one database per service), Redis and RabbitMQ.
- Secrets were generated for the run and thrown away afterwards: a random `SECRET_KEY` and fake PayHere credentials (`local_merchant`). No real `.env` file, database or third-party key was used; Cloudinary and Resend were left unset.
- The gateway's rate limit was removed in the local copy of the Nginx configuration so the tests could run at full speed.
- The stack, its volume and the temporary files were deleted after the run.

## Notes

- **One failure:** `nginx/tests/test_nginx_config.py::test_all_11_location_routes_exist` fails. The test is out of date with the gateway configuration (it was already failing before this run) and is not run by the infra CI. It needs its own fix.
- **A test that failed once:** `analytics_service`'s `test_given_students_when_summary_built_then_each_is_listed_with_completion` failed on the first local run (`assert 0 == 50`) and passed on three reruns. It looks dependent on leftover database state or timing; it has not been investigated.
- **Local integration failure:** `test_given_admin_when_request_signed_url_then_returns_url_and_expiry` returned 503 `CLOUDINARY_NOT_CONFIGURED` because the throwaway stack has no Cloudinary credentials. It passes on staging, where they are set.
- **Payment and enrolment tests (PR #11):** the 68 tests in `test_payment_flow.py` and `test_enrollment_flow.py` are not in `develop` yet, so they are not in the register. They passed on the local stack, including the PayHere webhook signature checks. They were not run on staging, which would need its PayHere credentials and would leave payment records behind.
- **Not run in this record:** the end-to-end smoke test `edura-tests/smoke/critical_path.py` (it runs after each staging deploy) and 7 Jest tests whose names are built at run time and so cannot be matched to the register.
- **Playwright tests** are not in the register yet because it is generated from the three repositories' source scan and the Playwright suite is a new folder; their six results are recorded here and in `test-case-table.md`.
- The `edura-backend` code under test includes the unmerged Given-When-Then renames (DDP-#67), so the names in the register are the names after that PR merges. The test logic is unchanged.
- CI is the authoritative run for each merge: every `Verify <service>` job in the Backend CI passes on the DDP-#67 branch (run 40635707724).

## How to repeat

```bash
# results folder with the JUnit XML of each pytest run (--junitxml) and the Jest file (--json --outputFile)
python3 edura-documents/testing/tools/generate_registers.py . --results path/to/results
```
