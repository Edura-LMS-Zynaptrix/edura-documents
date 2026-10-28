# Test Case Documentation (guideline §6.3.3)

Functional test cases for the key requirements, in the §6.3.3 format. The complete list of automated tests is `test-register.md`; this table gives the full detail (requirement, preconditions, input, expected and actual output) for the cases that prove each functional requirement (FR-001 to FR-015, SDS Table 2).

- **Date executed:** 2026-10-28.
- **Where the Actual Output comes from:**
  - **Live** = run against the staging environment (`https://staging.eduralms.com`) with `edura-tests/integration` (branch DDP-#66, 197 passed, 1 skipped) or the Playwright suite `edura-tests/e2e` (DDP-#68, 5 passed).
  - **CI** = passed in the Backend CI run for the 11 services (778 tests) or in the in-process mock-gateway run of `edura-tests/integration/test_payment_enrollment_flow.py`.
- **Status key:** Pass, Fail, Blocked. A requirement with no automated test is listed in "Requirements without an automated test" instead of being given an invented result.
- Priority: P1 = must pass, P2 = should pass.

## FR-001: Authentication and role-based access

| Field | TC-FR-01-01 | TC-FR-01-02 | TC-FR-01-03 | TC-FR-01-04 |
|---|---|---|---|---|
| Name | Student logs in with valid credentials | Wrong password is refused | Student cannot use an admin endpoint | Logout revokes the refresh token |
| Requirement | FR-001 | FR-001 | FR-001 | FR-001 |
| Test file | `integration/test_auth_flow.py` | `integration/test_auth_flow.py` | `integration/test_admin_flow.py` | `integration/test_auth_flow.py` |
| Test | `test_given_valid_credentials_when_login_then_returns_bearer_token` | `test_given_wrong_password_when_login_then_401` | `test_given_student_when_get_admin_root_then_403` | `test_given_logged_in_session_when_logout_then_refresh_is_rejected` |
| Type / Priority | Integration / P1 | Integration / P1 | Integration / P1 | Integration / P1 |
| Preconditions | A verified student exists | A verified student exists | A verified student is logged in | A student is logged in and holds a refresh token |
| Input | `POST /api/auth/login` with the correct email and password | `POST /api/auth/login` with a wrong password | the admin root endpoint with the student's bearer token | `POST /api/auth/logout`, then `POST /api/auth/refresh` with the same token |
| Expected output | HTTP 200; a bearer `access_token` | HTTP 401 | HTTP 403 | Logout 200; the later refresh returns HTTP 401 |
| Actual output | HTTP 200, bearer token returned | HTTP 401 | HTTP 403 | Logout 200; refresh 401 |
| Status | Pass (Live) | Pass (Live) | Pass (Live) | Pass (Live) |

## FR-002: Registration and email verification

| Field | TC-FR-02-01 | TC-FR-02-02 | TC-FR-02-03 | TC-FR-02-04 |
|---|---|---|---|---|
| Name | New student registers | Weak password is rejected | Valid verification link verifies the account | Invalid verification token is refused |
| Requirement | FR-002 | FR-002 | FR-002 | FR-002 |
| Test file | `integration/test_auth_flow.py` | `integration/test_auth_flow.py` | `integration/test_auth_flow.py` | `integration/test_auth_flow.py` |
| Test | `test_given_new_email_when_register_then_returns_unverified_student` | `test_given_weak_password_when_register_then_422` | `test_given_valid_token_when_verify_then_account_is_verified` | `test_given_garbage_token_when_verify_then_400` |
| Type / Priority | Integration / P1 | Integration / P1 | Integration / P1 | Integration / P1 |
| Preconditions | The email is not registered | None | An unverified account exists; a token signed for it | None |
| Input | `POST /api/auth/register` with a new email, a strong password and a profile | `POST /api/auth/register` with a password that breaks the policy | `POST /api/auth/verify-email` with the signed token | `POST /api/auth/verify-email` with a random string |
| Expected output | Account created, not yet verified | HTTP 422 | Account marked verified; login now succeeds | HTTP 400 |
| Actual output | Account created, unverified | HTTP 422 | Account verified | HTTP 400 |
| Status | Pass (Live) | Pass (Live) | Pass (Live) | Pass (Live) |

UI evidence: Playwright `e2e/tests/01-register-and-login.spec.ts` registers through the form, verifies, signs in and is redirected away from `/login` (Pass, Live). A duplicate email returns HTTP 400 (`test_given_existing_email_when_register_then_400_email_exists`, Pass, Live).

## FR-003: Content access and upload rules

| Field | TC-FR-03-01 | TC-FR-03-02 | TC-FR-03-03 |
|---|---|---|---|
| Name | Admin streams a lesson | Unenrolled student cannot stream | Disallowed file type is refused |
| Requirement | FR-003 | FR-003 | FR-003 |
| Test file | `integration/test_content_flow.py` | `integration/test_content_flow.py` | `integration/test_content_flow.py` |
| Test | `test_given_admin_when_stream_lesson_then_embed_url_built_from_video_id` | `test_given_unenrolled_student_when_stream_then_403` | `test_given_disallowed_mime_when_upload_then_415` |
| Type / Priority | Integration / P1 | Integration / P1 | Integration / P2 |
| Preconditions | Admin token | A student not enrolled in the course | Admin token |
| Input | `GET /api/content/lessons/{id}/stream` with a video id | The same request with the student's token | `POST` upload with a disallowed MIME type |
| Expected output | HTTP 200; embed URL built from the video id | HTTP 403 (not enrolled) | HTTP 415 |
| Actual output | HTTP 200, embed URL returned | HTTP 403 | HTTP 415 |
| Status | Pass (Live) | Pass (Live) | Pass (Live) |

## FR-004 and FR-005: Assessments and automatic grading

| Field | TC-FR-04-01 | TC-FR-04-02 | TC-FR-05-01 | TC-FR-05-02 |
|---|---|---|---|---|
| Name | Admin adds an MCQ question | Question without a correct answer is rejected | Correct answers give full marks | Wrong answers give zero |
| Requirement | FR-004 | FR-004 | FR-005 | FR-005 |
| Test file | `integration/test_assessment_flow.py` | `integration/test_assessment_flow.py` | `integration/test_assessment_flow.py` | `integration/test_assessment_flow.py` |
| Test | `test_given_assessment_when_admin_adds_mcq_then_correct_answer_taken_from_option` | `test_given_no_correct_answer_when_add_question_then_422` | `test_given_correct_answer_when_submit_then_full_score_and_passed` | `test_given_wrong_answer_when_submit_then_zero_score_and_failed` |
| Type / Priority | Integration / P1 | Integration / P1 | Integration / P1 | Integration / P1 |
| Preconditions | An assessment exists; admin token | An assessment exists; admin token | An enrolled student has an active exam session | An enrolled student has an active exam session |
| Input | Add a question with options, one marked correct | Add a question with no option marked correct | Submit the correct option | Submit a wrong option |
| Expected output | Question stored with its correct answer | HTTP 422 | Full score; result passed | Score 0; result failed |
| Actual output | Question stored | HTTP 422 | Full score, passed | Score 0, failed |
| Status | Pass (Live) | Pass (Live) | Pass (Live) | Pass (Live) |

UI evidence: Playwright `e2e/tests/03-take-exam.spec.ts` enrols, starts an exam, answers every question, submits and sees "Exam Results" with "Marks Obtained" (Pass, Live).

## FR-006: Bank-slip (receipt) payment

| Field | TC-FR-06-01 | TC-FR-06-02 |
|---|---|---|
| Name | Admin approves an uploaded receipt | Fake PDF is refused |
| Requirement | FR-006 | FR-006 |
| Test file | `payment_service/tests/test_payment_events.py` | `payment_service/tests/test_payment_events.py` |
| Test | `test_given_uploaded_receipt_when_admin_approves_then_payment_and_review_announced` | `test_given_pdf_and_fake_pdf_when_receipt_uploaded_then_real_one_stored_and_fake_refused` |
| Type / Priority | Unit / P1 | Unit / P2 |
| Preconditions | A receipt is uploaded for a payment | A pending payment |
| Input | Admin approves the receipt | Upload a file named `.pdf` that is not a PDF |
| Expected output | Payment confirmed; review event published | Real PDF stored; fake refused |
| Actual output | As expected | As expected |
| Status | Pass (CI) | Pass (CI) |

## FR-007 to FR-009: PayHere payment, webhook and automatic access

| Field | TC-FR-07-01 | TC-FR-08-01 | TC-FR-08-02 | TC-FR-09-01 |
|---|---|---|---|---|
| Name | Paid course opens checkout | Webhook with an invalid signature is rejected | Duplicate webhook is idempotent | Success webhook grants access |
| Requirement | FR-007 | FR-008 | FR-008 | FR-009 |
| Test file | `e2e/tests/02-browse-and-enrol.spec.ts` | `integration/test_payment_enrollment_flow.py` | `integration/test_payment_enrollment_flow.py` | `integration/test_payment_enrollment_flow.py` |
| Test | `test_given_a_paid_course_when_the_student_chooses_to_purchase_then_checkout_opens_with_the_course_price` | `test_ac3_invalid_hmac_blocks_enrollment` | `test_ac4_duplicate_webhook_is_idempotent` | `test_ac1_webhook_to_enrollment_chain` |
| Type / Priority | E2E / P1 | Integration / P1 | Integration / P1 | Integration / P1 |
| Preconditions | A signed-in student; paid course 10 (LKR 2,500) | A pending payment with an order id | A payment already confirmed by one webhook | A pending payment for a course |
| Input | Click Buy on the course page | `POST /webhook` with a wrong signature | The same valid webhook sent twice | `POST /webhook` with a valid signature and a success status |
| Expected output | Browser at `/payment?type=course&id=10` showing the price | HTTP 400; no enrolment created | Both answered HTTP 200 SUCCESS; exactly one payment record | HTTP 200 SUCCESS; payment SUCCESS; enrolment ACTIVE |
| Actual output | Checkout opened with LKR 2,500 | HTTP 400; enrolment lookup 404 | Both 200 SUCCESS; one record | Payment SUCCESS; enrolment ACTIVE |
| Status | Pass (Live) | Pass (CI, mock gateway) | Pass (CI, mock gateway) | Pass (CI, mock gateway) |

The webhook cases ran only against the mock gateway. Running them against staging needs the staging PayHere credentials, which were not available (listed in the coverage report gaps).

## FR-010: Progress tracking

| Field | TC-FR-10-01 | TC-FR-10-02 |
|---|---|---|
| Name | Watching a lesson is recorded | Dashboard count increases |
| Requirement | FR-010 | FR-010 |
| Test file | `integration/test_progress_flow.py` | `integration/test_progress_flow.py` |
| Test | `test_given_student_when_mark_lesson_watched_then_progress_recorded` | `test_given_watched_lesson_when_get_dashboard_then_watched_count_increases` |
| Type / Priority | Integration / P1 | Integration / P1 |
| Preconditions | An enrolled student | A student who has marked a lesson watched |
| Input | Mark a lesson watched | `GET` the progress dashboard before and after |
| Expected output | Progress recorded | Watched count is higher after |
| Actual output | Progress recorded | Count increased |
| Status | Pass (Live) | Pass (Live) |

## FR-013 and FR-014: Anti-cheating and gamification

| Field | TC-FR-13-01 | TC-FR-14-01 |
|---|---|---|
| Name | Violation during an exam is recorded | Public badge catalogue is available |
| Requirement | FR-013 | FR-014 |
| Test file | `integration/test_assessment_flow.py` | `integration/test_assessment_flow.py` |
| Test | `test_given_session_when_record_violation_then_204` | `test_given_anonymous_visitor_when_list_badges_then_catalogue_returned` |
| Type / Priority | Integration / P2 | Integration / P2 |
| Preconditions | An active exam session | None |
| Input | Record a violation for the session | `GET` the badge list without a token |
| Expected output | HTTP 204 | The catalogue of badges |
| Actual output | HTTP 204 | Catalogue returned |
| Status | Pass (Live) | Pass (Live) |

## FR-012: Analytics

| Field | TC-FR-12-01 |
|---|---|
| Name | Admin reads platform analytics; a student cannot |
| Requirement | FR-012 |
| Test file | `integration/test_notification_analytics_flow.py` |
| Test | `test_given_admin_when_get_admin_stats_then_200`, `test_given_student_when_get_admin_stats_then_403` |
| Type / Priority | Integration / P2 |
| Preconditions | An admin token and a student token |
| Input | `GET` the admin statistics endpoint with each token |
| Expected output | Admin 200; student 403 |
| Actual output | Admin 200; student 403 |
| Status | Pass (Live) |

## FR-015: Completion certificates

| Field | TC-FR-15-01 | TC-FR-15-02 | TC-FR-15-03 |
|---|---|---|---|
| Name | Completed course issues a certificate | Failed assessment blocks the certificate | Certificate is not issued twice |
| Requirement | FR-015 (BR-004) | FR-015 (BR-004) | FR-015 |
| Test file | `progress_service/tests/test_progress.py` | `progress_service/tests/test_progress_service.py` | `progress_service/tests/test_progress_service.py` |
| Test | `test_given_completed_course_when_certificate_issued_then_record_created_and_event_published` | `test_given_failed_assessment_when_course_completed_then_certificate_is_not_issued` | `test_given_issued_certificate_when_completion_repeats_then_certificate_is_not_issued_again` |
| Type / Priority | Unit / P2 | Unit / P2 | Unit / P2 |
| Preconditions | A student watched 100% of the course and passed every assessment | 100% watched, one assessment failed | A certificate already exists for the student and course |
| Input | Completion is recorded | Completion is recorded | Completion is recorded again |
| Expected output | A certificate record is created and `certificate.issued` is published | No certificate | No second certificate |
| Actual output | As expected | As expected | As expected |
| Status | Pass (CI) | Pass (CI) | Pass (CI) |

**Partly implemented.** The eligibility rule, the database record and the `certificate.issued` event work and are tested. The record stores only a placeholder link (`/certificates/<student>_<course>.pdf`): no PDF is generated, nothing stores it, and the frontend has no page to view or download a certificate. The requirement says the certificate is "generated and issued", so it is only partly met.

## Requirements not fully covered

| Requirement | Position |
|---|---|
| FR-011 Gemini digital assistant | Not implemented; out of scope for this release (SRS 3.3 excludes advanced AI features). The chat in `admin_service` is the human support chat. No test case is needed. |
| FR-012 Excel export | **Not implemented.** The backend has no Excel (xlsx) or analytics CSV export. Only the progress report in PDF is built (`analytics_service/report.py`, `POST /students/{user_id}/send-report`, emailed to the student) and it is unit-tested (`analytics_service/tests/test_progress.py`). The PDF half of FR-012 is met; the Excel half is not. |
| FR-015 Certificate PDF | See above: record and event only, no generated PDF and no frontend view. |

These gaps belong in the final report under "Limitations & future work". List FR-011, FR-012 (Excel) and FR-015 (PDF) as known deviations from the SRS.
