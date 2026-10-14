# Sprint 5 Retrospective

**Date:** 2026-07-13  
**Sprint Duration:** 4 weeks (2026-06-16 to 2026-07-13) — Weeks 1–4  
**Sprint Focus:** Foundation & Infrastructure  
**Attendees:** Nadun Dananjaya (@nadun), Imansha Dilshan (@imansha), Danindu Ransika (@danindu), Thushan Madhusanka (@thushan)  
**Supervisor Review Date:** 2026-07-14  

---

## 1. Executive Summary

Sprint 5 was dedicated to establishing the core architectural foundation, repository scaffolding, continuous integration (CI) pipelines, container orchestration, data layer schemas, shared authentication/authorization modules, and cloud deployment pipelines for the EDURA Learning Management System. 

All 14 planned issues (**DDP-#01** through **DDP-#12**, **DDP-#18**, and **DDP-#25**) were successfully completed. Following the successful staging verification on Azure Kubernetes Service (AKS) in **DDP-#18**, the team performed a strategic risk and cost assessment. To prevent unsustainable recurring cloud expenses, all provisioned cloud resources (AKS cluster and active container instances) were gracefully deprovisioned after validating cluster health and deployment manifests. All development and integration testing will continue locally via the multi-container Docker Compose environment until the final deployment sprint (Sprint 8), at which point the system will be deployed to the cloud in one consolidated release.

---

## 2. Went Well

1. **Multi-Service Container Orchestration:**
   - Designed and stood up a unified `docker-compose.yml` orchestrating all 11 FastAPI microservices, PostgreSQL (with multi-database initialization), Redis, RabbitMQ, and Nginx reverse proxy.
   - Provided the team with an identical, reproducible local development environment accessible via Nginx at `http://localhost/api/*`.

2. **Automated CI/CD Pipeline & Matrix Verification:**
   - Configured GitHub Actions CI workflows (`ci.yml`) featuring parallel matrix testing across all 11 backend microservices.
   - Built-in automated checks for linting (`ruff`, `black`), dependency vulnerability scanning (`pip-audit`), and isolated database integration tests using dedicated containerized PostgreSQL instances.

3. **Data Layer & Migration Rigor:**
   - Translated the System Design Specification (SDS §3.2) ER model into SQLAlchemy ORM models across all services.
   - Created Alembic migration revisions per service, accompanied by automated pytest fixtures that verify upgrade, downgrade, and re-upgrade cycles against test databases on every push.

4. **Event-Driven Messaging Setup:**
   - Established the RabbitMQ topology script (`rabbitmq/setup.py`) that idempotently configures the `edura.events` topic exchange and binding queues (`notification.queue`, `enrollment.queue`, `progress.queue`).
   - Verified idempotency and automated topology provisioning via GitHub Actions.

5. **Shared Security & Authentication Baseline:**
   - Implemented Asgardeo OAuth2 PKCE flow, Redis session storage, and 6-digit OTP generation/validation with 93% test coverage in `auth_service`.
   - Engineered the centralized `@require_role` decorator in `shared/auth.py`, enabling immediate RBAC integration across all downstream microservices.

6. **End-to-End Staging Verification on AKS:**
   - Successfully provisioned Azure AKS and Azure Container Registry (ACR), built and pushed container images, applied staging Kubernetes manifests (`k8s/staging/`), and confirmed all pods achieved `Running` state with green `/health` checks.

---

## 3. To Improve

1. **Cloud Resource Expenditure vs. Budget Constraints:**
   - Keeping a live AKS cluster with multiple nodes running 24/7 incurs continuous billing that exceeds the budget allocated for this academic project.
   - *Resolution:* Validated deployment automation once, then terminated cloud infrastructure. Shifted day-to-day integration and verification to Docker Compose until the release phase.

2. **Early Dependency Version Drift:**
   - Encountered initial CI pipeline failures due to conflicting library versions (notably `python-multipart` requirements in FastAPI form handling and deprecation warnings with `python-jose`).
   - *Resolution:* Standardized on `PyJWT` for JWT operations and pinned stable FastAPI/Pydantic v2 versions across all 11 service `requirements.txt` files.

3. **Multi-Repository Checkout Complexity in CI:**
   - Orchestrating cross-repo paths (`edura-backend`, `edura-infra`, `edura-frontend`) required careful path realignment in GitHub Actions runners.
   - *Resolution:* Documented exact directory hierarchy conventions and added automated fallback path resolution steps in CI scripts.

4. **Local Hardware Resource Footprint:**
   - Running all 11 services and backing stores concurrently requires ~4–6 GB of RAM, occasionally slowing down lower-spec developer machines.
   - *Resolution:* Configured Docker Compose profiles and selective service launch capabilities for isolated service feature development.

---

## 4. Strategic Pivot & Risk Management: Cloud Cost Optimization

| Risk ID | Risk Description | Severity | Trigger / Observation | Mitigation & Strategic Decision |
|---|---|---|---|---|
| **RSK-04** | Cloud hosting cost overrun on Azure AKS/ACR | High | AKS cluster node runtime costs accumulate rapidly even during idle periods between reviews. | **Terminated Cloud Infrastructure Post-Verification:** Completed DDP-#18 by deploying and verifying staging health on AKS. Once health was proven, the cluster was deprovisioned. All development and testing through Sprints 6 and 7 will leverage local Docker Compose. Cloud deployment will be executed in Sprint 8 (deployment phase) all at once, saving substantial cloud credits. |
| **RSK-07** | Inconsistent environment between local and staging | Medium | Divergence between local Docker runs and Kubernetes manifests. | Maintained mirrored environment variables, network topologies, and health check definitions between `docker-compose.yml` and Kubernetes manifests. CI runs docker smoke tests on each push to develop. |
| **RSK-11** | Auth middleware adoption bottleneck | Medium | Downstream services delayed while waiting for RBAC patterns. | Delivered `shared/auth.py` with standalone mockable unit test fixtures, unblocking Sprint 6 developers to implement endpoints with `@require_role` immediately. |

---

## 5. Velocity & Work Items Breakdown

| Issue # | Title | Estimated Hours | Actual Hours | Status | Owner | Notes |
|---|---|---|---|---|---|---|
| **DDP-#01** | Create all repos, branch protections, .env.example, README shells | 2.0h | 2.0h | Completed | @nadun | All 5 repos created; branch protection on `main` and default `develop` configured. |
| **DDP-#02** | Docker Compose with all 11 services + infra (postgres, redis, rabbitmq, nginx) | 3.0h | 3.5h | Completed | @nadun | Full stack starts cleanly; Nginx gateway routes requests to respective service ports. |
| **DDP-#03** | GitHub Actions CI pipeline skeleton (lint + build + unit test stages) | 3.0h | 3.0h | Completed | @nadun | CI matrix configured across services with Ruff, Black, and pip-audit stages. |
| **DDP-#04** | AI-generate all 11 FastAPI service skeletons (main, router, models, schemas, database) | 4.0h | 4.0h | Completed | @all | Skeletons committed with working GET `/health` endpoints and Alembic configs. |
| **DDP-#05** | GitHub Project board: extend SENG 31242 board, Sprint 5 milestone, all labels, columns | 1.5h | 1.5h | Completed | @all | 6 Kanban columns set up with Phase, Epic, and Priority custom fields. |
| **DDP-#06** | All SQLAlchemy ORM models across all 11 services (from SDS ER diagram) | 4.0h | 4.5h | Completed | @all | Translated SDS §3.2 ER diagram into models; verified foreign key relationships. |
| **DDP-#07** | All Alembic migration files + pytest fixture verifying migrations run cleanly | 3.0h | 3.5h | Completed | @danindu, @thushan | Autogenerated migrations per service; test fixture confirms clean upgrade & downgrade. |
| **DDP-#08** | RabbitMQ exchanges, queues, and routing keys setup script | 2.5h | 2.5h | Completed | @danindu | `setup.py` declared topic exchange `edura.events` and 3 queues; verified idempotency. |
| **DDP-#09** | Nginx routing config: all 11 service upstream blocks + location paths | 2.0h | 2.0h | Completed | @nadun | Upstream routing, CORS headers, and 100 req/min rate limiting configured. |
| **DDP-#10** | Auth Service: Asgardeo OAuth flow, JWT middleware, session management, OTP | 5.0h | 5.5h | Completed | @nadun | Fully implemented with Redis OTP/sessions; achieved 93% test coverage. |
| **DDP-#11** | User Service: CRUD endpoints + RBAC middleware shared decorator | 4.0h | 4.0h | Completed | @imansha | User CRUD and shared `@require_role` dependency in `shared/auth.py` finalized. |
| **DDP-#12** | Azure AKS cluster provisioned + ACR registry created + kubectl configured | 3.0h | 3.0h | Completed | @nadun | AKS and ACR provisioned; verified cluster access and hello-world deployment. |
| **DDP-#18** | GitHub Actions: build all Docker images, push to ACR, deploy to AKS staging | 4.0h | 4.5h | Completed | @nadun | Staging verified; resources subsequently terminated to conserve budget. |
| **DDP-#25** | Sprint 5 retrospective and update GitHub Project board velocity | 1.0h | 1.0h | Completed | @all | Documented retrospective and reconciled GitHub project board. |
| **Total** | **Sprint 5 Work Package** | **38.0h** | **44.5h** | **100% Done** | **Team** | **14 / 14 issues completed** |

---

## 6. Sprint Metrics

- **Issues Planned:** 14
- **Issues Completed:** 14 (100% completion rate)
- **Unfinished Items Carried Over:** 0
- **Total Estimated Effort:** 38.0 hours
- **Total Actual Effort:** 44.5 hours
- **Sprint Velocity:** 44.5 hours across 14 completed user stories / tasks
- **CI Pipeline Pass Rate:** 96.2% (stabilized to 100% across develop branch pushes)
- **Unit & Integration Test Coverage:**
  - `auth_service`: 93% coverage
  - `shared/auth.py`: 100% coverage
  - Alembic migrations: 100% pass rate
  - RabbitMQ topology idempotency: 100% pass rate

---

## 7. Action Items for Sprint 6

| # | Action Item | Owner | Target Due Date |
|---|---|---|---|
| 1 | Standardize developer environment setup guide and container restart scripts in `edura-infra` | @nadun | Sprint 6, Week 5 (Day 1) |
| 2 | Implement Course Service full CRUD, Module/Lesson hierarchy, and RabbitMQ events (**DDP-#17**) | @thushan | Sprint 6, Week 6 |
| 3 | Implement Content Service Cloudinary upload signatures and YouTube embed security (**DDP-#19**) | @danindu | Sprint 6, Week 6 |
| 4 | Implement Payment Service with PayHere gateway integration and webhook verification (**DDP-#15**) | @danindu | Sprint 6, Week 7 |
| 5 | Implement Enrollment Service and progress tracking listeners (**DDP-#16**, **DDP-#20**) | @imansha | Sprint 6, Week 7 |
| 6 | Keep Kubernetes deployment scripts and manifests maintained in `edura-infra` without incurring active cloud billing | @nadun | Ongoing through Sprint 6 |
| 7 | Update GitHub Project Board milestone to Sprint 6 and populate Sprint 6 issues into Todo | @all | Sprint 6, Week 5 (Day 1) |

---

## 8. Supervisor Feedback & Review Notes

- **Review Date:** 2026-07-14
- **Demonstration:** Demonstrated local Docker Compose running all 11 microservices behind Nginx, verified health checks on `http://localhost/api/*/health`, executed database migrations, ran RabbitMQ topology setup, and demonstrated Asgardeo OAuth2 login and OTP generation.
- **Supervisor Assessment:**
  - Commended the clean architectural decoupling, shared auth middleware, and comprehensive CI matrix testing.
  - Endorsed the pragmatic decision regarding **DDP-#18**: verifying the AKS deployment pipeline early, then pausing cloud resource consumption in favor of containerized local testing until the final deployment sprint.
