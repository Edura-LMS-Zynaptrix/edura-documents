# API Endpoint Test Case Register

Generated: 2026-10-25 · Source: backend pytest suites (one run per service) · Guideline: development guideline §6.3.3 / §6.4

## Summary

| Measure | Value |
|---|---|
| Endpoints (unique method + gateway path) | 154 |
| Endpoints with at least one integration test | 154 (100.0%) |
| In scope (called by the frontend) | 135 |
| Deferred / future work (not called by the frontend) | 19 |
| Result of last run | All tests passing, Status = Pass |

"Integration test" here means a test that sends a real HTTP request to the FastAPI app against a test database (§6.3.2). An endpoint counts as covered when at least one test reaches its handler. Paths are shown as the gateway exposes them (`/api/<service>/...`).

Deferred endpoints were reduced to future work after the scope discussion with the customer. They are still tested, so the 100% rule holds.

## Register

| TC ID | Service | Method | Endpoint | Scope | Type | Priority | Tests | Test files | Status |
|---|---|---|---|---|---|---|---|---|---|
| TC-API-001 | admin_service | GET | `/api/admin/admin` | Deferred | Integration | P3 | 7 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-002 | admin_service | GET | `/api/admin/chat/admin/conversations` | In scope | Integration | P1 | 4 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-003 | admin_service | GET | `/api/admin/chat/admin/conversations/student/{}` | In scope | Integration | P1 | 4 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-004 | admin_service | DELETE | `/api/admin/chat/admin/conversations/{}` | In scope | Integration | P1 | 3 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-005 | admin_service | GET | `/api/admin/chat/admin/conversations/{}/messages` | In scope | Integration | P1 | 3 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-006 | admin_service | POST | `/api/admin/chat/admin/conversations/{}/reply` | In scope | Integration | P1 | 5 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-007 | admin_service | GET | `/api/admin/chat/history` | In scope | Integration | P1 | 6 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-008 | admin_service | POST | `/api/admin/chat/send` | In scope | Integration | P1 | 13 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-009 | admin_service | POST | `/api/admin/chat/sync` | In scope | Integration | P1 | 6 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-010 | admin_service | GET | `/api/admin/feedback/admin/all` | In scope | Integration | P1 | 6 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-011 | admin_service | DELETE | `/api/admin/feedback/admin/{}` | In scope | Integration | P1 | 3 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-012 | admin_service | PATCH | `/api/admin/feedback/admin/{}/read` | In scope | Integration | P1 | 3 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-013 | admin_service | POST | `/api/admin/feedback/submit` | In scope | Integration | P1 | 17 | `admin_service/tests/test_admin.py` | Pass |
| TC-API-014 | analytics_service | GET | `/api/analytics/admin/analytics` | In scope | Integration | P1 | 4 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-015 | analytics_service | GET | `/api/analytics/admin/stats` | In scope | Integration | P1 | 3 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-016 | analytics_service | GET | `/api/analytics/analytics` | Deferred | Integration | P3 | 1 | `analytics_service/tests/test_analytics.py` | Pass |
| TC-API-017 | analytics_service | GET | `/api/analytics/courses/{}/struggle` | In scope | Integration | P1 | 5 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-018 | analytics_service | GET | `/api/analytics/me/progress` | In scope | Integration | P1 | 3 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-019 | analytics_service | GET | `/api/analytics/platform-stats` | In scope | Integration | P1 | 4 | `analytics_service/tests/test_analytics.py` | Pass |
| TC-API-020 | analytics_service | GET | `/api/analytics/students/progress-summary` | In scope | Integration | P1 | 6 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-021 | analytics_service | GET | `/api/analytics/students/{}/progress` | In scope | Integration | P1 | 5 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-022 | analytics_service | POST | `/api/analytics/students/{}/send-report` | In scope | Integration | P1 | 11 | `analytics_service/tests/test_analytics.py`<br>`analytics_service/tests/test_progress.py` | Pass |
| TC-API-023 | assessment_service | GET | `/api/assessments` | In scope | Integration | P1 | 3 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-024 | assessment_service | POST | `/api/assessments` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-025 | assessment_service | GET | `/api/assessments/badges` | Deferred | Integration | P3 | 1 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-026 | assessment_service | GET | `/api/assessments/badges/dashboard` | In scope | Integration | P1 | 2 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-027 | assessment_service | GET | `/api/assessments/badges/my` | In scope | Integration | P1 | 1 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-028 | assessment_service | POST | `/api/assessments/bulk-import` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-029 | assessment_service | GET | `/api/assessments/bulk-import/template` | In scope | Integration | P1 | 1 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-030 | assessment_service | DELETE | `/api/assessments/by-module/{}` | In scope | Integration | P1 | 3 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-031 | assessment_service | GET | `/api/assessments/my-attempts` | In scope | Integration | P1 | 2 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-032 | assessment_service | GET | `/api/assessments/my-submissions` | In scope | Integration | P1 | 3 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-033 | assessment_service | GET | `/api/assessments/questions/csv-template` | In scope | Integration | P1 | 2 | `assessment_service/tests/test_assessment.py` | Pass |
| TC-API-034 | assessment_service | DELETE | `/api/assessments/questions/{}` | In scope | Integration | P1 | 2 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-035 | assessment_service | PUT | `/api/assessments/questions/{}` | In scope | Integration | P1 | 5 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-036 | assessment_service | GET | `/api/assessments/rankings/exam/{}` | In scope | Integration | P1 | 2 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-037 | assessment_service | GET | `/api/assessments/rankings/exams` | In scope | Integration | P1 | 3 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-038 | assessment_service | GET | `/api/assessments/rankings/leaderboard` | In scope | Integration | P1 | 5 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-039 | assessment_service | GET | `/api/assessments/submissions/{}/review` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-040 | assessment_service | DELETE | `/api/assessments/{}` | In scope | Integration | P1 | 2 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-041 | assessment_service | GET | `/api/assessments/{}` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-042 | assessment_service | PUT | `/api/assessments/{}` | In scope | Integration | P1 | 3 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-043 | assessment_service | GET | `/api/assessments/{}/my-last-attempt` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-044 | assessment_service | GET | `/api/assessments/{}/questions` | In scope | Integration | P1 | 1 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-045 | assessment_service | POST | `/api/assessments/{}/questions` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-046 | assessment_service | POST | `/api/assessments/{}/questions/images-zip` | In scope | Integration | P1 | 4 | `assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-047 | assessment_service | POST | `/api/assessments/{}/questions/import-csv` | In scope | Integration | P1 | 6 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-048 | assessment_service | POST | `/api/assessments/{}/start` | In scope | Integration | P1 | 19 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-049 | assessment_service | POST | `/api/assessments/{}/submit` | In scope | Integration | P1 | 11 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-050 | assessment_service | POST | `/api/assessments/{}/violations` | In scope | Integration | P1 | 12 | `assessment_service/tests/test_assessment.py`<br>`assessment_service/tests/test_assessment_service.py` | Pass |
| TC-API-051 | auth_service | GET | `/api/auth/admin` | Deferred | Integration | P3 | 2 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-052 | auth_service | POST | `/api/auth/admin/create-admin` | In scope | Integration | P1 | 3 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-053 | auth_service | POST | `/api/auth/change-password` | In scope | Integration | P1 | 2 | `auth_service/tests/test_auth_routes.py` | Pass |
| TC-API-054 | auth_service | POST | `/api/auth/forgot-password` | In scope | Integration | P1 | 4 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-055 | auth_service | POST | `/api/auth/google` | In scope | Integration | P1 | 9 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-056 | auth_service | POST | `/api/auth/login` | In scope | Integration | P1 | 17 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-057 | auth_service | POST | `/api/auth/logout` | In scope | Integration | P1 | 2 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-058 | auth_service | GET | `/api/auth/me` | In scope | Integration | P1 | 1 | `auth_service/tests/test_auth_routes.py` | Pass |
| TC-API-059 | auth_service | POST | `/api/auth/otp/request` | Deferred | Integration | P3 | 2 | `auth_service/tests/test_auth_routes.py` | Pass |
| TC-API-060 | auth_service | POST | `/api/auth/otp/verify` | Deferred | Integration | P3 | 2 | `auth_service/tests/test_auth_routes.py` | Pass |
| TC-API-061 | auth_service | GET | `/api/auth/protected` | Deferred | Integration | P3 | 2 | `auth_service/tests/test_auth_service.py` | Pass |
| TC-API-062 | auth_service | POST | `/api/auth/refresh` | In scope | Integration | P1 | 7 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-063 | auth_service | POST | `/api/auth/register` | In scope | Integration | P1 | 30 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-064 | auth_service | POST | `/api/auth/resend-verification` | In scope | Integration | P1 | 5 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-065 | auth_service | POST | `/api/auth/reset-password` | In scope | Integration | P1 | 7 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-066 | auth_service | POST | `/api/auth/set-password` | In scope | Integration | P1 | 2 | `auth_service/tests/test_auth_routes.py` | Pass |
| TC-API-067 | auth_service | DELETE | `/api/auth/users/{}` | In scope | Integration | P1 | 1 | `auth_service/tests/test_auth_routes.py` | Pass |
| TC-API-068 | auth_service | PUT | `/api/auth/users/{}/status` | In scope | Integration | P1 | 2 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-069 | auth_service | POST | `/api/auth/verify-email` | In scope | Integration | P1 | 12 | `auth_service/tests/test_auth_routes.py`<br>`auth_service/tests/test_auth_service.py` | Pass |
| TC-API-070 | content_service | DELETE | `/api/content/assets` | In scope | Integration | P1 | 6 | `content_service/tests/test_content_service.py` | Pass |
| TC-API-071 | content_service | POST | `/api/content/avatar` | In scope | Integration | P1 | 2 | `content_service/tests/test_content_service.py` | Pass |
| TC-API-072 | content_service | GET | `/api/content/lessons/{}/stream` | Deferred | Integration | P3 | 6 | `content_service/tests/test_content.py`<br>`content_service/tests/test_content_service.py` | Pass |
| TC-API-073 | content_service | POST | `/api/content/signed-url` | Deferred | Integration | P3 | 5 | `content_service/tests/test_content.py` | Pass |
| TC-API-074 | content_service | POST | `/api/content/upload` | In scope | Integration | P1 | 8 | `content_service/tests/test_content.py` | Pass |
| TC-API-075 | content_service | POST | `/api/content/upload-material` | In scope | Integration | P1 | 7 | `content_service/tests/test_content_service.py` | Pass |
| TC-API-076 | course_service | GET | `/api/courses` | In scope | Integration | P1 | 7 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-077 | course_service | POST | `/api/courses` | In scope | Integration | P1 | 8 | `course_service/tests/test_course_service.py`<br>`course_service/tests/test_courses.py` | Pass |
| TC-API-078 | course_service | PATCH | `/api/courses/checkpoint-questions/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-079 | course_service | GET | `/api/courses/checkpoints/csv-template` | In scope | Integration | P1 | 1 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-080 | course_service | DELETE | `/api/courses/checkpoints/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-081 | course_service | PATCH | `/api/courses/checkpoints/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-082 | course_service | DELETE | `/api/courses/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-083 | course_service | GET | `/api/courses/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-084 | course_service | PUT | `/api/courses/{}` | In scope | Integration | P1 | 9 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-085 | course_service | GET | `/api/courses/{}/modules` | In scope | Integration | P1 | 1 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-086 | course_service | POST | `/api/courses/{}/modules` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-087 | course_service | DELETE | `/api/courses/{}/modules/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-088 | course_service | PUT | `/api/courses/{}/modules/{}` | In scope | Integration | P1 | 3 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-089 | course_service | GET | `/api/courses/{}/modules/{}/lessons` | In scope | Integration | P1 | 7 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-090 | course_service | POST | `/api/courses/{}/modules/{}/lessons` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-091 | course_service | DELETE | `/api/courses/{}/modules/{}/lessons/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-092 | course_service | PUT | `/api/courses/{}/modules/{}/lessons/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-093 | course_service | DELETE | `/api/courses/{}/modules/{}/lessons/{}/checkpoints` | Deferred | Integration | P3 | 1 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-094 | course_service | GET | `/api/courses/{}/modules/{}/lessons/{}/checkpoints` | Deferred | Integration | P3 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-095 | course_service | POST | `/api/courses/{}/modules/{}/lessons/{}/checkpoints/import-csv` | Deferred | Integration | P3 | 4 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-096 | course_service | GET | `/api/courses/{}/modules/{}/materials` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-097 | course_service | POST | `/api/courses/{}/modules/{}/materials` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-098 | course_service | DELETE | `/api/courses/{}/modules/{}/materials/{}` | In scope | Integration | P1 | 1 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-099 | course_service | PUT | `/api/courses/{}/modules/{}/materials/{}` | In scope | Integration | P1 | 2 | `course_service/tests/test_course_service.py` | Pass |
| TC-API-100 | enrollment_service | GET | `/api/enrollments` | Deferred | Integration | P3 | 4 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-101 | enrollment_service | GET | `/api/enrollments/admin/class-enrollments` | In scope | Integration | P1 | 1 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-102 | enrollment_service | POST | `/api/enrollments/admin/class-enrollments` | In scope | Integration | P1 | 1 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-103 | enrollment_service | DELETE | `/api/enrollments/admin/class-enrollments/{}` | In scope | Integration | P1 | 1 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-104 | enrollment_service | GET | `/api/enrollments/admin/class-packages` | In scope | Integration | P1 | 2 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-105 | enrollment_service | POST | `/api/enrollments/admin/class-packages` | In scope | Integration | P1 | 4 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-106 | enrollment_service | POST | `/api/enrollments/admin/class-packages/auto-generate` | In scope | Integration | P1 | 2 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-107 | enrollment_service | DELETE | `/api/enrollments/admin/class-packages/{}` | In scope | Integration | P1 | 2 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-108 | enrollment_service | PATCH | `/api/enrollments/admin/class-packages/{}` | In scope | Integration | P1 | 2 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-109 | enrollment_service | GET | `/api/enrollments/admin/eligible` | In scope | Integration | P1 | 3 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-110 | enrollment_service | GET | `/api/enrollments/admin/enrolled` | In scope | Integration | P1 | 2 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-111 | enrollment_service | POST | `/api/enrollments/admin/grant` | In scope | Integration | P1 | 5 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-112 | enrollment_service | DELETE | `/api/enrollments/admin/revoke` | In scope | Integration | P1 | 3 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-113 | enrollment_service | GET | `/api/enrollments/class-packages` | In scope | Integration | P1 | 3 | `enrollment_service/tests/test_enrollment.py`<br>`enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-114 | enrollment_service | POST | `/api/enrollments/class-packages/{}/enroll-free` | In scope | Integration | P1 | 2 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-115 | enrollment_service | GET | `/api/enrollments/me` | In scope | Integration | P1 | 1 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-116 | enrollment_service | GET | `/api/enrollments/me/access` | In scope | Integration | P1 | 1 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-117 | enrollment_service | GET | `/api/enrollments/my-class-enrollments` | In scope | Integration | P1 | 1 | `enrollment_service/tests/test_enrollment_service.py` | Pass |
| TC-API-118 | notification_service | GET | `/api/notifications/notification` | Deferred | Integration | P3 | 1 | `notification_service/tests/test_notification_service.py` | Pass |
| TC-API-119 | payment_service | GET | `/api/payments` | In scope | Integration | P1 | 1 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-120 | payment_service | GET | `/api/payments/admin/bank-accounts` | In scope | Integration | P1 | 2 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-121 | payment_service | POST | `/api/payments/admin/bank-accounts` | In scope | Integration | P1 | 2 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-122 | payment_service | DELETE | `/api/payments/admin/bank-accounts/{}` | In scope | Integration | P1 | 2 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-123 | payment_service | PATCH | `/api/payments/admin/bank-accounts/{}` | In scope | Integration | P1 | 2 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-124 | payment_service | GET | `/api/payments/bank-accounts` | In scope | Integration | P1 | 1 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-125 | payment_service | POST | `/api/payments/checkout` | In scope | Integration | P1 | 4 | `payment_service/tests/test_payment_service.py`<br>`payment_service/tests/test_payments.py` | Pass |
| TC-API-126 | payment_service | POST | `/api/payments/free-enroll` | In scope | Integration | P1 | 3 | `payment_service/tests/test_payment_events.py`<br>`payment_service/tests/test_payment_service.py` | Pass |
| TC-API-127 | payment_service | GET | `/api/payments/internal/admin-stats` | Deferred | Integration | P3 | 2 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-128 | payment_service | GET | `/api/payments/receipts` | In scope | Integration | P1 | 1 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-129 | payment_service | POST | `/api/payments/receipts` | In scope | Integration | P1 | 10 | `payment_service/tests/test_payment_events.py`<br>`payment_service/tests/test_payment_service.py`<br>`payment_service/tests/test_payments.py` | Pass |
| TC-API-130 | payment_service | PUT | `/api/payments/receipts/{}/verify` | In scope | Integration | P1 | 5 | `payment_service/tests/test_payment_events.py`<br>`payment_service/tests/test_payment_service.py` | Pass |
| TC-API-131 | payment_service | POST | `/api/payments/webhook` | Deferred | Integration | P3 | 5 | `payment_service/tests/test_payment_service.py` | Pass |
| TC-API-132 | progress_service | GET | `/api/progress/courses/{}` | Deferred | Integration | P3 | 5 | `progress_service/tests/test_progress.py`<br>`progress_service/tests/test_progress_service.py` | Pass |
| TC-API-133 | progress_service | GET | `/api/progress/courses/{}/leaderboard` | In scope | Integration | P1 | 4 | `progress_service/tests/test_progress.py`<br>`progress_service/tests/test_progress_service.py` | Pass |
| TC-API-134 | progress_service | GET | `/api/progress/courses/{}/lessons/progress` | In scope | Integration | P1 | 4 | `progress_service/tests/test_progress.py`<br>`progress_service/tests/test_progress_service.py` | Pass |
| TC-API-135 | progress_service | POST | `/api/progress/courses/{}/lessons/progress` | In scope | Integration | P1 | 7 | `progress_service/tests/test_progress.py`<br>`progress_service/tests/test_progress_service.py` | Pass |
| TC-API-136 | user_service | GET | `/api/users` | In scope | Integration | P1 | 3 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-137 | user_service | POST | `/api/users` | In scope | Integration | P1 | 9 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-138 | user_service | GET | `/api/users/grade-subjects` | In scope | Integration | P1 | 1 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-139 | user_service | POST | `/api/users/grade-subjects` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-140 | user_service | DELETE | `/api/users/grade-subjects/{}` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-141 | user_service | PUT | `/api/users/grade-subjects/{}` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-142 | user_service | POST | `/api/users/referral/apply` | In scope | Integration | P1 | 8 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-143 | user_service | GET | `/api/users/referral/events` | In scope | Integration | P1 | 1 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-144 | user_service | GET | `/api/users/referral/summary` | In scope | Integration | P1 | 1 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-145 | user_service | GET | `/api/users/stats` | Deferred | Integration | P3 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-146 | user_service | GET | `/api/users/streams` | In scope | Integration | P1 | 1 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-147 | user_service | POST | `/api/users/streams` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-148 | user_service | DELETE | `/api/users/streams/{}` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-149 | user_service | PUT | `/api/users/streams/{}` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-150 | user_service | GET | `/api/users/subjects` | In scope | Integration | P1 | 1 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-151 | user_service | DELETE | `/api/users/{}` | In scope | Integration | P1 | 1 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-152 | user_service | GET | `/api/users/{}` | In scope | Integration | P1 | 2 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-153 | user_service | PUT | `/api/users/{}` | In scope | Integration | P1 | 3 | `user_service/tests/test_user_service.py` | Pass |
| TC-API-154 | user_service | PUT | `/api/users/{}/role` | Deferred | Integration | P3 | 1 | `user_service/tests/test_user_service.py` | Pass |
