# Architectural Decision Record (ADR)
## ADR-12: Services communicate through events and local copies, not direct HTTP calls

### Status
Decided / Approved

### Context
The SDS (Chapter 2) describes loosely coupled, independently deployable services with a database per service, communicating "through asynchronous message queuing using RabbitMQ and synchronous REST APIs where appropriate". The infrastructure repository defines the matching broker topology: one `edura.events` topic exchange, a durable queue per consuming service, and fixed routing keys.

The first implementation followed that only partly. Eight services also called each other directly over HTTP through `/internal/...` routes: for example, assessment asked five other services for names, titles, access and uploads, analytics asked six, and auth and user each called the other during sign-up. This caused the problems the SDS tries to avoid:

- **Coupling and cascading failure.** If user_service was slow or down, registration, leaderboards and admin lists failed. Auth and user depended on each other (a cycle).
- **Latency.** A single page could wait on several chained network calls.
- **Hidden contracts.** The internal routes had no authentication of their own; they were protected only by the gateway hiding them.

### Decision
**No service calls another service over HTTP.** The browser talks only to the nginx gateway, and between services there are only two mechanisms:

1. **Events.** A service announces every change to data other services care about on the `edura.events` exchange (`auth.user-registered`, `user.profile-upserted`, `course.upserted`, `access.changed`, `payment.success`, `assessment.graded`, ...). The full catalogue, and which queue binds which key, is in `edura-backend/shared/events.py`; `edura-infra/rabbitmq/setup.py` declares the same topology.
2. **Local copies (replicas).** A service that needs another service's data keeps its own small copy in `replica_*` tables, updated by the events. A name lookup, an access check or a price check becomes a query on the service's own database. A copy is written only by the service's event consumer; the service's own logic only reads it.

Further rules that follow from this:

- **Event handlers set a row to the state the event announces** (an upsert), so at-least-once delivery is safe: handling a message twice changes nothing.
- **Resync at startup.** Each owner re-announces its reference data shortly after it starts, so a new, emptied or late-created copy catches up.
- **Sign-up is one event.** auth_service validates the registration form (the schema is shared in `shared/profile_schema.py`) and publishes `auth.user-registered` with the profile. user_service builds the profile from it. If user_service is down, the message waits in its durable queue.
- **Access is announced as a whole.** enrollment_service, which owns the access rules (course enrollment, single-lesson grant, class packages), publishes the complete picture for a student as `access.changed`. Course, content, assessment and analytics each keep it and gate content locally.
- **Files go straight to storage.** Payment (receipts) and assessment (question images) upload to Cloudinary through a shared helper and keep the returned `public_id` in their own table, instead of asking content_service to do it.
- **Reports are built from a read model.** analytics_service owns no business data; it keeps replica tables fed by events and builds progress, struggle analysis, dashboards and the PDF report from them.

### Consequences
**Positive**
- A service keeps working when the others are down: sign-up, access checks, leaderboards and prices no longer fail because another service is slow.
- No inter-service HTTP, so no `*_SERVICE_URL` configuration, no unauthenticated internal routes to defend, and no cycles at runtime.
- Each service can be developed, deployed and scaled independently, as the SDS intends.

**Negative / trade-offs**
- **Eventual consistency.** A change reaches other services a few tens of milliseconds later (longer if a consumer is down). Examples: a new Google account's profile appears just after sign-in (the client looks again briefly); a student's access to paid content opens just after payment.
- **Data is stored more than once** (names, titles, prices), which costs a little space and means the owner is the only source of truth.
- **Publishing is best-effort after the database commit.** If the broker is unavailable at that instant, the event is not sent. The startup resync repairs this; a transactional outbox would remove the gap and is listed as future work.
- **More moving parts to test.** Event handlers and replicas have their own tests, and the broker topology must match between the services and the infrastructure repository.

### Alternatives considered
- **An internal API gateway that all service-to-service calls pass through.** Simpler, but the services would still depend on each other being up at request time; it only moves the coupling.
- **RPC over RabbitMQ (request/reply).** Removes the HTTP routes but keeps the same runtime dependency.
- **A shared database.** Rejected: it breaks the database-per-service rule in the SDS.
