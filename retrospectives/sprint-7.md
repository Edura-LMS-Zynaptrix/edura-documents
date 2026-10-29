# Sprint 7 Retrospective

**Date written:** 2026-09-07 
**Planned sprint duration:** 4 weeks (2026-08-11 to 2026-09-07), Weeks 9 to 12  
**Sprint Focus:** Integration & UX  
**Attendees:** Nadun Dananjaya (@nadun), Imansha Dilshan (@imansha), Danindu Ransika (@danindu), Thushan Madhusanka (@thushan)  
**Supervisor Review Date:** not recorded  

---

## 1. Executive Summary

Sprint 7 was planned to turn the finished backend (Sprint 6) into a usable product: the first cross-service tests (the end-to-end smoke test, the payment webhook flow, the assessment flow) and the web interfaces for students, administrators and teachers, with a feature freeze at the end of Week 12.

All 10 planned delivery issues (**DDP-#24**, **#26** to **#33** and **#36**) were closed, but **none of them inside the sprint dates**. The first closed on 15 October (38 days after the sprint's due date of 7 September) and the last on 27 October (50 days after). One of the ten, the optional Gemini assistant (**DDP-#36**), was closed as *not planned*. Three of the others were closed with part of their scope missing: the payment UI (**DDP-#28**, PayHere hidden), the progress dashboard (**DDP-#31**, no certificate download page) and the assessment-flow tests (**DDP-#32**, not merged). The Sprint 7 retrospective (**DDP-#51**) is this document.

The interface work was done almost entirely by one developer, in two bursts (12 to 19 September, then 10 to 14 October), and reached the repository as one large pull request on 15 October. The integration tests were merged on 24 October, after the staging deployment pipeline existed. Most of the technical debt this created (no frontend tests, no coverage gate, test counts that did not match the repository, no security review, no staging) was found and fixed in Sprint 8 (Section 3).

---

## 2. Planned versus Actual

### 2.1 What the plan said

| Week | Dates | Planned work |
|---|---|---|
| 9 | 11 to 17 Aug | Integration testing: smoke test (#24), payment webhook flow (#29), assessment flow (#32) |
| 10 | 18 to 24 Aug | UI I: course viewer (#26), assessment UI (#27), payment UI (#28) |
| 11 | 25 to 31 Aug | UI II: admin dashboard (#30), progress dashboard, leaderboard and certificates (#31) |
| 12 | 1 to 7 Sep | Teacher dashboard (#33), optional Gemini assistant (#36); feature freeze |

The plan also assumed a staging URL "live from Week 4" so that the frontend would be built against real APIs, and tests written in the same pull request as the feature.

### 2.2 What happened

| Date | Event |
|---|---|
| 11 Aug to 7 Sep | No frontend or tests-repository commits. Backend and infra work continues (Asgardeo login, payment, enrollment, notification and assessment services merged 18 to 26 Aug; the Nginx and RabbitMQ configuration on 13 Aug). |
| 8 to 27 Sep | The gap the plan left between Sprint 7 and Sprint 8; no sprint was scheduled. |
| 12 to 19 Sep | The frontend is built: project structure, Redux slices, course and exam management, admin screens, video progress, Cloudinary assets. Backend changes for the UI are made in the same days (Google sign-in, profile creation, receipt upload, free enrolment, lesson progress). |
| 10 to 14 Oct | Remaining UI and API work: feedback and bank-account endpoints, analytics fixes, the email verification flow. |
| 15 Oct | Frontend PR #12 ("student and admin screens wired to the backend services") and backend PR #34 ("Implement Core Edura Features Across Microservices") are merged; five UI issues are closed. |
| 15 to 24 Oct | Tests PRs for the smoke test (#6) and the payment webhook flow (#7) wait nine and eight days; the smoke script is realigned with the changed API (#10). |
| 24 Oct | The staging deployment pipeline (Azure Kubernetes Service) is merged in the infra repository; staging goes live. Smoke test and payment tests merged; #24 and #29 closed. |
| 25 Oct | #31 and #36 closed (the Gemini widget as *not planned*). A set of integration tests for notification, payment, progress and user flows (tests PR #11) is opened and closed without merging. |
| 27 Oct | #32 closed. |
| 28 Oct | Live staging integration tests for 8 service flows are merged (DDP-#66, Sprint 8). |

### 2.3 Velocity and work items

| Issue # | Title | Planned window | Est. hours | Owner | Closed | Result | Notes |
|---|---|---|---|---|---|---|---|
| **DDP-#24** | End-to-end smoke test (register, verify, login, enroll, view course) | Week 9 | 3.0 | @all | 24 Oct | Completed late | PR opened 15 Oct, merged 24 Oct; realigned with the changed API in PR #10. Runs after each staging deploy. |
| **DDP-#29** | Integration tests: PayHere webhook flow | Week 9 | 3.0 | @danindu | 24 Oct | Completed late | PR opened 16 Oct, merged 24 Oct. Runs against an in-process mock gateway. |
| **DDP-#32** | Integration tests: full assessment flow | Week 9 | 4.0 | @thushan | 27 Oct | Closed before the tests were merged | The tests for this flow were in PR #11, closed unmerged on 25 Oct. The live assessment-flow tests were merged in Sprint 8 (DDP-#66, 28 Oct). |
| **DDP-#26** | Course content viewer (YouTube, Cloudinary notes, lesson navigation) | Week 10 | 4.0 | @imansha | 15 Oct | Completed late | In PR #12. |
| **DDP-#27** | Assessment UI (timed quiz, MCQ, submission, results, anti-cheat) | Week 10 | 4.0 | @imansha | 15 Oct | Completed late | In PR #12. |
| **DDP-#28** | Payment flow UI (PayHere redirect, receipt upload, status) | Week 10 | 3.0 | @imansha | 15 Oct | Completed, partly | In PR #12. The PayHere option is hidden in the checkout page and uses PayHere's sandbox; the bank deposit is the working method. |
| **DDP-#30** | Admin dashboard (receipts, users, violations, analytics) | Week 11 | 4.0 | @imansha | 15 Oct | Completed late | In PR #12. |
| **DDP-#31** | Progress dashboard, leaderboard, certificate download page | Week 11 | 3.0 | @thushan | 25 Oct | Closed, partly | Dashboard and leaderboard delivered. No certificate page: the backend stores a certificate record only, and no PDF is generated. |
| **DDP-#33** | Teacher dashboard (course, module, lesson, assessment builders) | Week 12 | 4.0 | @imansha | 15 Oct | Completed late | In PR #12. Delivered as screens in the admin panel, not as a separate teacher route. |
| **DDP-#36** | Gemini AI assistant widget (optional) | Week 12 | 3.0 | @imansha | 25 Oct | Not planned | Descoped; the assistant is outside the delivered scope. |
| **DDP-#51** | Sprint 7 retrospective and board velocity | After Week 12 | 1.0 | @all | open | In progress | This document. |
| **Total** | **Sprint 7 work package** | | **36.0** | **Team** | | **10 of 10 closed; 1 not planned; 3 closed with scope missing** | Actual hours not tracked. |

Owner load in the plan: @imansha 22 hours (6 of the 7 UI issues), @thushan 7 hours, @danindu 3 hours, shared 3 hours. @nadun, who owns infrastructure, had no Sprint 7 issue; his staging pipeline work landed on 24 October.

### 2.4 Sprint metrics

- **Issues planned:** 11 (10 delivery issues and the retrospective)
- **Issues closed inside the sprint dates (to 7 Sep):** 0
- **Delivery issues closed:** 10 (9 as completed, 1 as not planned); three of the nine were closed with part of their scope missing (#28 PayHere hidden, #31 certificate page, #32 tests not merged)
- **Days after the due date when the first and last issue closed:** 38 and 50
- **Planned effort:** 36.0 hours; **actual effort:** not recorded
- **Commits in the window (11 Aug to 28 Oct, excluding merges):** frontend 40 (all from 12 Sep), tests 13 (all October), backend 75, infra 29

---

## 3. Problems in Sprint 7 and the Fixes Made in Sprint 8

| # | Problem found in Sprint 7 | Evidence | Fix in Sprint 8 |
|---|---|---|---|
| 1 | **No tests for the frontend and no coverage gate.** The plan said tests and feature code go in the same pull request; the 7 UI issues shipped with none. | The frontend repository had no unit tests until 25 Oct. | DDP-#52 added 854 Jest tests (31 files); DDP-#50 added lint, build, unit-test and security checks to the frontend CI; DDP-#58 enforces an 80% coverage threshold. Frontend coverage is now 98.3% lines and 91.5% branches. |
| 2 | **Backend coverage was not enforced or measured properly.** | No coverage gate in the backend CI. | DDP-#35 added the coverage gate (80% on new code, 90% on auth and payment) and the badge; DDP-#61 covered a missed route; DDP-#63 added branch coverage and excluded test files and migrations from the figures. Backend coverage is 98.6% lines and 97.8% branches; auth_service and payment_service are above 90% on branches. |
| 3 | **Integration tests did not match what the repository held.** #32 was closed before its tests were merged; PR #11 was closed unmerged; the test register counted 274 integration tests while the repository had 5. | Closed issues and PR history in Section 2. | DDP-#66 added 198 live staging integration tests for 8 service flows; DDP-#60 regenerated the test and endpoint registers; DDP-#71 recorded the result of every test (1,850 tests, 1,836 passed at the time, the one failure since fixed). DDP-#54 removed hard-coded secret defaults from the tests. |
| 4 | **The frontend was built without a staging URL and against changing APIs.** The plan promised staging by Week 4; the AKS cluster had been paused to save cost (Sprint 5 retrospective, ADR-13). | Staging went live on 24 Oct. The authentication approach changed (Asgardeo PKCE login, then Google sign-in with the Auth Service's own tokens on 18 Sep), the email verification flow was added on 14 Oct, profile creation became event-driven on 24 Oct. The smoke script had to be realigned (PR #10), and a sign-up profile race was fixed (frontend PR #14). | The staging pipeline (build, push, deploy, health checks) is merged and runs on every push to `develop`; the smoke test runs after each deploy. Service-link variable and gateway rate-limit problems found on first deploy were fixed (infra PRs #26 and #27). The event-driven design is recorded in ADR-12 and the deployment adjustments in ADR-13. |
| 5 | **One large, unreviewed UI pull request.** Six of seven UI issues belonged to one developer, and they reached `develop` as one pull request (PR #12). | 22 of 35 planned hours on one person; frontend feature commits from one author. | A second developer wrote the frontend test suite (DDP-#52) and the pipeline checks (DDP-#50); the coding standards document (DDP-#53) records the review expectations. |
| 6 | **No security or quality review.** | Nothing in Sprint 7 covered OWASP or dependency scanning. | DDP-#34 OWASP sweep and checklist (DDP-#62); security response headers (DDP-#64); lint and dependency scans for the infra and tests pipelines (DDP-#56, DDP-#57); default RabbitMQ account removed (DDP-#73); threat model and ADR-17 for the limitations that were accepted. |
| 7 | **Documentation lagged the work.** The Sprint 5 and 6 retrospectives were merged on 25 Oct and this one is written now; ADR-13 and the coding standards had never been written. | Pull request dates in the documents repository. | DDP-#53 (coding standards), DDP-#55 (ADR-16), DDP-#59 (ADR-13), DDP-#65 (ADR-17), the coverage, OWASP, performance and test-case documents (DDP-#62, #69, #70, #74, #75), and the final development report. |
| 8 | **Issues closed ahead of their delivery.** #31 and #32 were closed with scope missing. | Section 2.3. | Remaining gaps are listed in the final report (limitations LIM-07 to LIM-10) and in ADR-17 instead of being left on closed issues. |

Two problems were found only because Sprint 8 added measurements, not because Sprint 7 caused them: the course service stopped answering under load (performance test, DDP-#70), fixed with health probes and a second replica (DDP-#73); and a gateway route test for the enrolment service had been out of date and never run in CI (DDP-#72).

---

## 4. Went Well

1. **The backend foundation held.** All 11 services and the RabbitMQ topology from Sprint 6 needed no redesign; the UI and the tests were built on the existing APIs.
2. **The planned UI scope was delivered.** The student, administrator and teacher interfaces covering course viewing, assessments, payment, administration and progress all exist and run on staging.
3. **Staging went live and stayed live.** Once the deployment pipeline existed (24 Oct), every merge to `develop` was deployed and checked automatically, and the smoke test runs after each deploy.
4. **A descoping decision was made openly.** The optional Gemini assistant (#36) was closed as *not planned* instead of being left to rot on the board, and recorded as outside the delivered scope.
5. **The first cross-service tests exist and run.** The smoke test and the payment webhook tests proved the event chain from payment to enrolment to content access.

---

## 5. To Improve

1. **Keep sprint dates honest.** The sprint's dates passed with no status change on the board, and the 20-day gap between Sprint 7 and Sprint 8 was not used to catch up. Update milestones and the board when a sprint slips, and hold the retrospective at the end of the sprint, not weeks later.
2. **Spread the work.** Putting six of seven UI issues on one developer made the whole sprint depend on one person's availability. Pair on large features and split pull requests so they can be reviewed.
3. **Close issues only when the acceptance criteria are met.** Closing #31 and #32 with scope missing hid gaps until the final review.
4. **Test with the feature.** Frontend tests and a coverage gate should have been in the first UI pull request, not added three weeks later.
5. **Get a staging environment before the UI work starts.** The plan said Week 4; keeping the cluster paused for cost saved money but pushed all integration problems to the last week. A cheap always-on staging (as now) would have caught the API changes earlier.
6. **Track actual hours.** With no actual hours, velocity cannot be compared with the estimates.

---

## 6. Risk Log Update

| Risk ID | Risk Description | Severity | Observation in Sprint 7 | Mitigation & Status |
|---|---|---|---|---|
| **RSK-05** | Payment gateway downtime or webhook drop | High | The PayHere option is hidden in the checkout page and points to PayHere's sandbox. | Idempotent webhook handling is tested; the bank deposit flow is the working method. Recorded as a limitation (LIM-10 in the final report). |
| **RSK-10** | Schema drift between UI and backend APIs | Medium | Authentication, email verification and profile creation changed between Sep and Oct; the smoke script and a sign-up flow broke. | Live staging integration tests and the smoke test after every deploy catch contract changes. Closed. |
| **RSK-11** | Single-developer bottleneck on the frontend | High | 6 of 7 UI issues on one person; one large pull request. | Open. Pair on large features; second reviewer required. |
| **RSK-12** | Integration delayed until a staging environment exists | High | Staging only from 24 Oct. | Closed: staging pipeline in place. |
| **RSK-13** | Work reported done without evidence (closed issues, unmerged tests) | Medium | #31, #32 and the 274-versus-5 test count. | Closed: registers regenerated, results recorded (DDP-#60, #71). |
| **RSK-14** | Capacity not verified before release | Medium | Found in Sprint 8: a service stalls at about 40 concurrent clients. | Partly mitigated by probes and a second replica (DDP-#73); the 500-user target is not met and is accepted (ADR-17, performance report). |

---

## 7. Action Items (rest of Sprint 8)

| # | Action Item | Owner | Target |
|---|---|---|---|
| 1 | Merge the open documents pull requests (test results, evidence refresh, retrospective, performance, threat model, final report) and re-export the PDFs | @danindu | Before submission |
| 2 | Execute the production deploy with the approval gate and tag `v1.0.0` (**DDP-#40**) | @nadun | Sprint 8 |
| 3 | Submit the final report and close **DDP-#45** and **DDP-#48**; peer evaluations are out of scope | @all | Sprint 8 |
| 4 | Reconcile the project board: set Sprint 7 and Sprint 8 issues to Done or Deferred with a reason; correct the milestone due dates | @all | Sprint 8 |
| 5 | Write the Sprint 8 retrospective | @all | After the demonstration |
| 6 | Add CHANGELOG files to the frontend, infra and tests repositories | To be assigned | Sprint 8 |
| 7 | Add the new CI jobs (Lint & Format, Security Scan, Gateway & Edge Config Tests) to the required status checks of `develop` | Organisation admin | Sprint 8 |

---

## 8. Supervisor Feedback & Review Notes

Not recorded. The supervisor review of Sprint 7 did not take place at the end of the sprint; add the review date and feedback here when it happens.
