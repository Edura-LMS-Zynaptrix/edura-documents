# Complete Test Case Register

Generated: 2026-10-25 · Source: static scan of every `test_*` function in the repositories · Guideline: development guideline §6.3.3 / §6.4

## Summary

| Layer / suite | Test cases |
|---|---|
| Backend – admin_service | 66 |
| Backend – analytics_service | 97 |
| Backend – assessment_service | 142 |
| Backend – auth_service | 88 |
| Backend – content_service | 37 |
| Backend – course_service | 81 |
| Backend – enrollment_service | 65 |
| Backend – notification_service | 38 |
| Backend – payment_service | 44 |
| Backend – progress_service | 39 |
| Backend – user_service | 85 |
| Cross-service integration (edura-tests/integration) | 274 |
| Infrastructure (edura-infra) | 12 |
| End-to-end smoke (edura-tests/smoke) | 1 |
| **Total** | **1069** |

Notes:

- **Frontend: 0 test cases.** No frontend test files exist in the repository.
- Type is derived from the file: `test_migrations` → Migration; service-logic modules (templates, email, consumer, read-model, messaging, payment events) → Unit; other backend files that send HTTP requests to the FastAPI app → Integration (API); `edura-tests/integration` → Integration (cross-service).
- The **Description** is the test's docstring if present, otherwise its humanised name.
- **Status** is blank until the suite is executed; this register was generated from source and no test run was done. Fill *Actual Output / Status* per §6.3.3 after a run. The endpoint-level register is in `test-register.md`.

## Backend – admin_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0001 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0002 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_consumer` | Startup creates tables and starts consumer | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0003 | Integration (API) | P1 | – | `test_startup_still_starts_consumer_when_db_unavailable` | Startup still starts consumer when db unavailable | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0004 | Integration (API) | P1 | – | `test_admin_endpoint_welcomes_admin` | Admin endpoint welcomes admin | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0005 | Integration (API) | P1 | – | `test_admin_role_is_case_insensitive` | Admin role is case insensitive | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0006 | Integration (API) | P1 | – | `test_admin_endpoint_forbids_other_roles` | Admin endpoint forbids other roles | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0007 | Integration (API) | P1 | – | `test_admin_endpoint_requires_token` | Admin endpoint requires token | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0008 | Integration (API) | P1 | – | `test_admin_endpoint_rejects_expired_token` | Admin endpoint rejects expired token | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0009 | Integration (API) | P1 | – | `test_admin_endpoint_rejects_bad_signature` | Admin endpoint rejects bad signature | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0010 | Integration (API) | P1 | – | `test_guest_submits_feedback` | Guest submits feedback | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0011 | Integration (API) | P1 | – | `test_signed_in_feedback_is_linked_to_user` | Signed in feedback is linked to user | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0012 | Integration (API) | P1 | – | `test_feedback_with_invalid_token_is_saved_as_guest` | Feedback with invalid token is saved as guest | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0013 | Integration (API) | P1 | – | `test_feedback_text_is_trimmed_and_blank_subject_dropped` | Feedback text is trimmed and blank subject dropped | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0014 | Integration (API) | P1 | – | `test_feedback_subject_is_optional` | Feedback subject is optional | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0015 | Integration (API) | P1 | – | `test_feedback_validation` | Feedback validation | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0016 | Integration (API) | P1 | – | `test_list_feedback_newest_first` | List feedback newest first | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0017 | Integration (API) | P1 | – | `test_list_feedback_paginates` | List feedback paginates | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0018 | Integration (API) | P1 | – | `test_list_feedback_rejects_bad_paging` | List feedback rejects bad paging | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0019 | Integration (API) | P1 | – | `test_list_feedback_requires_admin` | List feedback requires admin | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0020 | Integration (API) | P1 | – | `test_mark_feedback_read` | Mark feedback read | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0021 | Integration (API) | P1 | – | `test_mark_feedback_read_not_found` | Mark feedback read not found | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0022 | Integration (API) | P1 | – | `test_mark_feedback_read_requires_admin` | Mark feedback read requires admin | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0023 | Integration (API) | P1 | – | `test_delete_feedback` | Delete feedback | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0024 | Integration (API) | P1 | – | `test_delete_feedback_not_found` | Delete feedback not found | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0025 | Integration (API) | P1 | – | `test_delete_feedback_requires_admin` | Delete feedback requires admin | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0026 | Integration (API) | P1 | – | `test_send_requires_identity` | Send requires identity | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0027 | Integration (API) | P1 | – | `test_guest_send_starts_and_reuses_thread` | Guest send starts and reuses thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0028 | Integration (API) | P1 | – | `test_signed_in_send_starts_user_thread` | Signed in send starts user thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0029 | Integration (API) | P1 | – | `test_signed_in_send_reuses_own_thread` | Signed in send reuses own thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0030 | Integration (API) | P1 | – | `test_signed_in_user_continues_unclaimed_guest_thread` | Signed in user continues unclaimed guest thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0031 | Integration (API) | P1 | – | `test_signed_in_user_cannot_use_another_users_thread` | Signed in user cannot use another users thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0032 | Integration (API) | P1 | – | `test_send_updates_last_message_at` | Send updates last message at | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0033 | Integration (API) | P1 | – | `test_send_validation` | Send validation | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0034 | Integration (API) | P1 | – | `test_history_empty_without_thread` | History empty without thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0035 | Integration (API) | P1 | – | `test_history_empty_without_identity` | History empty without identity | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0036 | Integration (API) | P1 | – | `test_guest_history_in_order` | Guest history in order | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0037 | Integration (API) | P1 | – | `test_signed_in_history_includes_admin_replies` | Signed in history includes admin replies | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0038 | Integration (API) | P1 | – | `test_guest_cannot_read_claimed_thread_by_session_id` | Guest cannot read claimed thread by session id | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0039 | Integration (API) | P1 | – | `test_sync_requires_sign_in` | Sync requires sign in | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0040 | Integration (API) | P1 | – | `test_sync_rejects_bad_session_id` | Sync rejects bad session id | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0041 | Integration (API) | P1 | – | `test_sync_nothing_to_sync` | Sync nothing to sync | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0042 | Integration (API) | P1 | – | `test_sync_attaches_guest_thread` | Sync attaches guest thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0043 | Integration (API) | P1 | – | `test_sync_merges_guest_thread_into_existing_one` | Sync merges guest thread into existing one | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0044 | Integration (API) | P1 | – | `test_sync_ignores_thread_claimed_by_someone_else` | Sync ignores thread claimed by someone else | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0045 | Integration (API) | P1 | – | `test_admin_chat_routes_require_admin` | Admin chat routes require admin | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0046 | Integration (API) | P1 | – | `test_admin_list_conversations_empty` | Admin list conversations empty | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0047 | Integration (API) | P1 | – | `test_admin_list_conversations_summary` | Admin list conversations summary | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0048 | Integration (API) | P1 | – | `test_admin_opens_existing_student_thread` | Admin opens existing student thread | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0049 | Integration (API) | P1 | – | `test_admin_starts_thread_with_known_student` | Admin starts thread with known student | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0050 | Integration (API) | P1 | – | `test_admin_cannot_start_thread_with_unknown_user` | Admin cannot start thread with unknown user | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0051 | Integration (API) | P1 | – | `test_admin_reading_messages_marks_student_messages_read` | Admin reading messages marks student messages read | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0052 | Integration (API) | P1 | – | `test_admin_messages_not_found` | Admin messages not found | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0053 | Integration (API) | P1 | – | `test_admin_reply` | Admin reply | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0054 | Integration (API) | P1 | – | `test_admin_reply_not_found` | Admin reply not found | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0055 | Integration (API) | P1 | – | `test_admin_reply_validation` | Admin reply validation | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0056 | Integration (API) | P1 | – | `test_admin_delete_conversation` | Admin delete conversation | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0057 | Integration (API) | P1 | – | `test_admin_delete_conversation_not_found` | Admin delete conversation not found | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0058 | Integration (API) | P1 | – | `test_display_names_skips_db_for_no_ids` | Display names skips db for no ids | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0059 | Integration (API) | P1 | – | `test_display_names_prefers_full_name_then_email` | Display names prefers full name then email | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0060 | Integration (API) | P1 | – | `test_consumer_stores_profile` | Consumer stores profile | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0061 | Integration (API) | P1 | – | `test_consumer_stores_account_then_profile` | Consumer stores account then profile | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0062 | Integration (API) | P1 | – | `test_consumer_deletes_profile` | Consumer deletes profile | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0063 | Integration (API) | P1 | – | `test_consumer_ignores_unrelated_events` | Consumer ignores unrelated events | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0064 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0065 | Integration (API) | P1 | – | `test_consumer_start_binds_admin_queue` | Consumer start binds admin queue | `edura-backend/admin_service/tests/test_admin.py` | |
| TC-0066 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/admin_service/tests/test_migrations.py` | |

## Backend – analytics_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0067 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0068 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_consumer` | Startup creates tables and starts consumer | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0069 | Integration (API) | P1 | – | `test_startup_still_starts_consumer_when_db_unavailable` | Startup still starts consumer when db unavailable | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0070 | Integration (API) | P1 | – | `test_analytics_endpoint_is_admin_only` | Analytics endpoint is admin only | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0071 | Integration (API) | P1 | – | `test_cache_round_trip` | Cache round trip | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0072 | Integration (API) | P1 | – | `test_cache_defaults_to_platform_stats_key_and_ttl` | Cache defaults to platform stats key and ttl | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0073 | Integration (API) | P1 | – | `test_cache_miss_returns_none` | Cache miss returns none | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0074 | Integration (API) | P1 | – | `test_cache_without_redis_is_a_no_op` | Cache without redis is a no op | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0075 | Integration (API) | P1 | – | `test_cache_errors_are_swallowed` | Cache errors are swallowed | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0076 | Integration (API) | P1 | – | `test_routes_still_work_when_redis_is_down` | Routes still work when redis is down | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0077 | Integration (API) | P1 | – | `test_platform_stats_is_public_and_ranks_top_four` | Platform stats is public and ranks top four | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0078 | Integration (API) | P1 | – | `test_platform_stats_with_empty_sources` | Platform stats with empty sources | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0079 | Integration (API) | P1 | – | `test_platform_stats_served_from_cache` | Platform stats served from cache | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0080 | Integration (API) | P1 | – | `test_platform_stats_from_the_read_model` | Platform stats from the read model | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0081 | Integration (API) | P1 | – | `test_summary_is_cached_for_a_minute` | Summary is cached for a minute | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0082 | Integration (API) | P1 | – | `test_empty_cached_summary_is_still_a_hit` | Empty cached summary is still a hit | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0083 | Integration (API) | P1 | – | `test_summary_503_when_read_model_down` | Summary 503 when read model down | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0084 | Integration (API) | P1 | – | `test_student_progress_404` | Student progress 404 | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0085 | Integration (API) | P1 | – | `test_me_progress_404_when_profile_missing` | Me progress 404 when profile missing | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0086 | Integration (API) | P1 | – | `test_me_progress_requires_sign_in` | Me progress requires sign in | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0087 | Integration (API) | P1 | – | `test_send_report_404_for_unknown_student` | Send report 404 for unknown student | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0088 | Integration (API) | P1 | – | `test_send_report_404_without_email` | Send report 404 without email | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0089 | Integration (API) | P1 | – | `test_send_report_503_when_account_lookup_fails` | Send report 503 when account lookup fails | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0090 | Integration (API) | P1 | – | `test_send_report_payload` | Send report payload | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0091 | Integration (API) | P1 | – | `test_send_report_names_unnamed_student` | Send report names unnamed student | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0092 | Integration (API) | P1 | – | `test_send_report_requires_admin` | Send report requires admin | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0093 | Integration (API) | P1 | – | `test_struggle_503_when_read_model_down` | Struggle 503 when read model down | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0094 | Integration (API) | P1 | – | `test_struggle_404_body` | Struggle 404 body | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0095 | Integration (API) | P1 | – | `test_struggle_requires_sign_in` | Struggle requires sign in | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0096 | Integration (API) | P1 | – | `test_admin_views_are_cached_for_thirty_seconds` | Admin views are cached for thirty seconds | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0097 | Integration (API) | P1 | – | `test_admin_analytics_503_when_read_model_down` | Admin analytics 503 when read model down | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0098 | Integration (API) | P1 | – | `test_admin_views_require_admin` | Admin views require admin | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0099 | Integration (API) | P1 | – | `test_when_handles_missing_naive_and_aware_timestamps` | When handles missing naive and aware timestamps | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0100 | Integration (API) | P1 | – | `test_build_stats_with_no_data` | Build stats with no data | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0101 | Integration (API) | P1 | – | `test_build_stats_fallback_labels` | Build stats fallback labels | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0102 | Integration (API) | P1 | – | `test_build_stats_keeps_eight_newest_activities` | Build stats keeps eight newest activities | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0103 | Integration (API) | P1 | – | `test_build_analytics_untitled_courses_and_ordering` | Build analytics untitled courses and ordering | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0104 | Integration (API) | P1 | – | `test_courses_for_looks_up_only_unpublished_courses` | Courses for looks up only unpublished courses | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0105 | Integration (API) | P1 | – | `test_run_wraps_query_errors_as_source_unavailable` | Run wraps query errors as source unavailable | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0106 | Integration (API) | P1 | – | `test_local_time_treats_naive_as_utc` | Local time treats naive as utc | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0107 | Integration (API) | P1 | – | `test_account` | Account | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0108 | Integration (API) | P1 | – | `test_profile_needs_a_name` | Profile needs a name | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0109 | Integration (API) | P1 | – | `test_empty_lookups_skip_the_database` | Empty lookups skip the database | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0110 | Integration (API) | P1 | – | `test_names_and_course_titles` | Names and course titles | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0111 | Integration (API) | P1 | – | `test_students_lists_named_students_by_name` | Students lists named students by name | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0112 | Integration (API) | P1 | – | `test_course_info_defaults` | Course info defaults | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0113 | Integration (API) | P1 | – | `test_course_modules` | Course modules | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0114 | Integration (API) | P1 | – | `test_exam_progress_combines_courses_and_single_lessons` | Exam progress combines courses and single lessons | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0115 | Integration (API) | P1 | – | `test_exam_progress_lists_only_this_students_attempts` | Exam progress lists only this students attempts | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0116 | Integration (API) | P1 | – | `test_first_attempts_for_course_without_exams` | First attempts for course without exams | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0117 | Integration (API) | P1 | – | `test_badge_count` | Badge count | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0118 | Integration (API) | P1 | – | `test_payments_without_completion_time_count_only_in_total` | Payments without completion time count only in total | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0119 | Integration (API) | P1 | – | `test_admin_sources_on_an_empty_read_model` | Admin sources on an empty read model | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0120 | Integration (API) | P1 | – | `test_enrollment_defaults_to_active_and_updates_in_place` | Enrollment defaults to active and updates in place | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0121 | Integration (API) | P1 | – | `test_assessment_upsert_defaults_and_update` | Assessment upsert defaults and update | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0122 | Integration (API) | P1 | – | `test_deleting_an_unknown_exam_is_harmless` | Deleting an unknown exam is harmless | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0123 | Integration (API) | P1 | – | `test_graded_event_without_submission_id_is_ignored` | Graded event without submission id is ignored | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0124 | Integration (API) | P1 | – | `test_graded_event_defaults_and_regrade` | Graded event defaults and regrade | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0125 | Integration (API) | P1 | – | `test_badges_are_stored_once_and_need_a_key` | Badges are stored once and need a key | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0126 | Integration (API) | P1 | – | `test_payment_without_order_id_is_ignored` | Payment without order id is ignored | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0127 | Integration (API) | P1 | – | `test_payment_defaults_completion_time_and_updates` | Payment defaults completion time and updates | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0128 | Integration (API) | P1 | – | `test_receipt_upload_does_not_reset_a_reviewed_receipt` | Receipt upload does not reset a reviewed receipt | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0129 | Integration (API) | P1 | – | `test_review_before_upload_creates_the_receipt` | Review before upload creates the receipt | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0130 | Integration (API) | P1 | – | `test_shared_events_go_to_the_replica_tables` | Shared events go to the replica tables | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0131 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0132 | Integration (API) | P1 | – | `test_consumer_start_binds_analytics_queue` | Consumer start binds analytics queue | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0133 | Integration (API) | P1 | – | `test_minutes_and_text_helpers` | Minutes and text helpers | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0134 | Integration (API) | P1 | – | `test_now_local_is_sri_lanka_time` | Now local is sri lanka time | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0135 | Integration (API) | P1 | – | `test_report_renders_subject_without_attempts_and_long_titles` | Report renders subject without attempts and long titles | `edura-backend/analytics_service/tests/test_analytics.py` | |
| TC-0136 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/analytics_service/tests/test_migrations.py` | |
| TC-0137 | Integration (API) | P1 | – | `test_student_progress_groups_by_course_and_orders_history` | Student progress groups by course and orders history | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0138 | Integration (API) | P1 | – | `test_student_progress_with_nothing_available` | Student progress with nothing available | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0139 | Integration (API) | P1 | – | `test_course_struggle_uses_first_attempts_and_ranks_hardest_first` | Course struggle uses first attempts and ranks hardest first | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0140 | Integration (API) | P1 | – | `test_report_pdf_renders_with_markup_characters_in_names` | Report pdf renders with markup characters in names | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0141 | Integration (API) | P1 | – | `test_admin_reads_a_students_progress` | Admin reads a students progress | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0142 | Integration (API) | P1 | – | `test_progress_is_admin_only` | Progress is admin only | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0143 | Integration (API) | P1 | – | `test_progress_404_for_unknown_or_non_student` | Progress 404 for unknown or non student | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0144 | Integration (API) | P1 | – | `test_student_reads_only_their_own_progress` | Student reads only their own progress | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0145 | Integration (API) | P1 | – | `test_summary` | Summary | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0146 | Integration (API) | P1 | – | `test_send_report_publishes_pdf_to_the_students_email` | Send report publishes pdf to the students email | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0147 | Integration (API) | P1 | – | `test_send_report_503_when_broker_is_down` | Send report 503 when broker is down | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0148 | Integration (API) | P1 | – | `test_source_outage_is_503_not_zeros` | Source outage is 503 not zeros | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0149 | Integration (API) | P1 | – | `test_struggle_route` | Struggle route | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0150 | Integration (API) | P1 | – | `test_dashboard_stats_and_activity_newest_first` | Dashboard stats and activity newest first | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0151 | Integration (API) | P1 | – | `test_analytics_names_courses_and_skips_deleted_ones` | Analytics names courses and skips deleted ones | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0152 | Integration (API) | P1 | – | `test_admin_routes` | Admin routes | `edura-backend/analytics_service/tests/test_progress.py` | |
| TC-0153 | Unit | P2 | – | `test_student_progress_comes_from_events_only` | Student progress comes from events only | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0154 | Unit | P2 | – | `test_nothing_is_open_without_access` | Nothing is open without access | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0155 | Unit | P2 | – | `test_expired_class_package_access_is_not_counted` | Expired class package access is not counted | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0156 | Unit | P2 | – | `test_a_lesson_granted_on_its_own_opens_only_that_lessons_exams` | A lesson granted on its own opens only that lessons exams | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0157 | Unit | P2 | – | `test_a_repeated_event_changes_nothing` | A repeated event changes nothing | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0158 | Unit | P2 | – | `test_deleting_an_exam_removes_its_attempts` | Deleting an exam removes its attempts | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0159 | Unit | P2 | – | `test_the_summary_lists_students_with_their_completion` | The summary lists students with their completion | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0160 | Unit | P2 | – | `test_struggle_analysis_uses_first_attempts` | Struggle analysis uses first attempts | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0161 | Unit | P2 | – | `test_admin_dashboard_numbers` | Admin dashboard numbers | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0162 | Unit | P2 | – | `test_deleted_courses_and_profiles_disappear` | Deleted courses and profiles disappear | `edura-backend/analytics_service/tests/test_readmodel.py` | |
| TC-0163 | Unit | P2 | – | `test_public_platform_numbers` | Public platform numbers | `edura-backend/analytics_service/tests/test_readmodel.py` | |

## Backend – assessment_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0164 | Integration (API) | P1 | – | `test_get_assessment` | Get assessment | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0165 | Integration (API) | P1 | – | `test_get_assessment_not_found` | Get assessment not found | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0166 | Integration (API) | P1 | – | `test_start_session_ac1` | Start session ac1 | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0167 | Integration (API) | P1 | – | `test_start_session_duplicate_blocked_ac5` | Start session duplicate blocked ac5 | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0168 | Integration (API) | P1 | – | `test_submit_assessment_ac2` | Submit assessment ac2 | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0169 | Integration (API) | P1 | – | `test_auto_submit_on_expiry_ac3` | Auto submit on expiry ac3 | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0170 | Integration (API) | P1 | – | `test_tab_switch_violation_ac4` | Tab switch violation ac4 | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0171 | Integration (API) | P1 | – | `test_other_violation_types` | Other violation types | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0172 | Integration (API) | P1 | – | `test_unauthorized_access` | Unauthorized access | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0173 | Integration (API) | P1 | – | `test_start_requires_enrollment` | Start requires enrollment | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0174 | Integration (API) | P1 | – | `test_start_blocked_before_scheduled_start` | Start blocked before scheduled start | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0175 | Integration (API) | P1 | – | `test_csv_template_download` | Csv template download | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0176 | Integration (API) | P1 | – | `test_csv_template_requires_teacher_or_admin` | Csv template requires teacher or admin | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0177 | Integration (API) | P1 | – | `test_csv_import_creates_valid_rows_and_reports_bad_ones` | Csv import creates valid rows and reports bad ones | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0178 | Integration (API) | P1 | – | `test_csv_import_rejects_non_csv` | Csv import rejects non csv | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0179 | Integration (API) | P1 | – | `test_list_by_module_orders_by_position_and_counts_questions` | List by module orders by position and counts questions | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0180 | Integration (API) | P1 | – | `test_perfect_first_attempt_earns_badges_once` | Perfect first attempt earns badges once | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0181 | Integration (API) | P1 | – | `test_rank_rows_ties_share_a_rank_and_districts_rank_separately` | Rank rows ties share a rank and districts rank separately | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0182 | Integration (API) | P1 | – | `test_leaderboard_is_public_and_uses_first_attempts` | Leaderboard is public and uses first attempts | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0183 | Integration (API) | P1 | – | `test_leaderboard_marks_caller_and_filters_district` | Leaderboard marks caller and filters district | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0184 | Integration (API) | P1 | – | `test_leaderboard_hides_unpublished_exams` | Leaderboard hides unpublished exams | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0185 | Integration (API) | P1 | – | `test_ranking_exams_public_and_per_student` | Ranking exams public and per student | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0186 | Integration (API) | P1 | – | `test_my_exam_rank` | My exam rank | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0187 | Integration (API) | P1 | – | `test_result_rank_matches_leaderboard_and_ignores_retakes` | Result rank matches leaderboard and ignores retakes | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0188 | Integration (API) | P1 | – | `test_sitting_an_exam_needs_the_access_list_to_say_so` | Sitting an exam needs the access list to say so | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0189 | Integration (API) | P1 | – | `test_a_lesson_grant_or_an_expired_grant_is_honoured` | A lesson grant or an expired grant is honoured | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0190 | Integration (API) | P1 | – | `test_a_teacher_can_only_manage_exams_of_courses_they_own` | A teacher can only manage exams of courses they own | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0191 | Integration (API) | P1 | – | `test_titles_and_leaderboard_names_come_from_the_local_copies` | Titles and leaderboard names come from the local copies | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0192 | Integration (API) | P1 | – | `test_the_graded_event_is_published_with_the_full_result` | The graded event is published with the full result | `edura-backend/assessment_service/tests/test_assessment.py` | |
| TC-0193 | Integration (API) | P1 | – | `test_health_needs_no_auth` | Health needs no auth | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0194 | Integration (API) | P1 | – | `test_startup_creates_tables_seeds_badges_and_starts_listeners` | Startup creates tables seeds badges and starts listeners | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0195 | Integration (API) | P1 | – | `test_startup_survives_db_and_seed_failures` | Startup survives db and seed failures | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0196 | Integration (API) | P1 | – | `test_consumer_start_binds_assessment_queue` | Consumer start binds assessment queue | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0197 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0198 | Integration (API) | P1 | – | `test_list_needs_a_filter` | List needs a filter | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0199 | Integration (API) | P1 | – | `test_list_hides_drafts_from_students_and_visitors` | List hides drafts from students and visitors | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0200 | Integration (API) | P1 | – | `test_student_cannot_read_a_draft_but_teacher_can` | Student cannot read a draft but teacher can | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0201 | Integration (API) | P1 | – | `test_get_requires_sign_in` | Get requires sign in | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0202 | Integration (API) | P1 | – | `test_create_exam_with_defaults_and_naive_start_as_utc` | Create exam with defaults and naive start as utc | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0203 | Integration (API) | P1 | – | `test_create_exam_permissions` | Create exam permissions | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0204 | Integration (API) | P1 | – | `test_teacher_gets_404_for_an_unknown_course` | Teacher gets 404 for an unknown course | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0205 | Integration (API) | P1 | – | `test_update_exam` | Update exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0206 | Integration (API) | P1 | – | `test_update_exam_errors` | Update exam errors | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0207 | Integration (API) | P1 | – | `test_delete_exam_removes_its_questions` | Delete exam removes its questions | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0208 | Integration (API) | P1 | – | `test_delete_all_exams_of_a_lesson` | Delete all exams of a lesson | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0209 | Integration (API) | P1 | – | `test_delete_empty_lesson_announces_nothing` | Delete empty lesson announces nothing | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0210 | Integration (API) | P1 | – | `test_delete_lesson_exams_needs_ownership` | Delete lesson exams needs ownership | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0211 | Integration (API) | P1 | – | `test_owner_lists_questions_with_answers` | Owner lists questions with answers | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0212 | Integration (API) | P1 | – | `test_create_question_from_options` | Create question from options | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0213 | Integration (API) | P1 | – | `test_create_question_explicit_answer_and_no_images` | Create question explicit answer and no images | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0214 | Integration (API) | P1 | – | `test_create_question_needs_a_correct_answer` | Create question needs a correct answer | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0215 | Integration (API) | P1 | – | `test_create_question_for_missing_exam` | Create question for missing exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0216 | Integration (API) | P1 | – | `test_update_question_options_set_the_answer` | Update question options set the answer | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0217 | Integration (API) | P1 | – | `test_update_question_options_may_omit_is_correct` | Update question options may omit is correct | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0218 | Integration (API) | P1 | – | `test_update_question_explicit_answer_wins` | Update question explicit answer wins | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0219 | Integration (API) | P1 | – | `test_update_question_clearing_options` | Update question clearing options | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0220 | Integration (API) | P1 | – | `test_update_and_delete_question_errors` | Update and delete question errors | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0221 | Integration (API) | P1 | – | `test_delete_question` | Delete question | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0222 | Integration (API) | P1 | – | `test_csv_import_too_large` | Csv import too large | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0223 | Integration (API) | P1 | – | `test_csv_import_must_be_utf8` | Csv import must be utf8 | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0224 | Integration (API) | P1 | – | `test_csv_import_with_only_bad_rows_creates_nothing` | Csv import with only bad rows creates nothing | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0225 | Integration (API) | P1 | – | `test_csv_import_needs_ownership` | Csv import needs ownership | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0226 | Integration (API) | P1 | – | `test_images_zip_attaches_question_and_option_images` | Images zip attaches question and option images | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0227 | Integration (API) | P1 | – | `test_images_zip_reports_upload_failures` | Images zip reports upload failures | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0228 | Integration (API) | P1 | – | `test_images_zip_rejects_bad_uploads` | Images zip rejects bad uploads | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0229 | Integration (API) | P1 | – | `test_images_zip_needs_ownership` | Images zip needs ownership | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0230 | Integration (API) | P1 | – | `test_safe_zip_limits` | Safe zip limits | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0231 | Integration (API) | P1 | – | `test_basename_handles_both_slashes` | Basename handles both slashes | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0232 | Integration (API) | P1 | – | `test_bulk_import_template_is_a_valid_bundle` | Bulk import template is a valid bundle | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0233 | Integration (API) | P1 | – | `test_bulk_import_creates_exams_and_reports_problems` | Bulk import creates exams and reports problems | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0234 | Integration (API) | P1 | – | `test_bulk_import_without_exams_csv` | Bulk import without exams csv | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0235 | Integration (API) | P1 | – | `test_bulk_import_ignores_deeply_nested_exams_csv` | Bulk import ignores deeply nested exams csv | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0236 | Integration (API) | P1 | – | `test_bulk_import_rejects_non_zip_and_non_owner` | Bulk import rejects non zip and non owner | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0237 | Integration (API) | P1 | – | `test_parse_helpers` | Parse helpers | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0238 | Integration (API) | P1 | – | `test_import_question_rows_continues_positions` | Import question rows continues positions | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0239 | Integration (API) | P1 | – | `test_upload_image_returns_url_then_public_id` | Upload image returns url then public id | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0240 | Integration (API) | P1 | – | `test_upload_image_refuses_non_images` | Upload image refuses non images | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0241 | Integration (API) | P1 | – | `test_upload_image_wraps_storage_errors` | Upload image wraps storage errors | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0242 | Integration (API) | P1 | – | `test_student_cannot_start_a_draft` | Student cannot start a draft | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0243 | Integration (API) | P1 | – | `test_teacher_can_preview_a_draft_without_enrollment` | Teacher can preview a draft without enrollment | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0244 | Integration (API) | P1 | – | `test_start_without_time_limit_gives_an_hour` | Start without time limit gives an hour | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0245 | Integration (API) | P1 | – | `test_start_again_after_the_old_session_expired` | Start again after the old session expired | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0246 | Integration (API) | P1 | – | `test_past_scheduled_start_is_open` | Past scheduled start is open | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0247 | Integration (API) | P1 | – | `test_submit_grades_and_clears_the_session` | Submit grades and clears the session | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0248 | Integration (API) | P1 | – | `test_submit_after_expiry_reuses_the_open_attempt` | Submit after expiry reuses the open attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0249 | Integration (API) | P1 | – | `test_submit_exam_without_questions_scores_zero` | Submit exam without questions scores zero | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0250 | Integration (API) | P1 | – | `test_submit_missing_exam_404` | Submit missing exam 404 | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0251 | Integration (API) | P1 | – | `test_badge_failure_does_not_fail_the_submit` | Badge failure does not fail the submit | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0252 | Integration (API) | P1 | – | `test_submit_returns_new_badges` | Submit returns new badges | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0253 | Integration (API) | P1 | – | `test_my_last_attempt` | My last attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0254 | Integration (API) | P1 | – | `test_my_last_attempt_is_served_on_the_api_prefixed_path` | My last attempt is served on the api prefixed path | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0255 | Integration (API) | P1 | – | `test_my_last_attempt_404_without_one` | My last attempt 404 without one | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0256 | Integration (API) | P1 | – | `test_my_attempts_summary_per_exam` | My attempts summary per exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0257 | Integration (API) | P1 | – | `test_my_attempts_for_course_without_exams` | My attempts for course without exams | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0258 | Integration (API) | P1 | – | `test_my_submissions_lists_attempts_newest_first` | My submissions lists attempts newest first | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0259 | Integration (API) | P1 | – | `test_my_submissions_empty_and_limit` | My submissions empty and limit | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0260 | Integration (API) | P1 | – | `test_student_reviews_own_attempt` | Student reviews own attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0261 | Integration (API) | P1 | – | `test_review_visibility` | Review visibility | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0262 | Integration (API) | P1 | – | `test_review_of_missing_or_unfinished_attempts` | Review of missing or unfinished attempts | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0263 | Integration (API) | P1 | – | `test_violation_types` | Violation types | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0264 | Integration (API) | P1 | – | `test_violation_without_session_uses_latest_attempt` | Violation without session uses latest attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0265 | Integration (API) | P1 | – | `test_violation_with_no_attempt_opens_one` | Violation with no attempt opens one | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0266 | Integration (API) | P1 | – | `test_violation_during_a_session_uses_its_attempt` | Violation during a session uses its attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0267 | Integration (API) | P1 | – | `test_ranking_exams_for_visitors_lists_every_attempted_exam` | Ranking exams for visitors lists every attempted exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0268 | Integration (API) | P1 | – | `test_leaderboard_pages_and_unknown_exam` | Leaderboard pages and unknown exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0269 | Integration (API) | P1 | – | `test_leaderboard_when_profiles_are_unavailable` | Leaderboard when profiles are unavailable | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0270 | Integration (API) | P1 | – | `test_my_rank_is_null_before_sitting` | My rank is null before sitting | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0271 | Integration (API) | P1 | – | `test_badge_catalogue_is_public_and_sorted` | Badge catalogue is public and sorted | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0272 | Integration (API) | P1 | – | `test_my_badges_and_dashboard` | My badges and dashboard | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0273 | Integration (API) | P1 | – | `test_seed_badges_is_idempotent` | Seed badges is idempotent | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0274 | Integration (API) | P1 | – | `test_early_bird` | Early bird | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0275 | Integration (API) | P1 | – | `test_night_owl` | Night owl | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0276 | Integration (API) | P1 | – | `test_daytime_attempt_earns_no_time_badges` | Daytime attempt earns no time badges | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0277 | Integration (API) | P1 | – | `test_consistency_king_needs_seven_days` | Consistency king needs seven days | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0278 | Integration (API) | P1 | – | `test_speed_demon_needs_a_third_of_the_time` | Speed demon needs a third of the time | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0279 | Integration (API) | P1 | – | `test_speed_demon_without_time_limit_uses_an_hour` | Speed demon without time limit uses an hour | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0280 | Integration (API) | P1 | – | `test_improved_star` | Improved star | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0281 | Integration (API) | P1 | – | `test_perfect_100_only_on_the_first_attempt` | Perfect 100 only on the first attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0282 | Integration (API) | P1 | – | `test_subject_expert_needs_five_first_passes_in_one_lesson` | Subject expert needs five first passes in one lesson | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0283 | Integration (API) | P1 | – | `test_first_step_only_on_the_first_paper` | First step only on the first paper | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0284 | Integration (API) | P1 | – | `test_century_club` | Century club | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0285 | Integration (API) | P1 | – | `test_junior_scholar_needs_four_active_weeks_and_an_old_account` | Junior scholar needs four active weeks and an old account | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0286 | Integration (API) | P1 | – | `test_badges_are_awarded_once_and_announced` | Badges are awarded once and announced | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0287 | Integration (API) | P1 | – | `test_concurrent_award_is_skipped` | Concurrent award is skipped | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0288 | Integration (API) | P1 | – | `test_local_time_conversion` | Local time conversion | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0289 | Integration (API) | P1 | – | `test_resync_announces_exams_badges_and_graded_attempts` | Resync announces exams badges and graded attempts | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0290 | Integration (API) | P1 | – | `test_resync_on_an_empty_database` | Resync on an empty database | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0291 | Integration (API) | P1 | – | `test_assessment_event_payload` | Assessment event payload | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0292 | Integration (API) | P1 | – | `test_badge_and_graded_events_without_timestamps` | Badge and graded events without timestamps | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0293 | Integration (API) | P1 | – | `test_lookups_with_no_ids_skip_the_database` | Lookups with no ids skip the database | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0294 | Integration (API) | P1 | – | `test_unknown_course_has_no_instructor` | Unknown course has no instructor | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0295 | Integration (API) | P1 | – | `test_memory_redis_get_set_delete` | Memory redis get set delete | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0296 | Integration (API) | P1 | – | `test_memory_redis_ttl` | Memory redis ttl | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0297 | Integration (API) | P1 | – | `test_memory_redis_expiry` | Memory redis expiry | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0298 | Integration (API) | P1 | – | `test_memory_redis_keys_by_prefix` | Memory redis keys by prefix | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0299 | Integration (API) | P1 | – | `test_get_redis_client_returns_the_module_client` | Get redis client returns the module client | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0300 | Integration (API) | P1 | – | `test_answers_of_tolerates_bad_json` | Answers of tolerates bad json | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0301 | Integration (API) | P1 | – | `test_time_taken_edge_cases` | Time taken edge cases | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0302 | Integration (API) | P1 | – | `test_question_helpers_tolerate_bad_json` | Question helpers tolerate bad json | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0303 | Integration (API) | P1 | – | `test_option_images_are_padded_and_trimmed` | Option images are padded and trimmed | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0304 | Integration (API) | P1 | – | `test_as_utc` | As utc | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0305 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/assessment_service/tests/test_migrations.py` | |

## Backend – auth_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0306 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0307 | Integration (API) | P1 | – | `test_startup_creates_tables_and_schedules_the_resync` | Startup creates tables and schedules the resync | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0308 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0309 | Integration (API) | P1 | – | `test_resync_reannounces_every_account` | Resync reannounces every account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0310 | Integration (API) | P1 | – | `test_public_registration_can_never_create_an_admin` | Public registration can never create an admin | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0311 | Integration (API) | P1 | – | `test_teachers_may_self_register` | Teachers may self register | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0312 | Integration (API) | P1 | – | `test_duplicate_registration` | Duplicate registration | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0313 | Integration (API) | P1 | – | `test_registration_profile_drops_empty_fields` | Registration profile drops empty fields | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0314 | Integration (API) | P1 | – | `test_password_strength_rules` | Password strength rules | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0315 | Integration (API) | P1 | – | `test_verification_link_for_a_changed_address_is_refused` | Verification link for a changed address is refused | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0316 | Integration (API) | P1 | – | `test_verifying_twice_announces_once` | Verifying twice announces once | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0317 | Integration (API) | P1 | – | `test_verification_link_for_a_deleted_account` | Verification link for a deleted account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0318 | Integration (API) | P1 | – | `test_resend_skips_accounts_that_need_no_link` | Resend skips accounts that need no link | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0319 | Integration (API) | P1 | – | `test_resend_is_throttled_and_same_for_unknown_addresses` | Resend is throttled and same for unknown addresses | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0320 | Integration (API) | P1 | – | `test_admin_route` | Admin route | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0321 | Integration (API) | P1 | – | `test_admin_creates_a_verified_admin_with_a_profile` | Admin creates a verified admin with a profile | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0322 | Integration (API) | P1 | – | `test_create_admin_errors` | Create admin errors | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0323 | Integration (API) | P1 | – | `test_deactivating_an_account_is_announced_and_blocks_login` | Deactivating an account is announced and blocks login | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0324 | Integration (API) | P1 | – | `test_admin_deletes_an_account` | Admin deletes an account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0325 | Integration (API) | P1 | – | `test_login_issues_a_token_and_a_secure_cookie` | Login issues a token and a secure cookie | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0326 | Integration (API) | P1 | – | `test_google_only_account_cannot_use_a_password` | Google only account cannot use a password | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0327 | Integration (API) | P1 | – | `test_refresh_from_the_cookie_rotates_it` | Refresh from the cookie rotates it | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0328 | Integration (API) | P1 | – | `test_refresh_errors` | Refresh errors | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0329 | Integration (API) | P1 | – | `test_expired_refresh_token` | Expired refresh token | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0330 | Integration (API) | P1 | – | `test_refresh_for_a_deleted_account` | Refresh for a deleted account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0331 | Integration (API) | P1 | – | `test_logout_without_a_cookie_still_succeeds` | Logout without a cookie still succeeds | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0332 | Integration (API) | P1 | – | `test_invalid_google_token` | Invalid google token | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0333 | Integration (API) | P1 | – | `test_new_google_user_without_a_name_uses_the_address` | New google user without a name uses the address | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0334 | Integration (API) | P1 | – | `test_google_links_onto_a_verified_password_account` | Google links onto a verified password account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0335 | Integration (API) | P1 | – | `test_returning_google_user_is_found_by_google_id` | Returning google user is found by google id | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0336 | Integration (API) | P1 | – | `test_passwordless_account_becomes_a_google_account` | Passwordless account becomes a google account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0337 | Integration (API) | P1 | – | `test_deactivated_google_account` | Deactivated google account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0338 | Integration (API) | P1 | – | `test_google_userinfo_call` | Google userinfo call | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0339 | Integration (API) | P1 | – | `test_me` | Me | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0340 | Integration (API) | P1 | – | `test_google_user_sets_a_password_then_logs_in_with_it` | Google user sets a password then logs in with it | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0341 | Integration (API) | P1 | – | `test_set_password_validation_and_missing_user` | Set password validation and missing user | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0342 | Integration (API) | P1 | – | `test_change_password` | Change password | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0343 | Integration (API) | P1 | – | `test_change_password_needs_an_existing_password` | Change password needs an existing password | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0344 | Integration (API) | P1 | – | `test_no_reset_link_for_a_deactivated_account` | No reset link for a deactivated account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0345 | Integration (API) | P1 | – | `test_reset_is_refused_once_the_account_is_deactivated` | Reset is refused once the account is deactivated | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0346 | Integration (API) | P1 | – | `test_reset_requires_matching_passwords` | Reset requires matching passwords | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0347 | Integration (API) | P1 | – | `test_reset_for_a_verified_account_is_not_reannounced` | Reset for a verified account is not reannounced | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0348 | Integration (API) | P1 | – | `test_reset_signs_out_every_session` | Reset signs out every session | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0349 | Integration (API) | P1 | – | `test_otp_round_trip_is_single_use` | Otp round trip is single use | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0350 | Integration (API) | P1 | – | `test_otp_purposes_are_separate` | Otp purposes are separate | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0351 | Integration (API) | P1 | – | `test_access_token_without_email` | Access token without email | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0352 | Integration (API) | P1 | – | `test_reset_token_parsing` | Reset token parsing | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0353 | Integration (API) | P1 | – | `test_verification_token_parsing` | Verification token parsing | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0354 | Integration (API) | P1 | – | `test_memory_redis_client` | Memory redis client | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0355 | Integration (API) | P1 | – | `test_refresh_token_is_stored_hashed` | Refresh token is stored hashed | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0356 | Integration (API) | P1 | – | `test_token_service_create_and_verify` | Token service create and verify | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0357 | Integration (API) | P1 | – | `test_otp_service_generate_and_verify` | Otp service generate and verify | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0358 | Integration (API) | P1 | – | `test_session_service_limit` | Session service limit | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0359 | Integration (API) | P1 | – | `test_register_and_login_success` | Register and login success | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0360 | Integration (API) | P1 | – | `test_login_invalid_credentials` | Login invalid credentials | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0361 | Integration (API) | P1 | – | `test_refresh_token_rotation_and_reuse` | Refresh token rotation and reuse | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0362 | Integration (API) | P1 | – | `test_protected_route_role_enforcement` | Protected route role enforcement | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0363 | Integration (API) | P1 | – | `test_missing_and_expired_token` | Missing and expired token | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0364 | Integration (API) | P1 | – | `test_register_rejects_weak_password` | Register rejects weak password | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0365 | Integration (API) | P1 | – | `test_forgot_password_does_not_reveal_unknown_emails` | Forgot password does not reveal unknown emails | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0366 | Integration (API) | P1 | – | `test_reset_password_flow_is_single_use_and_signs_out` | Reset password flow is single use and signs out | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0367 | Integration (API) | P1 | – | `test_reset_password_rejects_garbage_token` | Reset password rejects garbage token | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0368 | Integration (API) | P1 | – | `test_logout_revokes_refresh_token` | Logout revokes refresh token | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0369 | Integration (API) | P1 | – | `test_register_sends_a_verification_link` | Register sends a verification link | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0370 | Integration (API) | P1 | – | `test_unverified_login_hides_whether_the_address_exists` | Unverified login hides whether the address exists | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0371 | Integration (API) | P1 | – | `test_verification_link_is_reusable_but_only_for_verification` | Verification link is reusable but only for verification | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0372 | Integration (API) | P1 | – | `test_expired_verification_link_is_rejected` | Expired verification link is rejected | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0373 | Integration (API) | P1 | – | `test_resend_verification` | Resend verification | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0374 | Integration (API) | P1 | – | `test_register_announces_the_account_with_its_profile` | Register announces the account with its profile | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0375 | Integration (API) | P1 | – | `test_register_without_a_profile_announces_the_account_only` | Register without a profile announces the account only | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0376 | Integration (API) | P1 | – | `test_register_rejects_an_invalid_profile_before_announcing_anything` | Register rejects an invalid profile before announcing anything | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0377 | Integration (API) | P1 | – | `test_register_does_not_depend_on_any_other_service` | The broker being down must not stop an account being created. | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0378 | Integration (API) | P1 | – | `test_account_changes_are_announced` | Account changes are announced | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0379 | Integration (API) | P1 | – | `test_google_sign_in_verifies_and_drops_an_unverified_password` | Google sign in verifies and drops an unverified password | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0380 | Integration (API) | P1 | – | `test_google_without_a_verified_address_does_not_verify` | Google without a verified address does not verify | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0381 | Integration (API) | P1 | – | `test_password_reset_proves_the_address` | Password reset proves the address | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0382 | Integration (API) | P1 | – | `test_new_google_account_is_announced_with_the_google_name_and_photo` | New google account is announced with the google name and photo | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0383 | Integration (API) | P1 | – | `test_admin_created_by_admin_is_announced_with_a_profile` | Admin created by admin is announced with a profile | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0384 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/auth_service/tests/test_migrations.py` | |
| TC-0385 | Unit | P2 | – | `test_publish_never_raises_when_the_broker_is_down` | Publish never raises when the broker is down | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0386 | Unit | P2 | – | `test_a_down_broker_is_skipped_for_a_few_seconds` | A down broker is skipped for a few seconds | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0387 | Unit | P2 | – | `test_publish_reconnects_once_after_an_idle_connection_dropped` | Publish reconnects once after an idle connection dropped | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0388 | Unit | P2 | – | `test_a_consumer_hands_the_event_to_its_handler_and_acks` | A consumer hands the event to its handler and acks | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0389 | Unit | P2 | – | `test_a_message_that_is_not_json_is_dropped_not_retried` | A message that is not json is dropped not retried | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0390 | Unit | P2 | – | `test_a_failing_handler_is_tried_three_times_then_dropped` | A failing handler is tried three times then dropped | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0391 | Unit | P2 | – | `test_a_handler_that_recovers_is_not_called_again` | A handler that recovers is not called again | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0392 | Unit | P2 | – | `test_resync_can_be_switched_off` | Resync can be switched off | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0393 | Unit | P2 | – | `test_every_service_queue_listens_to_something_and_nothing_twice` | Every service queue listens to something and nothing twice | `edura-backend/auth_service/tests/test_shared_messaging.py` | |

## Backend – content_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0394 | Integration (API) | P1 | TestHealth | `test_health_returns_ok` | Health returns ok | `edura-backend/content_service/tests/test_content.py` | |
| TC-0395 | Integration (API) | P1 | TestSignedUrl | `test_missing_token_returns_401` | Missing token returns 401 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0396 | Integration (API) | P1 | TestSignedUrl | `test_student_not_enrolled_returns_403` | Student not enrolled returns 403 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0397 | Integration (API) | P1 | TestSignedUrl | `test_enrolled_student_gets_signed_url` | Enrolled student gets signed url | `edura-backend/content_service/tests/test_content.py` | |
| TC-0398 | Integration (API) | P1 | TestSignedUrl | `test_teacher_gets_signed_url_without_enrollment_check` | Teacher gets signed url without enrollment check | `edura-backend/content_service/tests/test_content.py` | |
| TC-0399 | Integration (API) | P1 | TestSignedUrl | `test_admin_gets_signed_url_without_enrollment_check` | Admin gets signed url without enrollment check | `edura-backend/content_service/tests/test_content.py` | |
| TC-0400 | Integration (API) | P1 | TestStreamLesson | `test_missing_token_returns_401` | Missing token returns 401 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0401 | Integration (API) | P1 | TestStreamLesson | `test_student_without_course_id_returns_422` | Student without course id returns 422 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0402 | Integration (API) | P1 | TestStreamLesson | `test_student_not_enrolled_returns_403` | Student not enrolled returns 403 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0403 | Integration (API) | P1 | TestStreamLesson | `test_enrolled_student_gets_embed_url` | Enrolled student gets embed url | `edura-backend/content_service/tests/test_content.py` | |
| TC-0404 | Integration (API) | P1 | TestStreamLesson | `test_teacher_gets_embed_url_without_enrollment` | Teacher gets embed url without enrollment | `edura-backend/content_service/tests/test_content.py` | |
| TC-0405 | Integration (API) | P1 | TestUpload | `test_student_cannot_upload` | Student cannot upload | `edura-backend/content_service/tests/test_content.py` | |
| TC-0406 | Integration (API) | P1 | TestUpload | `test_missing_token_returns_401` | Missing token returns 401 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0407 | Integration (API) | P1 | TestUpload | `test_file_too_large_returns_413` | File too large returns 413 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0408 | Integration (API) | P1 | TestUpload | `test_disallowed_mime_type_returns_415` | Disallowed mime type returns 415 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0409 | Integration (API) | P1 | TestUpload | `test_mime_mismatch_returns_415` | Mime mismatch returns 415 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0410 | Integration (API) | P1 | TestUpload | `test_valid_pdf_upload_passes` | Valid pdf upload passes | `edura-backend/content_service/tests/test_content.py` | |
| TC-0411 | Integration (API) | P1 | TestUpload | `test_valid_png_upload_passes` | Valid png upload passes | `edura-backend/content_service/tests/test_content.py` | |
| TC-0412 | Integration (API) | P1 | TestUpload | `test_admin_can_upload` | Admin can upload | `edura-backend/content_service/tests/test_content.py` | |
| TC-0413 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_consumer` | Startup creates tables and starts consumer | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0414 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0415 | Integration (API) | P1 | – | `test_access_comes_from_access_events` | Access comes from access events | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0416 | Integration (API) | P1 | – | `test_enrolled_student_streams_through_the_real_access_check` | Enrolled student streams through the real access check | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0417 | Integration (API) | P1 | – | `test_consumer_start_and_rollback` | Consumer start and rollback | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0418 | Integration (API) | P1 | – | `test_material_upload` | Material upload | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0419 | Integration (API) | P1 | – | `test_material_upload_rejections` | Material upload rejections | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0420 | Integration (API) | P1 | – | `test_material_upload_is_for_staff` | Material upload is for staff | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0421 | Integration (API) | P1 | – | `test_delete_uploaded_asset` | Delete uploaded asset | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0422 | Integration (API) | P1 | – | `test_only_content_assets_can_be_deleted` | Only content assets can be deleted | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0423 | Integration (API) | P1 | – | `test_delete_asset_validation_and_roles` | Delete asset validation and roles | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0424 | Integration (API) | P1 | – | `test_any_user_can_upload_an_avatar` | Any user can upload an avatar | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0425 | Integration (API) | P1 | – | `test_avatar_rejections` | Avatar rejections | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0426 | Integration (API) | P1 | – | `test_missing_credentials_are_a_503` | Missing credentials are a 503 | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0427 | Integration (API) | P1 | – | `test_upload_asset_passes_safe_options` | Upload asset passes safe options | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0428 | Integration (API) | P1 | – | `test_delete_asset_tries_each_resource_type` | Delete asset tries each resource type | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0429 | Integration (API) | P1 | – | `test_signed_url_expires_in_an_hour` | Signed url expires in an hour | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0430 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/content_service/tests/test_migrations.py` | |

## Backend – course_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0431 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0432 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_listeners` | Startup creates tables and starts listeners | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0433 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0434 | Integration (API) | P1 | – | `test_resync_reannounces_every_course_and_lesson` | Resync reannounces every course and lesson | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0435 | Integration (API) | P1 | – | `test_consumer_stores_access_and_start_binds_queue` | Consumer stores access and start binds queue | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0436 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0437 | Integration (API) | P1 | – | `test_grade_bands` | Grade bands | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0438 | Integration (API) | P1 | – | `test_public_sees_only_published_courses` | Public sees only published courses | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0439 | Integration (API) | P1 | – | `test_staff_filter_by_status` | Staff filter by status | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0440 | Integration (API) | P1 | – | `test_grade_filter_keeps_ungraded_courses` | Grade filter keeps ungraded courses | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0441 | Integration (API) | P1 | – | `test_stream_filter_applies_only_at_a_level` | Stream filter applies only at a level | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0442 | Integration (API) | P1 | – | `test_pagination_and_page_size_limits` | Pagination and page size limits | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0443 | Integration (API) | P1 | – | `test_include_modules_hides_inactive_lessons_from_students` | Include modules hides inactive lessons from students | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0444 | Integration (API) | P1 | – | `test_include_modules_with_no_courses` | Include modules with no courses | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0445 | Integration (API) | P1 | – | `test_course_without_modules_lists_empty` | Course without modules lists empty | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0446 | Integration (API) | P1 | – | `test_get_course_visibility` | Get course visibility | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0447 | Integration (API) | P1 | – | `test_list_modules` | List modules | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0448 | Integration (API) | P1 | – | `test_create_course_as_draft` | Create course as draft | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0449 | Integration (API) | P1 | – | `test_create_course_validation` | Create course validation | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0450 | Integration (API) | P1 | – | `test_create_course_permissions` | Create course permissions | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0451 | Integration (API) | P1 | – | `test_update_course_fields` | Update course fields | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0452 | Integration (API) | P1 | – | `test_update_course_validation` | Update course validation | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0453 | Integration (API) | P1 | – | `test_publishing_a_video_course_needs_a_video` | Publishing a video course needs a video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0454 | Integration (API) | P1 | – | `test_publishing_an_exam_course_needs_only_a_lesson` | Publishing an exam course needs only a lesson | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0455 | Integration (API) | P1 | – | `test_switching_to_exam_while_publishing_uses_the_new_type` | Switching to exam while publishing uses the new type | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0456 | Integration (API) | P1 | – | `test_archiving_unpublishes` | Archiving unpublishes | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0457 | Integration (API) | P1 | – | `test_course_ownership` | Course ownership | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0458 | Integration (API) | P1 | – | `test_delete_course_removes_everything_under_it` | Delete course removes everything under it | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0459 | Integration (API) | P1 | – | `test_create_module` | Create module | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0460 | Integration (API) | P1 | – | `test_module_ownership_and_missing` | Module ownership and missing | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0461 | Integration (API) | P1 | – | `test_module_must_belong_to_the_course` | Module must belong to the course | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0462 | Integration (API) | P1 | – | `test_update_module` | Update module | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0463 | Integration (API) | P1 | – | `test_delete_module_clears_its_children` | Delete module clears its children | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0464 | Integration (API) | P1 | – | `test_delete_empty_module` | Delete empty module | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0465 | Integration (API) | P1 | – | `test_create_and_update_video` | Create and update video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0466 | Integration (API) | P1 | – | `test_create_video_needs_a_youtube_id` | Create video needs a youtube id | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0467 | Integration (API) | P1 | – | `test_video_not_found` | Video not found | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0468 | Integration (API) | P1 | – | `test_delete_video_unpins_its_materials` | Delete video unpins its materials | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0469 | Integration (API) | P1 | – | `test_videos_need_sign_in` | Videos need sign in | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0470 | Integration (API) | P1 | – | `test_students_need_access_to_open_videos` | Students need access to open videos | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0471 | Integration (API) | P1 | – | `test_staff_open_videos_without_enrollment` | Staff open videos without enrollment | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0472 | Integration (API) | P1 | – | `test_inactive_lesson_is_hidden_from_students` | Inactive lesson is hidden from students | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0473 | Integration (API) | P1 | – | `test_videos_list_with_checkpoints_in_order` | Videos list with checkpoints in order | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0474 | Integration (API) | P1 | – | `test_videos_of_a_draft_course_are_hidden` | Videos of a draft course are hidden | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0475 | Integration (API) | P1 | – | `test_empty_lesson_has_no_videos` | Empty lesson has no videos | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0476 | Integration (API) | P1 | – | `test_create_material_pinned_to_a_video` | Create material pinned to a video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0477 | Integration (API) | P1 | – | `test_material_cannot_pin_a_video_from_another_lesson` | Material cannot pin a video from another lesson | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0478 | Integration (API) | P1 | – | `test_list_materials_filtered_by_video` | List materials filtered by video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0479 | Integration (API) | P1 | – | `test_update_material` | Update material | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0480 | Integration (API) | P1 | – | `test_material_not_found_and_delete` | Material not found and delete | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0481 | Integration (API) | P1 | – | `test_parse_timestamp` | Parse timestamp | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0482 | Integration (API) | P1 | – | `test_parse_timestamp_rejects` | Parse timestamp rejects | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0483 | Integration (API) | P1 | – | `test_checkpoint_template` | Checkpoint template | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0484 | Integration (API) | P1 | – | `test_import_checkpoints` | Import checkpoints | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0485 | Integration (API) | P1 | – | `test_import_adds_to_an_existing_checkpoint` | Import adds to an existing checkpoint | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0486 | Integration (API) | P1 | – | `test_import_checkpoint_errors` | Import checkpoint errors | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0487 | Integration (API) | P1 | – | `test_checkpoints_for_a_missing_video` | Checkpoints for a missing video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0488 | Integration (API) | P1 | – | `test_clear_checkpoints` | Clear checkpoints | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0489 | Integration (API) | P1 | – | `test_move_checkpoint` | Move checkpoint | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0490 | Integration (API) | P1 | – | `test_checkpoint_ownership_and_missing` | Checkpoint ownership and missing | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0491 | Integration (API) | P1 | – | `test_delete_checkpoint` | Delete checkpoint | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0492 | Integration (API) | P1 | – | `test_edit_checkpoint_question` | Edit checkpoint question | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0493 | Integration (API) | P1 | – | `test_checkpoint_question_validation` | Checkpoint question validation | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0494 | Integration (API) | P1 | – | `test_course_event_defaults` | Course event defaults | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0495 | Integration (API) | P1 | TestAssertCourseOwner | `test_matching_teacher_passes` | Matching teacher passes | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0496 | Integration (API) | P1 | TestAssertCourseOwner | `test_mismatched_teacher_raises_403` | Mismatched teacher raises 403 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0497 | Integration (API) | P1 | TestAssertCourseOwner | `test_admin_bypasses_ownership` | Admin bypasses ownership | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0498 | Integration (API) | P1 | TestStudentBlockedFromCreateCourse | `test_student_cannot_create_course` | Student cannot create course | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0499 | Integration (API) | P1 | TestStudentBlockedFromCreateCourse | `test_no_token_returns_401` | No token returns 401 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0500 | Integration (API) | P1 | TestCreateAndGetCourse | `test_teacher_creates_course_returns_201` | Teacher creates course returns 201 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0501 | Integration (API) | P1 | TestCreateAndGetCourse | `test_get_course_by_id` | Get course by id | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0502 | Integration (API) | P1 | TestCreateAndGetCourse | `test_get_nonexistent_course_returns_404` | Get nonexistent course returns 404 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0503 | Integration (API) | P1 | TestOwnershipEnforcement | `test_teacher_b_cannot_update_teacher_a_course` | Teacher b cannot update teacher a course | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0504 | Integration (API) | P1 | TestOwnershipEnforcement | `test_admin_can_update_any_course` | Admin can update any course | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0505 | Integration (API) | P1 | TestPublishCourse | `test_publish_requires_module_with_lesson` | Publish requires module with lesson | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0506 | Integration (API) | P1 | TestPublishCourse | `test_publish_with_content_fires_rabbitmq_event` | Publish with content fires rabbitmq event | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0507 | Integration (API) | P1 | TestModuleAndLessonCRUD | `test_create_module_returns_201` | Create module returns 201 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0508 | Integration (API) | P1 | TestModuleAndLessonCRUD | `test_create_lesson_returns_201` | Create lesson returns 201 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0509 | Integration (API) | P1 | TestStudentCourseBrowse | `test_student_only_sees_published_courses` | Student only sees published courses | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0510 | Integration (API) | P1 | TestStudentCourseBrowse | `test_student_cannot_get_draft_course_directly` | Student cannot get draft course directly | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0511 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/course_service/tests/test_migrations.py` | |

## Backend – enrollment_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0512 | Integration (API) | P1 | – | `test_get_enrollment_success` | Get enrollment success | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0513 | Integration (API) | P1 | – | `test_get_enrollment_not_found_returns_404` | Get enrollment not found returns 404 | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0514 | Integration (API) | P1 | – | `test_enrollment_lookup_needs_login_and_is_private` | Enrollment lookup needs login and is private | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0515 | Integration (API) | P1 | – | `test_payment_success_activates_the_enrollment_and_announces_it` | Payment success activates the enrollment and announces it | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0516 | Integration (API) | P1 | – | `test_a_repeated_payment_extends_expiry_without_a_second_enrollment` | A repeated payment extends expiry without a second enrollment | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0517 | Integration (API) | P1 | – | `test_subscription_expiry_suspends_and_removes_access` | Subscription expiry suspends and removes access | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0518 | Integration (API) | P1 | – | `test_class_package_opens_published_courses_of_its_grade_until_it_expires` | Class package opens published courses of its grade until it expires | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0519 | Integration (API) | P1 | – | `test_an_expired_or_inactive_package_opens_nothing` | An expired or inactive package opens nothing | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0520 | Integration (API) | P1 | – | `test_a_lesson_grant_opens_just_that_lesson_unless_the_whole_course_is_open` | A lesson grant opens just that lesson unless the whole course is open | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0521 | Integration (API) | P1 | – | `test_a_package_holders_access_is_refreshed_when_a_course_is_published` | A package holders access is refreshed when a course is published | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0522 | Integration (API) | P1 | – | `test_renaming_a_course_does_not_re_announce_anyones_access` | Renaming a course does not re announce anyones access | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0523 | Integration (API) | P1 | – | `test_the_course_copy_follows_the_catalogue` | The course copy follows the catalogue | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0524 | Integration (API) | P1 | – | `test_eligible_students_are_those_in_the_course_grade_band_without_access` | Eligible students are those in the course grade band without access | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0525 | Integration (API) | P1 | – | `test_admin_grant_enrolls_announces_and_lists_by_name` | Admin grant enrolls announces and lists by name | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0526 | Integration (API) | P1 | – | `test_package_names_use_the_local_stream_copy` | Package names use the local stream copy | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0527 | Integration (API) | P1 | – | `test_auto_generate_makes_a_package_per_grade_and_active_stream` | Auto generate makes a package per grade and active stream | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0528 | Integration (API) | P1 | – | `test_class_package_changes_are_announced_to_holders` | Class package changes are announced to holders | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0529 | Integration (API) | P1 | – | `test_the_old_internal_endpoints_are_gone` | The old internal endpoints are gone | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0530 | Integration (API) | P1 | – | `test_this_service_reads_people_from_its_own_copy` | This service reads people from its own copy | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0531 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0532 | Integration (API) | P1 | – | `test_lifespan_creates_tables_and_starts_listeners` | Lifespan creates tables and starts listeners | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0533 | Integration (API) | P1 | – | `test_lifespan_survives_schema_errors` | Lifespan survives schema errors | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0534 | Integration (API) | P1 | – | `test_resync_announces_access_and_enrollments` | Resync announces access and enrollments | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0535 | Integration (API) | P1 | – | `test_consumer_start_binds_enrollment_queue` | Consumer start binds enrollment queue | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0536 | Integration (API) | P1 | – | `test_incomplete_payment_and_expiry_events_are_ignored` | Incomplete payment and expiry events are ignored | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0537 | Integration (API) | P1 | – | `test_expiry_without_enrollment_still_announces_access` | Expiry without enrollment still announces access | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0538 | Integration (API) | P1 | – | `test_people_and_streams_go_to_their_copies` | People and streams go to their copies | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0539 | Integration (API) | P1 | – | `test_deleting_a_course_reannounces_package_holders` | Deleting a course reannounces package holders | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0540 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0541 | Integration (API) | P1 | – | `test_lapsed_active_enrollment_restarts_from_now` | Lapsed active enrollment restarts from now | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0542 | Integration (API) | P1 | – | `test_suspended_enrollment_is_reactivated` | Suspended enrollment is reactivated | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0543 | Integration (API) | P1 | – | `test_suspend_unknown_enrollment_returns_none` | Suspend unknown enrollment returns none | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0544 | Integration (API) | P1 | – | `test_allowed_student_grades` | Allowed student grades | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0545 | Integration (API) | P1 | – | `test_package_covers` | Package covers | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0546 | Integration (API) | P1 | – | `test_course_access_paths` | Course access paths | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0547 | Integration (API) | P1 | – | `test_grant_package_reactivates_an_existing_row` | Grant package reactivates an existing row | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0548 | Integration (API) | P1 | – | `test_direct_enrollment_wins_over_package_end_date` | Direct enrollment wins over package end date | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0549 | Integration (API) | P1 | – | `test_my_enrollments_include_lesson_grants` | My enrollments include lesson grants | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0550 | Integration (API) | P1 | – | `test_my_access_to_a_course` | My access to a course | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0551 | Integration (API) | P1 | – | `test_get_enrollment_as_admin` | Get enrollment as admin | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0552 | Integration (API) | P1 | – | `test_list_packages_by_grade_and_stream` | List packages by grade and stream | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0553 | Integration (API) | P1 | – | `test_list_packages_marks_the_callers_own` | List packages marks the callers own | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0554 | Integration (API) | P1 | – | `test_enroll_in_a_free_package` | Enroll in a free package | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0555 | Integration (API) | P1 | – | `test_free_enroll_errors` | Free enroll errors | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0556 | Integration (API) | P1 | – | `test_my_class_enrollments` | My class enrollments | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0557 | Integration (API) | P1 | – | `test_admin_creates_and_filters_packages` | Admin creates and filters packages | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0558 | Integration (API) | P1 | – | `test_package_validation` | Package validation | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0559 | Integration (API) | P1 | – | `test_admin_package_routes_are_admin_only` | Admin package routes are admin only | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0560 | Integration (API) | P1 | – | `test_update_and_delete_missing_package` | Update and delete missing package | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0561 | Integration (API) | P1 | – | `test_deleting_a_package_removes_holders_and_reannounces` | Deleting a package removes holders and reannounces | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0562 | Integration (API) | P1 | – | `test_admin_lists_class_enrollments_with_names` | Admin lists class enrollments with names | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0563 | Integration (API) | P1 | – | `test_admin_grants_a_package_with_an_end_date` | Admin grants a package with an end date | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0564 | Integration (API) | P1 | – | `test_admin_revokes_a_class_enrollment` | Admin revokes a class enrollment | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0565 | Integration (API) | P1 | – | `test_grant_reactivates_a_cancelled_enrollment` | Grant reactivates a cancelled enrollment | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0566 | Integration (API) | P1 | – | `test_grant_skips_students_who_already_have_it` | Grant skips students who already have it | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0567 | Integration (API) | P1 | – | `test_grant_a_single_lesson` | Grant a single lesson | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0568 | Integration (API) | P1 | – | `test_grant_validation` | Grant validation | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0569 | Integration (API) | P1 | – | `test_revoke_a_course_keeps_the_record` | Revoke a course keeps the record | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0570 | Integration (API) | P1 | – | `test_revoke_a_lesson` | Revoke a lesson | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0571 | Integration (API) | P1 | – | `test_enrolled_list_includes_lesson_grants` | Enrolled list includes lesson grants | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0572 | Integration (API) | P1 | – | `test_eligible_needs_a_known_course` | Eligible needs a known course | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0573 | Integration (API) | P1 | – | `test_eligible_search_by_school` | Eligible search by school | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0574 | Integration (API) | P1 | – | `test_display_names_with_no_ids` | Display names with no ids | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0575 | Integration (API) | P1 | – | `test_enrollment_activated_payload` | Enrollment activated payload | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0576 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/enrollment_service/tests/test_migrations.py` | |

## Backend – notification_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0577 | Unit | P2 | – | `test_process_otp_requested_success` | Process otp requested success | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0578 | Unit | P2 | – | `test_process_payment_success` | Process payment success | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0579 | Unit | P2 | – | `test_process_certificate_issued` | Process certificate issued | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0580 | Unit | P2 | – | `test_process_proctoring_violation` | Process proctoring violation | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0581 | Unit | P2 | – | `test_email_failure_acks_and_logs_failed` | Email failure acks and logs failed | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0582 | Unit | P2 | – | `test_missing_email_acks_without_processing` | Missing email acks without processing | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0583 | Unit | P2 | – | `test_unhandled_routing_key_acks` | Unhandled routing key acks | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0584 | Unit | P2 | – | `test_start_consumer` | Start consumer | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0585 | Unit | P2 | – | `test_process_progress_report_attaches_pdf` | Process progress report attaches pdf | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0586 | Unit | P2 | – | `test_process_email_verification_sends_the_link` | Process email verification sends the link | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0587 | Unit | P2 | – | `test_password_reset_email_includes_reset_link` | Password reset email includes reset link | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0588 | Unit | P2 | – | `test_password_reset_email_uses_default_values` | Password reset email uses default values | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0589 | Unit | P2 | – | `test_send_email_posts_to_resend_with_the_api_key` | Send email posts to resend with the api key | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0590 | Unit | P2 | – | `test_send_email_with_pdf_attachment` | Send email with pdf attachment | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0591 | Unit | P2 | – | `test_no_attachments_key_when_there_are_none` | No attachments key when there are none | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0592 | Unit | P2 | – | `test_missing_api_key_fails_clearly_without_calling_resend` | Missing api key fails clearly without calling resend | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0593 | Unit | P2 | – | `test_a_rejected_email_raises_with_resends_reason` | A rejected email raises with resends reason | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0594 | Unit | P2 | – | `test_an_unreachable_resend_raises_a_delivery_error` | An unreachable resend raises a delivery error | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0595 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/notification_service/tests/test_migrations.py` | |
| TC-0596 | Integration (API) | P1 | – | `test_password_changed_email` | Password changed email | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0597 | Integration (API) | P1 | – | `test_student_email_and_id_fields_are_accepted` | Student email and id fields are accepted | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0598 | Integration (API) | P1 | – | `test_verification_link_lifetime_is_shown_in_hours` | Verification link lifetime is shown in hours | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0599 | Integration (API) | P1 | – | `test_progress_report_subject_without_a_month` | Progress report subject without a month | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0600 | Integration (API) | P1 | – | `test_broken_messages_are_dropped_not_requeued` | Broken messages are dropped not requeued | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0601 | Integration (API) | P1 | – | `test_consumer_retries_until_the_broker_is_reachable` | Consumer retries until the broker is reachable | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0602 | Integration (API) | P1 | – | `test_prepare_database_creates_tables_and_tolerates_sqlite` | Prepare database creates tables and tolerates sqlite | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0603 | Integration (API) | P1 | – | `test_prepare_database_survives_create_all_failure` | Prepare database survives create all failure | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0604 | Integration (API) | P1 | – | `test_enum_migrations_run_on_postgres` | Enum migrations run on postgres | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0605 | Integration (API) | P1 | – | `test_resend_error_that_is_not_json` | Resend error that is not json | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0606 | Integration (API) | P1 | – | `test_resend_error_without_a_message_uses_the_body` | Resend error without a message uses the body | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0607 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0608 | Integration (API) | P1 | – | `test_notification_route_is_for_notification_managers` | Notification route is for notification managers | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0609 | Integration (API) | P1 | – | `test_startup_creates_tables` | Startup creates tables | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0610 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0611 | Unit | P2 | – | `test_render_otp_email` | Render otp email | `edura-backend/notification_service/tests/test_templates.py` | |
| TC-0612 | Unit | P2 | – | `test_render_payment_confirm` | Render payment confirm | `edura-backend/notification_service/tests/test_templates.py` | |
| TC-0613 | Unit | P2 | – | `test_render_cert_issued` | Render cert issued | `edura-backend/notification_service/tests/test_templates.py` | |
| TC-0614 | Unit | P2 | – | `test_render_violation_alert` | Render violation alert | `edura-backend/notification_service/tests/test_templates.py` | |

## Backend – payment_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0615 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/payment_service/tests/test_migrations.py` | |
| TC-0616 | Unit | P2 | – | `test_the_course_price_copy_follows_catalogue_events` | The course price copy follows catalogue events | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0617 | Unit | P2 | – | `test_free_enrollment_is_decided_from_the_local_price` | Free enrollment is decided from the local price | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0618 | Unit | P2 | – | `test_receipt_is_checked_by_its_bytes_stored_and_announced` | Receipt is checked by its bytes stored and announced | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0619 | Unit | P2 | – | `test_approving_a_receipt_announces_the_payment_and_the_review` | Approving a receipt announces the payment and the review | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0620 | Unit | P2 | – | `test_rejecting_a_receipt_announces_only_the_review` | Rejecting a receipt announces only the review | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0621 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0622 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_consumer` | Startup creates tables and starts consumer | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0623 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0624 | Integration (API) | P1 | – | `test_consumer_start_binds_payment_queue` | Consumer start binds payment queue | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0625 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0626 | Integration (API) | P1 | – | `test_checkout_creates_a_pending_payment_with_a_valid_hash` | Checkout creates a pending payment with a valid hash | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0627 | Integration (API) | P1 | – | `test_checkout_without_amount_defaults_to_1000` | Checkout without amount defaults to 1000 | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0628 | Integration (API) | P1 | – | `test_checkout_roles` | Checkout roles | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0629 | Integration (API) | P1 | – | `test_webhook_confirms_payment_and_announces_it` | Webhook confirms payment and announces it | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0630 | Integration (API) | P1 | – | `test_webhook_is_idempotent` | Webhook is idempotent | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0631 | Integration (API) | P1 | – | `test_webhook_failure_status_marks_payment_failed` | Webhook failure status marks payment failed | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0632 | Integration (API) | P1 | – | `test_webhook_rejects_bad_signatures` | Webhook rejects bad signatures | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0633 | Integration (API) | P1 | – | `test_webhook_for_unknown_order` | Webhook for unknown order | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0634 | Integration (API) | P1 | – | `test_signature_check_is_case_insensitive` | Signature check is case insensitive | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0635 | Integration (API) | P1 | – | `test_free_course_enrolls_once` | Free course enrolls once | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0636 | Integration (API) | P1 | – | `test_free_enroll_errors` | Free enroll errors | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0637 | Integration (API) | P1 | – | `test_upload_receipt` | Upload receipt | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0638 | Integration (API) | P1 | – | `test_receipt_bytes_must_match_the_declared_type` | Receipt bytes must match the declared type | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0639 | Integration (API) | P1 | – | `test_empty_receipt_is_refused` | Empty receipt is refused | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0640 | Integration (API) | P1 | – | `test_storage_outage_is_reported` | Storage outage is reported | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0641 | Integration (API) | P1 | – | `test_teacher_cannot_upload_receipts` | Teacher cannot upload receipts | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0642 | Integration (API) | P1 | – | `test_list_payments_by_role` | List payments by role | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0643 | Integration (API) | P1 | – | `test_admin_lists_receipts_with_filter` | Admin lists receipts with filter | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0644 | Integration (API) | P1 | – | `test_approve_receipt` | Approve receipt | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0645 | Integration (API) | P1 | – | `test_reject_receipt_with_reason` | Reject receipt with reason | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0646 | Integration (API) | P1 | – | `test_receipt_review_errors` | Receipt review errors | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0647 | Integration (API) | P1 | – | `test_admin_stats` | Admin stats | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0648 | Integration (API) | P1 | – | `test_admin_stats_when_empty` | Admin stats when empty | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0649 | Integration (API) | P1 | – | `test_sl_time_conversion` | Sl time conversion | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0650 | Integration (API) | P1 | – | `test_bank_account_crud` | Bank account crud | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0651 | Integration (API) | P1 | – | `test_bank_account_errors` | Bank account errors | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0652 | Integration (API) | P1 | – | `test_payment_success_defaults_completion_time` | Payment success defaults completion time | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0653 | Integration (API) | P1 | – | `test_receipt_reviewed_without_time` | Receipt reviewed without time | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0654 | Integration (API) | P1 | TestPayHereSignature | `test_verify_payhere_signature_valid` | Verify payhere signature valid | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0655 | Integration (API) | P1 | TestPayHereSignature | `test_verify_payhere_signature_invalid` | Verify payhere signature invalid | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0656 | Integration (API) | P1 | TestPaymentEndpoints | `test_checkout_missing_token_returns_401` | Checkout missing token returns 401 | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0657 | Integration (API) | P1 | TestPaymentEndpoints | `test_manual_receipt_upload_file_too_large_returns_400` | Manual receipt upload file too large returns 400 | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0658 | Integration (API) | P1 | TestPaymentEndpoints | `test_manual_receipt_upload_invalid_mime_returns_400` | Manual receipt upload invalid mime returns 400 | `edura-backend/payment_service/tests/test_payments.py` | |

## Backend – progress_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0659 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/progress_service/tests/test_migrations.py` | |
| TC-0660 | Integration (API) | P1 | – | `test_completion_percentage_calculation` | Unit test: 3 of 5 lessons watched -> completion_percentage = 60.0% | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0661 | Integration (API) | P1 | – | `test_certificate_eligibility_passed_and_failed` | Unit test: | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0662 | Integration (API) | P1 | – | `test_integration_lesson_watched_events_to_100_percent` | Integration test: processing lesson.watched events until completion reaches 100%. | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0663 | Integration (API) | P1 | – | `test_integration_certificate_issued_event_published` | Integration test: Certificate record created & certificate.issued event published. | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0664 | Integration (API) | P1 | – | `test_api_progress_dashboard_endpoint` | Integration test: GET /api/progress/courses/{course_id} | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0665 | Integration (API) | P1 | – | `test_api_leaderboard_endpoint` | Integration test: GET /api/progress/courses/{course_id}/leaderboard | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0666 | Integration (API) | P1 | – | `test_consumer_process_message` | Test consumer.process_message handling lesson.watched and assessment.graded. | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0667 | Integration (API) | P1 | – | `test_memory_redis_client_and_health` | Memory redis client and health | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0668 | Integration (API) | P1 | – | `test_api_mark_lesson_watched_and_list_progress` | Integration test: POST then GET /courses/{course_id}/lessons/progress | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0669 | Integration (API) | P1 | – | `test_api_lesson_progress_is_private_to_each_student` | Api lesson progress is private to each student | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0670 | Integration (API) | P1 | – | `test_api_mark_lesson_watched_rejects_bad_requests` | Api mark lesson watched rejects bad requests | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0671 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0672 | Integration (API) | P1 | – | `test_lifespan_creates_tables_and_starts_the_consumer_thread` | Lifespan creates tables and starts the consumer thread | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0673 | Integration (API) | P1 | – | `test_lifespan_survives_create_all_failure` | Lifespan survives create all failure | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0674 | Integration (API) | P1 | – | `test_mark_lesson_watched_and_list_progress` | Mark lesson watched and list progress | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0675 | Integration (API) | P1 | – | `test_rewatching_keeps_the_longest_watch_time` | Rewatching keeps the longest watch time | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0676 | Integration (API) | P1 | – | `test_only_students_mark_lessons_watched` | Only students mark lessons watched | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0677 | Integration (API) | P1 | – | `test_dashboard_with_no_progress` | Dashboard with no progress | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0678 | Integration (API) | P1 | – | `test_dashboard_rejects_a_token_without_a_user` | Dashboard rejects a token without a user | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0679 | Integration (API) | P1 | – | `test_dashboard_after_activity` | Dashboard after activity | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0680 | Integration (API) | P1 | – | `test_leaderboard_falls_back_to_the_database` | Leaderboard falls back to the database | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0681 | Integration (API) | P1 | – | `test_leaderboard_prefers_redis` | Leaderboard prefers redis | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0682 | Integration (API) | P1 | – | `test_leaderboard_is_capped_at_ten` | Leaderboard is capped at ten | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0683 | Integration (API) | P1 | – | `test_unknown_lesson_count_treats_one_lesson_as_the_whole_course` | Unknown lesson count treats one lesson as the whole course | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0684 | Integration (API) | P1 | – | `test_more_lessons_drop_completion_but_keep_the_first_completion_date` | More lessons drop completion but keep the first completion date | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0685 | Integration (API) | P1 | – | `test_a_failed_assessment_blocks_the_certificate` | A failed assessment blocks the certificate | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0686 | Integration (API) | P1 | – | `test_certificate_is_issued_once` | Certificate is issued once | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0687 | Integration (API) | P1 | – | `test_points_are_scores_plus_a_completion_bonus` | Points are scores plus a completion bonus | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0688 | Integration (API) | P1 | – | `test_incomplete_events_are_acked_without_changes` | Incomplete events are acked without changes | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0689 | Integration (API) | P1 | – | `test_graded_event_without_a_course_goes_to_course_1` | Graded event without a course goes to course 1 | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0690 | Integration (API) | P1 | – | `test_lesson_watched_event` | Lesson watched event | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0691 | Integration (API) | P1 | – | `test_bad_messages_are_dropped` | Bad messages are dropped | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0692 | Integration (API) | P1 | – | `test_consumer_reconnects_until_the_broker_answers` | Consumer reconnects until the broker answers | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0693 | Integration (API) | P1 | – | `test_certificate_event_is_published_durably` | Certificate event is published durably | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0694 | Integration (API) | P1 | – | `test_certificate_event_defaults_the_time_and_never_raises` | Certificate event defaults the time and never raises | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0695 | Integration (API) | P1 | – | `test_memory_redis_strings_and_ttl` | Memory redis strings and ttl | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0696 | Integration (API) | P1 | – | `test_memory_redis_sorted_sets` | Memory redis sorted sets | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0697 | Integration (API) | P1 | – | `test_memory_redis_keys_and_delete` | Memory redis keys and delete | `edura-backend/progress_service/tests/test_progress_service.py` | |

## Backend – user_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0698 | Integration (API) | P1 | TestAdminOnly | `test_admin_passes` | Admin passes | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0699 | Integration (API) | P1 | TestAdminOnly | `test_student_blocked` | Student blocked | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0700 | Integration (API) | P1 | TestAdminOnly | `test_teacher_blocked` | Teacher blocked | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0701 | Integration (API) | P1 | TestTeacherOrAdmin | `test_teacher_passes` | Teacher passes | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0702 | Integration (API) | P1 | TestTeacherOrAdmin | `test_admin_passes` | Admin passes | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0703 | Integration (API) | P1 | TestTeacherOrAdmin | `test_student_blocked` | Student blocked | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0704 | Integration (API) | P1 | TestMissingToken | `test_no_header_returns_401` | No header returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0705 | Integration (API) | P1 | TestMissingToken | `test_token_without_bearer_prefix_returns_401` | Token without bearer prefix returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0706 | Integration (API) | P1 | TestMissingToken | `test_empty_bearer_returns_401` | Empty bearer returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0707 | Integration (API) | P1 | TestExpiredToken | `test_expired_token_returns_401` | Expired token returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0708 | Integration (API) | P1 | TestInvalidToken | `test_garbage_token_returns_401` | Garbage token returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0709 | Integration (API) | P1 | TestInvalidToken | `test_wrong_secret_returns_401` | Wrong secret returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0710 | Integration (API) | P1 | TestPayloadInjection | `test_payload_sub_and_role_accessible` | Payload sub and role accessible | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0711 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/user_service/tests/test_migrations.py` | |
| TC-0712 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0713 | Integration (API) | P1 | – | `test_startup_seeds_reference_data_once` | Startup seeds reference data once | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0714 | Integration (API) | P1 | – | `test_seeding_keeps_an_existing_catalogue` | Seeding keeps an existing catalogue | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0715 | Integration (API) | P1 | – | `test_seeding_failure_is_logged_not_raised` | Seeding failure is logged not raised | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0716 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0717 | Integration (API) | P1 | – | `test_signup_creates_profile_and_account` | Signup creates profile and account | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0718 | Integration (API) | P1 | – | `test_repeated_signup_event_keeps_one_profile` | Repeated signup event keeps one profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0719 | Integration (API) | P1 | – | `test_signup_without_a_form_only_stores_the_account` | Signup without a form only stores the account | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0720 | Integration (API) | P1 | – | `test_signup_with_missing_role_defaults_to_student` | Signup with missing role defaults to student | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0721 | Integration (API) | P1 | – | `test_account_update_never_creates_a_profile` | Account update never creates a profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0722 | Integration (API) | P1 | – | `test_enrollment_credits_the_referrer_once` | Enrollment credits the referrer once | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0723 | Integration (API) | P1 | – | `test_manual_grant_or_missing_student_earns_nothing` | Manual grant or missing student earns nothing | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0724 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0725 | Integration (API) | P1 | – | `test_consumer_start_binds_user_queue` | Consumer start binds user queue | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0726 | Integration (API) | P1 | – | `test_resync_announces_streams_then_profiles` | Resync announces streams then profiles | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0727 | Integration (API) | P1 | – | `test_admin_lists_users_newest_first_with_account_details` | Admin lists users newest first with account details | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0728 | Integration (API) | P1 | – | `test_admin_list_filters_and_pages` | Admin list filters and pages | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0729 | Integration (API) | P1 | – | `test_admin_only_routes` | Admin only routes | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0730 | Integration (API) | P1 | – | `test_role_stats` | Role stats | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0731 | Integration (API) | P1 | – | `test_create_own_profile_takes_role_and_email_from_the_token` | Create own profile takes role and email from the token | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0732 | Integration (API) | P1 | – | `test_create_profile_twice_is_a_conflict` | Create profile twice is a conflict | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0733 | Integration (API) | P1 | – | `test_create_profile_validation` | Create profile validation | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0734 | Integration (API) | P1 | – | `test_create_profile_with_a_referral_code` | Create profile with a referral code | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0735 | Integration (API) | P1 | – | `test_unknown_referral_code_is_ignored_at_signup` | Unknown referral code is ignored at signup | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0736 | Integration (API) | P1 | – | `test_read_own_and_other_profiles` | Read own and other profiles | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0737 | Integration (API) | P1 | – | `test_own_email_falls_back_to_the_account_copy` | Own email falls back to the account copy | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0738 | Integration (API) | P1 | – | `test_update_own_profile` | Update own profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0739 | Integration (API) | P1 | – | `test_update_profile_permissions_and_missing` | Update profile permissions and missing | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0740 | Integration (API) | P1 | – | `test_referral_code_entered_on_profile_edit` | Referral code entered on profile edit | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0741 | Integration (API) | P1 | – | `test_admin_changes_role` | Admin changes role | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0742 | Integration (API) | P1 | – | `test_admin_deletes_profile` | Admin deletes profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0743 | Integration (API) | P1 | – | `test_stream_crud_and_events` | Stream crud and events | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0744 | Integration (API) | P1 | – | `test_stream_errors` | Stream errors | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0745 | Integration (API) | P1 | – | `test_grade_subject_crud` | Grade subject crud | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0746 | Integration (API) | P1 | – | `test_grade_subject_errors` | Grade subject errors | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0747 | Integration (API) | P1 | – | `test_subjects_for_a_grade` | Subjects for a grade | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0748 | Integration (API) | P1 | – | `test_referral_summary` | Referral summary | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0749 | Integration (API) | P1 | – | `test_referral_events_list` | Referral events list | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0750 | Integration (API) | P1 | – | `test_apply_referral_code` | Apply referral code | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0751 | Integration (API) | P1 | – | `test_apply_referral_code_errors` | Apply referral code errors | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0752 | Integration (API) | P1 | – | `test_apply_needs_a_student_with_a_profile` | Apply needs a student with a profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0753 | Integration (API) | P1 | – | `test_credit_needs_a_pending_event_and_a_referrer` | Credit needs a pending event and a referrer | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0754 | Integration (API) | P1 | – | `test_bind_referral_refuses_self_and_second_referrals` | Bind referral refuses self and second referrals | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0755 | Integration (API) | P1 | – | `test_find_referrer_ignores_blank_codes` | Find referrer ignores blank codes | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0756 | Integration (API) | P1 | – | `test_referral_code_prefix` | Referral code prefix | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0757 | Integration (API) | P1 | – | `test_referral_code_falls_back_after_collisions` | Referral code falls back after collisions | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0758 | Integration (API) | P1 | – | `test_profile_event_payload` | Profile event payload | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0759 | Integration (API) | P1 | – | `test_stream_event_defaults` | Stream event defaults | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0760 | Integration (API) | P1 | TestGetUser | `test_own_record_returns_200` | Own record returns 200 | `edura-backend/user_service/tests/test_users.py` | |
| TC-0761 | Integration (API) | P1 | TestGetUser | `test_admin_can_fetch_any_user` | Admin can fetch any user | `edura-backend/user_service/tests/test_users.py` | |
| TC-0762 | Integration (API) | P1 | TestGetUser | `test_nonexistent_user_returns_404` | Nonexistent user returns 404 | `edura-backend/user_service/tests/test_users.py` | |
| TC-0763 | Integration (API) | P1 | TestGetUserCrossAccess | `test_student_cannot_view_other_student` | Student cannot view other student | `edura-backend/user_service/tests/test_users.py` | |
| TC-0764 | Integration (API) | P1 | TestGetUserCrossAccess | `test_teacher_cannot_view_other_user` | Teacher cannot view other user | `edura-backend/user_service/tests/test_users.py` | |
| TC-0765 | Integration (API) | P1 | TestUpdateRole | `test_admin_updates_role_to_teacher` | Admin updates role to teacher | `edura-backend/user_service/tests/test_users.py` | |
| TC-0766 | Integration (API) | P1 | TestUpdateRole | `test_invalid_role_returns_422` | Invalid role returns 422 | `edura-backend/user_service/tests/test_users.py` | |
| TC-0767 | Integration (API) | P1 | TestUpdateRole | `test_student_cannot_update_own_role` | Student cannot update own role | `edura-backend/user_service/tests/test_users.py` | |
| TC-0768 | Integration (API) | P1 | TestRoleEnforcement | `test_student_blocked_from_admin_list_endpoint` | Student blocked from admin list endpoint | `edura-backend/user_service/tests/test_users.py` | |
| TC-0769 | Integration (API) | P1 | TestRoleEnforcement | `test_admin_can_access_list_endpoint` | Admin can access list endpoint | `edura-backend/user_service/tests/test_users.py` | |
| TC-0770 | Integration (API) | P1 | TestUpdateProfile | `test_student_updates_own_profile` | Student updates own profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0771 | Integration (API) | P1 | TestUpdateProfile | `test_student_cannot_update_other_profile` | Student cannot update other profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0772 | Integration (API) | P1 | TestDeleteUser | `test_admin_can_delete_user` | Admin can delete user | `edura-backend/user_service/tests/test_users.py` | |
| TC-0773 | Integration (API) | P1 | TestDeleteUser | `test_student_cannot_delete` | Student cannot delete | `edura-backend/user_service/tests/test_users.py` | |
| TC-0774 | Integration (API) | P1 | TestSignupEvents | `test_registration_builds_the_profile_and_stores_the_account` | Registration builds the profile and stores the account | `edura-backend/user_service/tests/test_users.py` | |
| TC-0775 | Integration (API) | P1 | TestSignupEvents | `test_a_repeated_event_does_not_create_a_second_profile` | A repeated event does not create a second profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0776 | Integration (API) | P1 | TestSignupEvents | `test_referral_code_from_the_signup_is_applied` | Referral code from the signup is applied | `edura-backend/user_service/tests/test_users.py` | |
| TC-0777 | Integration (API) | P1 | TestSignupEvents | `test_an_admin_created_without_a_form_still_gets_a_profile` | An admin created without a form still gets a profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0778 | Integration (API) | P1 | TestSignupEvents | `test_account_changes_update_the_listing` | Account changes update the listing | `edura-backend/user_service/tests/test_users.py` | |
| TC-0779 | Integration (API) | P1 | TestSignupEvents | `test_enrollment_credits_the_referrer_once_but_not_for_manual_grants` | Enrollment credits the referrer once but not for manual grants | `edura-backend/user_service/tests/test_users.py` | |
| TC-0780 | Integration (API) | P1 | TestProfileAnnouncements | `test_updating_and_deleting_a_profile_is_announced` | Updating and deleting a profile is announced | `edura-backend/user_service/tests/test_users.py` | |
| TC-0781 | Integration (API) | P1 | TestProfileAnnouncements | `test_streams_are_announced` | Streams are announced | `edura-backend/user_service/tests/test_users.py` | |
| TC-0782 | Integration (API) | P1 | TestNoDirectCalls | `test_the_old_internal_endpoints_are_gone` | The old internal endpoints are gone | `edura-backend/user_service/tests/test_users.py` | |

## Cross-service integration (edura-tests/integration)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0783 | Integration (cross-service) | P1 | TestAdminRoot | `test_given_admin_when_get_admin_root_then_welcome` | Given admin when get admin root then welcome | `edura-tests/integration/test_admin_flow.py` | |
| TC-0784 | Integration (cross-service) | P1 | TestAdminRoot | `test_given_student_when_get_admin_root_then_403` | Given student when get admin root then 403 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0785 | Integration (cross-service) | P1 | TestAdminRoot | `test_given_no_token_when_get_admin_root_then_401` | Given no token when get admin root then 401 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0786 | Integration (cross-service) | P1 | TestFeedbackSubmit | `test_given_anonymous_visitor_when_submit_feedback_then_201_unlinked` | Given anonymous visitor when submit feedback then 201 unlinked | `edura-tests/integration/test_admin_flow.py` | |
| TC-0787 | Integration (cross-service) | P1 | TestFeedbackSubmit | `test_given_signed_in_student_when_submit_feedback_then_linked_to_user` | Given signed in student when submit feedback then linked to user | `edura-tests/integration/test_admin_flow.py` | |
| TC-0788 | Integration (cross-service) | P1 | TestFeedbackSubmit | `test_given_invalid_category_when_submit_feedback_then_422` | Given invalid category when submit feedback then 422 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0789 | Integration (cross-service) | P1 | TestFeedbackSubmit | `test_given_bad_email_when_submit_feedback_then_422` | Given bad email when submit feedback then 422 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0790 | Integration (cross-service) | P1 | TestFeedbackSubmit | `test_given_empty_message_when_submit_feedback_then_422` | Given empty message when submit feedback then 422 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0791 | Integration (cross-service) | P1 | TestFeedbackTriage | `test_given_submitted_feedback_when_admin_lists_then_includes_it` | Given submitted feedback when admin lists then includes it | `edura-tests/integration/test_admin_flow.py` | |
| TC-0792 | Integration (cross-service) | P1 | TestFeedbackTriage | `test_given_limit_over_500_when_admin_lists_then_422` | Given limit over 500 when admin lists then 422 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0793 | Integration (cross-service) | P1 | TestFeedbackTriage | `test_given_student_when_list_feedback_then_403` | Given student when list feedback then 403 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0794 | Integration (cross-service) | P1 | TestFeedbackTriage | `test_given_unread_feedback_when_admin_marks_read_then_flag_set` | Given unread feedback when admin marks read then flag set | `edura-tests/integration/test_admin_flow.py` | |
| TC-0795 | Integration (cross-service) | P1 | TestFeedbackTriage | `test_given_unknown_feedback_when_mark_read_then_404` | Given unknown feedback when mark read then 404 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0796 | Integration (cross-service) | P1 | TestFeedbackTriage | `test_given_feedback_when_admin_deletes_then_204_and_404_after` | Given feedback when admin deletes then 204 and 404 after | `edura-tests/integration/test_admin_flow.py` | |
| TC-0797 | Integration (cross-service) | P1 | TestGuestChat | `test_given_guest_session_when_send_message_then_stored_in_conversation` | Given guest session when send message then stored in conversation | `edura-tests/integration/test_admin_flow.py` | |
| TC-0798 | Integration (cross-service) | P1 | TestGuestChat | `test_given_anonymous_without_session_when_send_then_400_identity_required` | Given anonymous without session when send then 400 identity required | `edura-tests/integration/test_admin_flow.py` | |
| TC-0799 | Integration (cross-service) | P1 | TestGuestChat | `test_given_bad_session_id_when_send_then_422` | Given bad session id when send then 422 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0800 | Integration (cross-service) | P1 | TestGuestChat | `test_given_two_messages_when_get_history_then_in_order` | Given two messages when get history then in order | `edura-tests/integration/test_admin_flow.py` | |
| TC-0801 | Integration (cross-service) | P1 | TestGuestChat | `test_given_unknown_session_when_get_history_then_empty` | Given unknown session when get history then empty | `edura-tests/integration/test_admin_flow.py` | |
| TC-0802 | Integration (cross-service) | P1 | TestGuestChat | `test_given_guest_thread_when_student_syncs_then_history_follows_account` | Given guest thread when student syncs then history follows account | `edura-tests/integration/test_admin_flow.py` | |
| TC-0803 | Integration (cross-service) | P1 | TestGuestChat | `test_given_nothing_to_sync_when_sync_then_nothing_message` | Given nothing to sync when sync then nothing message | `edura-tests/integration/test_admin_flow.py` | |
| TC-0804 | Integration (cross-service) | P1 | TestGuestChat | `test_given_no_token_when_sync_then_401` | Given no token when sync then 401 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0805 | Integration (cross-service) | P1 | TestAdminChat | `test_given_guest_message_when_admin_lists_conversations_then_shown_as_guest` | Given guest message when admin lists conversations then shown as guest | `edura-tests/integration/test_admin_flow.py` | |
| TC-0806 | Integration (cross-service) | P1 | TestAdminChat | `test_given_conversation_when_admin_reads_messages_then_marked_read` | Given conversation when admin reads messages then marked read | `edura-tests/integration/test_admin_flow.py` | |
| TC-0807 | Integration (cross-service) | P1 | TestAdminChat | `test_given_conversation_when_admin_replies_then_reply_flagged_from_admin` | Given conversation when admin replies then reply flagged from admin | `edura-tests/integration/test_admin_flow.py` | |
| TC-0808 | Integration (cross-service) | P1 | TestAdminChat | `test_given_unknown_conversation_when_admin_replies_then_404` | Given unknown conversation when admin replies then 404 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0809 | Integration (cross-service) | P1 | TestAdminChat | `test_given_conversation_when_admin_deletes_then_204_and_history_empty` | Given conversation when admin deletes then 204 and history empty | `edura-tests/integration/test_admin_flow.py` | |
| TC-0810 | Integration (cross-service) | P1 | TestAdminChat | `test_given_unknown_student_when_admin_opens_thread_then_404` | Given unknown student when admin opens thread then 404 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0811 | Integration (cross-service) | P1 | TestAdminChat | `test_given_student_when_admin_opens_thread_then_conversation_created` | Given student when admin opens thread then conversation created | `edura-tests/integration/test_admin_flow.py` | |
| TC-0812 | Integration (cross-service) | P1 | TestAdminChat | `test_given_student_when_list_admin_conversations_then_403` | Given student when list admin conversations then 403 | `edura-tests/integration/test_admin_flow.py` | |
| TC-0813 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_admin_when_create_assessment_then_201_with_zero_questions` | Given admin when create assessment then 201 with zero questions | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0814 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_assessment_when_update_then_changes_persist` | Given assessment when update then changes persist | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0815 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_assessment_when_get_by_id_then_returns_it` | Given assessment when get by id then returns it | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0816 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_unpublished_assessment_when_student_gets_it_then_404` | Given unpublished assessment when student gets it then 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0817 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_assessment_when_delete_then_204_and_404_after` | Given assessment when delete then 204 and 404 after | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0818 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_unknown_course_when_teacher_creates_assessment_then_404` | Given unknown course when teacher creates assessment then 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0819 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_student_when_create_assessment_then_403` | Given student when create assessment then 403 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0820 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_missing_title_when_create_assessment_then_422` | Given missing title when create assessment then 422 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0821 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_no_filter_when_list_assessments_then_422_filter_required` | Given no filter when list assessments then 422 filter required | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0822 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_course_filter_when_anonymous_lists_then_only_published` | Given course filter when anonymous lists then only published | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0823 | Integration (cross-service) | P1 | TestAssessmentAuthoring | `test_given_module_delete_when_by_module_then_204` | Given module delete when by module then 204 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0824 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_assessment_when_admin_adds_mcq_then_correct_answer_taken_from_option` | Given assessment when admin adds mcq then correct answer taken from option | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0825 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_question_when_admin_lists_then_includes_it` | Given question when admin lists then includes it | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0826 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_no_correct_answer_when_add_question_then_422` | Given no correct answer when add question then 422 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0827 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_question_when_update_then_text_changes` | Given question when update then text changes | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0828 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_question_when_delete_then_204_and_404_after` | Given question when delete then 204 and 404 after | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0829 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_student_when_list_questions_then_403` | Given student when list questions then 403 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0830 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_csv_when_admin_imports_then_questions_created` | Given csv when admin imports then questions created | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0831 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_non_csv_when_import_questions_then_415` | Given non csv when import questions then 415 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0832 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_admin_when_download_templates_then_files_returned` | Given admin when download templates then files returned | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0833 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_non_zip_when_bulk_import_then_rejected` | Given non zip when bulk import then rejected | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0834 | Integration (cross-service) | P1 | TestQuestionAuthoring | `test_given_student_when_download_template_then_403` | Given student when download template then 403 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0835 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_unenrolled_student_when_start_then_403_not_enrolled` | Given unenrolled student when start then 403 not enrolled | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0836 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_enrolled_student_when_start_then_questions_without_answers` | Given enrolled student when start then questions without answers | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0837 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_active_session_when_start_again_then_409_session_already_active` | Given active session when start again then 409 session already active | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0838 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_correct_answer_when_submit_then_full_score_and_passed` | Given correct answer when submit then full score and passed | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0839 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_wrong_answer_when_submit_then_zero_score_and_failed` | Given wrong answer when submit then zero score and failed | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0840 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_unknown_session_when_submit_then_auto_submitted_flag_set` | Given unknown session when submit then auto submitted flag set | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0841 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_submitted_exam_when_get_last_attempt_then_same_score` | Given submitted exam when get last attempt then same score | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0842 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_no_attempt_when_get_last_attempt_then_404` | Given no attempt when get last attempt then 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0843 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_session_when_record_violation_then_204` | Given session when record violation then 204 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0844 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_no_token_when_start_then_401` | Given no token when start then 401 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0845 | Integration (cross-service) | P1 | TestTakingAnExam | `test_given_unknown_assessment_when_start_then_404` | Given unknown assessment when start then 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0846 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_graded_attempt_when_list_my_submissions_then_listed` | Given graded attempt when list my submissions then listed | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0847 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_graded_attempt_when_list_my_attempts_then_summary_counts_one` | Given graded attempt when list my attempts then summary counts one | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0848 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_limit_over_50_when_list_my_submissions_then_422` | Given limit over 50 when list my submissions then 422 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0849 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_other_students_submission_when_review_then_403_or_404` | Given other students submission when review then 403 or 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0850 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_unknown_submission_when_review_then_404` | Given unknown submission when review then 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0851 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_graded_attempt_when_get_exam_rank_then_student_is_ranked` | Given graded attempt when get exam rank then student is ranked | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0852 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_graded_attempt_when_list_ranking_exams_then_exam_present` | Given graded attempt when list ranking exams then exam present | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0853 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_published_exam_when_get_leaderboard_publicly_then_list` | Given published exam when get leaderboard publicly then list | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0854 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_unknown_exam_when_get_leaderboard_then_404` | Given unknown exam when get leaderboard then 404 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0855 | Integration (cross-service) | P1 | TestResultsAndRankings | `test_given_limit_over_200_when_get_leaderboard_then_422` | Given limit over 200 when get leaderboard then 422 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0856 | Integration (cross-service) | P1 | TestBadges | `test_given_anonymous_visitor_when_list_badges_then_catalogue_returned` | Given anonymous visitor when list badges then catalogue returned | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0857 | Integration (cross-service) | P1 | TestBadges | `test_given_new_student_when_get_my_badges_then_empty` | Given new student when get my badges then empty | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0858 | Integration (cross-service) | P1 | TestBadges | `test_given_new_student_when_get_badge_dashboard_then_nothing_earned` | Given new student when get badge dashboard then nothing earned | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0859 | Integration (cross-service) | P1 | TestBadges | `test_given_no_token_when_get_my_badges_then_401` | Given no token when get my badges then 401 | `edura-tests/integration/test_assessment_flow.py` | |
| TC-0860 | Integration (cross-service) | P1 | TestRegister | `test_given_new_email_when_register_then_returns_unverified_student` | Given new email when register then returns unverified student | `edura-tests/integration/test_auth_flow.py` | |
| TC-0861 | Integration (cross-service) | P1 | TestRegister | `test_given_existing_email_when_register_then_400_email_exists` | Given existing email when register then 400 email exists | `edura-tests/integration/test_auth_flow.py` | |
| TC-0862 | Integration (cross-service) | P1 | TestRegister | `test_given_admin_role_when_register_then_downgraded_to_student` | Given admin role when register then downgraded to student | `edura-tests/integration/test_auth_flow.py` | |
| TC-0863 | Integration (cross-service) | P1 | TestRegister | `test_given_weak_password_when_register_then_422` | Given weak password when register then 422 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0864 | Integration (cross-service) | P1 | TestVerifyEmail | `test_given_valid_token_when_verify_then_account_is_verified` | Given valid token when verify then account is verified | `edura-tests/integration/test_auth_flow.py` | |
| TC-0865 | Integration (cross-service) | P1 | TestVerifyEmail | `test_given_garbage_token_when_verify_then_400` | Given garbage token when verify then 400 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0866 | Integration (cross-service) | P1 | TestVerifyEmail | `test_given_token_for_other_email_when_verify_then_400` | Given token for other email when verify then 400 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0867 | Integration (cross-service) | P1 | TestLogin | `test_given_valid_credentials_when_login_then_returns_bearer_token` | Given valid credentials when login then returns bearer token | `edura-tests/integration/test_auth_flow.py` | |
| TC-0868 | Integration (cross-service) | P1 | TestLogin | `test_given_wrong_password_when_login_then_401` | Given wrong password when login then 401 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0869 | Integration (cross-service) | P1 | TestLogin | `test_given_unknown_email_when_login_then_401` | Given unknown email when login then 401 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0870 | Integration (cross-service) | P1 | TestMeAndProtectedRoutes | `test_given_valid_token_when_get_me_then_returns_own_account` | Given valid token when get me then returns own account | `edura-tests/integration/test_auth_flow.py` | |
| TC-0871 | Integration (cross-service) | P1 | TestMeAndProtectedRoutes | `test_given_no_token_when_get_me_then_401` | Given no token when get me then 401 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0872 | Integration (cross-service) | P1 | TestMeAndProtectedRoutes | `test_given_student_token_when_delete_user_then_403` | Given student token when delete user then 403 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0873 | Integration (cross-service) | P1 | TestRefreshAndLogout | `test_given_valid_refresh_token_when_refresh_then_new_access_token` | Given valid refresh token when refresh then new access token | `edura-tests/integration/test_auth_flow.py` | |
| TC-0874 | Integration (cross-service) | P1 | TestRefreshAndLogout | `test_given_no_refresh_token_when_refresh_then_401_missing` | Given no refresh token when refresh then 401 missing | `edura-tests/integration/test_auth_flow.py` | |
| TC-0875 | Integration (cross-service) | P1 | TestRefreshAndLogout | `test_given_logged_in_session_when_logout_then_refresh_is_rejected` | Given logged in session when logout then refresh is rejected | `edura-tests/integration/test_auth_flow.py` | |
| TC-0876 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_admin_when_delete_user_then_204_and_login_fails` | Given admin when delete user then 204 and login fails | `edura-tests/integration/test_auth_flow.py` | |
| TC-0877 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_unknown_id_when_admin_delete_then_404` | Given unknown id when admin delete then 404 | `edura-tests/integration/test_auth_flow.py` | |
| TC-0878 | Integration (cross-service) | P1 | TestSignedUrl | `test_given_admin_when_request_signed_url_then_returns_url_and_expiry` | Given admin when request signed url then returns url and expiry | `edura-tests/integration/test_content_flow.py` | |
| TC-0879 | Integration (cross-service) | P1 | TestSignedUrl | `test_given_unenrolled_student_when_request_signed_url_then_403_not_enrolled` | Given unenrolled student when request signed url then 403 not enrolled | `edura-tests/integration/test_content_flow.py` | |
| TC-0880 | Integration (cross-service) | P1 | TestSignedUrl | `test_given_no_token_when_request_signed_url_then_401` | Given no token when request signed url then 401 | `edura-tests/integration/test_content_flow.py` | |
| TC-0881 | Integration (cross-service) | P1 | TestSignedUrl | `test_given_missing_course_id_when_request_signed_url_then_422` | Given missing course id when request signed url then 422 | `edura-tests/integration/test_content_flow.py` | |
| TC-0882 | Integration (cross-service) | P1 | TestLessonStream | `test_given_admin_when_stream_lesson_then_embed_url_built_from_video_id` | Given admin when stream lesson then embed url built from video id | `edura-tests/integration/test_content_flow.py` | |
| TC-0883 | Integration (cross-service) | P1 | TestLessonStream | `test_given_student_without_course_id_when_stream_then_422` | Given student without course id when stream then 422 | `edura-tests/integration/test_content_flow.py` | |
| TC-0884 | Integration (cross-service) | P1 | TestLessonStream | `test_given_unenrolled_student_when_stream_then_403` | Given unenrolled student when stream then 403 | `edura-tests/integration/test_content_flow.py` | |
| TC-0885 | Integration (cross-service) | P1 | TestLessonStream | `test_given_missing_video_id_when_stream_then_422` | Given missing video id when stream then 422 | `edura-tests/integration/test_content_flow.py` | |
| TC-0886 | Integration (cross-service) | P1 | TestUploadRejections | `test_given_no_token_when_upload_then_401` | Given no token when upload then 401 | `edura-tests/integration/test_content_flow.py` | |
| TC-0887 | Integration (cross-service) | P1 | TestUploadRejections | `test_given_student_when_upload_then_403` | Given student when upload then 403 | `edura-tests/integration/test_content_flow.py` | |
| TC-0888 | Integration (cross-service) | P1 | TestUploadRejections | `test_given_disallowed_mime_when_upload_then_415` | Given disallowed mime when upload then 415 | `edura-tests/integration/test_content_flow.py` | |
| TC-0889 | Integration (cross-service) | P1 | TestUploadRejections | `test_given_pdf_declared_but_text_content_when_upload_then_415` | Given pdf declared but text content when upload then 415 | `edura-tests/integration/test_content_flow.py` | |
| TC-0890 | Integration (cross-service) | P1 | TestUploadRejections | `test_given_disallowed_mime_when_upload_material_then_415` | Given disallowed mime when upload material then 415 | `edura-tests/integration/test_content_flow.py` | |
| TC-0891 | Integration (cross-service) | P1 | TestUploadRejections | `test_given_student_when_upload_material_then_403` | Given student when upload material then 403 | `edura-tests/integration/test_content_flow.py` | |
| TC-0892 | Integration (cross-service) | P1 | TestAvatarUpload | `test_given_no_token_when_upload_avatar_then_401` | Given no token when upload avatar then 401 | `edura-tests/integration/test_content_flow.py` | |
| TC-0893 | Integration (cross-service) | P1 | TestAvatarUpload | `test_given_pdf_when_upload_avatar_then_415` | Given pdf when upload avatar then 415 | `edura-tests/integration/test_content_flow.py` | |
| TC-0894 | Integration (cross-service) | P1 | TestAvatarUpload | `test_given_png_declared_but_not_an_image_when_upload_avatar_then_415` | Given png declared but not an image when upload avatar then 415 | `edura-tests/integration/test_content_flow.py` | |
| TC-0895 | Integration (cross-service) | P1 | TestDeleteAsset | `test_given_foreign_public_id_when_delete_asset_then_403_not_deletable` | Given foreign public id when delete asset then 403 not deletable | `edura-tests/integration/test_content_flow.py` | |
| TC-0896 | Integration (cross-service) | P1 | TestDeleteAsset | `test_given_path_traversal_when_delete_asset_then_403` | Given path traversal when delete asset then 403 | `edura-tests/integration/test_content_flow.py` | |
| TC-0897 | Integration (cross-service) | P1 | TestDeleteAsset | `test_given_student_when_delete_asset_then_403` | Given student when delete asset then 403 | `edura-tests/integration/test_content_flow.py` | |
| TC-0898 | Integration (cross-service) | P1 | TestDeleteAsset | `test_given_missing_public_id_when_delete_asset_then_422` | Given missing public id when delete asset then 422 | `edura-tests/integration/test_content_flow.py` | |
| TC-0899 | Integration (cross-service) | P1 | TestCourseLifecycle | `test_given_admin_when_create_course_then_201_draft` | Given admin when create course then 201 draft | `edura-tests/integration/test_course_flow.py` | |
| TC-0900 | Integration (cross-service) | P1 | TestCourseLifecycle | `test_given_created_course_when_get_by_id_then_returns_it` | Given created course when get by id then returns it | `edura-tests/integration/test_course_flow.py` | |
| TC-0901 | Integration (cross-service) | P1 | TestCourseLifecycle | `test_given_created_course_when_update_then_changes_persist` | Given created course when update then changes persist | `edura-tests/integration/test_course_flow.py` | |
| TC-0902 | Integration (cross-service) | P1 | TestCourseLifecycle | `test_given_created_course_when_delete_then_204_and_404_after` | Given created course when delete then 204 and 404 after | `edura-tests/integration/test_course_flow.py` | |
| TC-0903 | Integration (cross-service) | P1 | TestCourseLifecycle | `test_given_admin_when_list_courses_then_paginated_with_items` | Given admin when list courses then paginated with items | `edura-tests/integration/test_course_flow.py` | |
| TC-0904 | Integration (cross-service) | P1 | TestCourseValidationAndAccess | `test_given_invalid_course_type_when_create_then_422` | Given invalid course type when create then 422 | `edura-tests/integration/test_course_flow.py` | |
| TC-0905 | Integration (cross-service) | P1 | TestCourseValidationAndAccess | `test_given_grade_out_of_range_when_create_then_422` | Given grade out of range when create then 422 | `edura-tests/integration/test_course_flow.py` | |
| TC-0906 | Integration (cross-service) | P1 | TestCourseValidationAndAccess | `test_given_no_token_when_create_course_then_401` | Given no token when create course then 401 | `edura-tests/integration/test_course_flow.py` | |
| TC-0907 | Integration (cross-service) | P1 | TestCourseValidationAndAccess | `test_given_student_when_create_course_then_403` | Given student when create course then 403 | `edura-tests/integration/test_course_flow.py` | |
| TC-0908 | Integration (cross-service) | P1 | TestCourseValidationAndAccess | `test_given_student_when_get_draft_course_then_not_visible` | Given student when get draft course then not visible | `edura-tests/integration/test_course_flow.py` | |
| TC-0909 | Integration (cross-service) | P1 | TestCourseValidationAndAccess | `test_given_unknown_id_when_get_course_then_404` | Given unknown id when get course then 404 | `edura-tests/integration/test_course_flow.py` | |
| TC-0910 | Integration (cross-service) | P1 | TestManualAccess | `test_given_course_and_student_when_admin_grants_then_enrollment_active` | Given course and student when admin grants then enrollment active | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0911 | Integration (cross-service) | P1 | TestManualAccess | `test_given_existing_grant_when_admin_grants_again_then_nothing_new_granted` | Given existing grant when admin grants again then nothing new granted | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0912 | Integration (cross-service) | P1 | TestManualAccess | `test_given_granted_student_when_list_me_then_course_listed_with_access` | Given granted student when list me then course listed with access | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0913 | Integration (cross-service) | P1 | TestManualAccess | `test_given_ungranted_student_when_get_access_then_no_course_access` | Given ungranted student when get access then no course access | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0914 | Integration (cross-service) | P1 | TestManualAccess | `test_given_granted_student_when_listed_enrolled_then_marked_manual` | Given granted student when listed enrolled then marked manual | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0915 | Integration (cross-service) | P1 | TestManualAccess | `test_given_granted_student_when_admin_revokes_then_enrollment_cancelled` | Given granted student when admin revokes then enrollment cancelled | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0916 | Integration (cross-service) | P1 | TestManualAccess | `test_given_no_access_when_admin_revokes_then_404` | Given no access when admin revokes then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0917 | Integration (cross-service) | P1 | TestManualAccess | `test_given_lesson_grant_when_revoked_then_removed` | Given lesson grant when revoked then removed | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0918 | Integration (cross-service) | P1 | TestManualAccess | `test_given_unknown_course_when_admin_grants_then_404` | Given unknown course when admin grants then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0919 | Integration (cross-service) | P1 | TestManualAccess | `test_given_empty_user_list_when_admin_grants_then_422` | Given empty user list when admin grants then 422 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0920 | Integration (cross-service) | P1 | TestManualAccess | `test_given_student_when_grant_access_then_403` | Given student when grant access then 403 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0921 | Integration (cross-service) | P1 | TestManualAccess | `test_given_unknown_course_when_admin_lists_eligible_then_404` | Given unknown course when admin lists eligible then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0922 | Integration (cross-service) | P1 | TestGetEnrollment | `test_given_student_when_look_up_other_student_then_403` | Given student when look up other student then 403 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0923 | Integration (cross-service) | P1 | TestGetEnrollment | `test_given_no_enrollment_when_look_up_then_404` | Given no enrollment when look up then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0924 | Integration (cross-service) | P1 | TestGetEnrollment | `test_given_no_token_when_look_up_then_401` | Given no token when look up then 401 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0925 | Integration (cross-service) | P1 | TestGetEnrollment | `test_given_missing_params_when_look_up_then_422` | Given missing params when look up then 422 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0926 | Integration (cross-service) | P1 | TestGetEnrollment | `test_given_new_student_when_list_me_then_empty` | Given new student when list me then empty | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0927 | Integration (cross-service) | P1 | TestGetEnrollment | `test_given_no_token_when_list_me_then_401` | Given no token when list me then 401 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0928 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_admin_when_create_package_then_201_and_listed` | Given admin when create package then 201 and listed | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0929 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_packages_when_filter_by_grade_then_only_that_grade` | Given packages when filter by grade then only that grade | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0930 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_package_when_patch_then_changes_persist` | Given package when patch then changes persist | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0931 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_unknown_package_when_patch_then_404` | Given unknown package when patch then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0932 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_package_when_delete_then_gone` | Given package when delete then gone | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0933 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_grade_out_of_range_when_create_package_then_422` | Given grade out of range when create package then 422 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0934 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_negative_price_when_create_package_then_422` | Given negative price when create package then 422 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0935 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_student_when_create_package_then_403` | Given student when create package then 403 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0936 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_admin_when_auto_generate_then_returns_created_summary` | Given admin when auto generate then returns created summary | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0937 | Integration (cross-service) | P1 | TestClassPackagesAdmin | `test_given_auto_generate_run_twice_then_second_run_creates_nothing` | Given auto generate run twice then second run creates nothing | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0938 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_anonymous_visitor_when_list_packages_then_active_ones_visible` | Given anonymous visitor when list packages then active ones visible | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0939 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_free_package_when_student_enrolls_then_active_enrollment` | Given free package when student enrolls then active enrollment | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0940 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_already_enrolled_when_enroll_free_again_then_400` | Given already enrolled when enroll free again then 400 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0941 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_paid_package_when_enroll_free_then_400_payment_required` | Given paid package when enroll free then 400 payment required | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0942 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_unknown_package_when_enroll_free_then_404` | Given unknown package when enroll free then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0943 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_admin_token_when_enroll_free_then_403` | Given admin token when enroll free then 403 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0944 | Integration (cross-service) | P1 | TestClassPackagesStudent | `test_given_new_student_when_list_my_class_enrollments_then_empty` | Given new student when list my class enrollments then empty | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0945 | Integration (cross-service) | P1 | TestClassEnrollmentsAdmin | `test_given_admin_grants_package_then_listed_and_revocable` | Given admin grants package then listed and revocable | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0946 | Integration (cross-service) | P1 | TestClassEnrollmentsAdmin | `test_given_unknown_package_when_admin_grants_then_404` | Given unknown package when admin grants then 404 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0947 | Integration (cross-service) | P1 | TestClassEnrollmentsAdmin | `test_given_student_when_list_class_enrollments_then_403` | Given student when list class enrollments then 403 | `edura-tests/integration/test_enrollment_flow.py` | |
| TC-0948 | Integration (cross-service) | P1 | TestNotificationService | `test_given_notification_manager_when_get_notification_then_welcome` | Given notification manager when get notification then welcome | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0949 | Integration (cross-service) | P1 | TestNotificationService | `test_given_admin_when_get_notification_then_403` | Given admin when get notification then 403 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0950 | Integration (cross-service) | P1 | TestNotificationService | `test_given_no_token_when_get_notification_then_401` | Given no token when get notification then 401 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0951 | Integration (cross-service) | P1 | TestPlatformStats | `test_given_anonymous_visitor_when_get_platform_stats_then_public_numbers` | Given anonymous visitor when get platform stats then public numbers | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0952 | Integration (cross-service) | P1 | TestAdminAnalytics | `test_given_admin_when_get_analytics_root_then_welcome` | Given admin when get analytics root then welcome | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0953 | Integration (cross-service) | P1 | TestAdminAnalytics | `test_given_student_when_get_analytics_root_then_403` | Given student when get analytics root then 403 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0954 | Integration (cross-service) | P1 | TestAdminAnalytics | `test_given_admin_when_get_admin_stats_then_200` | Given admin when get admin stats then 200 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0955 | Integration (cross-service) | P1 | TestAdminAnalytics | `test_given_admin_when_get_admin_analytics_then_200` | Given admin when get admin analytics then 200 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0956 | Integration (cross-service) | P1 | TestAdminAnalytics | `test_given_student_when_get_admin_stats_then_403` | Given student when get admin stats then 403 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0957 | Integration (cross-service) | P1 | TestAdminAnalytics | `test_given_no_token_when_get_admin_analytics_then_401` | Given no token when get admin analytics then 401 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0958 | Integration (cross-service) | P1 | TestStudentProgressViews | `test_given_admin_when_get_progress_summary_then_200` | Given admin when get progress summary then 200 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0959 | Integration (cross-service) | P1 | TestStudentProgressViews | `test_given_student_when_get_progress_summary_then_403` | Given student when get progress summary then 403 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0960 | Integration (cross-service) | P1 | TestStudentProgressViews | `test_given_unknown_student_when_admin_gets_progress_then_404` | Given unknown student when admin gets progress then 404 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0961 | Integration (cross-service) | P1 | TestStudentProgressViews | `test_given_unknown_student_when_send_report_then_404` | Given unknown student when send report then 404 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0962 | Integration (cross-service) | P1 | TestStudentProgressViews | `test_given_student_when_get_me_progress_then_200_or_not_found_yet` | Given student when get me progress then 200 or not found yet | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0963 | Integration (cross-service) | P1 | TestStudentProgressViews | `test_given_admin_when_get_me_progress_then_403` | Given admin when get me progress then 403 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0964 | Integration (cross-service) | P1 | TestCourseStruggle | `test_given_unknown_course_when_admin_gets_struggle_then_404` | Given unknown course when admin gets struggle then 404 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0965 | Integration (cross-service) | P1 | TestCourseStruggle | `test_given_student_when_get_struggle_then_403` | Given student when get struggle then 403 | `edura-tests/integration/test_notification_analytics_flow.py` | |
| TC-0966 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac1_webhook_to_enrollment_chain` | AC1: Given a seeded student and course on staging | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0967 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac2_content_access_granted_after_enrollment` | AC2: Given the enrollment is now ACTIVE (from AC1) | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0968 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac3_invalid_hmac_blocks_enrollment` | AC3: Given a webhook POST with an invalid HMAC signature | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0969 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac4_duplicate_webhook_is_idempotent` | AC4: Given a valid webhook has already been processed (AC1) | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0970 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_full_payment_enrollment_flow` | End-to-End sequence covering all 4 Acceptance Criteria in a single unified execution. | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0971 | Integration (cross-service) | P1 | TestCheckout | `test_given_student_when_checkout_then_pending_order_with_hash` | Given student when checkout then pending order with hash | `edura-tests/integration/test_payment_flow.py` | |
| TC-0972 | Integration (cross-service) | P1 | TestCheckout | `test_given_checkout_when_list_own_payments_then_pending_payment_listed` | Given checkout when list own payments then pending payment listed | `edura-tests/integration/test_payment_flow.py` | |
| TC-0973 | Integration (cross-service) | P1 | TestCheckout | `test_given_no_token_when_checkout_then_401` | Given no token when checkout then 401 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0974 | Integration (cross-service) | P1 | TestCheckout | `test_given_missing_course_id_when_checkout_then_422` | Given missing course id when checkout then 422 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0975 | Integration (cross-service) | P1 | TestListPayments | `test_given_no_token_when_list_payments_then_401` | Given no token when list payments then 401 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0976 | Integration (cross-service) | P1 | TestListPayments | `test_given_new_student_when_list_payments_then_empty` | Given new student when list payments then empty | `edura-tests/integration/test_payment_flow.py` | |
| TC-0977 | Integration (cross-service) | P1 | TestListPayments | `test_given_admin_when_list_payments_then_200` | Given admin when list payments then 200 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0978 | Integration (cross-service) | P1 | TestWebhook | `test_given_failed_status_code_when_webhook_then_payment_marked_failed` | Given failed status code when webhook then payment marked failed | `edura-tests/integration/test_payment_flow.py` | |
| TC-0979 | Integration (cross-service) | P1 | TestWebhook | `test_given_bad_signature_when_webhook_then_400_invalid_signature` | Given bad signature when webhook then 400 invalid signature | `edura-tests/integration/test_payment_flow.py` | |
| TC-0980 | Integration (cross-service) | P1 | TestWebhook | `test_given_valid_signature_but_unknown_order_when_webhook_then_404` | Given valid signature but unknown order when webhook then 404 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0981 | Integration (cross-service) | P1 | TestFreeEnroll | `test_given_unknown_course_when_free_enroll_then_404` | Given unknown course when free enroll then 404 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0982 | Integration (cross-service) | P1 | TestFreeEnroll | `test_given_admin_token_when_free_enroll_then_403` | Given admin token when free enroll then 403 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0983 | Integration (cross-service) | P1 | TestFreeEnroll | `test_given_no_token_when_free_enroll_then_401` | Given no token when free enroll then 401 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0984 | Integration (cross-service) | P1 | TestReceipts | `test_given_disallowed_mime_when_upload_receipt_then_400_invalid_mime` | Given disallowed mime when upload receipt then 400 invalid mime | `edura-tests/integration/test_payment_flow.py` | |
| TC-0985 | Integration (cross-service) | P1 | TestReceipts | `test_given_file_over_2mb_when_upload_receipt_then_400_too_large` | Given file over 2mb when upload receipt then 400 too large | `edura-tests/integration/test_payment_flow.py` | |
| TC-0986 | Integration (cross-service) | P1 | TestReceipts | `test_given_no_token_when_upload_receipt_then_401` | Given no token when upload receipt then 401 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0987 | Integration (cross-service) | P1 | TestReceipts | `test_given_admin_when_list_receipts_then_200` | Given admin when list receipts then 200 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0988 | Integration (cross-service) | P1 | TestReceipts | `test_given_invalid_status_filter_when_list_receipts_then_422` | Given invalid status filter when list receipts then 422 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0989 | Integration (cross-service) | P1 | TestReceipts | `test_given_student_when_list_receipts_then_403` | Given student when list receipts then 403 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0990 | Integration (cross-service) | P1 | TestReceipts | `test_given_unknown_receipt_when_verify_then_404` | Given unknown receipt when verify then 404 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0991 | Integration (cross-service) | P1 | TestReceipts | `test_given_student_when_verify_receipt_then_403` | Given student when verify receipt then 403 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0992 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_active_account_when_public_list_then_visible_without_token` | Given active account when public list then visible without token | `edura-tests/integration/test_payment_flow.py` | |
| TC-0993 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_inactive_account_when_public_list_then_hidden_but_admin_sees` | Given inactive account when public list then hidden but admin sees | `edura-tests/integration/test_payment_flow.py` | |
| TC-0994 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_account_when_patch_then_changes_persist` | Given account when patch then changes persist | `edura-tests/integration/test_payment_flow.py` | |
| TC-0995 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_unknown_account_when_patch_then_404` | Given unknown account when patch then 404 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0996 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_account_when_delete_then_204_and_gone` | Given account when delete then 204 and gone | `edura-tests/integration/test_payment_flow.py` | |
| TC-0997 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_empty_bank_name_when_create_then_422` | Given empty bank name when create then 422 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0998 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_student_when_create_bank_account_then_403` | Given student when create bank account then 403 | `edura-tests/integration/test_payment_flow.py` | |
| TC-0999 | Integration (cross-service) | P1 | TestBankAccounts | `test_given_student_when_list_admin_accounts_then_403` | Given student when list admin accounts then 403 | `edura-tests/integration/test_payment_flow.py` | |
| TC-1000 | Integration (cross-service) | P1 | TestInternalEndpointsBlocked | `test_given_gateway_when_request_internal_admin_stats_then_blocked` | Given gateway when request internal admin stats then blocked | `edura-tests/integration/test_payment_flow.py` | |
| TC-1001 | Integration (cross-service) | P1 | TestLessonProgress | `test_given_student_when_mark_lesson_watched_then_progress_recorded` | Given student when mark lesson watched then progress recorded | `edura-tests/integration/test_progress_flow.py` | |
| TC-1002 | Integration (cross-service) | P1 | TestLessonProgress | `test_given_watched_lesson_when_get_lesson_progress_then_listed` | Given watched lesson when get lesson progress then listed | `edura-tests/integration/test_progress_flow.py` | |
| TC-1003 | Integration (cross-service) | P1 | TestLessonProgress | `test_given_new_student_when_get_lesson_progress_then_empty` | Given new student when get lesson progress then empty | `edura-tests/integration/test_progress_flow.py` | |
| TC-1004 | Integration (cross-service) | P1 | TestLessonProgress | `test_given_missing_lesson_id_when_mark_watched_then_422` | Given missing lesson id when mark watched then 422 | `edura-tests/integration/test_progress_flow.py` | |
| TC-1005 | Integration (cross-service) | P1 | TestLessonProgress | `test_given_admin_when_mark_lesson_watched_then_403` | Given admin when mark lesson watched then 403 | `edura-tests/integration/test_progress_flow.py` | |
| TC-1006 | Integration (cross-service) | P1 | TestLessonProgress | `test_given_no_token_when_mark_lesson_watched_then_401` | Given no token when mark lesson watched then 401 | `edura-tests/integration/test_progress_flow.py` | |
| TC-1007 | Integration (cross-service) | P1 | TestProgressDashboard | `test_given_student_when_get_dashboard_then_shape_is_complete` | Given student when get dashboard then shape is complete | `edura-tests/integration/test_progress_flow.py` | |
| TC-1008 | Integration (cross-service) | P1 | TestProgressDashboard | `test_given_watched_lesson_when_get_dashboard_then_watched_count_increases` | Given watched lesson when get dashboard then watched count increases | `edura-tests/integration/test_progress_flow.py` | |
| TC-1009 | Integration (cross-service) | P1 | TestProgressDashboard | `test_given_no_token_when_get_dashboard_then_401` | Given no token when get dashboard then 401 | `edura-tests/integration/test_progress_flow.py` | |
| TC-1010 | Integration (cross-service) | P1 | TestLeaderboard | `test_given_student_when_get_leaderboard_then_list_of_ranked_items` | Given student when get leaderboard then list of ranked items | `edura-tests/integration/test_progress_flow.py` | |
| TC-1011 | Integration (cross-service) | P1 | TestLeaderboard | `test_given_no_token_when_get_leaderboard_then_401` | Given no token when get leaderboard then 401 | `edura-tests/integration/test_progress_flow.py` | |
| TC-1012 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_new_registration_when_event_processed_then_profile_exists` | Given new registration when event processed then profile exists | `edura-tests/integration/test_user_flow.py` | |
| TC-1013 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_own_token_when_get_own_profile_then_200_with_email` | Given own token when get own profile then 200 with email | `edura-tests/integration/test_user_flow.py` | |
| TC-1014 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_student_when_get_other_profile_then_403` | Given student when get other profile then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1015 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_unknown_id_when_admin_get_then_404` | Given unknown id when admin get then 404 | `edura-tests/integration/test_user_flow.py` | |
| TC-1016 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_own_token_when_update_profile_then_changes_persist` | Given own token when update profile then changes persist | `edura-tests/integration/test_user_flow.py` | |
| TC-1017 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_grade_out_of_range_when_update_then_422` | Given grade out of range when update then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1018 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_student_when_update_other_profile_then_403` | Given student when update other profile then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1019 | Integration (cross-service) | P1 | TestProfileReadUpdate | `test_given_no_token_when_get_profile_then_401` | Given no token when get profile then 401 | `edura-tests/integration/test_user_flow.py` | |
| TC-1020 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_admin_when_list_users_then_paginated` | Given admin when list users then paginated | `edura-tests/integration/test_user_flow.py` | |
| TC-1021 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_invalid_role_filter_when_list_then_422` | Given invalid role filter when list then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1022 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_student_when_list_users_then_403` | Given student when list users then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1023 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_new_student_when_search_by_name_then_found` | Given new student when search by name then found | `edura-tests/integration/test_user_flow.py` | |
| TC-1024 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_admin_when_get_stats_then_counts_present` | Given admin when get stats then counts present | `edura-tests/integration/test_user_flow.py` | |
| TC-1025 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_student_when_get_stats_then_403` | Given student when get stats then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1026 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_admin_when_change_role_then_profile_role_updates` | Given admin when change role then profile role updates | `edura-tests/integration/test_user_flow.py` | |
| TC-1027 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_invalid_role_when_change_role_then_422` | Given invalid role when change role then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1028 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_student_when_change_role_then_403` | Given student when change role then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1029 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_admin_when_delete_profile_then_204_and_404_after` | Given admin when delete profile then 204 and 404 after | `edura-tests/integration/test_user_flow.py` | |
| TC-1030 | Integration (cross-service) | P1 | TestAdminUserManagement | `test_given_unknown_id_when_admin_delete_then_404` | Given unknown id when admin delete then 404 | `edura-tests/integration/test_user_flow.py` | |
| TC-1031 | Integration (cross-service) | P1 | TestStreams | `test_given_admin_when_create_stream_then_201` | Given admin when create stream then 201 | `edura-tests/integration/test_user_flow.py` | |
| TC-1032 | Integration (cross-service) | P1 | TestStreams | `test_given_created_stream_when_list_then_includes_it` | Given created stream when list then includes it | `edura-tests/integration/test_user_flow.py` | |
| TC-1033 | Integration (cross-service) | P1 | TestStreams | `test_given_inactive_stream_when_list_active_only_then_hidden` | Given inactive stream when list active only then hidden | `edura-tests/integration/test_user_flow.py` | |
| TC-1034 | Integration (cross-service) | P1 | TestStreams | `test_given_stream_when_update_then_changes_persist` | Given stream when update then changes persist | `edura-tests/integration/test_user_flow.py` | |
| TC-1035 | Integration (cross-service) | P1 | TestStreams | `test_given_unknown_stream_when_update_then_404` | Given unknown stream when update then 404 | `edura-tests/integration/test_user_flow.py` | |
| TC-1036 | Integration (cross-service) | P1 | TestStreams | `test_given_stream_when_delete_then_204_and_gone` | Given stream when delete then 204 and gone | `edura-tests/integration/test_user_flow.py` | |
| TC-1037 | Integration (cross-service) | P1 | TestStreams | `test_given_empty_name_when_create_stream_then_422` | Given empty name when create stream then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1038 | Integration (cross-service) | P1 | TestStreams | `test_given_student_when_create_stream_then_403` | Given student when create stream then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1039 | Integration (cross-service) | P1 | TestGradeSubjects | `test_given_admin_when_create_grade_subject_then_201` | Given admin when create grade subject then 201 | `edura-tests/integration/test_user_flow.py` | |
| TC-1040 | Integration (cross-service) | P1 | TestGradeSubjects | `test_given_grade_subject_when_list_by_grade_then_includes_it` | Given grade subject when list by grade then includes it | `edura-tests/integration/test_user_flow.py` | |
| TC-1041 | Integration (cross-service) | P1 | TestGradeSubjects | `test_given_grade_subject_when_update_then_changes_persist` | Given grade subject when update then changes persist | `edura-tests/integration/test_user_flow.py` | |
| TC-1042 | Integration (cross-service) | P1 | TestGradeSubjects | `test_given_grade_above_11_when_create_then_422` | Given grade above 11 when create then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1043 | Integration (cross-service) | P1 | TestGradeSubjects | `test_given_unknown_subject_when_delete_then_404` | Given unknown subject when delete then 404 | `edura-tests/integration/test_user_flow.py` | |
| TC-1044 | Integration (cross-service) | P1 | TestGradeSubjects | `test_given_grade_subject_when_delete_then_204` | Given grade subject when delete then 204 | `edura-tests/integration/test_user_flow.py` | |
| TC-1045 | Integration (cross-service) | P1 | TestSubjectsForGrade | `test_given_grade_9_subject_when_get_subjects_then_name_listed` | Given grade 9 subject when get subjects then name listed | `edura-tests/integration/test_user_flow.py` | |
| TC-1046 | Integration (cross-service) | P1 | TestSubjectsForGrade | `test_given_grade_12_with_stream_when_get_subjects_then_stream_subjects` | Given grade 12 with stream when get subjects then stream subjects | `edura-tests/integration/test_user_flow.py` | |
| TC-1047 | Integration (cross-service) | P1 | TestSubjectsForGrade | `test_given_grade_12_without_stream_when_get_subjects_then_empty` | Given grade 12 without stream when get subjects then empty | `edura-tests/integration/test_user_flow.py` | |
| TC-1048 | Integration (cross-service) | P1 | TestSubjectsForGrade | `test_given_grade_out_of_range_when_get_subjects_then_422` | Given grade out of range when get subjects then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1049 | Integration (cross-service) | P1 | TestReferrals | `test_given_student_with_profile_when_get_summary_then_has_code` | Given student with profile when get summary then has code | `edura-tests/integration/test_user_flow.py` | |
| TC-1050 | Integration (cross-service) | P1 | TestReferrals | `test_given_student_with_profile_when_get_events_then_list` | Given student with profile when get events then list | `edura-tests/integration/test_user_flow.py` | |
| TC-1051 | Integration (cross-service) | P1 | TestReferrals | `test_given_limit_over_200_when_get_events_then_422` | Given limit over 200 when get events then 422 | `edura-tests/integration/test_user_flow.py` | |
| TC-1052 | Integration (cross-service) | P1 | TestReferrals | `test_given_unknown_code_when_apply_referral_then_rejected` | Given unknown code when apply referral then rejected | `edura-tests/integration/test_user_flow.py` | |
| TC-1053 | Integration (cross-service) | P1 | TestReferrals | `test_given_admin_token_when_apply_referral_then_403` | Given admin token when apply referral then 403 | `edura-tests/integration/test_user_flow.py` | |
| TC-1054 | Integration (cross-service) | P1 | TestReferrals | `test_given_no_token_when_get_summary_then_401` | Given no token when get summary then 401 | `edura-tests/integration/test_user_flow.py` | |
| TC-1055 | Integration (cross-service) | P1 | TestOwnProfileCreation | `test_given_no_token_when_create_own_profile_then_401` | Given no token when create own profile then 401 | `edura-tests/integration/test_user_flow.py` | |
| TC-1056 | Integration (cross-service) | P1 | TestOwnProfileCreation | `test_given_existing_profile_when_create_own_profile_then_conflict` | Given existing profile when create own profile then conflict | `edura-tests/integration/test_user_flow.py` | |

## Infrastructure (edura-infra)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-1057 | Config | P2 | – | `test_nginx_conf_exists` | Nginx conf exists | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-1058 | Config | P2 | – | `test_all_11_upstream_blocks_exist` | All 11 upstream blocks exist | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-1059 | Config | P2 | – | `test_all_11_location_routes_exist` | All 11 location routes exist | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-1060 | Config | P2 | – | `test_rate_limiting_configured` | Rate limiting configured | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-1061 | Config | P2 | – | `test_cors_headers_configured` | Cors headers configured | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-1062 | Config | P2 | – | `test_proxy_headers_forwarded` | Proxy headers forwarded | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-1063 | Config | P2 | – | `test_setup_rabbitmq_topology_mocked` | Unit test using mock pika blocking connection to test topology calls. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-1064 | Config | P2 | – | `test_obsolete_queues_are_removed` | Obsolete queues are removed | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-1065 | Config | P2 | – | `test_topology_is_consistent` | Every binding targets a declared queue; nothing is bound twice; every service has a queue. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-1066 | Config | P2 | – | `test_setup_idempotency` | Test that running setup multiple times is idempotent and produces no errors. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-1067 | Config | P2 | – | `test_topology_queues_and_exchange_declared` | Verify exchange and queues are passive-declared without error. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-1068 | Config | P2 | – | `test_pub_sub_smoke` | Publish payment.success event and verify it reaches both enrollment.queue and notification.queue. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |

## End-to-end smoke (edura-tests/smoke)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-1069 | E2E | P1 | – | `test_critical_path` | Register → verify email → login → course list → checkout → webhook → active enrollment → lesson stream → assessment start → progress view (DDP-#24), with cleanup | `edura-tests/smoke/critical_path.py` | |
