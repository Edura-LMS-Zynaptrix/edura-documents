## **Faculty of Science** 

## **Software Engineering Teaching Unit** 

## **University of Kelaniya, Sri Lanka** 

## **SENG 34213** 

**System Development Project** Course Guideline & Industrial Standards 

|**Programme**|Bachelor of Science (Hons.) in Software Engineering|
|---|---|
|**Year / Semester**|Year 3, Semester 2|
|**Duration**|16 Weeks (4 Months)|
|**Credits**|3|
|**Prerequisite**|SENG 31242 – System Design Project (Pass)|
|**Version**|1.0|
|**Issued By**|Software Engineering Teaching Unit|
|**Date**|2026|



_© Software Engineering Teaching Unit, University of Kelaniya_ 

## **Contents** 

|**1**|**Overview**|**Overview**|**3**|
|---|---|---|---|
||1.1|Course Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
||1.2|Learning Outcomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|3|
||1.3|Project Continuity<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|4|
|**2**|**Project Timeline (16 Weeks)**||**5**|
||2.1|Phase Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|5|
||2.2|Sprint Calendar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|6|
|**3**|**Development Environment & Repository Setup**||**7**|
||3.1|Code Repository Structure . . . . . . . . . . . . . . . . . . . . . . . . .|7|
||3.2|Branch Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|8|
||3.3|Semantic Versioning<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|9|
||3.4|Commit Message Convention<br>. . . . . . . . . . . . . . . . . . . . . . .|9|
|**4**|**GitHub Project Management – Development Phase**||**12**|
||4.1|Extending the Project Board. . . . . . . . . . . . . . . . . . . . . . . .|12|
||4.2|Development Epics . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|13|
||4.3|Writing Development Issue (Ticket) Descriptions . . . . . . . . . . . . .|13|
|||4.3.1<br>Example: High-Quality Development Issue . . . . . . . . . . . .|16|
|**5**|**Coding Standards**||**20**|
||5.1|Principles<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|20|
||5.2|Language-Specifc Standards . . . . . . . . . . . . . . . . . . . . . . . .|20|
||5.3|Code Review Standards<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|21|
|**6**|**Testing Standards**||**23**|
||6.1|Testing Philosophy . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
||6.2|Test Pyramid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
||6.3|Writing Professional Test Cases . . . . . . . . . . . . . . . . . . . . . .|24|



1 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

|||6.3.1<br>Unit Test Standards|.|.|. . . . . . . . . . . . . . . . . . . . . .|24|
|---|---|---|---|---|---|---|
|||6.3.2<br>Integration Test Standards . . . . . . . . . . . . . . . . . . . . .||||26|
|||6.3.3<br>Test Case Documentation|||. . . . . . . . . . . . . . . . . . . . .|28|
||6.4|Test Coverage Requirements|.|.|. . . . . . . . . . . . . . . . . . . . . .|29|
|**7**|**Continuous Integration & Deployment**|||||**30**|
||7.1|CI/CD Pipeline Requirements||.|. . . . . . . . . . . . . . . . . . . . . .|30|
||7.2|Required Pipeline Stages . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|31|
|**8**|**Security & Code Quality**|||||**35**|
||8.1|OWASP Top 10 Compliance|.|.|. . . . . . . . . . . . . . . . . . . . . .|35|
||8.2|Code Quality Gates . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|36|
|**9**|**Final Product Demonstration**|||||**37**|
||9.1|Demonstration Requirements||.|. . . . . . . . . . . . . . . . . . . . . .|37|
||9.2|Demonstration Script . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|37|
||9.3|GitHub Repository Submission|||. . . . . . . . . . . . . . . . . . . . . .|38|
|**10 **|**Deliverables & Assessment**|||||**39**|
||10.1|Final Deliverables . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|40|
||10.2|Peer Evaluation Submission|.|.|. . . . . . . . . . . . . . . . . . . . . .|41|
||10.3|Assessment<br>. . . . . . . . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|42|
||10.4|Final Report Structure . . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|42|
|**A **|**Defnition of Done – Master Checklist**|||||**44**|
|**B **|**Sprint Ceremony Templates**|||||**45**|
||B.1|Sprint Review Agenda<br>. . .|.|.|. . . . . . . . . . . . . . . . . . . . . .|45|
||B.2|Retrospective Template (Committed to GitHub Wiki) . . . . . . . . . .||||45|
|**C **|**GitHub Sprint Checklist – Development Phase**|||||**47**|
|**D **|**Peer Evaluation Form**|||||**48**|



2 

## **Chapter 1** 

## **Overview** 

## **1.1 Course Description** 

– SENG 34213 System Development Project is the capstone development course of the Software Engineering degree programme. Spanning **16 weeks (4 months)** across the second semester of Year 3, this course continues directly from SENG 31242, transforming the approved design artefacts into a working, tested, and deployable software product. Students operate as a professional software engineering team, following industry-standard engineering practices: sprint-based development, continuous integration, code review, test-driven development, and staged deployment. The final deliverable is a **working product demonstrated live to a panel** , with all source code publicly or privately hosted on GitHub. 

## **Prerequisite** 

**–** A pass (C or higher) in **SENG 31242 System Design Project** is a strict prerequisite. Students who did not complete SENG 31242 in the same academic year may not enrol without written approval from the Head of the Software Engineering Teaching Unit. 

## **1.2 Learning Outcomes** 

Upon successful completion of this course, students will be able to: 

- **LO1.** Implement a working software product from an approved SRS and SDS, adhering to the agreed architecture. 

- **LO2.** Write production-quality code following SOLID principles and team- 

3 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

agreed coding standards. 

- **LO3.** Design, write, and maintain automated test suites covering unit, integration, and acceptance levels. 

- **LO4.** Implement a CI/CD pipeline using GitHub Actions for automated build, test, and deployment. 

- **LO5.** Apply industry-standard Git workflows including branch strategy, PR reviews, and semantic versioning. 

- **LO6.** Write professional-grade issue descriptions, test cases, and technical documentation. 

- **LO7.** Demonstrate a live working product to a panel of evaluators and industry representatives. 

- **LO8.** Reflect critically on engineering decisions, technical debt, and lessons learned. 

## **1.3 Project Continuity** 

This course **continues** the project started in SENG 31242. Teams must: 

- Use the same GitHub Organisation created in SENG 31242. 

- Extend the project board into the Development phase (Phase = Development). 

- Add source code repositories to the existing GitHub Organisation. 

- Demonstrate that implementation decisions are traceable to the SRS and SDS. 

## **Design Changes During Development** 

It is normal for designs to evolve during implementation. Any significant deviation from the approved SDS must be documented as a new Architectural Decision Record (ADR) and reviewed with the supervisor within one sprint. The SDS must be updated to reflect the final implemented design. 

4 

## **Chapter 2** 

## **Project Timeline (16 Weeks)** 

## **2.1 Phase Overview** 

|**Week(s)**|**Phase**||**Gate**|**Key Activities**|
|---|---|---|---|---|
|1|Development|Kick-|✓Repo setup|Add code repos, set up CI scaf-|
||Of|||fold, agree coding standards|
|1–4|Sprint<br>1<br>–|Core|Sprint 1 Review|Data layer, auth, core domain|
||Foundation|||models, CI pipeline live|
|5–8|Sprint 2 – Feature||Sprint 2 Review|Primary features implemented|
||Development|||and unit-tested|
|9–12|Sprint 3 – Integra-||Sprint 3 Review|Integration testing, API con-|
||tion & Polish|||tracts, UI completion|
|13–14|Sprint 4 – Testing &||Test<br>coverage|Full test suite, performance|
||Hardening||gate|testing, security review|
|15|Pre-Demo Staging||Supervisor sign-|Staged deployment;<br>end-to-|
||||of|end demo rehearsal|
|16|Final Demo &|Sub-|Panel approval|Live product demonstration; f-|
||mission|||nal report submission|



5 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **2.2 Sprint Calendar** 

|**Sprint**|**Weeks**|**Duration**|**Focus Theme**|**Review Format**|
|---|---|---|---|---|
|Sprint 5|1–4|4 weeks|Foundation & Infrastructure|Demo + retrospective|
|Sprint 6|5–8|4 weeks|Core Features|Demo + retrospective|
|Sprint 7|9–12|4 weeks|Integration & UX|Demo + retrospective|
|Sprint 8|13–16|4 weeks|Quality & Release|Final panel demo|



Sprint numbers continue from SENG 31242 (Sprints 1–4). In SENG 34213, Sprints 5–8 are the development sprints. 

6 

## **Chapter 3** 

## **Development Environment & Repository Setup** 

## **3.1 Code Repository Structure** 

Add the following repositories to the existing GitHub Organisation: 

|**Repository**|**Contents**|
|---|---|
|`backend`|Server-side code (API, business logic, data access layer)|
|`frontend`|Client-side code (web/mobile application)|
|`infra`|Infrastructure as Code (Docker, docker-compose, CI/CD, deployment|
||scripts)|
|`tests`|Integration and end-to-end test suites (if not co-located with service|
||code)|
|`documents`|(Continued from SENG 31242) Updated SRS, SDS, ADRs, meeting|
||notes|



**Note:** For simpler monolith architectures, backend and frontend may be in a single `app` repository. Justify in the ADR. 

7 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **3.2 Branch Strategy** 

|**Branch**|**Purpose**|
|---|---|
|`main`|Production-ready code. Protected. Only accepts|
||merges via approved PR. Tagged with semantic|
||version on each release.|
|`develop`|Integration branch. Features are merged here frst;|
||only merged to `main` when a release is ready.|
|`feature/<ticket-id>-<slug>`|One<br>branch<br>per<br>GitHub<br>Issue.<br>Example:|
||`feature/42-user-auth`|
|`fix/<ticket-id>-<slug>`|Bug<br>fx<br>branches.<br>Example:|
||`fix/67-login-token-expiry`|
|`hotfix/<slug>`|Emergency production fxes branched from `main`|
||directly.|
|`release/<version>`|Release preparation (version bump, changelog,|
||smoke tests).|



## **Branch Hygiene** 

Feature branches must be **short-lived** . A branch that is open for more than **5 working days** without a PR indicates a work breakdown problem. Split the issue into smaller sub-issues immediately. 

8 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

– Figure 3.1: Git branch strategy `main` (green) is the production branch tagged with SemVer releases; `develop` (blue) is the integration branch; `feature/*` branches (purple, orange) are short-lived and merge into `develop` via PR; `hotfix/*` (red, dashed) branches directly from `main` for emergency fixes. 

## **3.3 Semantic Versioning** 

All releases must be tagged using **Semantic Versioning (SemVer)** : `vMAJOR.MINOR.PATCH` 

|**Segment**|**When to Increment**|**Example**|
|---|---|---|
|MAJOR|Breaking API or data model change|v1.0.0 _→_v2.0.0|
|MINOR|New feature, backwards-compatible|v1.0.0 _→_v1.1.0|
|PATCH|Bug fix, backwards-compatible|v1.1.0 _→_v1.1.1|



Sprint milestones: Sprint 5 ships `v0.1.0` ; Sprint 6 ships `v0.2.0` ; Sprint 7 ships `v0.3.0` ; Sprint 8 ships `v1.0.0` . 

## **3.4 Commit Message Convention** 

The same Conventional Commits format used in SENG 31242 continues, with additional types: 

9 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

**Type Use When** `feat` Implementing a new feature (increment MINOR) `fix` Fixing a bug (increment PATCH) `test` Adding or updating tests (no version change) `ci` Changes to CI/CD pipeline configuration `build` Build system or dependency changes `perf` Performance improvement `refactor` Code restructuring without feature/fix change `docs` Documentation updates `chore` Housekeeping (tooling, configs, non-production files) `style` Code formatting only (no logic change) `revert` Reverting a previous commit 

1 `feat(auth): implement JWT refresh token rotation` 

2 

3 `Implements sliding -window refresh token strategy as specified in` 4 `SDS Section 4.3.2 (Security Design). Tokens are rotated on each` 

5 `use; compromised tokens are invalidated on next rotation attempt.` 6 7 `Closes #54` 8 `Refs ADR -07` 

9 

10 `fix(payment): prevent double -charge on network timeout` 

11 

12 `Added idempotency key validation before processing any charge` 13 `request. Resolves customer -reported issue where slow network` 14 `connections triggered duplicate API calls.` 

15 

16 `Closes #89` 

17 

18 `test(inventory): add integration tests for low -stock alert` 

10 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

`trigger` 19 20 `Covers happy path and edge cases: exactly at threshold ,` 21 `one below threshold , and zero stock. Mocks the notification` 22 `service to assert it is called with correct payload.` 23 24 `Refs #77` 

Listing 3.1: Exemplary commit messages for development 

11 

## **Chapter 4** 

## **– GitHub Project Management Development Phase** 

## **4.1 Extending the Project Board** 

– The GitHub Project board from SENG 31242 is extended no new board is created. Set the **Phase** field value to `Development` on all new issues. 

– Figure 4.1: GitHub Projects Board view with development-phase issues. The _Phase_ field distinguishes Design from Development cards. Issues flow left-to-right: Backlog _→_ To Do _→_ In Progress _→_ In Review _→_ Done. 

12 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **4.2 Development Epics** 

In addition to continuing epics from the design phase, create the following development epics: 

|**Epic Label**|**Description**|
|---|---|
|`epic:dev-setup`|Repos, CI/CD scafold, coding standards, local dev environment|
|`epic:data-layer`|Database schema, migrations, ORM models, repositories|
|`epic:api`|REST/GraphQL endpoints, request validation, error handling|
|`epic:auth`|Authentication, authorisation, session management|
|`epic:core-features`|Primary business logic features (one epic per domain)|
|`epic:ui-frontend`|Frontend components, state management, routing|
|`epic:integration`|Service integration, third-party APIs, event handling|
|`epic:testing`|Unit tests, integration tests, E2E tests, test coverage|
|`epic:ci-cd`|Pipeline confguration, deployment scripts, environments|
|`epic:security`|Vulnerability scanning, input validation, secrets management|
|`epic:performance`|Load testing, query optimisation, caching|
|`epic:documentation`|API docs, README updates, developer guides|



## **4.3 Writing Development Issue (Ticket) Descriptions** 

Development tickets demand a higher level of technical precision than design-phase tickets. 

13 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

Figure 4.2: GitHub Issue creation form – the title follows the `[DDP-#NN] type(scope): summary` convention; the description pane contains the user story, BDD acceptance criteria, and estimate in Markdown; the sidebar sets assignee, labels, sprint milestone, priority and phase. 

1 `## User Story` 2 `As a [role], I want to [action] so that [benefit ].` 3 4 `## Background / Context` 5 `<!-- Reference the SRS requirement and SDS design element that` 6 `drives this ticket. Never implement without traceable design. --> -` 7 `SRS Reference: FR -<number > -` 8 `SDS Reference: Section <X.Y>, Class <ClassName > -` 9 `ADR Reference: ADR -<number > (if applicable)` 

10 11 `## Acceptance Criteria` 12 `<!-- Written as BDD scenarios (Given -When -Then) or as` 13 `precise testable statements. Each AC must have a` 

14 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

```
corresponding
```

14 `test case. -->` 

- 15 

16 `### AC1: Happy Path` 17 `** Given ** [precondition]` 

- 18 `** When ** [action]` 

- 19 `** Then ** [expected outcome]` 

- 20 21 `### AC2: Error Handling` 22 `** Given ** [invalid input or error condition]` 23 `** When ** [action]` 

- 24 `** Then ** [expected error response with HTTP status and error body]` 

25 

- 26 `### AC3: Edge Case` 

- 27 `** Given ** [boundary condition]` 28 `** When ** [action]` 29 `** Then ** [expected outcome]` 

- 30 31 `## Technical Notes` 

- 32 `<!-- Implementation guidance: algorithms to use , patterns to follow ,` 

- 33 `libraries recommended , known pitfalls , constraints -->` 

- 34 

- 35 `## Test Requirements` 

- 36 `<!-- List specific tests that must be written and pass -->` 37 `- [ ] Unit test: <what is being tested >` 38 `- [ ] Integration test: <what is being tested >` 39 `- [ ] Negative test: <what error condition is being tested >` 

- 40 

- 41 `## Definition of Done (DoD)` 

- 42 `- [ ] Code implemented and follows team coding standards` 43 `- [ ] All Acceptance Criteria unit tests written and passing` 44 `- [ ] Integration tests written and passing` 

15 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

45 `- [ ] Code coverage for new code >= 80%` 46 `- [ ] PR raised against ‘develop ‘ branch` 47 `- [ ] At least 1 peer code review completed; all comments resolved` 48 `- [ ] No new linting errors introduced -` 49 `[ ] CI pipeline passes (build , lint , test)` 50 `- [ ] API documentation updated (if endpoint added/modified)` 51 `- [ ] Issue linked in commit messages` 52 

53 `## Estimate` 54 `Estimated: X hours` 55 56 `## Dependencies` 57 `<!-- List any other issues that must be completed first -->` 58 `Blocked by: #<issue -number >` 

Listing 4.1: Development issue description template 

## **4.3.1 Example: High-Quality Development Issue** 

1 `Title: [DDP -#54] Implement JWT Refresh Token Rotation` 2 3 `Labels: epic:auth , P2 -Critical , feat` 4 `Assignee: @k.fernando` 5 `Sprint: Sprint 5 (Week 3)` 6 `Estimate: 6 hours` 7 8 `## User Story` 9 `As a logged -in user , I want my session to automatically stay` 10 `active without re -logging in frequently , so that my experience` 11 `is not interrupted during normal use.` 12 13 `## Background / Context` 

16 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

- 14 `- SRS Reference: FR -06 (Session Management), NFR -03 (Security )` 

- `- --` 

- 15 `SDS Reference: Section 4.3.2 (Security Design Auth Flow)` 16 `- ADR Reference: ADR -07 (JWT over server -side sessions)` 

- 17 

- 18 `The SDS specifies a sliding -window refresh token strategy.` 19 `Access tokens expire in 15 minutes; refresh tokens expire in` 20 `7 days and rotate on each use.` 

- 21 

22 `## Acceptance Criteria` 

- 23 

24 `### AC1: Successful Token Refresh` 

- 25 `Given a user holds a valid , unexpired refresh token` 26 `When the client calls POST /auth/refresh` 

- 27 `Then the system returns a new access token (15 min expiry)` 28 `and a new refresh token (7 day expiry)` 29 `and the old refresh token is invalidated immediately` 

- 30 

- 31 `### AC2: Expired Refresh Token` 32 `Given a user holds a refresh token older than 7 days` 33 `When the client calls POST /auth/refresh` 34 `Then the system returns HTTP 401 with body:` 35 `{" error ": " REFRESH_TOKEN_EXPIRED ", "message ": "..."}` 36 `and no new tokens are issued` 

- 37 

- 38 `### AC3: Reuse of Invalidated Token (Token Theft Detection)` 39 `Given a refresh token has already been rotated (used once)` 40 `When the client attempts to use the old (invalidated) token` 41 `Then the system returns HTTP 401 with body:` 42 `{" error ": " REFRESH_TOKEN_REUSE ", "message ": "..."}` 43 `and ALL active sessions for that user are immediately` 44 `terminated (security: assume token theft)` 

- 45 46 `### AC4: Concurrent Request Safety` 

17 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

- 47 `Given two simultaneous requests with the same refresh token` 48 `When both requests hit the endpoint concurrently` 49 `Then only one succeeds; the other receives HTTP 409 or 401` 50 `No duplicate token pairs are created` 

- 51 

- 52 `## Technical Notes` 

- 53 `- Store refresh tokens in the DB table ‘refresh_tokens ‘` 54 `(schema in ADR -07 Appendix).` 

- 

- 55 `Use ‘crypto.randomBytes (64).toString(’hex ’)‘ for token` 56 `generation -- do NOT use predictable IDs.` 

- 57 `- Wrap rotate + invalidate in a DB transaction to prevent` 58 `race conditions (AC4).` 

- 59 `- Store tokens as SHA -256 hash in DB; return raw token to` 60 `client only (never store raw).` 

- 61 

- 62 `## Test Requirements` 

- 63 `- [ ] Unit test: TokenService. rotateRefreshToken () happy path` 64 `- [ ] Unit test: TokenService. rotateRefreshToken () expired token` 

- 65 `- [ ] Unit test: TokenService. rotateRefreshToken () already - used token` 

- 66 `- [ ] Integration test: POST /auth/refresh with valid token` 67 `- [ ] Integration test: POST /auth/refresh with expired token` 68 `- [ ] Integration test: POST /auth/refresh with reused token` 69 `(assert all sessions terminated)` 70 `- [ ] Integration test: concurrent refresh requests (AC4)` 

71 

72 `## Definition of Done` 

- 73 `- [ ] All AC tests passing` 74 `- [ ] Coverage on TokenService >= 90%` 75 `- [ ] PR raised against ‘develop ‘` 76 `- [ ] Security implications reviewed by one additional team member` 

18 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

77 `- [ ] Postman collection updated with refresh endpoint example` 78 `- [ ] CHANGELOG.md updated under [Unreleased]` 79 80 `## Estimate` 81 `Estimated: 6 hours` 82 83 `## Dependencies` 84 `Blocked by: #48 (DB migration for refresh_tokens table)` 

Listing 4.2: Example development issue with full detail 

19 

## **Chapter 5** 

## **Coding Standards** 

## **5.1 Principles** 

All code produced in SENG 34213 must adhere to: 

- 

- 1. **SOLID Principles** Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion. 

2. **DRY** (Don’t Repeat Yourself) – Avoid code duplication; extract shared logic into utilities or services. 

- 

- 3. **YAGNI** (You Aren’t Gonna Need It) Implement only what is required by the current sprint’s acceptance criteria. 

- 

- 4. **Clean Code** Meaningful naming, small functions with a single responsibility, minimal side effects, no magic numbers. 

## **5.2 Language-Specific Standards** 

Each team must select and commit to a language-specific style guide at the start of Sprint 5. Acceptable choices include: 

|**Language**|||**Recommended Style Guide**|
|---|---|---|---|
|JavaScript|/|TypeScript|Airbnb Style Guide + ESLint + Prettier|
|Python|||PEP 8 + Flake8 or Ruf linter + Black formatter|
|Java|||Google Java Style Guide + Checkstyle|
|C#|||Microsoft C# Coding Conventions + dotnet-format|
|PHP|||PSR-12 + PHP<br>~~C~~odeSnifer|



The selected linter configuration file ( `.eslintrc` , `setup.cfg` , etc.) must be committed 

20 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

to the repository root in Sprint 5, Week 1. 

## **5.3 Code Review Standards** 

Every PR must receive at least **one** approving review before merging. Reviewers must assess: 

|**Dimension**|**Review Questions**|
|---|---|
|Correctness|Does the code do what the ticket specifes? Do all AC tests pass?|
|Readability|Can a new team member understand the code without the author’s|
||help?|
|Architecture|Is the code consistent with the SDS design and agreed architecture?|
|Test Quality|Are tests meaningful? Do they test behaviour, not implementation?|
|Security|Any hardcoded secrets? SQL injection risk? Unvalidated input?|
|Performance|Any N+1 queries? Blocking calls in async context?|
|Error Handling|Are all error cases handled? Are errors surfaced meaningfully?|



## **Review Comment Etiquette** 

– **Authors:** Do not resolve a reviewer’s comment yourself the reviewer resolves it after verifying the change. 

**Reviewers:** Prefix comments with: 

- `[blocker]:` Must be fixed before merge. 

- `[suggestion]:` Improvement recommended but not mandatory for this PR. 

- `[question]:` Asking for clarification; not necessarily a problem. 

• `[nit]:` Minor style point; reviewer’s preference only. 

21 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

– Figure 5.1: GitHub Pull Request conversation view the left panel shows reviewer comments prefixed with `[blocker]` and `[suggestion]` tags, CI check results, and the (greyed-out) merge button blocked by an unresolved comment. The right sidebar shows assignee, labels, milestone and linked issue. 

22 

## **Chapter 6** 

## **Testing Standards** 

## **6.1 Testing Philosophy** 

## **Testing as Professional Practice** 

In industry, code that has no tests is considered **unfinished** , not “working”. – Tests are not an afterthought they are part of the Definition of Done for every issue. The grade for this course explicitly rewards test quality and coverage. 

## **6.2 Test Pyramid** 

|**Layer**|**Scope**|**Speed**||**Min. Coverage Tar-**|
|---|---|---|---|---|
|||||**get**|
|Unit Tests|Single function or class|Very|fast|80% of all new code|
||in isolation|(_<_1 ms)|||
|Integration Tests|Module-to-module or|Moderate||All API endpoints|
||service-to-DB interac-||||
||tions||||
|End-to-End|Full<br>user<br>journey|Slow||All happy paths; top 3|
|(E2E)|through UI and back-|||critical fows|
||end||||



23 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **6.3 Writing Professional Test Cases** 

## **6.3.1 Unit Test Standards** 

Unit tests must follow the **Arrange-Act-Assert (AAA)** pattern with the **GivenWhen-Then** naming convention: 

- 1 `describe(’TokenService ’, () => {` 2 `describe(’rotateRefreshToken ’, () => {` 

- 3 

- 4 `it(’should return new token pair given a valid refresh token ’, async () => {` 

- 5 `// Arrange` 

- 6 `const validToken = ’valid -refresh -token -hash ’;` 

- 7 `const mockStoredToken = {` 

- 8 `id: ’token -uuid -1’,` 

- 9 `tokenHash: sha256(validToken),` 

- 10 `userId: ’user -123’,` 

- 11 `expiresAt: addDays(new Date (), 5), // 5 days from now` 12 `used: false ,` 

- 13 

```
};
```

- 14 `tokenRepository .findByHash. mockResolvedValue ( mockStoredToken );` 

- 15 `tokenRepository .invalidate. mockResolvedValue (true);` 

- 16 `tokenRepository .create. mockResolvedValue ({ token: ’new - token ’ });` 

- 17 

- 18 `// Act` 

- 19 `const result = await tokenService. rotateRefreshToken ( validToken);` 

- 20 

- 21 `// Assert` 

- 22 `expect(result). toHaveProperty (’accessToken ’);` 23 `expect(result). toHaveProperty (’refreshToken ’);` 24 `expect( tokenRepository .invalidate). toHaveBeenCalledWith` 

24 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

```
(’token -uuid -1’);
```

- 25 `expect( tokenRepository .create). toHaveBeenCalledOnce ();` 26 `});` 

- 27 

- 28 `it(’should throw UnauthorisedException given an expired refresh token ’, async () => {` 

- 29 `// Arrange` 30 `const expiredToken = ’expired -refresh -token ’;` 31 `const mockStoredToken = {` 32 `id: ’token -uuid -2’,` 33 `tokenHash: sha256(expiredToken),` 34 `userId: ’user -123’,` 

- 35 `expiresAt: subDays(new Date (), 1), // Expired yesterday` 

36 `used: false ,` 

- 37 `};` 38 `tokenRepository .findByHash. mockResolvedValue ( mockStoredToken );` 

- 39 

- 40 `// Act & Assert` 

- 41 `await expect(` 

- 42 `tokenService . rotateRefreshToken (expiredToken)` 43 `).rejects.toThrow( UnauthorisedException );` 44 `expect( tokenRepository .invalidate).not. toHaveBeenCalled ();` 

- 45 `});` 

- 46 

- 47 `it(’should invalidate all user sessions given a reused token ’, async () => {` 

- 48 `// Arrange` 49 `const reusedToken = ’already -used -token ’;` 50 `const mockStoredToken = {` 51 `id: ’token -uuid -3’,` 52 `userId: ’user -123’,` 

25 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

53 `expiresAt: addDays(new Date (), 3),` 54 `used: true , // Already rotated` 55 `};` 56 `tokenRepository .findByHash. mockResolvedValue ( mockStoredToken );` 57 58 `// Act & Assert` 59 `await expect(` 60 `tokenService . rotateRefreshToken (reusedToken)` 

61 `).rejects.toThrow( SecurityException );` 62 `expect( sessionService . revokeAllSessions )` 63 `. toHaveBeenCalledWith (’user -123 ’);` 

64 `});` 65 `});` 66 `});` 

Listing 6.1: Professional unit test example (JavaScript/Jest) 

## **6.3.2 Integration Test Standards** 

Integration tests exercise real HTTP endpoints against a test database: 

1 `describe(’POST /auth/refresh ’, () => {` 2 3 `beforeEach(async () => {` 4 `await testDatabase .seed (); // Seed known test data` 5 `});` 6 7 `afterEach(async () => {` 8 `await testDatabase .clean (); // Rollback between tests` 9 `});` 

10 

11 `it(’returns 200 with new token pair for valid refresh token ’, async () => {` 12 `// Arrange` 13 `const { refreshToken } = await createTestUserSession ();` 

26 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

- 14 

- 15 `// Act` 

- 16 `const response = await request(app)` 

- 17 `.post(’/auth/refresh ’)` 

- 18 `.set(’Content -Type ’, ’application/json ’)` 

- 19 `.send ({ refreshToken });` 

- 20 

- 21 `// Assert` 

- 22 `expect(response.status).toBe (200);` 

- 23 `expect(response.body).toMatchObject ({` 

- 24 `accessToken: expect.any(String),` 

- 25 `refreshToken : expect.any(String),` 

- 26 `});` 

- 27 `// Verify old token is invalidated in DB` 28 `const oldToken = await tokenRepository .findByValue( refreshToken );` 

- 29 `expect(oldToken.used).toBe(true);` 

- 30 

   - `});` 

- 31 

- 32 

   - `it(’returns 401 with REFRESH_TOKEN_EXPIRED for stale token ’, async () => {` 

- 33 `const { refreshToken } = await createTestUserSession ({` 

- 34 `expiredAt: subDays(new Date (), 1)` 35 `});` 

- 36 

- 37 `const response = await request(app)` 

- 38 `.post(’/auth/refresh ’)` 

- 39 `.send ({ refreshToken });` 

- 40 

- 41 `expect(response.status).toBe (401);` 

- 42 `expect(response.body.error).toBe(’REFRESH_TOKEN_EXPIRED ’)` 

      - `;` 

- 43 

   - `});` 

- 44 `});` 

27 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## Listing 6.2: Integration test example 

## **6.3.3 Test Case Documentation** 

Each functional test case must be documented in the development report appendix using the following format: 

|**Field**|**Content**|
|---|---|
|Test Case ID|TC-FR-06-01|
|Test Case Name|Successful Refresh Token Rotation|
|Related Requirement|FR-06 (Session Management)|
|Related Test File|`tests/integration/auth/refresh.test.ts`|
|Type|Integration|
|Priority|P1 – Must Pass|
|Preconditions|User exists in DB; valid, unexpired refresh token exists|
|Input|`POST /auth/refresh` with valid `refreshToken` in body|
|Expected Output|HTTP 200; new `accessToken` and `refreshToken` returned;|
||old refresh token marked `used = true` in DB|
|Actual Output|(Filled during execution)|
|Status|Pass / Fail / Blocked|



28 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **6.4 Test Coverage Requirements** 

|**Layer**||**Minimum Coverage**|**Measurement Tool**|**Measurement Tool**|
|---|---|---|---|---|
|Unit|Tests|80% for all new code|Jest / Coverage.py|/|
|(lines/branches)|||JaCoCo||
|API Endpoints||100% of endpoints must|Manual<br>tracking|in|
|||have at least one integration|test register||
|||test|||
|Critical Business|Logic|90% branch coverage|Specifed in SDS||



Coverage reports must be generated by the CI pipeline and linked in each Sprint Review. 

29 

## **Chapter 7** 

## **Continuous Integration & Deployment** 

## **7.1 CI/CD Pipeline Requirements** 

All projects must implement a GitHub Actions CI/CD pipeline by **end of Sprint 5** . **(Week 4)** 

30 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **7.2 Required Pipeline Stages** 

|**Stage**|**Trigger**|**Actions**|
|---|---|---|
|**Lint & Format**|Every push to any branch|Run linter; fail on|
|||errors.<br>Run for-|
|||matter check; fail|
|||if code is unformat-|
|||ted.|
|**Build**|Every push to any branch|Compile / transpile;|
|||fail on build error.|
|**Unit Tests**|Every push to any branch|Run full unit test|
|||suite; fail if any test|
|||fails; generate cov-|
|||erage report.|
|**Integration Tests**|Push to `develop` or PR to `develop`|Spin<br>up<br>test|
|||database;<br>run|
|||integration<br>tests;|
|||tear down.|
|**Security Scan**|Push to `develop` or `main`|Run<br>dependency|
|||vulnerability scan|
|||(e.g.<br>`npm audit`,|
|||Snyk,<br>Depend-|
|||abot).|
|**Deploy – Staging**|Merge to `develop`|Auto-deploy<br>to|
|||staging<br>environ-|
|||ment (e.g. Railway,|
|||Render, or Docker|
|||on a cloud VM).|
|**Deploy – Production**|Merge to `main` (manual approval)|Deploy tagged re-|
|||lease to production|
|||environment.|



31 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

1 `name: CI Pipeline` 

2 

- 3 `on:` 

- 4 `push:` 5 `branches: [ develop , main , ’feature /**’ , ’fix /**’ ]` 6 `pull_request :` 7 `branches: [ develop , main ]` 

- 8 

- 9 `jobs :` 

- 10 `lint:` 

- 11 `name: Lint & Format Check` 12 `runs -on: ubuntu -latest` 

- 13 `steps:` 

- 14 `- uses: actions/checkout@v4` 15 `- name: Set up Node.js` 16 `uses: actions/setup -node@v4` 

- 17 `with:` 

18 `node -version: ’20’` 

- 19 `cache: ’npm’` 

- 20 `- run: npm ci` 21 `- run: npm run lint` 22 `- run: npm run format:check` 

- 23 

- 24 `test :` 

- 25 `name: Unit & Integration Tests` 26 `runs -on: ubuntu -latest` 

- 27 `needs: lint` 

- 28 `services:` 

- 29 `postgres:` 

- 30 `image: postgres :16` 

- 31 `env :` 

- 32 `POSTGRES_DB: testdb` 

- 33 `POSTGRES_USER: test` 34 `POSTGRES_PASSWORD : test` 

32 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

|35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62|`options: >-`|
|---|---|
||`--health -cmd`<br>`pg_isready`|
||`--health -interval 10s`|
||`--health -retries 5`|
||`steps:`|
||`- uses: actions/checkout@v4`|
||`- name: Set up Node.js`|
||`uses: actions/setup -node@v4`|
||`with:`|
||`node -version: ’20’`|
||`cache: ’npm’`|
||`- run: npm ci`|
||`- run: npm run test:unit -- --coverage`|
||`- run: npm run test:integration`|
||`env:`|
||`DATABASE_URL : postgresql :// test:test@localhost`|
||`:5432/ testdb`|
||`- name: Upload`<br>`coverage`<br>`report`|
||`uses: actions/upload -artifact@v4`|
||`with:`|
||`name: coverage -report`|
||`path: coverage/`|
|||
||`security:`|
||`name: Security`<br>`Scan`|
||`runs -on: ubuntu -latest`|
||`steps:`|
||`- uses: actions/checkout@v4`|
||`- run: npm audit`<br>`--audit -level=high`|



Listing 7.1: Minimal GitHub Actions workflow structure (.github/workflows/ci.yml) 

33 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **Secrets Management** 

**NEVER** commit secrets (API keys, passwords, tokens, connection strings) to the – repository even in private repositories. Use GitHub Secrets for CI/CD pipelines and a `.env` file (in `.gitignore` ) for local development. Commit a `.env.example` file with all required keys and placeholder values. 

– Figure 7.1: GitHub Actions CI Pipeline run showing all five stages (Lint & Format, Build, Unit & Integration Tests, Security Scan, Deploy to Staging) passing in sequence. Each stage must pass before the next begins. 

34 

## **Chapter 8** 

## **Security & Code Quality** 

## **8.1 OWASP Top 10 Compliance** 

All teams must demonstrate that the following OWASP Top 10 risks have been addressed in their implementation. Evidence must be provided in the Final Report. 

35 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

|**Risk**|**ID**|**Mitigation Required**|
|---|---|---|
|Broken Access Control|A01|Role-based access checks on every endpoint; tests|
|||verify unauthorised access returns 403|
|Cryptographic Failures|A02|Passwords hashed with bcrypt (cost factor _≥_12);|
|||tokens stored as hashes; TLS enforced|
|Injection|A03|Parameterised queries or ORM used throughout;|
|||input validated and sanitised|
|Insecure Design|A04|Threat model documented in SDS Security section;|
|||design reviewed against it|
|Security Misconfguration|A05|Default credentials removed; error messages do not|
|||leak stack traces in production|
|Vulnerable Components|A06|Dependency scan in CI pipeline; no high/critical|
|||vulnerabilities|
|Auth Failures|A07|Account lockout after N failed attempts; secure|
|||session management; MFA optional|
|Integrity Failures|A08|Package lock fles committed; pipeline verifes in-|
|||tegrity|
|Logging Failures|A09|All auth events, errors, and data access logged;|
|||logs do not contain PII or secrets|
|SSRF|A10|External URL inputs validated; allow-list of per-|
|||mitted domains|



## **8.2 Code Quality Gates** 

The following quality gates are enforced by the CI pipeline: 

- Zero linting errors on any new or modified file. 

- Unit test coverage on new code _≥_ 80%. 

- No known high or critical vulnerabilities in dependencies. 

- All PR comments marked `[blocker]` resolved before merge. 

- No merge to `main` without at least 1 approved review. 

36 

## **Chapter 9** 

## **Final Product Demonstration** 

## **9.1 Demonstration Requirements** 

The final product demonstration takes place in **Week 16** before a panel of academic staff and, where possible, an industry representative and the project client/stakeholder. 

|**Format**|Live demonstration + Q&A|
|---|---|
|**Duration**|20 minutes demonstration + 15 minutes Q&A|
|**Attendees**|All team members must be present and contribute|
|**Environment**|Deployed staging environment (not localhost)|
|**GitHub Submission**|Repository URL(s) shared with panel before the session|



## **9.2 Demonstration Script** 

Teams must prepare a structured demonstration script covering: 

- 

- 1. **Context** (2 min) Who is the client/user? What problem does the product solve? 

- 

- 2. **Live Feature Walk-Through** (12 min) Demonstrate all primary use cases identified in the SRS, using realistic test data. 

- 

- 3. **Technical Architecture** (3 min) Briefly show the repository structure, CI pipeline run, and test coverage report. 

- 

- 4. **Limitations & Future Work** (2 min) Honest assessment of what was not completed and why. 

- 

- 5. **Lessons Learned** (1 min) One key engineering lesson per team member. 

37 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **Demonstration on Staging** 

The demonstration **must** run on the deployed staging environment, not on a local machine. A live deployment failure during the demo that has not been resolved before the session begins will be treated as a failed demonstration. 

## **9.3 GitHub Repository Submission** 

At least **48 hours** before the demonstration, teams must submit to the supervisor: 

- URL of the GitHub Organisation. 

- URL(s) of all repositories. 

- URL of the deployed staging application. 

- URL of the GitHub Project board. 

- Credentials for a demo user account (where applicable). 

The README of each repository must include: 

- Project description and link to the broader project. 

- Prerequisites (language runtime, environment variables required). 

- **Step-by-step installation and run instructions** (must work on a fresh machine). 

- Link to deployed application. 

- CI pipeline status badge. 

- Test coverage badge. 

38 

## **Chapter 10** 

## **Deliverables & Assessment** 

39 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **10.1 Final Deliverables** 

|**#**|**Artefact**||**Format**|**Format**||**Location / Submission**|
|---|---|---|---|---|---|---|
|1|Updated SRS||PDF|||`documents/srs/srs-final.pdf`|
|2|Updated SDS (fnal imple-||PDF|||`documents/sds/sds-final.pdf`|
||mentation)||||||
|3|Final<br>Development|Re-|PDF|+|hard|Submitted to Teaching Unit|
||port||copy||||
|4|Source Code (all reposito-||GitHub|||Organisation URL|
||ries)||||||
|5|CI/CD Pipeline||GitHub Actions|||Visible in repository|
|6|Test Coverage Report||HTML/PDF|||`documents/testing/`|
|||||||`coverage-sprint8.pdf`|
|7|Test Case Register||PDF|||`documents/testing/`|
|||||||`test-register.pdf`|
|8|OWASP Compliance Evi-||PDF|||`documents/security/`|
||dence|||||`owasp-checklist.pdf`|
|9|Performance Test Results||PDF|||`documents/testing/`|
|||||||`performance-report.pdf`|
|10|Deployed<br>Application||README|||`README.md` of main reposi-|
||URL|||||tory|
|11|Retrospective Reports|(all|Markdown|||`documents/retrospectives/`|
||sprints)||||||
|12|Peer Evaluation Form||PDF|(per|stu-|eKelaniya – see §10.2|
||||dent)||||



40 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **10.2 Peer Evaluation Submission** 

Each student is required to complete an individual **Peer Evaluation Form** (see Appendix D) assessing themselves and every other team member. The peer evaluation is **confidential** – responses are seen only by the academic supervisor and are not shared with teammates. 

## **Mandatory Individual Submission** 

Peer evaluations are an **individual** obligation. Each student must submit their own completed form. A missing peer evaluation will result in a **deduction of marks** from the student’s Continuous Progress component. The team leader’s submission does not substitute for any other team member. 

## **How to submit:** 

1. Download the Peer Evaluation Form from Appendix D or from the eKelaniya course page. 

2. Complete **all** sections: Self, and one section per team member. 

3. Every rating **must** be accompanied by a written justification comment. Attach supporting evidence (screenshots, commit logs, CI reports, meeting notes) where relevant. 

4. Save the completed form as a PDF named: `PeerEval <StudentNumber>` ~~`S`~~ `ENG34213.pdf` 

5. Submit the PDF via the designated submission link on **eKelaniya** : `https://ekel.kln.ac.lk/` 

   - Navigate to: _SENG 34213 → Assessments → Peer Evaluation Submission_ 

**Deadline:** Peer evaluations must be submitted **within 48 hours** of the Final Product Demonstration. Late submissions will not be accepted without prior written approval from the supervisor. 

41 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **10.3 Assessment** 

|**Component**|**Weight**|**Minimum**|
|---|---|---|
|Final Working Product (functionality, completeness)|30%|40%|
|Code Quality (standards, architecture conformance, review|20%|40%|
|discipline)|||
|Testing (coverage, quality of test cases, CI integration)|20%|40%|
|Final Product Demonstration|15%|40%|
|Continuous Progress (GitHub activity, sprint delivery, ret-|15%|40%|
|rospectives)|||
|**Total**|**100%**|**40% overall**|



## **10.4 Final Report Structure** 

The development report extends the design report from SENG 31242: 

1. Introduction (updated from design report) 

2. System Analysis (unchanged from SENG 31242, unless scope changed) 

3. System Design (updated SDS to reflect final implementation) 

## 4. **System Implementation** 

- Technology stack (justified) 

- Module/component descriptions with code excerpts 

- Database implementation 

- CI/CD pipeline description 

- Challenges faced and engineering decisions made 

## 5. **Testing** 

- Testing strategy 

- Test case register (Appendix) 

- Coverage report summary 

- Performance test results 

42 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

- Security compliance evidence 

## 6. **Evaluation** 

   - Degree of objectives met (cross-referenced to SRS) 

   - Client feedback (if available) 

   - Limitations and known defects 

   - Future work 

7. Conclusion 

8. References 

9. Appendices 

43 

## **Appendix A** 

## **– Definition of Done Master Check-** 

## **list** 

The following DoD applies to every issue merged during the development phase. 

- Acceptance Criteria in the issue are all verified as true 

- Code follows the team’s agreed style guide (linter passes) 

- Unit tests written for all new logic; all tests pass 

- Integration tests written for new API endpoints; all tests pass 

- Code coverage on new code _≥_ 80% 

- No hardcoded secrets or credentials 

- PR raised against `develop` ; description completed in full 

- At least 1 peer code review completed; all `[blocker]` comments resolved 

- CI pipeline passes: lint + build + unit + integration tests 

- Feature deployed to staging and manually smoke-tested 

- API documentation updated (Swagger/OpenAPI or Postman collection) 

- CHANGELOG.md updated under `[Unreleased]` 

- GitHub Issue linked in commit messages ( `Closes #XX` ) 

- GitHub Issue moved to **Done** on Project board 

44 

## **Appendix B** 

## **Sprint Ceremony Templates** 

## **B.1 Sprint Review Agenda** 

1. Demo of completed issues (3–5 min per issue max) 

2. Sprint metrics: issues completed vs. planned, velocity, CI pass rate, coverage delta 

3. Supervisor feedback 

4. Unfinished items: moved to next sprint backlog with root cause note 

## **B.2 Retrospective Template (Committed to GitHub** 

## **Wiki)** 

1 `# Sprint <N> Retrospective` 

2 `Date: YYYY -MM -DD` 

3 `Attendees: [list all members]` 

4 

5 `## Went Well` 

6 `1. ...` 7 `2. ...` 

8 `3. ...` 

9 

10 `## To Improve` 

11 `1. ...` 

12 `2. ...` 

13 `3. ...` 

14 

15 `## Action Items` 

45 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

16 `| Action | Owner | Due |` 17 `|--------|-------|-----|` 18 `| ... | @name | Sprint N+1, Week 1 |` 19 20 `## Metrics` 21 `- Issues planned: X` 22 `- Issues completed: Y` 23 `- Velocity: Z story points` 24 `- CI pipeline pass rate: X%` 25 `- Test coverage: X%` 

Listing B.1: Sprint retrospective template 

46 

## **Appendix C** 

## **– GitHub Sprint Checklist Development Phase** 

- Code repositories created with correct structure and branch protections 

- `develop` branch created and set as default 

- `.gitignore` and `.env.example` committed 

- Linter configuration committed to repository root 

- GitHub Actions CI workflow created and passing on first empty push 

- Sprint 5 Milestone created with correct dates 

- Development epics and labels created 

- Sprint 5 backlog populated with at least 15 development issues 

- All issues have: assignee, estimate, priority label, epic label, acceptance criteria 

- Sprint capacity calculated per member 

- Coding standards document committed to `documents/standards/` 

- Test framework installed and first test file committed 

- README badges (CI status, coverage) added to all code repositories 

47 

## **Appendix D** 

## **Peer Evaluation Form** 

## **PEER EVALUATION FORM** 

_CONFIDENTIAL_ 

Software Engineering Teaching Unit — University of Kelaniya 

|**Student Number:** . . . . . . . . . . . . . . . . .|**Date:** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|
|---|---|
|**Group / Team:** . . . . . . . . . . . . . . . . . . . .|**Project:** . . . . . . . . . . . . . . . . . . . . . . . . . . . .|



## **Instructions** 

Rate each team member (including yourself) on the criteria below using a scale of 1–5: 

**==> picture [236 x 9] intentionally omitted <==**

Poor Below Average Average Good Excellent 

**MANDATORY:** All ratings must be justified with written comments. If you have supporting evidence (e.g. screenshots, CI pipeline logs, commit history, emails), attach them in the _Proof / Evidence_ section for each team member. 

## **Self Evaluation** 

**Name: Role / Position:** 

_Rating Scale: 1 = Poor 2 = Below Average 3 = Average 4 = Good 5 = Excellent_ 

**MANDATORY:** You must justify every rating with a comment. Attach proof / evidence where applicable. 

48 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

|**Criterion**|**Rating**<br>**(1–5)**|**Comments (Mandatory — justify**<br>**your rating)**|
|---|---|---|
|Contribution Quality|||
|Commitment & Ef-<br>fort|||
|Collaboration|||
|Reliability|||
|Initiative|||



**1. What did this team member do particularly well?** 

**2. What could this team member improve? 3. Overall Assessment:** 

**4. Proof / Evidence (attach if needed):** 

49 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **Team Member 1** 

**Name: Role / Position:** _Rating Scale: 1 = Poor 2 = Below Average 3 = Average 4 = Good 5 = Excellent_ 

## **MANDATORY:** You must justify every rating with a comment. Attach proof / evidence 

where applicable. 

|**Criterion**|**Rating**<br>**(1–5)**|**Comments (Mandatory — justify**<br>**your rating)**|
|---|---|---|
|Contribution Quality|||
|Commitment & Ef-<br>fort|||
|Collaboration|||
|Reliability|||
|Initiative|||



50 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

**1. What did this team member do particularly well?** 

**2. What could this team member improve?** 

**3. Overall Assessment:** 

**4. Proof / Evidence (attach if needed):** 

51 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **Team Member 2** 

**Name: Role / Position:** _Rating Scale: 1 = Poor 2 = Below Average 3 = Average 4 = Good 5 = Excellent_ 

## **MANDATORY:** You must justify every rating with a comment. Attach proof / evidence 

where applicable. 

|**Criterion**|**Rating**<br>**(1–5)**|**Comments (Mandatory — justify**<br>**your rating)**|
|---|---|---|
|Contribution Quality|||
|Commitment & Ef-<br>fort|||
|Collaboration|||
|Reliability|||
|Initiative|||



52 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

**1. What did this team member do particularly well?** 

**2. What could this team member improve?** 

**3. Overall Assessment:** 

**4. Proof / Evidence (attach if needed):** 

53 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **Team Member 3** 

**Name: Role / Position:** _Rating Scale: 1 = Poor 2 = Below Average 3 = Average 4 = Good 5 = Excellent_ 

## **MANDATORY:** You must justify every rating with a comment. Attach proof / evidence 

where applicable. 

|**Criterion**|**Rating**<br>**(1–5)**|**Comments (Mandatory — justify**<br>**your rating)**|
|---|---|---|
|Contribution Quality|||
|Commitment & Ef-<br>fort|||
|Collaboration|||
|Reliability|||
|Initiative|||



54 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

**1. What did this team member do particularly well?** 

**2. What could this team member improve?** 

**3. Overall Assessment:** 

**4. Proof / Evidence (attach if needed):** 

55 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

## **Team Member 4** _**(complete only if team has 5 members)**_ 

**Name: Role / Position:** _Rating Scale: 1 = Poor 2 = Below Average 3 = Average 4 = Good 5 = Excellent_ 

## **MANDATORY:** You must justify every rating with a comment. Attach proof / evidence 

where applicable. 

|**Criterion**|**Rating**<br>**(1–5)**|**Comments (Mandatory — justify**<br>**your rating)**|
|---|---|---|
|Contribution Quality|||
|Commitment & Ef-<br>fort|||
|Collaboration|||
|Reliability|||
|Initiative|||



56 

_– SENG 34213 System Development Project_ 

_Software Engineering Teaching Unit_ 

**1. What did this team member do particularly well?** 

**2. What could this team member improve?** 

**3. Overall Assessment:** 

**4. Proof / Evidence (attach if needed):** 

57 

