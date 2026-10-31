# Sprint 8 Retrospective

**Date written:** 2026-10-25; updated 2026-10-31 after the production release  
**Planned sprint duration:** 4 weeks (2026-09-28 to 2026-10-23), Weeks 13 to 16  
**Sprint Focus:** Testing, hardening, release and documentation  
**Attendees:** Nadun Dananjaya (@nadun), Imansha Dilshan (@imansha), Danindu Ransika (@danindu), Thushan Madhusanka (@thushan)  
**Supervisor Review Date:** not recorded  

---

## 1. Executive Summary

Sprint 8 was planned as the testing, fixing and release sprint: unit-test coverage, a security sweep, a demonstration walk-through on staging, production manifests and a production deployment tagged `v1.0.0`, and the final documents.

Almost all of the sprint's work was done between 24 and 31 October, after the planned end date of 23 October. The sprint plan lists 14 items for Sprint 8 (DDP-#34, #35 and #37 to #48). Five of them (#38, #43, #44, #46, #47: the P1 bug fixes, two demonstration rehearsals, the pre-demo verification and the live demonstration) were never created as GitHub issues (ADR-16). Of the nine that were: **six were closed as completed** (#34, #35, #39, #42, #45, #48), **one was closed as completed without evidence** (the production seed data, #41), **one was closed as not planned** (the demonstration walk-through, #37), and **the production deployment and `v1.0.0` tag (#40) were completed on 31 October**. About 25 further issues that were not in the plan (tests, CI, security headers, documents) were opened and closed during the sprint.

What the sprint achieved: the backend and the frontend now have test suites that match their documentation and CI gates for coverage (backend 98.6% lines and 97.8% branches, 778 tests; frontend 98.3% lines and 91.5% branches, 854 tests), live integration tests, UI tests and a performance report, an OWASP review, a threat model, security response headers, a RabbitMQ account that is no longer `guest`, and the final SRS, SDS and development report as PDFs.

The production deployment was completed late, on 31 October: a second AKS node, a static IP and DNS for `eduralms.com`, separate secrets, the deploy pipeline with its approval gate, and `v1.0.0` tagged with a GitHub Release in the four code repositories. Production uses the original Neon databases and the PayHere sandbox; staging is still on the same databases until its Neon branches are created.

What it did not achieve: 500 concurrent users (NFR-009), a certificate PDF, the Gemini assistant and Excel export, and a demonstration walk-through that was recorded as an issue.

One defect was introduced by a Sprint 8 change and found on 29 October, after the sprint: replacing the RabbitMQ `guest` account (DDP-#73) left the notification and progress consumers connecting without credentials, so staging sent no e-mail until backend issue #58 fixed it (Section 3).

---

## 2. Planned versus Actual

### 2.1 What the plan said

The sprint plan schedules Sprint 8 as a two-week run of days (Days 9 to 14) and does not assign the items to calendar weeks:

| Plan item | Planned work |
|---|---|
| DDP-#34, #35 | OWASP Top 10 sweep; unit-test coverage to at least 80% overall and 90% on auth and payment |
| DDP-#37, #38 | Demonstration walk-through on staging with failures logged as bugs; fix the P1 bugs |
| DDP-#39, #40, #41 | Production manifests; production deploy with the approval gate and `v1.0.0`; production seed data |
| DDP-#42 | Fix P2 bugs; coverage report, test register, OWASP checklist and CHANGELOG |
| DDP-#43, #44, #46, #47 | Two demonstration rehearsals; pre-demo verification; the live demonstration |
| DDP-#45, #48 | Final report Chapters 4 and 5; submit the final report |

The plan also said that Sprint 8 is for testing, fixes and demo preparation only, after the Week 12 feature freeze.

### 2.2 What happened

| Date | Event |
|---|---|
| 28 Sep to 23 Oct | The planned sprint dates. The repositories show almost no Sprint 8 work in this window; Sprint 7's interface work was merged on 15 October and staging went live on 24 October. |
| 24 Oct | Staging pipeline merged in the infra repository; staging goes live. |
| 25 Oct | Frontend unit test suite (DDP-#52); Sprint 5 and 6 retrospectives and ADR-12 merged. |
| 26 Oct | Backend coverage work (DDP-#35) and the OWASP sweep (DDP-#34) closed; production manifests issue (#39) closed. |
| 27 Oct | Frontend CI checks (DDP-#50), test environment file (DDP-#54), P2 bug and documents issue (#42) closed; the demonstration walk-through (#37) closed as not planned. |
| 28 Oct | Live staging integration tests (DDP-#66), Playwright UI tests (DDP-#68), performance tests and report (DDP-#70), lint and security stages for infra and tests (DDP-#56, #57), security headers (DDP-#64), gateway test fix (DDP-#72), probes, second replica and RabbitMQ account (DDP-#73), branch coverage (DDP-#63), Given-When-Then test names (DDP-#67), and the ADRs, standards and OWASP documents. |
| 29 Oct | Final SRS (#44), final SDS (#46), final report and the test, OWASP and coverage PDFs merged or updated; required status checks and branch protection set on all repositories; CHANGELOG files added to all four code repositories; e-mail on staging found broken and fixed (backend #58); retrospective for Sprint 7 merged. |
| 31 Oct | A review of the repositories against the development guideline found the gaps listed in Section 3.1. The frontend coverage badge was fixed (DDP-#81) and a new advisory in `follow-redirects` that failed the frontend security scan was resolved by updating the package; the documents README was corrected (DDP-#82). The release branches `release/v1.0.0` were merged to `main` in the backend, frontend, infra and tests repositories, production was deployed from `main` through the approval gate, and `v1.0.0` was tagged and released. |

### 2.3 Work items

| Issue # | Title | Closed | Result | Notes |
|---|---|---|---|---|
| **DDP-#35** | Unit test coverage to at least 80% and 90% on auth and payment | 26 Oct | Completed late | Backend coverage gate and badge added. |
| **DDP-#34** | OWASP Top 10 compliance sweep | 26 Oct | Completed late | OWASP checklist (DDP-#62) and ADR-17 for the accepted limitations. |
| **DDP-#37** | Demonstration walk-through on staging, log failures as bugs | 27 Oct | Not planned | Closed without being done as an issue; the automated smoke, integration and UI tests were added instead. |
| **DDP-#42** | Fix P2 bugs and generate the final deliverable documents | 27 Oct | Completed late | Coverage report, OWASP checklist and CHANGELOG files delivered through other issues. |
| **DDP-#39** | Kubernetes manifests for production | 26 Oct | Completed late | `k8s/production` and a deploy job gated by a `production` environment with required reviewers. The gate was used for the 31 October deployment. |
| **DDP-#41** | Seed the production database with demo accounts and content | 26 Oct | Closed as completed, no evidence | The plan expected `infra/scripts/seed_production.py`; the repository contains no seed or demo-data script. Treat as not delivered. On 31 October production was pointed at the original Neon databases, which hold the data seeded for staging, so no separate seed was needed. |
| **DDP-#40** | Production deploy, approval gate and `v1.0.0` | 31 Oct | Completed late | Deployed from `main` through the approval gate; 18 pods running, nine public health routes return 200, HTTPS valid. The rollback was not demonstrated and the smoke check on production was run by hand (the automated smoke job runs on staging only). |
| **DDP-#45** | Final report Chapters 4 and 5 | 29 Oct | Completed late | Final report merged; corrected export in DDP-#80. |
| **DDP-#48** | Submit final report; commit final retrospective | 29 Oct | Completed | Peer evaluations are submitted individually on eKelaniya. |
| **DDP-#38, #43, #44, #46, #47** | P1 bug fixes, two rehearsals, pre-demo verification, live demonstration | not created | Not tracked | Activities without a deliverable (ADR-16). |

Most of the work was done under issues created during the sprint (DDP-#50 to DDP-#82); 41 issues across the five repositories carry the Sprint 8 milestone, and all 41 were closed by 31 October. They are listed by repository in the changelogs. Estimates and actual hours were not recorded for them.

### 2.4 Sprint metrics

- **Plan items:** 14, of which 9 became GitHub issues
- **Planned issues closed inside the sprint dates (to 23 Oct):** 0
- **Planned issues:** 7 completed (#34, #35, #39, #40, #42, #45, #48), 1 closed as completed without evidence (#41), 1 not planned (#37)
- **Issues with the Sprint 8 milestone:** 41, all closed by 31 October (backend 7, frontend 4, infra 7, tests 6, documents 17)
- **Commits since 28 Sep, excluding merges:** backend 48, frontend 33, infra 15, tests 14
- **Tests:** backend 778; frontend 854; live integration 198; the registers record 1,850 test cases (see the test register)
- **Coverage:** backend 98.6% lines, 97.8% branches; frontend 98.3% lines, 91.5% branches
- **Actual effort:** not recorded

---

## 3. Problems in Sprint 8

| # | Problem | Evidence | Action |
|---|---|---|---|
| 1 | **The sprint's work was done after the sprint.** The first issue closed on 25 October, two days after the planned end. | Section 2.2. | Hold the review at the sprint's end and move the dates on the board when a sprint slips. |
| 2 | **A security change broke e-mail on staging, and no test noticed.** DDP-#73 replaced the RabbitMQ `guest` account with an `edura` account, but three connections (the notification consumer, the progress consumer and the certificate publisher) opened a connection without credentials. The broker refused them (`ACCESS_REFUSED`), so no verification, reset or payment e-mail was sent and progress events were not consumed. Locally it still worked, because Docker Compose still has `guest`. | Pod log of the notification service on 29 October; fixed by backend PR #59 (issue #58). | Unit tests mock `pika`, and the smoke test does not check that e-mail arrives. Add a check that the notification consumer is connected after each deploy, and run local tests with the same credentials as staging. |
| 3 | **Issues closed without evidence.** #41 (production seed data) is closed as completed with no script in the repository; #37 was closed as not planned. | Section 2.3. | Close issues only when the acceptance criteria are met and link the evidence. |
| 4 | **The performance requirement is not met.** One `course-service` pod stopped answering at roughly 10 to 20 concurrent clients; after probes and a second replica it handles about 20 without errors and times out at 40. NFR-009 asks for 500. | Performance report (Tests 3 and 4). | Accepted and recorded in ADR-17 and the final report. Not fixed: more replicas on a larger node, a higher CPU limit, paging or caching of the course list. |
| 5 | **Several features of the SRS were not built.** Gemini assistant, Excel export, certificate PDF, backup job, payment reconciliation. | Final report, limitations; ADR-17. | Recorded as limitations. |
| 6 | **Documents drifted from the code.** The first versions of the final SRS and report described OTP-based verification, synchronous calls, a PKCE login and correlation IDs that the code does not have. | Corrected in DDP-#76, #77 and #80. | Check document claims against the code before submission; keep the change lists (SRS, SDS Chapter 9). |
| 7 | **Documentation and tracking were written at the end.** Retrospectives for Sprints 5 to 7 were merged between 25 and 29 October. | Pull request dates in the documents repository. | Write the retrospective in the last week of each sprint. |

Smaller points: the required status checks for `develop` were only set on 29 October; the production-deployment steps (second node, IP, DNS, secrets) needed an organisation admin and were done on 31 October.

### 3.1 Gaps found in the review against the guideline (31 October)

| Gap | Guideline | Status |
|---|---|---|
| Frontend coverage badge showed "unknown" (Codecov was never fed) | §9.3, App. C | Fixed (DDP-#81, frontend #26) |
| New high-severity advisory in `follow-redirects` failed the frontend security scan | §8.2 | Fixed by updating to 1.16.2; two allow-list entries removed (DDP-#81) |
| Documents README listed files that do not exist and lacked the ADR-15 note | §9.3 | Fixed (DDP-#82, documents #50) |
| No account lockout, no authentication-event log, emails in logs, fallback `SECRET_KEY`, default bcrypt cost, no Python lock file | §8.1 A02, A07, A08, A09 | Not fixed; accepted in ADR-17 |
| Refresh-token reuse does not end the user's other sessions; rotation is not safe against concurrent requests | §4.3.1 (AC3, AC4) | Not fixed; not yet in ADR-17 |
| Webhook signature compared with `==` | §8.1 A02 | Not fixed |
| No Kubernetes network policies (threat T17) | §8.1 A05 | Not fixed |
| No Content-Security-Policy; no injection-payload test; 22 accepted frontend advisories (20 after the update above) | §8.1 A03, A05, A06 | Not fixed; recorded in the OWASP checklist and ADR-14 |
| The threat model is not in the SDS | §8.1 A04 | Open; the SDS source document was not available to edit |
| Staging and production use the same original Neon databases | SDS §8.4 | Open until the staging branches are created |
| ADR-14 and the OWASP checklist still show 22 accepted advisories | §8.1 A06 | To be updated |

---

## 4. Went Well

1. **Testing caught up.** Backend, frontend, integration, UI and performance tests now exist, and the registers and coverage figures can be reproduced from the repositories.
2. **Quality gates are in place.** Lint, build, unit-test and security checks run on every repository; coverage gates (80% on new code, 90% on auth and payment) and required status checks protect `develop` and `main`.
3. **Security review was done and recorded.** OWASP checklist, threat model, security headers, removal of the default RabbitMQ account and a dependency scan, with the remaining limitations written down in ADR-17.
4. **The documents were reconciled with the code.** The SRS, SDS and report were rewritten as implemented, with the diagrams redrawn and the differences from the first versions listed.
5. **Staging worked as the delivery environment.** Every merge to `develop` is deployed and smoke-tested, and the demonstration can run on a deployed URL.
6. **A defect was found and fixed within a day of being noticed.** The RabbitMQ credentials problem was traced to three connections, fixed with a regression test and deployed.
7. **The release followed the guideline's flow.** Release branches, a CHANGELOG per repository, pull requests to `main`, a deployment that waited for a required reviewer, and `v1.0.0` tags with GitHub Releases.
8. **A review against the guideline was done before submission.** It produced a written list of gaps (Section 3.1), three of which were fixed the same day.

---

## 5. To Improve

1. **Start the release work earlier.** The production deployment was left until the day of the retrospective update. Provision the production environment (node, IP, DNS, databases, secrets) while the code is still changing.
2. **Do not ship a security change without a runtime check.** Test the deployed system after changing credentials, not only the unit tests.
3. **Close issues on evidence.** Link the pull request or file when closing, and reopen issues closed without it.
4. **Track hours and dates.** Actual hours were never recorded in Sprints 7 and 8, and the board dates drifted.
5. **Keep the plan and the issue list in step.** The plan listed 10 issues and the sprint needed about 34; create the issues before the work, as ADR-16 says.
6. **Spread the infrastructure work.** Production steps that need organisation admin rights depended on one or two people.

---

## 6. Risk Log Update

| Risk ID | Risk Description | Severity | Observation in Sprint 8 | Mitigation & Status |
|---|---|---|---|---|
| **RSK-11** | Single-developer bottleneck on the frontend | High | The test suite and CI checks for the frontend were written by a second developer. | Partly mitigated. Review rules are in the coding standards. |
| **RSK-14** | Capacity not verified before release | Medium | NFR-009 not met on staging (about 20 concurrent clients per service). | Accepted (ADR-17); probes and a second replica added. |
| **RSK-15** | A change to credentials or configuration breaks a consumer silently | High | The e-mail consumers could not connect for the time between DDP-#73 and backend #58. | Fixed; add a post-deploy check that the consumers are connected. Open. |
| **RSK-16** | Production deployment not done before the demonstration | Medium | Production was deployed on 31 October. | Closed. Staging and production share databases until the staging branches exist; see RSK-17. |
| **RSK-17** | Staging tests change production data | High | Production uses the original Neon databases that staging also uses. | Do not run the integration, UI or load tests against staging until the staging branches are created. Open. |

---

## 7. Action Items

| # | Action Item | Owner | Target |
|---|---|---|---|
| 1 | Create the staging branches of the 11 Neon databases and point staging at them (production keeps the originals) | To be assigned | Before the demonstration |
| 2 | Add a rollback demonstration and an automated read-only smoke check for production | To be assigned | Before the demonstration |
| 3 | Add a post-deploy check that the notification consumer is connected and that a verification e-mail is accepted | To be assigned | Before the demonstration |
| 4 | Confirm that the demo accounts and content are still in the production databases after the staging branches are created (production uses the original databases, which staging has seeded) | To be assigned | Before the demonstration |
| 5 | Update ADR-13, the SDS, the final report, ADR-14 and the OWASP checklist now that production is live; add the threat model to the SDS | @all | Before submission |
| 6 | Reconcile the project board: set remaining cards to Done or Deferred, and correct the milestone due dates | @all | Before submission |
| 7 | Submit the individual peer evaluations on eKelaniya | Each student | Before the deadline |
| 8 | Decide which gaps in Section 3.1 are fixed before submission and which are recorded in ADR-17 | @all | Before submission |

---

## 8. Supervisor Feedback & Review Notes

Not recorded. The supervisor review for Sprint 8 has not taken place at the time of writing; add the review date and feedback here when it happens.
