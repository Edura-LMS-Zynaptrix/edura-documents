# API Endpoint Register

Generated: 2026-10-27 · Source: FastAPI routes in `edura-backend` and the HTTP calls in the service tests (`testing/tools/generate_registers.py`) · Guideline §6.4: every endpoint must have at least one integration test

## Summary

| Service | Endpoints | Tested | Probably tested | No test found |
|---|---|---|---|---|
| admin_service | 14 | 14 | 0 | 0 |
| analytics_service | 10 | 10 | 0 | 0 |
| assessment_service | 34 | 30 | 3 | 1 |
| auth_service | 20 | 20 | 0 | 0 |
| content_service | 7 | 5 | 2 | 0 |
| course_service | 25 | 15 | 10 | 0 |
| enrollment_service | 19 | 19 | 0 | 0 |
| notification_service | 2 | 2 | 0 | 0 |
| payment_service | 14 | 14 | 0 | 0 |
| progress_service | 9 | 7 | 2 | 0 |
| user_service | 20 | 20 | 0 | 0 |
| **Total** | **174** | **156** | **17** | **1** |

Notes:

- Paths are as defined in each service (the gateway adds its own `/api/...` prefix, see `edura-infra/nginx/nginx.conf`).
- *Yes*: a test sends a request with that method to a matching path. *Probable*: the test builds the start of the path with a helper, so only the end of the path could be matched (or the call is made in a shared helper function); confirm these by hand. **No**: no matching call was found; this is a static match, so check each row by hand before concluding the endpoint is untested.
- *Test file (direct tests)* shows the files whose tests call the endpoint, with the number of tests in brackets.

## admin_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/admin` | `admin_only` | Yes | `test_admin.py` (6) |
| GET | `/chat/admin/conversations` | `admin_list_conversations` | Yes | `test_admin.py` (3) |
| GET | `/chat/admin/conversations/student/{user_id}` | `admin_conversation_for_student` | Yes | `test_admin.py` (3) |
| DELETE | `/chat/admin/conversations/{conversation_id}` | `admin_delete_conversation` | Yes | `test_admin.py` (2) |
| GET | `/chat/admin/conversations/{conversation_id}/messages` | `admin_conversation_messages` | Yes | `test_admin.py` (2) |
| POST | `/chat/admin/conversations/{conversation_id}/reply` | `admin_reply` | Yes | `test_admin.py` (3) |
| GET | `/chat/history` | `chat_history` | Yes | `test_admin.py` (6) |
| POST | `/chat/send` | `send_message` | Yes | `test_admin.py` (9) |
| POST | `/chat/sync` | `sync_session` | Yes | `test_admin.py` (6) |
| GET | `/feedback/admin/all` | `list_feedback` | Yes | `test_admin.py` (4) |
| DELETE | `/feedback/admin/{feedback_id}` | `delete_feedback` | Yes | `test_admin.py` (3) |
| PATCH | `/feedback/admin/{feedback_id}/read` | `mark_feedback_read` | Yes | `test_admin.py` (3) |
| POST | `/feedback/submit` | `submit_feedback` | Yes | `test_admin.py` (11) |
| GET | `/health` | `health` | Yes | `test_admin.py` (1) |

## analytics_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/admin/analytics` | `admin_analytics` | Yes | `test_analytics.py` (1), `test_progress.py` (1) |
| GET | `/admin/stats` | `admin_stats` | Yes | `test_progress.py` (1) |
| GET | `/analytics` | `analytics_only` | Yes | `test_analytics.py` (1) |
| GET | `/courses/{course_id}/struggle` | `course_struggle` | Yes | `test_analytics.py` (3), `test_progress.py` (2) |
| GET | `/health` | `health` | Yes | `test_analytics.py` (1) |
| GET | `/me/progress` | `my_progress` | Yes | `test_analytics.py` (2), `test_progress.py` (1) |
| GET | `/platform-stats` | `platform_stats` | Yes | `test_analytics.py` (4) |
| GET | `/students/progress-summary` | `students_progress_summary` | Yes | `test_analytics.py` (4), `test_progress.py` (2) |
| GET | `/students/{user_id}/progress` | `student_progress` | Yes | `test_progress.py` (4), `test_analytics.py` (1) |
| POST | `/students/{user_id}/send-report` | `send_student_report` | Yes | `test_analytics.py` (6), `test_progress.py` (3) |

## assessment_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/` | `list_assessments` | Yes | `test_assessment_service.py` (2), `test_assessment.py` (1) |
| POST | `/` | `create_assessment` | Yes | `test_assessment_service.py` (3), `test_assessment.py` (1) |
| GET | `/api/assessments/{assessment_id}` | `get_assessment` | Yes | `test_assessment.py` (2) |
| GET | `/api/assessments/{assessment_id}/my-last-attempt` | `get_my_last_attempt` | **No** | – |
| POST | `/api/assessments/{assessment_id}/start` | `start_assessment_session` | Yes | `test_assessment.py` (11) |
| POST | `/api/assessments/{assessment_id}/submit` | `submit_assessment` | Yes | `test_assessment.py` (5) |
| POST | `/api/assessments/{assessment_id}/violations` | `record_violation` | Yes | `test_assessment.py` (2) |
| GET | `/badges` | `list_badges` | Yes | `test_assessment_service.py` (1) |
| GET | `/badges/dashboard` | `badge_dashboard` | Yes | `test_assessment.py` (1), `test_assessment_service.py` (1) |
| GET | `/badges/my` | `my_badges` | Yes | `test_assessment_service.py` (1) |
| POST | `/bulk-import` | `bulk_import_exams` | Probable | `test_assessment_service.py` (4) |
| GET | `/bulk-import/template` | `bulk_import_template` | Yes | `test_assessment_service.py` (1) |
| DELETE | `/by-module/{module_id}` | `delete_module_assessments` | Yes | `test_assessment_service.py` (3) |
| GET | `/health` | `health` | Yes | `test_assessment_service.py` (1) |
| GET | `/my-attempts` | `list_my_attempts` | Yes | `test_assessment_service.py` (2) |
| GET | `/my-submissions` | `list_my_submissions` | Yes | `test_assessment_service.py` (2), `test_assessment.py` (1) |
| GET | `/questions/csv-template` | `download_questions_csv_template` | Yes | `test_assessment.py` (2) |
| DELETE | `/questions/{question_id}` | `delete_question` | Yes | `test_assessment_service.py` (2) |
| PUT | `/questions/{question_id}` | `update_question` | Yes | `test_assessment_service.py` (5) |
| GET | `/rankings/exam/{exam_id}` | `my_exam_rank` | Yes | `test_assessment.py` (1), `test_assessment_service.py` (1) |
| GET | `/rankings/exams` | `ranking_exams` | Yes | `test_assessment.py` (2), `test_assessment_service.py` (1) |
| GET | `/rankings/leaderboard` | `ranking_leaderboard` | Yes | `test_assessment.py` (3), `test_assessment_service.py` (2) |
| GET | `/submissions/{submission_id}/review` | `review_submission` | Yes | `test_assessment_service.py` (3), `test_assessment.py` (1) |
| DELETE | `/{assessment_id}` | `delete_assessment` | Yes | `test_assessment.py` (1), `test_assessment_service.py` (1) |
| GET | `/{assessment_id}` | `get_assessment` | Yes | `test_assessment_service.py` (8), `test_assessment.py` (3) |
| PUT | `/{assessment_id}` | `update_assessment` | Yes | `test_assessment_service.py` (2), `test_assessment.py` (1) |
| GET | `/{assessment_id}/my-last-attempt` | `get_my_last_attempt` | Yes | `test_assessment_service.py` (2), `test_assessment.py` (1) |
| GET | `/{assessment_id}/questions` | `list_questions` | Yes | `test_assessment_service.py` (1) |
| POST | `/{assessment_id}/questions` | `create_question` | Yes | `test_assessment_service.py` (4) |
| POST | `/{assessment_id}/questions/images-zip` | `upload_question_images_zip` | Probable | `test_assessment_service.py` (4) |
| POST | `/{assessment_id}/questions/import-csv` | `import_questions_csv` | Probable | `test_assessment_service.py` (helper), `test_assessment.py` (helper) |
| POST | `/{assessment_id}/start` | `start_assessment_session` | Yes | `test_assessment.py` (11), `test_assessment_service.py` (8) |
| POST | `/{assessment_id}/submit` | `submit_assessment` | Yes | `test_assessment_service.py` (6), `test_assessment.py` (5) |
| POST | `/{assessment_id}/violations` | `record_violation` | Yes | `test_assessment_service.py` (4), `test_assessment.py` (2) |

## auth_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/admin` | `admin_only` | Yes | `test_auth_routes.py` (1), `test_auth_service.py` (1) |
| POST | `/admin/create-admin` | `create_admin` | Yes | `test_auth_routes.py` (2), `test_auth_service.py` (1) |
| POST | `/change-password` | `change_password` | Yes | `test_auth_routes.py` (2) |
| POST | `/forgot-password` | `forgot_password` | Yes | `test_auth_routes.py` (1) |
| POST | `/google` | `google_login` | Yes | `test_auth_routes.py` (6), `test_auth_service.py` (3) |
| GET | `/health` | `health` | Yes | `test_auth_routes.py` (1) |
| POST | `/login` | `login` | Yes | `test_auth_service.py` (10), `test_auth_routes.py` (7) |
| POST | `/logout` | `logout` | Yes | `test_auth_routes.py` (1), `test_auth_service.py` (1) |
| GET | `/me` | `get_me` | Yes | `test_auth_routes.py` (1) |
| POST | `/otp/request` | `request_otp` | Yes | `test_auth_routes.py` (2) |
| POST | `/otp/verify` | `verify_otp` | Yes | `test_auth_routes.py` (2) |
| GET | `/protected` | `protected_route` | Yes | `test_auth_service.py` (2) |
| POST | `/refresh` | `refresh` | Yes | `test_auth_routes.py` (4), `test_auth_service.py` (3) |
| POST | `/register` | `register` | Yes | `test_auth_service.py` (17), `test_auth_routes.py` (5) |
| POST | `/resend-verification` | `resend_verification` | Yes | `test_auth_routes.py` (2), `test_auth_service.py` (1) |
| POST | `/reset-password` | `reset_password` | Yes | `test_auth_routes.py` (4), `test_auth_service.py` (3) |
| POST | `/set-password` | `set_password` | Yes | `test_auth_routes.py` (2) |
| DELETE | `/users/{user_id}` | `delete_user` | Yes | `test_auth_routes.py` (1) |
| PUT | `/users/{user_id}/status` | `update_user_status` | Yes | `test_auth_routes.py` (1), `test_auth_service.py` (1) |
| POST | `/verify-email` | `verify_email` | Yes | `test_auth_service.py` (5), `test_auth_routes.py` (3) |

## content_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| DELETE | `/assets` | `delete_uploaded_asset` | Yes | `test_content_service.py` (3) |
| POST | `/avatar` | `upload_avatar` | Probable | `test_content_service.py` (2) |
| GET | `/health` | `health` | Yes | `test_content.py` (1) |
| GET | `/lessons/{lesson_id}/stream` | `stream_lesson` | Yes | `test_content.py` (5), `test_content_service.py` (1) |
| POST | `/signed-url` | `generate_signed_url` | Yes | `test_content.py` (5) |
| POST | `/upload` | `upload_file` | Yes | `test_content.py` (8) |
| POST | `/upload-material` | `upload_material` | Probable | `test_content_service.py` (3) |

## course_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/` | `list_courses` | Yes | `test_course_service.py` (7), `test_courses.py` (1) |
| POST | `/` | `create_course` | Yes | `test_course_service.py` (3), `test_courses.py` (3) |
| PATCH | `/checkpoint-questions/{question_id}` | `update_checkpoint_question` | Yes | `test_course_service.py` (2) |
| GET | `/checkpoints/csv-template` | `checkpoint_csv_template` | Yes | `test_course_service.py` (1) |
| DELETE | `/checkpoints/{checkpoint_id}` | `delete_checkpoint` | Yes | `test_course_service.py` (2) |
| PATCH | `/checkpoints/{checkpoint_id}` | `update_checkpoint` | Yes | `test_course_service.py` (2) |
| GET | `/health` | `health` | Yes | `test_course_service.py` (1) |
| DELETE | `/{course_id}` | `delete_course` | Yes | `test_course_service.py` (2) |
| GET | `/{course_id}` | `get_course` | Yes | `test_course_service.py` (3), `test_courses.py` (3) |
| PUT | `/{course_id}` | `update_course` | Yes | `test_course_service.py` (7), `test_courses.py` (4) |
| GET | `/{course_id}/modules` | `list_modules` | Yes | `test_course_service.py` (1) |
| POST | `/{course_id}/modules` | `create_module` | Yes | `test_course_service.py` (2), `test_courses.py` (1) |
| DELETE | `/{course_id}/modules/{module_id}` | `delete_module` | Yes | `test_delete_module_clears_its_children` (checked by hand) |
| PUT | `/{course_id}/modules/{module_id}` | `update_module` | Yes | `test_course_service.py` (3) |
| GET | `/{course_id}/modules/{module_id}/lessons` | `list_lessons` | Probable | `test_course_service.py` (6) |
| POST | `/{course_id}/modules/{module_id}/lessons` | `create_lesson` | Yes | `test_courses.py` (1) |
| DELETE | `/{course_id}/modules/{module_id}/lessons/{lesson_id}` | `delete_lesson` | Probable | `test_course_service.py` (1) |
| PUT | `/{course_id}/modules/{module_id}/lessons/{lesson_id}` | `update_lesson` | Probable | `test_course_service.py` (1) |
| DELETE | `/{course_id}/modules/{module_id}/lessons/{lesson_id}/checkpoints` | `clear_checkpoints` | Probable | `test_course_service.py` (1) |
| GET | `/{course_id}/modules/{module_id}/lessons/{lesson_id}/checkpoints` | `list_checkpoints` | Probable | `test_course_service.py` (1) |
| POST | `/{course_id}/modules/{module_id}/lessons/{lesson_id}/checkpoints/import-csv` | `import_checkpoints_csv` | Probable | `test_course_service.py` (helper) |
| GET | `/{course_id}/modules/{module_id}/materials` | `list_materials` | Probable | `test_course_service.py` (1) |
| POST | `/{course_id}/modules/{module_id}/materials` | `create_material` | Probable | `test_course_service.py` (2) |
| DELETE | `/{course_id}/modules/{module_id}/materials/{material_id}` | `delete_material` | Probable | `test_course_service.py` (1) |
| PUT | `/{course_id}/modules/{module_id}/materials/{material_id}` | `update_material` | Probable | `test_course_service.py` (1) |

## enrollment_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/api/enrollments` | `get_enrollment` | Yes | `test_enrollment.py` (3), `test_enrollment_service.py` (1) |
| GET | `/api/enrollments/admin/class-enrollments` | `admin_list_class_enrollments` | Yes | `test_enrollment_service.py` (1) |
| POST | `/api/enrollments/admin/class-enrollments` | `admin_grant_class_enrollment` | Yes | `test_enrollment_service.py` (1) |
| DELETE | `/api/enrollments/admin/class-enrollments/{enrollment_id}` | `admin_revoke_class_enrollment` | Yes | `test_enrollment_service.py` (1) |
| GET | `/api/enrollments/admin/class-packages` | `admin_list_class_packages` | Yes | `test_enrollment_service.py` (1) |
| POST | `/api/enrollments/admin/class-packages` | `admin_create_class_package` | Yes | `test_enrollment_service.py` (2) |
| POST | `/api/enrollments/admin/class-packages/auto-generate` | `admin_auto_generate_class_packages` | Yes | `test_enrollment.py` (1), `test_enrollment_service.py` (1) |
| DELETE | `/api/enrollments/admin/class-packages/{package_id}` | `admin_delete_class_package` | Yes | `test_enrollment_service.py` (2) |
| PATCH | `/api/enrollments/admin/class-packages/{package_id}` | `admin_update_class_package` | Yes | `test_enrollment.py` (1), `test_enrollment_service.py` (1) |
| GET | `/api/enrollments/admin/eligible` | `admin_eligible_students` | Yes | `test_enrollment_service.py` (2), `test_enrollment.py` (1) |
| GET | `/api/enrollments/admin/enrolled` | `admin_enrolled_students` | Yes | `test_enrollment.py` (1), `test_enrollment_service.py` (1) |
| POST | `/api/enrollments/admin/grant` | `admin_grant_access` | Yes | `test_enrollment_service.py` (4), `test_enrollment.py` (1) |
| DELETE | `/api/enrollments/admin/revoke` | `admin_revoke_access` | Yes | `test_enrollment_service.py` (2), `test_enrollment.py` (1) |
| GET | `/api/enrollments/class-packages` | `list_class_packages` | Yes | `test_enrollment_service.py` (2), `test_enrollment.py` (1) |
| POST | `/api/enrollments/class-packages/{package_id}/enroll-free` | `enroll_free_class_package` | Yes | `test_enrollment_service.py` (1) |
| GET | `/api/enrollments/me` | `list_my_enrollments` | Yes | `test_enrollment_service.py` (1) |
| GET | `/api/enrollments/me/access` | `my_course_access` | Yes | `test_enrollment_service.py` (1) |
| GET | `/api/enrollments/my-class-enrollments` | `my_class_enrollments` | Yes | `test_enrollment_service.py` (1) |
| GET | `/health` | `health` | Yes | `test_enrollment_service.py` (1) |

## notification_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/health` | `health` | Yes | `test_notification_service.py` (1) |
| GET | `/notification` | `notification_only` | Yes | `test_notification_service.py` (1) |

## payment_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/` | `list_user_payments` | Yes | `test_payment_service.py` (1) |
| GET | `/admin/bank-accounts` | `list_all_bank_accounts` | Yes | `test_payment_service.py` (2) |
| POST | `/admin/bank-accounts` | `create_bank_account` | Yes | `test_payment_service.py` (2) |
| DELETE | `/admin/bank-accounts/{account_id}` | `delete_bank_account` | Yes | `test_payment_service.py` (2) |
| PATCH | `/admin/bank-accounts/{account_id}` | `update_bank_account` | Yes | `test_payment_service.py` (2) |
| GET | `/bank-accounts` | `list_active_bank_accounts` | Yes | `test_payment_service.py` (1) |
| POST | `/checkout` | `init_checkout` | Yes | `test_payment_service.py` (3), `test_payments.py` (1) |
| POST | `/free-enroll` | `free_enroll` | Yes | `test_payment_service.py` (2), `test_payment_events.py` (1) |
| GET | `/health` | `health` | Yes | `test_payment_service.py` (1) |
| GET | `/internal/admin-stats` | `admin_stats_internal` | Yes | `test_payment_service.py` (2) |
| GET | `/receipts` | `list_receipts` | Yes | `test_payment_service.py` (1) |
| POST | `/receipts` | `upload_manual_receipt` | Yes | `test_payment_events.py` (3), `test_payments.py` (2) |
| PUT | `/receipts/{receipt_id}/verify` | `verify_receipt` | Yes | `test_payment_events.py` (2), `test_payment_service.py` (2) |
| POST | `/webhook` | `payhere_webhook` | Yes | `test_payment_service.py` (5) |

## progress_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/api/progress/courses/{course_id}` | `get_progress_dashboard` | Yes | `test_progress.py` (1), `test_progress_service.py` (1) |
| GET | `/api/progress/courses/{course_id}/leaderboard` | `get_leaderboard` | Yes | `test_progress.py` (1), `test_progress_service.py` (1) |
| GET | `/api/progress/courses/{course_id}/lessons/progress` | `get_lesson_progress` | Yes | `test_progress_service.py` (1) |
| POST | `/api/progress/courses/{course_id}/lessons/progress` | `mark_lesson_watched` | Probable | `test_progress_service.py` (helper) |
| GET | `/courses/{course_id}` | `get_progress_dashboard` | Yes | `test_progress_service.py` (3), `test_progress.py` (1) |
| GET | `/courses/{course_id}/leaderboard` | `get_leaderboard` | Yes | `test_progress_service.py` (3), `test_progress.py` (1) |
| GET | `/courses/{course_id}/lessons/progress` | `get_lesson_progress` | Yes | `test_progress_service.py` (1) |
| POST | `/courses/{course_id}/lessons/progress` | `mark_lesson_watched` | Probable | `test_progress_service.py` (helper) |
| GET | `/health` | `health` | Yes | `test_progress.py` (1), `test_progress_service.py` (1) |

## user_service

| Method | Path | Handler | Tested | Test file (direct tests) |
|---|---|---|---|---|
| GET | `/` | `list_users` | Yes | `test_users.py` (3), `test_user_service.py` (2) |
| POST | `/` | `create_own_profile` | Yes | `test_user_service.py` (5) |
| GET | `/grade-subjects` | `list_grade_subjects` | Yes | `test_user_service.py` (1) |
| POST | `/grade-subjects` | `create_grade_subject` | Yes | `test_user_service.py` (2) |
| DELETE | `/grade-subjects/{subject_id}` | `delete_grade_subject` | Yes | `test_user_service.py` (2) |
| PUT | `/grade-subjects/{subject_id}` | `update_grade_subject` | Yes | `test_user_service.py` (2) |
| GET | `/health` | `health` | Yes | `test_user_service.py` (1) |
| POST | `/referral/apply` | `referral_apply` | Yes | `test_user_service.py` (3) |
| GET | `/referral/events` | `referral_events` | Yes | `test_user_service.py` (1) |
| GET | `/referral/summary` | `referral_summary` | Yes | `test_user_service.py` (1) |
| GET | `/stats` | `get_role_stats` | Yes | `test_user_service.py` (1) |
| GET | `/streams` | `list_streams` | Yes | `test_user_service.py` (1) |
| POST | `/streams` | `create_stream` | Yes | `test_user_service.py` (2), `test_users.py` (1) |
| DELETE | `/streams/{stream_id}` | `delete_stream` | Yes | `test_user_service.py` (2), `test_users.py` (1) |
| PUT | `/streams/{stream_id}` | `update_stream` | Yes | `test_user_service.py` (2) |
| GET | `/subjects` | `get_subjects_for_grade` | Yes | `test_user_service.py` (1) |
| DELETE | `/{user_id}` | `delete_user` | Yes | `test_users.py` (3), `test_user_service.py` (1) |
| GET | `/{user_id}` | `get_user` | Yes | `test_auth.py` (13), `test_user_service.py` (8), `test_users.py` (5) |
| PUT | `/{user_id}` | `update_user` | Yes | `test_user_service.py` (3), `test_users.py` (3) |
| PUT | `/{user_id}/role` | `update_user_role` | Yes | `test_users.py` (3), `test_user_service.py` (1) |
