# Sprint 6 Retrospective

**Date:** 2026-08-10  
**Sprint Duration:** 4 weeks (2026-07-14 to 2026-08-10) — Weeks 5–8  
**Sprint Focus:** Core Features  
**Attendees:** Nadun Dananjaya (@nadun), Imansha Dilshan (@imansha), Danindu Ransika (@danindu), Thushan Madhusanka (@thushan)  
**Supervisor Review Date:** 2026-08-11  

---

## 1. Executive Summary

Sprint 6 focused on feature implementation and unit testing across all business domains of the EDURA Learning Management System. The team transitioned from architectural infrastructure to functional microservice endpoints, domain logic, event-driven messaging, and initial client interface integration.

All 11 planned issues (**DDP-#13** through **DDP-#17**, **DDP-#19** through **DDP-#23**, and **DDP-#49**) were successfully completed. All 11 microservices were validated live in the containerized Docker Compose environment, with active connections to their respective Neon PostgreSQL cloud databases, Redis cache, RabbitMQ event bus, and Nginx reverse proxy. Every service endpoint is operational and responding with `{"status":"ok"}` on `GET /health`.

---

## 2. Went Well

1. **Parallel Feature Implementation Across Discrete Microservices:**
   - The architectural decoupling established in Sprint 5 enabled all four developers to build their assigned services in parallel without merge conflicts or implementation bottlenecks:
     - **Course Service (DDP-#13):** Implemented Course → Module → Lesson hierarchy with teacher ownership checks and `course.published` event emission.
     - **Content Service (DDP-#14):** Delivered time-limited Cloudinary signed URLs (1-hour expiration) and secure YouTube embed token generation with MIME/magic-number file validation.
     - **Payment Service (DDP-#15):** Integrated PayHere checkout initiation, HMAC-SHA256 webhook signature validation, idempotency via unique transaction IDs, and manual bank receipt upload to cloud storage.
     - **Enrollment Service (DDP-#16):** Implemented access grant/suspension lifecycle listening to payment and subscription events.
     - **Assessment Service (DDP-#17):** Built timed quiz sessions using Redis, automated MCQ/True-False grading, and browser tab-switch anti-cheat violation tracking.
     - **Progress Service (DDP-#19):** Engineered lesson watch tracking, course completion percentage calculation (BR-004), and Redis sorted-set leaderboard caching.
     - **Notification Service (DDP-#20):** Built pure RabbitMQ consumer dispatching templated transactional emails for OTP, payment confirmations, and course certificates.
     - **Admin Service (DDP-#21):** Delivered receipt verification dashboards, user role assignment endpoints, and audit logging.
     - **Analytics Service (DDP-#23):** Built aggregation queries and PDF/Excel report exports using ReportLab and openpyxl.

2. **Event-Driven Asynchronous Topology in Practice:**
   - Verified end-to-end messaging across the `edura.events` RabbitMQ topic exchange:
     - `payment.success` triggers immediate enrollment creation in `enrollment_service` and confirmation email dispatch in `notification_service`.
     - `assessment.graded` and `lesson.watched` trigger real-time progress calculations in `progress_service`.
     - `auth.otp-requested` triggers instant notification delivery.

3. **Live Containerized Stack Verification:**
   - All 14 containers (11 FastAPI services, Redis 7, RabbitMQ 3.12, and Nginx) are healthy and active locally.
   - All 11 microservice endpoints successfully resolved and tested through the Nginx reverse proxy on port 80 (`http://localhost/api/*`).

4. **Frontend Initial Milestones (DDP-#22):**
   - Stood up initial Next.js pages (Login, Registration, Student Dashboard, Course Catalog) wired to the staging API Gateway with Redux Toolkit for authentication and session state.

---

## 3. To Improve

1. **Inter-Service Event Tracing & Local Debugging:**
   - Debugging asynchronous workflows across multiple independent consumers (e.g. tracing a payment webhook event to enrollment and notification queues) was initially challenging without centralized logging.
   - *Resolution:* Added structured JSON logging with correlation IDs (`X-Correlation-ID`) across inter-service HTTP calls and RabbitMQ message headers.

2. **Third-Party Service Mocking:**
   - Developing offline with external APIs (PayHere gateway, Cloudinary, Asgardeo) caused delays when developers lacked sandbox credentials.
   - *Resolution:* Created mock fallback modes and fixture servers in each service for offline unit and integration testing.

3. **Frontend-Backend Contract Alignment:**
   - Encountered minor property naming discrepancies (e.g., camelCase in TypeScript vs. snake_case in Pydantic v2 schemas) during initial Next.js page integrations.
   - *Resolution:* Enforced OpenAPI schema exports and strict TypeScript contract generation before frontend feature development.

4. **Materialized View Refresh Timing:**
   - Analytics Service aggregations were running directly against transactional data during testing.
   - *Resolution:* Implemented cached query summaries in Redis to maintain fast response times under dashboard load.

---

## 4. Strategic Risk Log & Governance

| Risk ID | Risk Description | Severity | Trigger / Observation | Mitigation & Strategic Decision |
|---|---|---|---|---|
| **RSK-05** | Third-party payment gateway downtime or webhook drop | High | PayHere sandbox delays during high concurrency testing. | Implemented idempotency checks on `transaction_id` and an asynchronous reconciliation task in Payment Service. Provided fallback manual bank receipt upload for admin verification. |
| **RSK-08** | Message broker queue overflow on consumer failure | Medium | If `notification_service` drops connection, unacknowledged messages accumulate in RabbitMQ. | Configured RabbitMQ dead-letter exchange (`edura.dlx`) and exponential backoff retry in consumer loops. |
| **RSK-10** | Schema drift between UI and backend APIs | Medium | Discrepancies between React form data and FastAPI Pydantic models. | Bound all frontend API clients to generated TypeScript interfaces matching FastAPI `/openapi.json` specifications. |

---

## 5. Velocity & Work Items Breakdown

| Issue # | Title | Estimated Hours | Actual Hours | Status | Owner | Notes |
|---|---|---|---|---|---|---|
| **DDP-#13** | Course Service: full CRUD, teacher ownership, RabbitMQ publish | 5.0h | 5.5h | Completed | @imansha | Implemented course, module, lesson CRUD; emits `course.published`. |
| **DDP-#14** | Content Service: Cloudinary signed URL + YouTube embed token | 3.0h | 3.0h | Completed | @imansha | 1-hour signed Cloudinary URL; MIME and magic-number validation. |
| **DDP-#15** | Payment Service: PayHere checkout + HMAC webhook + receipt upload | 5.0h | 5.5h | Completed | @danindu | PayHere HMAC verification; idempotency via transaction key. |
| **DDP-#16** | Enrollment Service: RabbitMQ consumer for payment.success | 3.0h | 3.0h | Completed | @danindu | Asynchronously activates course access on `payment.success`. |
| **DDP-#17** | Assessment Service: MCQ/TF quiz CRUD + timed session + anti-cheat | 5.0h | 5.5h | Completed | @thushan | Redis timer session, tab-switch violation logging, auto-grade. |
| **DDP-#19** | Progress Tracking: watch-status, completion %, leaderboard (Redis) | 4.0h | 4.5h | Completed | @thushan | Completion rules (BR-004), Redis sorted-set leaderboard. |
| **DDP-#20** | Notification Service: RabbitMQ consumer + SMTP email dispatch | 3.0h | 3.0h | Completed | @thushan | Jinja2 email templates for OTP, payment, and certificates. |
| **DDP-#21** | Admin Service: receipt verification dashboard + audit log | 3.0h | 3.5h | Completed | @danindu | Receipt approval/rejection endpoints with audit trail. |
| **DDP-#22** | Next.js: Login, Register, Student Dashboard, Course Catalog | 5.0h | 6.0h | Completed | @imansha | Connected to live APIs via Nginx gateway; Redux auth slice. |
| **DDP-#23** | Analytics Service: aggregation queries + PDF/Excel report endpoints | 4.0h | 4.5h | Completed | @thushan | Revenue summary, course metrics, ReportLab PDF export. |
| **DDP-#49** | Sprint 6 Retrospective & update GitHub Project board velocity | 1.0h | 1.0h | Completed | @all | Documented retrospective and reconciled project board. |
| **Total** | **Sprint 6 Work Package** | **41.0h** | **45.0h** | **100% Done** | **Team** | **11 / 11 issues completed** |

---

## 6. Sprint Metrics

- **Issues Planned:** 11
- **Issues Completed:** 11 (100% completion rate)
- **Unfinished Items Carried Over:** 0
- **Total Estimated Effort:** 41.0 hours
- **Total Actual Effort:** 45.0 hours
- **Sprint Velocity:** 45.0 hours across 11 completed user stories / tasks
- **Service Availability:** 11 / 11 services returning HTTP 200 `{"status":"ok"}` on `GET /health`
- **Docker Compose Stack Health:** 14 / 14 containers running and healthy
- **Test Pass Rate:** 100% across unit and integration test suites

---

## 7. Action Items for Sprint 7 (Integration & UX)

| # | Action Item | Owner | Target Due Date |
|---|---|---|---|
| 1 | Build comprehensive end-to-end integration test suite covering the full learner enrollment and assessment lifecycle (**DDP-#24**) | @danindu | Sprint 7, Week 9 |
| 2 | Complete Next.js Course Content Viewer with YouTube embed and notes download (**DDP-#26**) | @imansha | Sprint 7, Week 9 |
| 3 | Build Next.js Assessment Quiz Player with Redis timer and anti-cheat tab-switch detection (**DDP-#27**) | @thushan | Sprint 7, Week 10 |
| 4 | Implement Teacher Course Builder & Lesson Editor UI in Next.js (**DDP-#28**) | @imansha | Sprint 7, Week 10 |
| 5 | Build Payment Checkout & PayHere Redirection UI flow with bank slip upload fallback (**DDP-#29**) | @danindu | Sprint 7, Week 11 |
| 6 | Build Admin Dashboard UI with pending receipt approval table and analytics charts (**DDP-#30**) | @imansha | Sprint 7, Week 11 |
| 7 | Prepare for **Feature Freeze Declaration** at the end of Sprint 7 (no new features after Week 12) | @all | Sprint 7, Week 12 |

---

## 8. Supervisor Feedback & Review Notes
