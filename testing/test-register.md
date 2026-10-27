# Complete Test Case Register

Generated: 2026-10-27 · Source: static scan of the test code in the repositories (`testing/tools/generate_registers.py`) · Guideline: development guideline §6.3.3 / §6.4

## Summary

| Layer / suite | Test cases |
|---|---|
| Backend – admin_service | 66 |
| Backend – analytics_service | 97 |
| Backend – assessment_service | 141 |
| Backend – auth_service | 88 |
| Backend – content_service | 37 |
| Backend – course_service | 81 |
| Backend – enrollment_service | 65 |
| Backend – notification_service | 38 |
| Backend – payment_service | 44 |
| Backend – progress_service | 36 |
| Backend – user_service | 85 |
| Cross-service integration (edura-tests/integration) | 5 |
| Infrastructure (edura-infra) | 12 |
| End-to-end smoke (edura-tests/smoke) | 1 |
| Frontend – Jest (edura-frontend) | 854 |
| **Total** | **1650** |

Notes:

- This register lists only tests that exist in the repositories on the date above. Re-run `testing/tools/generate_registers.py` after tests are added or removed.
- Type: `test_migrations` → Migration; backend test files that send HTTP requests to the FastAPI app → Integration (API); other backend tests → Unit; `edura-tests/integration` → Integration (cross-service); `edura-infra` → Config; `edura-tests/smoke` → E2E; `edura-frontend` Jest tests → Unit.
- Priority: P1 for integration and end-to-end tests, P2 for unit, migration and config tests.
- **Description** is the test's docstring if present, otherwise its humanised name. For frontend tests it is the `it(...)` title and **Class** is the top-level `describe(...)`.
- **Status** is blank until the suite is executed; this register was generated from source and no test run was done. Record *Actual Output* and *Status* per §6.3.3 after a run.
- This register is the index of test cases. The fields it does not hold (related requirement, preconditions, input, expected and actual output) still have to be written, in the §6.3.3 format, for the key cases in the development report appendix.
- The endpoint-level register is in `endpoint-register.md`.

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
| TC-0254 | Integration (API) | P1 | – | `test_my_last_attempt_404_without_one` | My last attempt 404 without one | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0255 | Integration (API) | P1 | – | `test_my_attempts_summary_per_exam` | My attempts summary per exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0256 | Integration (API) | P1 | – | `test_my_attempts_for_course_without_exams` | My attempts for course without exams | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0257 | Integration (API) | P1 | – | `test_my_submissions_lists_attempts_newest_first` | My submissions lists attempts newest first | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0258 | Integration (API) | P1 | – | `test_my_submissions_empty_and_limit` | My submissions empty and limit | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0259 | Integration (API) | P1 | – | `test_student_reviews_own_attempt` | Student reviews own attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0260 | Integration (API) | P1 | – | `test_review_visibility` | Review visibility | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0261 | Integration (API) | P1 | – | `test_review_of_missing_or_unfinished_attempts` | Review of missing or unfinished attempts | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0262 | Integration (API) | P1 | – | `test_violation_types` | Violation types | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0263 | Integration (API) | P1 | – | `test_violation_without_session_uses_latest_attempt` | Violation without session uses latest attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0264 | Integration (API) | P1 | – | `test_violation_with_no_attempt_opens_one` | Violation with no attempt opens one | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0265 | Integration (API) | P1 | – | `test_violation_during_a_session_uses_its_attempt` | Violation during a session uses its attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0266 | Integration (API) | P1 | – | `test_ranking_exams_for_visitors_lists_every_attempted_exam` | Ranking exams for visitors lists every attempted exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0267 | Integration (API) | P1 | – | `test_leaderboard_pages_and_unknown_exam` | Leaderboard pages and unknown exam | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0268 | Integration (API) | P1 | – | `test_leaderboard_when_profiles_are_unavailable` | Leaderboard when profiles are unavailable | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0269 | Integration (API) | P1 | – | `test_my_rank_is_null_before_sitting` | My rank is null before sitting | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0270 | Integration (API) | P1 | – | `test_badge_catalogue_is_public_and_sorted` | Badge catalogue is public and sorted | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0271 | Integration (API) | P1 | – | `test_my_badges_and_dashboard` | My badges and dashboard | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0272 | Integration (API) | P1 | – | `test_seed_badges_is_idempotent` | Seed badges is idempotent | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0273 | Integration (API) | P1 | – | `test_early_bird` | Early bird | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0274 | Integration (API) | P1 | – | `test_night_owl` | Night owl | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0275 | Integration (API) | P1 | – | `test_daytime_attempt_earns_no_time_badges` | Daytime attempt earns no time badges | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0276 | Integration (API) | P1 | – | `test_consistency_king_needs_seven_days` | Consistency king needs seven days | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0277 | Integration (API) | P1 | – | `test_speed_demon_needs_a_third_of_the_time` | Speed demon needs a third of the time | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0278 | Integration (API) | P1 | – | `test_speed_demon_without_time_limit_uses_an_hour` | Speed demon without time limit uses an hour | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0279 | Integration (API) | P1 | – | `test_improved_star` | Improved star | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0280 | Integration (API) | P1 | – | `test_perfect_100_only_on_the_first_attempt` | Perfect 100 only on the first attempt | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0281 | Integration (API) | P1 | – | `test_subject_expert_needs_five_first_passes_in_one_lesson` | Subject expert needs five first passes in one lesson | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0282 | Integration (API) | P1 | – | `test_first_step_only_on_the_first_paper` | First step only on the first paper | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0283 | Integration (API) | P1 | – | `test_century_club` | Century club | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0284 | Integration (API) | P1 | – | `test_junior_scholar_needs_four_active_weeks_and_an_old_account` | Junior scholar needs four active weeks and an old account | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0285 | Integration (API) | P1 | – | `test_badges_are_awarded_once_and_announced` | Badges are awarded once and announced | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0286 | Integration (API) | P1 | – | `test_concurrent_award_is_skipped` | Concurrent award is skipped | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0287 | Integration (API) | P1 | – | `test_local_time_conversion` | Local time conversion | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0288 | Integration (API) | P1 | – | `test_resync_announces_exams_badges_and_graded_attempts` | Resync announces exams badges and graded attempts | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0289 | Integration (API) | P1 | – | `test_resync_on_an_empty_database` | Resync on an empty database | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0290 | Integration (API) | P1 | – | `test_assessment_event_payload` | Assessment event payload | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0291 | Integration (API) | P1 | – | `test_badge_and_graded_events_without_timestamps` | Badge and graded events without timestamps | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0292 | Integration (API) | P1 | – | `test_lookups_with_no_ids_skip_the_database` | Lookups with no ids skip the database | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0293 | Integration (API) | P1 | – | `test_unknown_course_has_no_instructor` | Unknown course has no instructor | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0294 | Integration (API) | P1 | – | `test_memory_redis_get_set_delete` | Memory redis get set delete | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0295 | Integration (API) | P1 | – | `test_memory_redis_ttl` | Memory redis ttl | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0296 | Integration (API) | P1 | – | `test_memory_redis_expiry` | Memory redis expiry | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0297 | Integration (API) | P1 | – | `test_memory_redis_keys_by_prefix` | Memory redis keys by prefix | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0298 | Integration (API) | P1 | – | `test_get_redis_client_returns_the_module_client` | Get redis client returns the module client | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0299 | Integration (API) | P1 | – | `test_answers_of_tolerates_bad_json` | Answers of tolerates bad json | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0300 | Integration (API) | P1 | – | `test_time_taken_edge_cases` | Time taken edge cases | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0301 | Integration (API) | P1 | – | `test_question_helpers_tolerate_bad_json` | Question helpers tolerate bad json | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0302 | Integration (API) | P1 | – | `test_option_images_are_padded_and_trimmed` | Option images are padded and trimmed | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0303 | Integration (API) | P1 | – | `test_as_utc` | As utc | `edura-backend/assessment_service/tests/test_assessment_service.py` | |
| TC-0304 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/assessment_service/tests/test_migrations.py` | |

## Backend – auth_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0305 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0306 | Integration (API) | P1 | – | `test_startup_creates_tables_and_schedules_the_resync` | Startup creates tables and schedules the resync | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0307 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0308 | Integration (API) | P1 | – | `test_resync_reannounces_every_account` | Resync reannounces every account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0309 | Integration (API) | P1 | – | `test_public_registration_can_never_create_an_admin` | Public registration can never create an admin | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0310 | Integration (API) | P1 | – | `test_teachers_may_self_register` | Teachers may self register | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0311 | Integration (API) | P1 | – | `test_duplicate_registration` | Duplicate registration | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0312 | Integration (API) | P1 | – | `test_registration_profile_drops_empty_fields` | Registration profile drops empty fields | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0313 | Integration (API) | P1 | – | `test_password_strength_rules` | Password strength rules | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0314 | Integration (API) | P1 | – | `test_verification_link_for_a_changed_address_is_refused` | Verification link for a changed address is refused | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0315 | Integration (API) | P1 | – | `test_verifying_twice_announces_once` | Verifying twice announces once | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0316 | Integration (API) | P1 | – | `test_verification_link_for_a_deleted_account` | Verification link for a deleted account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0317 | Integration (API) | P1 | – | `test_resend_skips_accounts_that_need_no_link` | Resend skips accounts that need no link | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0318 | Integration (API) | P1 | – | `test_resend_is_throttled_and_same_for_unknown_addresses` | Resend is throttled and same for unknown addresses | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0319 | Integration (API) | P1 | – | `test_admin_route` | Admin route | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0320 | Integration (API) | P1 | – | `test_admin_creates_a_verified_admin_with_a_profile` | Admin creates a verified admin with a profile | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0321 | Integration (API) | P1 | – | `test_create_admin_errors` | Create admin errors | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0322 | Integration (API) | P1 | – | `test_deactivating_an_account_is_announced_and_blocks_login` | Deactivating an account is announced and blocks login | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0323 | Integration (API) | P1 | – | `test_admin_deletes_an_account` | Admin deletes an account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0324 | Integration (API) | P1 | – | `test_login_issues_a_token_and_a_secure_cookie` | Login issues a token and a secure cookie | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0325 | Integration (API) | P1 | – | `test_google_only_account_cannot_use_a_password` | Google only account cannot use a password | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0326 | Integration (API) | P1 | – | `test_refresh_from_the_cookie_rotates_it` | Refresh from the cookie rotates it | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0327 | Integration (API) | P1 | – | `test_refresh_errors` | Refresh errors | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0328 | Integration (API) | P1 | – | `test_expired_refresh_token` | Expired refresh token | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0329 | Integration (API) | P1 | – | `test_refresh_for_a_deleted_account` | Refresh for a deleted account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0330 | Integration (API) | P1 | – | `test_logout_without_a_cookie_still_succeeds` | Logout without a cookie still succeeds | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0331 | Integration (API) | P1 | – | `test_invalid_google_token` | Invalid google token | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0332 | Integration (API) | P1 | – | `test_new_google_user_without_a_name_uses_the_address` | New google user without a name uses the address | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0333 | Integration (API) | P1 | – | `test_google_links_onto_a_verified_password_account` | Google links onto a verified password account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0334 | Integration (API) | P1 | – | `test_returning_google_user_is_found_by_google_id` | Returning google user is found by google id | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0335 | Integration (API) | P1 | – | `test_passwordless_account_becomes_a_google_account` | Passwordless account becomes a google account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0336 | Integration (API) | P1 | – | `test_deactivated_google_account` | Deactivated google account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0337 | Integration (API) | P1 | – | `test_google_userinfo_call` | Google userinfo call | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0338 | Integration (API) | P1 | – | `test_me` | Me | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0339 | Integration (API) | P1 | – | `test_google_user_sets_a_password_then_logs_in_with_it` | Google user sets a password then logs in with it | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0340 | Integration (API) | P1 | – | `test_set_password_validation_and_missing_user` | Set password validation and missing user | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0341 | Integration (API) | P1 | – | `test_change_password` | Change password | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0342 | Integration (API) | P1 | – | `test_change_password_needs_an_existing_password` | Change password needs an existing password | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0343 | Integration (API) | P1 | – | `test_no_reset_link_for_a_deactivated_account` | No reset link for a deactivated account | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0344 | Integration (API) | P1 | – | `test_reset_is_refused_once_the_account_is_deactivated` | Reset is refused once the account is deactivated | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0345 | Integration (API) | P1 | – | `test_reset_requires_matching_passwords` | Reset requires matching passwords | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0346 | Integration (API) | P1 | – | `test_reset_for_a_verified_account_is_not_reannounced` | Reset for a verified account is not reannounced | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0347 | Integration (API) | P1 | – | `test_reset_signs_out_every_session` | Reset signs out every session | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0348 | Integration (API) | P1 | – | `test_otp_round_trip_is_single_use` | Otp round trip is single use | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0349 | Integration (API) | P1 | – | `test_otp_purposes_are_separate` | Otp purposes are separate | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0350 | Integration (API) | P1 | – | `test_access_token_without_email` | Access token without email | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0351 | Integration (API) | P1 | – | `test_reset_token_parsing` | Reset token parsing | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0352 | Integration (API) | P1 | – | `test_verification_token_parsing` | Verification token parsing | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0353 | Integration (API) | P1 | – | `test_memory_redis_client` | Memory redis client | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0354 | Integration (API) | P1 | – | `test_refresh_token_is_stored_hashed` | Refresh token is stored hashed | `edura-backend/auth_service/tests/test_auth_routes.py` | |
| TC-0355 | Integration (API) | P1 | – | `test_token_service_create_and_verify` | Token service create and verify | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0356 | Integration (API) | P1 | – | `test_otp_service_generate_and_verify` | Otp service generate and verify | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0357 | Integration (API) | P1 | – | `test_session_service_limit` | Session service limit | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0358 | Integration (API) | P1 | – | `test_register_and_login_success` | Register and login success | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0359 | Integration (API) | P1 | – | `test_login_invalid_credentials` | Login invalid credentials | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0360 | Integration (API) | P1 | – | `test_refresh_token_rotation_and_reuse` | Refresh token rotation and reuse | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0361 | Integration (API) | P1 | – | `test_protected_route_role_enforcement` | Protected route role enforcement | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0362 | Integration (API) | P1 | – | `test_missing_and_expired_token` | Missing and expired token | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0363 | Integration (API) | P1 | – | `test_register_rejects_weak_password` | Register rejects weak password | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0364 | Integration (API) | P1 | – | `test_forgot_password_does_not_reveal_unknown_emails` | Forgot password does not reveal unknown emails | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0365 | Integration (API) | P1 | – | `test_reset_password_flow_is_single_use_and_signs_out` | Reset password flow is single use and signs out | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0366 | Integration (API) | P1 | – | `test_reset_password_rejects_garbage_token` | Reset password rejects garbage token | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0367 | Integration (API) | P1 | – | `test_logout_revokes_refresh_token` | Logout revokes refresh token | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0368 | Integration (API) | P1 | – | `test_register_sends_a_verification_link` | Register sends a verification link | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0369 | Integration (API) | P1 | – | `test_unverified_login_hides_whether_the_address_exists` | Unverified login hides whether the address exists | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0370 | Integration (API) | P1 | – | `test_verification_link_is_reusable_but_only_for_verification` | Verification link is reusable but only for verification | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0371 | Integration (API) | P1 | – | `test_expired_verification_link_is_rejected` | Expired verification link is rejected | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0372 | Integration (API) | P1 | – | `test_resend_verification` | Resend verification | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0373 | Integration (API) | P1 | – | `test_register_announces_the_account_with_its_profile` | Register announces the account with its profile | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0374 | Integration (API) | P1 | – | `test_register_without_a_profile_announces_the_account_only` | Register without a profile announces the account only | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0375 | Integration (API) | P1 | – | `test_register_rejects_an_invalid_profile_before_announcing_anything` | Register rejects an invalid profile before announcing anything | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0376 | Integration (API) | P1 | – | `test_register_does_not_depend_on_any_other_service` | The broker being down must not stop an account being created. | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0377 | Integration (API) | P1 | – | `test_account_changes_are_announced` | Account changes are announced | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0378 | Integration (API) | P1 | – | `test_google_sign_in_verifies_and_drops_an_unverified_password` | Google sign in verifies and drops an unverified password | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0379 | Integration (API) | P1 | – | `test_google_without_a_verified_address_does_not_verify` | Google without a verified address does not verify | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0380 | Integration (API) | P1 | – | `test_password_reset_proves_the_address` | Password reset proves the address | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0381 | Integration (API) | P1 | – | `test_new_google_account_is_announced_with_the_google_name_and_photo` | New google account is announced with the google name and photo | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0382 | Integration (API) | P1 | – | `test_admin_created_by_admin_is_announced_with_a_profile` | Admin created by admin is announced with a profile | `edura-backend/auth_service/tests/test_auth_service.py` | |
| TC-0383 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/auth_service/tests/test_migrations.py` | |
| TC-0384 | Unit | P2 | – | `test_publish_never_raises_when_the_broker_is_down` | Publish never raises when the broker is down | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0385 | Unit | P2 | – | `test_a_down_broker_is_skipped_for_a_few_seconds` | A down broker is skipped for a few seconds | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0386 | Unit | P2 | – | `test_publish_reconnects_once_after_an_idle_connection_dropped` | Publish reconnects once after an idle connection dropped | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0387 | Unit | P2 | – | `test_a_consumer_hands_the_event_to_its_handler_and_acks` | A consumer hands the event to its handler and acks | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0388 | Unit | P2 | – | `test_a_message_that_is_not_json_is_dropped_not_retried` | A message that is not json is dropped not retried | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0389 | Unit | P2 | – | `test_a_failing_handler_is_tried_three_times_then_dropped` | A failing handler is tried three times then dropped | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0390 | Unit | P2 | – | `test_a_handler_that_recovers_is_not_called_again` | A handler that recovers is not called again | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0391 | Unit | P2 | – | `test_resync_can_be_switched_off` | Resync can be switched off | `edura-backend/auth_service/tests/test_shared_messaging.py` | |
| TC-0392 | Unit | P2 | – | `test_every_service_queue_listens_to_something_and_nothing_twice` | Every service queue listens to something and nothing twice | `edura-backend/auth_service/tests/test_shared_messaging.py` | |

## Backend – content_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0393 | Integration (API) | P1 | TestHealth | `test_health_returns_ok` | Health returns ok | `edura-backend/content_service/tests/test_content.py` | |
| TC-0394 | Integration (API) | P1 | TestSignedUrl | `test_missing_token_returns_401` | Missing token returns 401 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0395 | Integration (API) | P1 | TestSignedUrl | `test_student_not_enrolled_returns_403` | Student not enrolled returns 403 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0396 | Integration (API) | P1 | TestSignedUrl | `test_enrolled_student_gets_signed_url` | Enrolled student gets signed url | `edura-backend/content_service/tests/test_content.py` | |
| TC-0397 | Integration (API) | P1 | TestSignedUrl | `test_teacher_gets_signed_url_without_enrollment_check` | Teacher gets signed url without enrollment check | `edura-backend/content_service/tests/test_content.py` | |
| TC-0398 | Integration (API) | P1 | TestSignedUrl | `test_admin_gets_signed_url_without_enrollment_check` | Admin gets signed url without enrollment check | `edura-backend/content_service/tests/test_content.py` | |
| TC-0399 | Integration (API) | P1 | TestStreamLesson | `test_missing_token_returns_401` | Missing token returns 401 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0400 | Integration (API) | P1 | TestStreamLesson | `test_student_without_course_id_returns_422` | Student without course id returns 422 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0401 | Integration (API) | P1 | TestStreamLesson | `test_student_not_enrolled_returns_403` | Student not enrolled returns 403 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0402 | Integration (API) | P1 | TestStreamLesson | `test_enrolled_student_gets_embed_url` | Enrolled student gets embed url | `edura-backend/content_service/tests/test_content.py` | |
| TC-0403 | Integration (API) | P1 | TestStreamLesson | `test_teacher_gets_embed_url_without_enrollment` | Teacher gets embed url without enrollment | `edura-backend/content_service/tests/test_content.py` | |
| TC-0404 | Integration (API) | P1 | TestUpload | `test_student_cannot_upload` | Student cannot upload | `edura-backend/content_service/tests/test_content.py` | |
| TC-0405 | Integration (API) | P1 | TestUpload | `test_missing_token_returns_401` | Missing token returns 401 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0406 | Integration (API) | P1 | TestUpload | `test_file_too_large_returns_413` | File too large returns 413 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0407 | Integration (API) | P1 | TestUpload | `test_disallowed_mime_type_returns_415` | Disallowed mime type returns 415 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0408 | Integration (API) | P1 | TestUpload | `test_mime_mismatch_returns_415` | Mime mismatch returns 415 | `edura-backend/content_service/tests/test_content.py` | |
| TC-0409 | Integration (API) | P1 | TestUpload | `test_valid_pdf_upload_passes` | Valid pdf upload passes | `edura-backend/content_service/tests/test_content.py` | |
| TC-0410 | Integration (API) | P1 | TestUpload | `test_valid_png_upload_passes` | Valid png upload passes | `edura-backend/content_service/tests/test_content.py` | |
| TC-0411 | Integration (API) | P1 | TestUpload | `test_admin_can_upload` | Admin can upload | `edura-backend/content_service/tests/test_content.py` | |
| TC-0412 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_consumer` | Startup creates tables and starts consumer | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0413 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0414 | Integration (API) | P1 | – | `test_access_comes_from_access_events` | Access comes from access events | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0415 | Integration (API) | P1 | – | `test_enrolled_student_streams_through_the_real_access_check` | Enrolled student streams through the real access check | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0416 | Integration (API) | P1 | – | `test_consumer_start_and_rollback` | Consumer start and rollback | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0417 | Integration (API) | P1 | – | `test_material_upload` | Material upload | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0418 | Integration (API) | P1 | – | `test_material_upload_rejections` | Material upload rejections | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0419 | Integration (API) | P1 | – | `test_material_upload_is_for_staff` | Material upload is for staff | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0420 | Integration (API) | P1 | – | `test_delete_uploaded_asset` | Delete uploaded asset | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0421 | Integration (API) | P1 | – | `test_only_content_assets_can_be_deleted` | Only content assets can be deleted | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0422 | Integration (API) | P1 | – | `test_delete_asset_validation_and_roles` | Delete asset validation and roles | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0423 | Integration (API) | P1 | – | `test_any_user_can_upload_an_avatar` | Any user can upload an avatar | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0424 | Integration (API) | P1 | – | `test_avatar_rejections` | Avatar rejections | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0425 | Integration (API) | P1 | – | `test_missing_credentials_are_a_503` | Missing credentials are a 503 | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0426 | Integration (API) | P1 | – | `test_upload_asset_passes_safe_options` | Upload asset passes safe options | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0427 | Integration (API) | P1 | – | `test_delete_asset_tries_each_resource_type` | Delete asset tries each resource type | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0428 | Integration (API) | P1 | – | `test_signed_url_expires_in_an_hour` | Signed url expires in an hour | `edura-backend/content_service/tests/test_content_service.py` | |
| TC-0429 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/content_service/tests/test_migrations.py` | |

## Backend – course_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0430 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0431 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_listeners` | Startup creates tables and starts listeners | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0432 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0433 | Integration (API) | P1 | – | `test_resync_reannounces_every_course_and_lesson` | Resync reannounces every course and lesson | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0434 | Integration (API) | P1 | – | `test_consumer_stores_access_and_start_binds_queue` | Consumer stores access and start binds queue | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0435 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0436 | Integration (API) | P1 | – | `test_grade_bands` | Grade bands | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0437 | Integration (API) | P1 | – | `test_public_sees_only_published_courses` | Public sees only published courses | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0438 | Integration (API) | P1 | – | `test_staff_filter_by_status` | Staff filter by status | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0439 | Integration (API) | P1 | – | `test_grade_filter_keeps_ungraded_courses` | Grade filter keeps ungraded courses | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0440 | Integration (API) | P1 | – | `test_stream_filter_applies_only_at_a_level` | Stream filter applies only at a level | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0441 | Integration (API) | P1 | – | `test_pagination_and_page_size_limits` | Pagination and page size limits | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0442 | Integration (API) | P1 | – | `test_include_modules_hides_inactive_lessons_from_students` | Include modules hides inactive lessons from students | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0443 | Integration (API) | P1 | – | `test_include_modules_with_no_courses` | Include modules with no courses | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0444 | Integration (API) | P1 | – | `test_course_without_modules_lists_empty` | Course without modules lists empty | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0445 | Integration (API) | P1 | – | `test_get_course_visibility` | Get course visibility | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0446 | Integration (API) | P1 | – | `test_list_modules` | List modules | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0447 | Integration (API) | P1 | – | `test_create_course_as_draft` | Create course as draft | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0448 | Integration (API) | P1 | – | `test_create_course_validation` | Create course validation | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0449 | Integration (API) | P1 | – | `test_create_course_permissions` | Create course permissions | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0450 | Integration (API) | P1 | – | `test_update_course_fields` | Update course fields | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0451 | Integration (API) | P1 | – | `test_update_course_validation` | Update course validation | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0452 | Integration (API) | P1 | – | `test_publishing_a_video_course_needs_a_video` | Publishing a video course needs a video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0453 | Integration (API) | P1 | – | `test_publishing_an_exam_course_needs_only_a_lesson` | Publishing an exam course needs only a lesson | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0454 | Integration (API) | P1 | – | `test_switching_to_exam_while_publishing_uses_the_new_type` | Switching to exam while publishing uses the new type | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0455 | Integration (API) | P1 | – | `test_archiving_unpublishes` | Archiving unpublishes | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0456 | Integration (API) | P1 | – | `test_course_ownership` | Course ownership | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0457 | Integration (API) | P1 | – | `test_delete_course_removes_everything_under_it` | Delete course removes everything under it | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0458 | Integration (API) | P1 | – | `test_create_module` | Create module | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0459 | Integration (API) | P1 | – | `test_module_ownership_and_missing` | Module ownership and missing | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0460 | Integration (API) | P1 | – | `test_module_must_belong_to_the_course` | Module must belong to the course | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0461 | Integration (API) | P1 | – | `test_update_module` | Update module | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0462 | Integration (API) | P1 | – | `test_delete_module_clears_its_children` | Delete module clears its children | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0463 | Integration (API) | P1 | – | `test_delete_empty_module` | Delete empty module | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0464 | Integration (API) | P1 | – | `test_create_and_update_video` | Create and update video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0465 | Integration (API) | P1 | – | `test_create_video_needs_a_youtube_id` | Create video needs a youtube id | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0466 | Integration (API) | P1 | – | `test_video_not_found` | Video not found | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0467 | Integration (API) | P1 | – | `test_delete_video_unpins_its_materials` | Delete video unpins its materials | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0468 | Integration (API) | P1 | – | `test_videos_need_sign_in` | Videos need sign in | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0469 | Integration (API) | P1 | – | `test_students_need_access_to_open_videos` | Students need access to open videos | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0470 | Integration (API) | P1 | – | `test_staff_open_videos_without_enrollment` | Staff open videos without enrollment | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0471 | Integration (API) | P1 | – | `test_inactive_lesson_is_hidden_from_students` | Inactive lesson is hidden from students | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0472 | Integration (API) | P1 | – | `test_videos_list_with_checkpoints_in_order` | Videos list with checkpoints in order | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0473 | Integration (API) | P1 | – | `test_videos_of_a_draft_course_are_hidden` | Videos of a draft course are hidden | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0474 | Integration (API) | P1 | – | `test_empty_lesson_has_no_videos` | Empty lesson has no videos | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0475 | Integration (API) | P1 | – | `test_create_material_pinned_to_a_video` | Create material pinned to a video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0476 | Integration (API) | P1 | – | `test_material_cannot_pin_a_video_from_another_lesson` | Material cannot pin a video from another lesson | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0477 | Integration (API) | P1 | – | `test_list_materials_filtered_by_video` | List materials filtered by video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0478 | Integration (API) | P1 | – | `test_update_material` | Update material | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0479 | Integration (API) | P1 | – | `test_material_not_found_and_delete` | Material not found and delete | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0480 | Integration (API) | P1 | – | `test_parse_timestamp` | Parse timestamp | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0481 | Integration (API) | P1 | – | `test_parse_timestamp_rejects` | Parse timestamp rejects | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0482 | Integration (API) | P1 | – | `test_checkpoint_template` | Checkpoint template | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0483 | Integration (API) | P1 | – | `test_import_checkpoints` | Import checkpoints | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0484 | Integration (API) | P1 | – | `test_import_adds_to_an_existing_checkpoint` | Import adds to an existing checkpoint | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0485 | Integration (API) | P1 | – | `test_import_checkpoint_errors` | Import checkpoint errors | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0486 | Integration (API) | P1 | – | `test_checkpoints_for_a_missing_video` | Checkpoints for a missing video | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0487 | Integration (API) | P1 | – | `test_clear_checkpoints` | Clear checkpoints | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0488 | Integration (API) | P1 | – | `test_move_checkpoint` | Move checkpoint | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0489 | Integration (API) | P1 | – | `test_checkpoint_ownership_and_missing` | Checkpoint ownership and missing | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0490 | Integration (API) | P1 | – | `test_delete_checkpoint` | Delete checkpoint | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0491 | Integration (API) | P1 | – | `test_edit_checkpoint_question` | Edit checkpoint question | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0492 | Integration (API) | P1 | – | `test_checkpoint_question_validation` | Checkpoint question validation | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0493 | Integration (API) | P1 | – | `test_course_event_defaults` | Course event defaults | `edura-backend/course_service/tests/test_course_service.py` | |
| TC-0494 | Integration (API) | P1 | TestAssertCourseOwner | `test_matching_teacher_passes` | Matching teacher passes | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0495 | Integration (API) | P1 | TestAssertCourseOwner | `test_mismatched_teacher_raises_403` | Mismatched teacher raises 403 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0496 | Integration (API) | P1 | TestAssertCourseOwner | `test_admin_bypasses_ownership` | Admin bypasses ownership | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0497 | Integration (API) | P1 | TestStudentBlockedFromCreateCourse | `test_student_cannot_create_course` | Student cannot create course | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0498 | Integration (API) | P1 | TestStudentBlockedFromCreateCourse | `test_no_token_returns_401` | No token returns 401 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0499 | Integration (API) | P1 | TestCreateAndGetCourse | `test_teacher_creates_course_returns_201` | Teacher creates course returns 201 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0500 | Integration (API) | P1 | TestCreateAndGetCourse | `test_get_course_by_id` | Get course by id | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0501 | Integration (API) | P1 | TestCreateAndGetCourse | `test_get_nonexistent_course_returns_404` | Get nonexistent course returns 404 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0502 | Integration (API) | P1 | TestOwnershipEnforcement | `test_teacher_b_cannot_update_teacher_a_course` | Teacher b cannot update teacher a course | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0503 | Integration (API) | P1 | TestOwnershipEnforcement | `test_admin_can_update_any_course` | Admin can update any course | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0504 | Integration (API) | P1 | TestPublishCourse | `test_publish_requires_module_with_lesson` | Publish requires module with lesson | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0505 | Integration (API) | P1 | TestPublishCourse | `test_publish_with_content_fires_rabbitmq_event` | Publish with content fires rabbitmq event | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0506 | Integration (API) | P1 | TestModuleAndLessonCRUD | `test_create_module_returns_201` | Create module returns 201 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0507 | Integration (API) | P1 | TestModuleAndLessonCRUD | `test_create_lesson_returns_201` | Create lesson returns 201 | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0508 | Integration (API) | P1 | TestStudentCourseBrowse | `test_student_only_sees_published_courses` | Student only sees published courses | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0509 | Integration (API) | P1 | TestStudentCourseBrowse | `test_student_cannot_get_draft_course_directly` | Student cannot get draft course directly | `edura-backend/course_service/tests/test_courses.py` | |
| TC-0510 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/course_service/tests/test_migrations.py` | |

## Backend – enrollment_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0511 | Integration (API) | P1 | – | `test_get_enrollment_success` | Get enrollment success | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0512 | Integration (API) | P1 | – | `test_get_enrollment_not_found_returns_404` | Get enrollment not found returns 404 | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0513 | Integration (API) | P1 | – | `test_enrollment_lookup_needs_login_and_is_private` | Enrollment lookup needs login and is private | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0514 | Integration (API) | P1 | – | `test_payment_success_activates_the_enrollment_and_announces_it` | Payment success activates the enrollment and announces it | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0515 | Integration (API) | P1 | – | `test_a_repeated_payment_extends_expiry_without_a_second_enrollment` | A repeated payment extends expiry without a second enrollment | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0516 | Integration (API) | P1 | – | `test_subscription_expiry_suspends_and_removes_access` | Subscription expiry suspends and removes access | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0517 | Integration (API) | P1 | – | `test_class_package_opens_published_courses_of_its_grade_until_it_expires` | Class package opens published courses of its grade until it expires | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0518 | Integration (API) | P1 | – | `test_an_expired_or_inactive_package_opens_nothing` | An expired or inactive package opens nothing | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0519 | Integration (API) | P1 | – | `test_a_lesson_grant_opens_just_that_lesson_unless_the_whole_course_is_open` | A lesson grant opens just that lesson unless the whole course is open | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0520 | Integration (API) | P1 | – | `test_a_package_holders_access_is_refreshed_when_a_course_is_published` | A package holders access is refreshed when a course is published | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0521 | Integration (API) | P1 | – | `test_renaming_a_course_does_not_re_announce_anyones_access` | Renaming a course does not re announce anyones access | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0522 | Integration (API) | P1 | – | `test_the_course_copy_follows_the_catalogue` | The course copy follows the catalogue | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0523 | Integration (API) | P1 | – | `test_eligible_students_are_those_in_the_course_grade_band_without_access` | Eligible students are those in the course grade band without access | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0524 | Integration (API) | P1 | – | `test_admin_grant_enrolls_announces_and_lists_by_name` | Admin grant enrolls announces and lists by name | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0525 | Integration (API) | P1 | – | `test_package_names_use_the_local_stream_copy` | Package names use the local stream copy | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0526 | Integration (API) | P1 | – | `test_auto_generate_makes_a_package_per_grade_and_active_stream` | Auto generate makes a package per grade and active stream | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0527 | Integration (API) | P1 | – | `test_class_package_changes_are_announced_to_holders` | Class package changes are announced to holders | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0528 | Integration (API) | P1 | – | `test_the_old_internal_endpoints_are_gone` | The old internal endpoints are gone | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0529 | Integration (API) | P1 | – | `test_this_service_reads_people_from_its_own_copy` | This service reads people from its own copy | `edura-backend/enrollment_service/tests/test_enrollment.py` | |
| TC-0530 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0531 | Integration (API) | P1 | – | `test_lifespan_creates_tables_and_starts_listeners` | Lifespan creates tables and starts listeners | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0532 | Integration (API) | P1 | – | `test_lifespan_survives_schema_errors` | Lifespan survives schema errors | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0533 | Integration (API) | P1 | – | `test_resync_announces_access_and_enrollments` | Resync announces access and enrollments | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0534 | Integration (API) | P1 | – | `test_consumer_start_binds_enrollment_queue` | Consumer start binds enrollment queue | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0535 | Integration (API) | P1 | – | `test_incomplete_payment_and_expiry_events_are_ignored` | Incomplete payment and expiry events are ignored | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0536 | Integration (API) | P1 | – | `test_expiry_without_enrollment_still_announces_access` | Expiry without enrollment still announces access | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0537 | Integration (API) | P1 | – | `test_people_and_streams_go_to_their_copies` | People and streams go to their copies | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0538 | Integration (API) | P1 | – | `test_deleting_a_course_reannounces_package_holders` | Deleting a course reannounces package holders | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0539 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0540 | Integration (API) | P1 | – | `test_lapsed_active_enrollment_restarts_from_now` | Lapsed active enrollment restarts from now | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0541 | Integration (API) | P1 | – | `test_suspended_enrollment_is_reactivated` | Suspended enrollment is reactivated | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0542 | Integration (API) | P1 | – | `test_suspend_unknown_enrollment_returns_none` | Suspend unknown enrollment returns none | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0543 | Integration (API) | P1 | – | `test_allowed_student_grades` | Allowed student grades | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0544 | Integration (API) | P1 | – | `test_package_covers` | Package covers | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0545 | Integration (API) | P1 | – | `test_course_access_paths` | Course access paths | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0546 | Integration (API) | P1 | – | `test_grant_package_reactivates_an_existing_row` | Grant package reactivates an existing row | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0547 | Integration (API) | P1 | – | `test_direct_enrollment_wins_over_package_end_date` | Direct enrollment wins over package end date | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0548 | Integration (API) | P1 | – | `test_my_enrollments_include_lesson_grants` | My enrollments include lesson grants | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0549 | Integration (API) | P1 | – | `test_my_access_to_a_course` | My access to a course | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0550 | Integration (API) | P1 | – | `test_get_enrollment_as_admin` | Get enrollment as admin | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0551 | Integration (API) | P1 | – | `test_list_packages_by_grade_and_stream` | List packages by grade and stream | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0552 | Integration (API) | P1 | – | `test_list_packages_marks_the_callers_own` | List packages marks the callers own | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0553 | Integration (API) | P1 | – | `test_enroll_in_a_free_package` | Enroll in a free package | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0554 | Integration (API) | P1 | – | `test_free_enroll_errors` | Free enroll errors | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0555 | Integration (API) | P1 | – | `test_my_class_enrollments` | My class enrollments | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0556 | Integration (API) | P1 | – | `test_admin_creates_and_filters_packages` | Admin creates and filters packages | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0557 | Integration (API) | P1 | – | `test_package_validation` | Package validation | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0558 | Integration (API) | P1 | – | `test_admin_package_routes_are_admin_only` | Admin package routes are admin only | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0559 | Integration (API) | P1 | – | `test_update_and_delete_missing_package` | Update and delete missing package | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0560 | Integration (API) | P1 | – | `test_deleting_a_package_removes_holders_and_reannounces` | Deleting a package removes holders and reannounces | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0561 | Integration (API) | P1 | – | `test_admin_lists_class_enrollments_with_names` | Admin lists class enrollments with names | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0562 | Integration (API) | P1 | – | `test_admin_grants_a_package_with_an_end_date` | Admin grants a package with an end date | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0563 | Integration (API) | P1 | – | `test_admin_revokes_a_class_enrollment` | Admin revokes a class enrollment | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0564 | Integration (API) | P1 | – | `test_grant_reactivates_a_cancelled_enrollment` | Grant reactivates a cancelled enrollment | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0565 | Integration (API) | P1 | – | `test_grant_skips_students_who_already_have_it` | Grant skips students who already have it | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0566 | Integration (API) | P1 | – | `test_grant_a_single_lesson` | Grant a single lesson | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0567 | Integration (API) | P1 | – | `test_grant_validation` | Grant validation | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0568 | Integration (API) | P1 | – | `test_revoke_a_course_keeps_the_record` | Revoke a course keeps the record | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0569 | Integration (API) | P1 | – | `test_revoke_a_lesson` | Revoke a lesson | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0570 | Integration (API) | P1 | – | `test_enrolled_list_includes_lesson_grants` | Enrolled list includes lesson grants | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0571 | Integration (API) | P1 | – | `test_eligible_needs_a_known_course` | Eligible needs a known course | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0572 | Integration (API) | P1 | – | `test_eligible_search_by_school` | Eligible search by school | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0573 | Integration (API) | P1 | – | `test_display_names_with_no_ids` | Display names with no ids | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0574 | Integration (API) | P1 | – | `test_enrollment_activated_payload` | Enrollment activated payload | `edura-backend/enrollment_service/tests/test_enrollment_service.py` | |
| TC-0575 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/enrollment_service/tests/test_migrations.py` | |

## Backend – notification_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0576 | Unit | P2 | – | `test_process_otp_requested_success` | Process otp requested success | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0577 | Unit | P2 | – | `test_process_payment_success` | Process payment success | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0578 | Unit | P2 | – | `test_process_certificate_issued` | Process certificate issued | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0579 | Unit | P2 | – | `test_process_proctoring_violation` | Process proctoring violation | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0580 | Unit | P2 | – | `test_email_failure_acks_and_logs_failed` | Email failure acks and logs failed | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0581 | Unit | P2 | – | `test_missing_email_acks_without_processing` | Missing email acks without processing | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0582 | Unit | P2 | – | `test_unhandled_routing_key_acks` | Unhandled routing key acks | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0583 | Unit | P2 | – | `test_start_consumer` | Start consumer | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0584 | Unit | P2 | – | `test_process_progress_report_attaches_pdf` | Process progress report attaches pdf | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0585 | Unit | P2 | – | `test_process_email_verification_sends_the_link` | Process email verification sends the link | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0586 | Unit | P2 | – | `test_password_reset_email_includes_reset_link` | Password reset email includes reset link | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0587 | Unit | P2 | – | `test_password_reset_email_uses_default_values` | Password reset email uses default values | `edura-backend/notification_service/tests/test_consumer.py` | |
| TC-0588 | Unit | P2 | – | `test_send_email_posts_to_resend_with_the_api_key` | Send email posts to resend with the api key | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0589 | Unit | P2 | – | `test_send_email_with_pdf_attachment` | Send email with pdf attachment | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0590 | Unit | P2 | – | `test_no_attachments_key_when_there_are_none` | No attachments key when there are none | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0591 | Unit | P2 | – | `test_missing_api_key_fails_clearly_without_calling_resend` | Missing api key fails clearly without calling resend | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0592 | Unit | P2 | – | `test_a_rejected_email_raises_with_resends_reason` | A rejected email raises with resends reason | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0593 | Unit | P2 | – | `test_an_unreachable_resend_raises_a_delivery_error` | An unreachable resend raises a delivery error | `edura-backend/notification_service/tests/test_email_service.py` | |
| TC-0594 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/notification_service/tests/test_migrations.py` | |
| TC-0595 | Integration (API) | P1 | – | `test_password_changed_email` | Password changed email | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0596 | Integration (API) | P1 | – | `test_student_email_and_id_fields_are_accepted` | Student email and id fields are accepted | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0597 | Integration (API) | P1 | – | `test_verification_link_lifetime_is_shown_in_hours` | Verification link lifetime is shown in hours | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0598 | Integration (API) | P1 | – | `test_progress_report_subject_without_a_month` | Progress report subject without a month | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0599 | Integration (API) | P1 | – | `test_broken_messages_are_dropped_not_requeued` | Broken messages are dropped not requeued | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0600 | Integration (API) | P1 | – | `test_consumer_retries_until_the_broker_is_reachable` | Consumer retries until the broker is reachable | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0601 | Integration (API) | P1 | – | `test_prepare_database_creates_tables_and_tolerates_sqlite` | Prepare database creates tables and tolerates sqlite | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0602 | Integration (API) | P1 | – | `test_prepare_database_survives_create_all_failure` | Prepare database survives create all failure | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0603 | Integration (API) | P1 | – | `test_enum_migrations_run_on_postgres` | Enum migrations run on postgres | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0604 | Integration (API) | P1 | – | `test_resend_error_that_is_not_json` | Resend error that is not json | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0605 | Integration (API) | P1 | – | `test_resend_error_without_a_message_uses_the_body` | Resend error without a message uses the body | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0606 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0607 | Integration (API) | P1 | – | `test_notification_route_is_for_notification_managers` | Notification route is for notification managers | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0608 | Integration (API) | P1 | – | `test_startup_creates_tables` | Startup creates tables | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0609 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/notification_service/tests/test_notification_service.py` | |
| TC-0610 | Unit | P2 | – | `test_render_otp_email` | Render otp email | `edura-backend/notification_service/tests/test_templates.py` | |
| TC-0611 | Unit | P2 | – | `test_render_payment_confirm` | Render payment confirm | `edura-backend/notification_service/tests/test_templates.py` | |
| TC-0612 | Unit | P2 | – | `test_render_cert_issued` | Render cert issued | `edura-backend/notification_service/tests/test_templates.py` | |
| TC-0613 | Unit | P2 | – | `test_render_violation_alert` | Render violation alert | `edura-backend/notification_service/tests/test_templates.py` | |

## Backend – payment_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0614 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/payment_service/tests/test_migrations.py` | |
| TC-0615 | Integration (API) | P1 | – | `test_the_course_price_copy_follows_catalogue_events` | The course price copy follows catalogue events | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0616 | Integration (API) | P1 | – | `test_free_enrollment_is_decided_from_the_local_price` | Free enrollment is decided from the local price | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0617 | Integration (API) | P1 | – | `test_receipt_is_checked_by_its_bytes_stored_and_announced` | Receipt is checked by its bytes stored and announced | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0618 | Integration (API) | P1 | – | `test_approving_a_receipt_announces_the_payment_and_the_review` | Approving a receipt announces the payment and the review | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0619 | Integration (API) | P1 | – | `test_rejecting_a_receipt_announces_only_the_review` | Rejecting a receipt announces only the review | `edura-backend/payment_service/tests/test_payment_events.py` | |
| TC-0620 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0621 | Integration (API) | P1 | – | `test_startup_creates_tables_and_starts_consumer` | Startup creates tables and starts consumer | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0622 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0623 | Integration (API) | P1 | – | `test_consumer_start_binds_payment_queue` | Consumer start binds payment queue | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0624 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0625 | Integration (API) | P1 | – | `test_checkout_creates_a_pending_payment_with_a_valid_hash` | Checkout creates a pending payment with a valid hash | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0626 | Integration (API) | P1 | – | `test_checkout_without_amount_defaults_to_1000` | Checkout without amount defaults to 1000 | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0627 | Integration (API) | P1 | – | `test_checkout_roles` | Checkout roles | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0628 | Integration (API) | P1 | – | `test_webhook_confirms_payment_and_announces_it` | Webhook confirms payment and announces it | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0629 | Integration (API) | P1 | – | `test_webhook_is_idempotent` | Webhook is idempotent | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0630 | Integration (API) | P1 | – | `test_webhook_failure_status_marks_payment_failed` | Webhook failure status marks payment failed | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0631 | Integration (API) | P1 | – | `test_webhook_rejects_bad_signatures` | Webhook rejects bad signatures | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0632 | Integration (API) | P1 | – | `test_webhook_for_unknown_order` | Webhook for unknown order | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0633 | Integration (API) | P1 | – | `test_signature_check_is_case_insensitive` | Signature check is case insensitive | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0634 | Integration (API) | P1 | – | `test_free_course_enrolls_once` | Free course enrolls once | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0635 | Integration (API) | P1 | – | `test_free_enroll_errors` | Free enroll errors | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0636 | Integration (API) | P1 | – | `test_upload_receipt` | Upload receipt | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0637 | Integration (API) | P1 | – | `test_receipt_bytes_must_match_the_declared_type` | Receipt bytes must match the declared type | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0638 | Integration (API) | P1 | – | `test_empty_receipt_is_refused` | Empty receipt is refused | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0639 | Integration (API) | P1 | – | `test_storage_outage_is_reported` | Storage outage is reported | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0640 | Integration (API) | P1 | – | `test_teacher_cannot_upload_receipts` | Teacher cannot upload receipts | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0641 | Integration (API) | P1 | – | `test_list_payments_by_role` | List payments by role | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0642 | Integration (API) | P1 | – | `test_admin_lists_receipts_with_filter` | Admin lists receipts with filter | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0643 | Integration (API) | P1 | – | `test_approve_receipt` | Approve receipt | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0644 | Integration (API) | P1 | – | `test_reject_receipt_with_reason` | Reject receipt with reason | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0645 | Integration (API) | P1 | – | `test_receipt_review_errors` | Receipt review errors | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0646 | Integration (API) | P1 | – | `test_admin_stats` | Admin stats | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0647 | Integration (API) | P1 | – | `test_admin_stats_when_empty` | Admin stats when empty | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0648 | Integration (API) | P1 | – | `test_sl_time_conversion` | Sl time conversion | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0649 | Integration (API) | P1 | – | `test_bank_account_crud` | Bank account crud | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0650 | Integration (API) | P1 | – | `test_bank_account_errors` | Bank account errors | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0651 | Integration (API) | P1 | – | `test_payment_success_defaults_completion_time` | Payment success defaults completion time | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0652 | Integration (API) | P1 | – | `test_receipt_reviewed_without_time` | Receipt reviewed without time | `edura-backend/payment_service/tests/test_payment_service.py` | |
| TC-0653 | Integration (API) | P1 | TestPayHereSignature | `test_verify_payhere_signature_valid` | Verify payhere signature valid | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0654 | Integration (API) | P1 | TestPayHereSignature | `test_verify_payhere_signature_invalid` | Verify payhere signature invalid | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0655 | Integration (API) | P1 | TestPaymentEndpoints | `test_checkout_missing_token_returns_401` | Checkout missing token returns 401 | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0656 | Integration (API) | P1 | TestPaymentEndpoints | `test_manual_receipt_upload_file_too_large_returns_400` | Manual receipt upload file too large returns 400 | `edura-backend/payment_service/tests/test_payments.py` | |
| TC-0657 | Integration (API) | P1 | TestPaymentEndpoints | `test_manual_receipt_upload_invalid_mime_returns_400` | Manual receipt upload invalid mime returns 400 | `edura-backend/payment_service/tests/test_payments.py` | |

## Backend – progress_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0658 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/progress_service/tests/test_migrations.py` | |
| TC-0659 | Integration (API) | P1 | – | `test_completion_percentage_calculation` | Unit test: 3 of 5 lessons watched -> completion_percentage = 60.0% | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0660 | Integration (API) | P1 | – | `test_certificate_eligibility_passed_and_failed` | Unit test: | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0661 | Integration (API) | P1 | – | `test_integration_lesson_watched_events_to_100_percent` | Integration test: processing lesson.watched events until completion reaches 100%. | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0662 | Integration (API) | P1 | – | `test_integration_certificate_issued_event_published` | Integration test: Certificate record created & certificate.issued event published. | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0663 | Integration (API) | P1 | – | `test_api_progress_dashboard_endpoint` | Integration test: GET /api/progress/courses/{course_id} | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0664 | Integration (API) | P1 | – | `test_api_leaderboard_endpoint` | Integration test: GET /api/progress/courses/{course_id}/leaderboard | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0665 | Integration (API) | P1 | – | `test_consumer_process_message` | Test consumer.process_message handling lesson.watched and assessment.graded. | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0666 | Integration (API) | P1 | – | `test_memory_redis_client_and_health` | Memory redis client and health | `edura-backend/progress_service/tests/test_progress.py` | |
| TC-0667 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0668 | Integration (API) | P1 | – | `test_lifespan_creates_tables_and_starts_the_consumer_thread` | Lifespan creates tables and starts the consumer thread | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0669 | Integration (API) | P1 | – | `test_lifespan_survives_create_all_failure` | Lifespan survives create all failure | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0670 | Integration (API) | P1 | – | `test_mark_lesson_watched_and_list_progress` | Mark lesson watched and list progress | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0671 | Integration (API) | P1 | – | `test_rewatching_keeps_the_longest_watch_time` | Rewatching keeps the longest watch time | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0672 | Integration (API) | P1 | – | `test_only_students_mark_lessons_watched` | Only students mark lessons watched | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0673 | Integration (API) | P1 | – | `test_dashboard_with_no_progress` | Dashboard with no progress | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0674 | Integration (API) | P1 | – | `test_dashboard_rejects_a_token_without_a_user` | Dashboard rejects a token without a user | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0675 | Integration (API) | P1 | – | `test_dashboard_after_activity` | Dashboard after activity | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0676 | Integration (API) | P1 | – | `test_leaderboard_falls_back_to_the_database` | Leaderboard falls back to the database | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0677 | Integration (API) | P1 | – | `test_leaderboard_prefers_redis` | Leaderboard prefers redis | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0678 | Integration (API) | P1 | – | `test_leaderboard_is_capped_at_ten` | Leaderboard is capped at ten | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0679 | Integration (API) | P1 | – | `test_unknown_lesson_count_treats_one_lesson_as_the_whole_course` | Unknown lesson count treats one lesson as the whole course | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0680 | Integration (API) | P1 | – | `test_more_lessons_drop_completion_but_keep_the_first_completion_date` | More lessons drop completion but keep the first completion date | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0681 | Integration (API) | P1 | – | `test_a_failed_assessment_blocks_the_certificate` | A failed assessment blocks the certificate | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0682 | Integration (API) | P1 | – | `test_certificate_is_issued_once` | Certificate is issued once | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0683 | Integration (API) | P1 | – | `test_points_are_scores_plus_a_completion_bonus` | Points are scores plus a completion bonus | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0684 | Integration (API) | P1 | – | `test_incomplete_events_are_acked_without_changes` | Incomplete events are acked without changes | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0685 | Integration (API) | P1 | – | `test_graded_event_without_a_course_goes_to_course_1` | Graded event without a course goes to course 1 | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0686 | Integration (API) | P1 | – | `test_lesson_watched_event` | Lesson watched event | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0687 | Integration (API) | P1 | – | `test_bad_messages_are_dropped` | Bad messages are dropped | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0688 | Integration (API) | P1 | – | `test_consumer_reconnects_until_the_broker_answers` | Consumer reconnects until the broker answers | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0689 | Integration (API) | P1 | – | `test_certificate_event_is_published_durably` | Certificate event is published durably | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0690 | Integration (API) | P1 | – | `test_certificate_event_defaults_the_time_and_never_raises` | Certificate event defaults the time and never raises | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0691 | Integration (API) | P1 | – | `test_memory_redis_strings_and_ttl` | Memory redis strings and ttl | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0692 | Integration (API) | P1 | – | `test_memory_redis_sorted_sets` | Memory redis sorted sets | `edura-backend/progress_service/tests/test_progress_service.py` | |
| TC-0693 | Integration (API) | P1 | – | `test_memory_redis_keys_and_delete` | Memory redis keys and delete | `edura-backend/progress_service/tests/test_progress_service.py` | |

## Backend – user_service

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0694 | Integration (API) | P1 | TestAdminOnly | `test_admin_passes` | Admin passes | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0695 | Integration (API) | P1 | TestAdminOnly | `test_student_blocked` | Student blocked | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0696 | Integration (API) | P1 | TestAdminOnly | `test_teacher_blocked` | Teacher blocked | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0697 | Integration (API) | P1 | TestTeacherOrAdmin | `test_teacher_passes` | Teacher passes | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0698 | Integration (API) | P1 | TestTeacherOrAdmin | `test_admin_passes` | Admin passes | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0699 | Integration (API) | P1 | TestTeacherOrAdmin | `test_student_blocked` | Student blocked | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0700 | Integration (API) | P1 | TestMissingToken | `test_no_header_returns_401` | No header returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0701 | Integration (API) | P1 | TestMissingToken | `test_token_without_bearer_prefix_returns_401` | Token without bearer prefix returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0702 | Integration (API) | P1 | TestMissingToken | `test_empty_bearer_returns_401` | Empty bearer returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0703 | Integration (API) | P1 | TestExpiredToken | `test_expired_token_returns_401` | Expired token returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0704 | Integration (API) | P1 | TestInvalidToken | `test_garbage_token_returns_401` | Garbage token returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0705 | Integration (API) | P1 | TestInvalidToken | `test_wrong_secret_returns_401` | Wrong secret returns 401 | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0706 | Integration (API) | P1 | TestPayloadInjection | `test_payload_sub_and_role_accessible` | Payload sub and role accessible | `edura-backend/user_service/tests/test_auth.py` | |
| TC-0707 | Migration | P2 | – | `test_migration_lifecycle` | Migration lifecycle | `edura-backend/user_service/tests/test_migrations.py` | |
| TC-0708 | Integration (API) | P1 | – | `test_health` | Health | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0709 | Integration (API) | P1 | – | `test_startup_seeds_reference_data_once` | Startup seeds reference data once | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0710 | Integration (API) | P1 | – | `test_seeding_keeps_an_existing_catalogue` | Seeding keeps an existing catalogue | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0711 | Integration (API) | P1 | – | `test_seeding_failure_is_logged_not_raised` | Seeding failure is logged not raised | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0712 | Integration (API) | P1 | – | `test_startup_survives_create_all_failure` | Startup survives create all failure | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0713 | Integration (API) | P1 | – | `test_signup_creates_profile_and_account` | Signup creates profile and account | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0714 | Integration (API) | P1 | – | `test_repeated_signup_event_keeps_one_profile` | Repeated signup event keeps one profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0715 | Integration (API) | P1 | – | `test_signup_without_a_form_only_stores_the_account` | Signup without a form only stores the account | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0716 | Integration (API) | P1 | – | `test_signup_with_missing_role_defaults_to_student` | Signup with missing role defaults to student | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0717 | Integration (API) | P1 | – | `test_account_update_never_creates_a_profile` | Account update never creates a profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0718 | Integration (API) | P1 | – | `test_enrollment_credits_the_referrer_once` | Enrollment credits the referrer once | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0719 | Integration (API) | P1 | – | `test_manual_grant_or_missing_student_earns_nothing` | Manual grant or missing student earns nothing | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0720 | Integration (API) | P1 | – | `test_consumer_rolls_back_and_reraises` | Consumer rolls back and reraises | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0721 | Integration (API) | P1 | – | `test_consumer_start_binds_user_queue` | Consumer start binds user queue | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0722 | Integration (API) | P1 | – | `test_resync_announces_streams_then_profiles` | Resync announces streams then profiles | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0723 | Integration (API) | P1 | – | `test_admin_lists_users_newest_first_with_account_details` | Admin lists users newest first with account details | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0724 | Integration (API) | P1 | – | `test_admin_list_filters_and_pages` | Admin list filters and pages | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0725 | Integration (API) | P1 | – | `test_admin_only_routes` | Admin only routes | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0726 | Integration (API) | P1 | – | `test_role_stats` | Role stats | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0727 | Integration (API) | P1 | – | `test_create_own_profile_takes_role_and_email_from_the_token` | Create own profile takes role and email from the token | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0728 | Integration (API) | P1 | – | `test_create_profile_twice_is_a_conflict` | Create profile twice is a conflict | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0729 | Integration (API) | P1 | – | `test_create_profile_validation` | Create profile validation | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0730 | Integration (API) | P1 | – | `test_create_profile_with_a_referral_code` | Create profile with a referral code | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0731 | Integration (API) | P1 | – | `test_unknown_referral_code_is_ignored_at_signup` | Unknown referral code is ignored at signup | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0732 | Integration (API) | P1 | – | `test_read_own_and_other_profiles` | Read own and other profiles | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0733 | Integration (API) | P1 | – | `test_own_email_falls_back_to_the_account_copy` | Own email falls back to the account copy | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0734 | Integration (API) | P1 | – | `test_update_own_profile` | Update own profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0735 | Integration (API) | P1 | – | `test_update_profile_permissions_and_missing` | Update profile permissions and missing | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0736 | Integration (API) | P1 | – | `test_referral_code_entered_on_profile_edit` | Referral code entered on profile edit | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0737 | Integration (API) | P1 | – | `test_admin_changes_role` | Admin changes role | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0738 | Integration (API) | P1 | – | `test_admin_deletes_profile` | Admin deletes profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0739 | Integration (API) | P1 | – | `test_stream_crud_and_events` | Stream crud and events | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0740 | Integration (API) | P1 | – | `test_stream_errors` | Stream errors | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0741 | Integration (API) | P1 | – | `test_grade_subject_crud` | Grade subject crud | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0742 | Integration (API) | P1 | – | `test_grade_subject_errors` | Grade subject errors | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0743 | Integration (API) | P1 | – | `test_subjects_for_a_grade` | Subjects for a grade | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0744 | Integration (API) | P1 | – | `test_referral_summary` | Referral summary | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0745 | Integration (API) | P1 | – | `test_referral_events_list` | Referral events list | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0746 | Integration (API) | P1 | – | `test_apply_referral_code` | Apply referral code | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0747 | Integration (API) | P1 | – | `test_apply_referral_code_errors` | Apply referral code errors | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0748 | Integration (API) | P1 | – | `test_apply_needs_a_student_with_a_profile` | Apply needs a student with a profile | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0749 | Integration (API) | P1 | – | `test_credit_needs_a_pending_event_and_a_referrer` | Credit needs a pending event and a referrer | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0750 | Integration (API) | P1 | – | `test_bind_referral_refuses_self_and_second_referrals` | Bind referral refuses self and second referrals | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0751 | Integration (API) | P1 | – | `test_find_referrer_ignores_blank_codes` | Find referrer ignores blank codes | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0752 | Integration (API) | P1 | – | `test_referral_code_prefix` | Referral code prefix | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0753 | Integration (API) | P1 | – | `test_referral_code_falls_back_after_collisions` | Referral code falls back after collisions | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0754 | Integration (API) | P1 | – | `test_profile_event_payload` | Profile event payload | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0755 | Integration (API) | P1 | – | `test_stream_event_defaults` | Stream event defaults | `edura-backend/user_service/tests/test_user_service.py` | |
| TC-0756 | Integration (API) | P1 | TestGetUser | `test_own_record_returns_200` | Own record returns 200 | `edura-backend/user_service/tests/test_users.py` | |
| TC-0757 | Integration (API) | P1 | TestGetUser | `test_admin_can_fetch_any_user` | Admin can fetch any user | `edura-backend/user_service/tests/test_users.py` | |
| TC-0758 | Integration (API) | P1 | TestGetUser | `test_nonexistent_user_returns_404` | Nonexistent user returns 404 | `edura-backend/user_service/tests/test_users.py` | |
| TC-0759 | Integration (API) | P1 | TestGetUserCrossAccess | `test_student_cannot_view_other_student` | Student cannot view other student | `edura-backend/user_service/tests/test_users.py` | |
| TC-0760 | Integration (API) | P1 | TestGetUserCrossAccess | `test_teacher_cannot_view_other_user` | Teacher cannot view other user | `edura-backend/user_service/tests/test_users.py` | |
| TC-0761 | Integration (API) | P1 | TestUpdateRole | `test_admin_updates_role_to_teacher` | Admin updates role to teacher | `edura-backend/user_service/tests/test_users.py` | |
| TC-0762 | Integration (API) | P1 | TestUpdateRole | `test_invalid_role_returns_422` | Invalid role returns 422 | `edura-backend/user_service/tests/test_users.py` | |
| TC-0763 | Integration (API) | P1 | TestUpdateRole | `test_student_cannot_update_own_role` | Student cannot update own role | `edura-backend/user_service/tests/test_users.py` | |
| TC-0764 | Integration (API) | P1 | TestRoleEnforcement | `test_student_blocked_from_admin_list_endpoint` | Student blocked from admin list endpoint | `edura-backend/user_service/tests/test_users.py` | |
| TC-0765 | Integration (API) | P1 | TestRoleEnforcement | `test_admin_can_access_list_endpoint` | Admin can access list endpoint | `edura-backend/user_service/tests/test_users.py` | |
| TC-0766 | Integration (API) | P1 | TestUpdateProfile | `test_student_updates_own_profile` | Student updates own profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0767 | Integration (API) | P1 | TestUpdateProfile | `test_student_cannot_update_other_profile` | Student cannot update other profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0768 | Integration (API) | P1 | TestDeleteUser | `test_admin_can_delete_user` | Admin can delete user | `edura-backend/user_service/tests/test_users.py` | |
| TC-0769 | Integration (API) | P1 | TestDeleteUser | `test_student_cannot_delete` | Student cannot delete | `edura-backend/user_service/tests/test_users.py` | |
| TC-0770 | Integration (API) | P1 | TestSignupEvents | `test_registration_builds_the_profile_and_stores_the_account` | Registration builds the profile and stores the account | `edura-backend/user_service/tests/test_users.py` | |
| TC-0771 | Integration (API) | P1 | TestSignupEvents | `test_a_repeated_event_does_not_create_a_second_profile` | A repeated event does not create a second profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0772 | Integration (API) | P1 | TestSignupEvents | `test_referral_code_from_the_signup_is_applied` | Referral code from the signup is applied | `edura-backend/user_service/tests/test_users.py` | |
| TC-0773 | Integration (API) | P1 | TestSignupEvents | `test_an_admin_created_without_a_form_still_gets_a_profile` | An admin created without a form still gets a profile | `edura-backend/user_service/tests/test_users.py` | |
| TC-0774 | Integration (API) | P1 | TestSignupEvents | `test_account_changes_update_the_listing` | Account changes update the listing | `edura-backend/user_service/tests/test_users.py` | |
| TC-0775 | Integration (API) | P1 | TestSignupEvents | `test_enrollment_credits_the_referrer_once_but_not_for_manual_grants` | Enrollment credits the referrer once but not for manual grants | `edura-backend/user_service/tests/test_users.py` | |
| TC-0776 | Integration (API) | P1 | TestProfileAnnouncements | `test_updating_and_deleting_a_profile_is_announced` | Updating and deleting a profile is announced | `edura-backend/user_service/tests/test_users.py` | |
| TC-0777 | Integration (API) | P1 | TestProfileAnnouncements | `test_streams_are_announced` | Streams are announced | `edura-backend/user_service/tests/test_users.py` | |
| TC-0778 | Integration (API) | P1 | TestNoDirectCalls | `test_the_old_internal_endpoints_are_gone` | The old internal endpoints are gone | `edura-backend/user_service/tests/test_users.py` | |

## Cross-service integration (edura-tests/integration)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0779 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac1_webhook_to_enrollment_chain` | AC1: Given a seeded student and course on staging | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0780 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac2_content_access_granted_after_enrollment` | AC2: Given the enrollment is now ACTIVE (from AC1) | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0781 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac3_invalid_hmac_blocks_enrollment` | AC3: Given a webhook POST with an invalid HMAC signature | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0782 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_ac4_duplicate_webhook_is_idempotent` | AC4: Given a valid webhook has already been processed (AC1) | `edura-tests/integration/test_payment_enrollment_flow.py` | |
| TC-0783 | Integration (cross-service) | P1 | TestPaymentEnrollmentFlow | `test_full_payment_enrollment_flow` | End-to-End sequence covering all 4 Acceptance Criteria in a single unified execution. | `edura-tests/integration/test_payment_enrollment_flow.py` | |

## Infrastructure (edura-infra)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0784 | Config | P2 | – | `test_nginx_conf_exists` | Nginx conf exists | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-0785 | Config | P2 | – | `test_all_11_upstream_blocks_exist` | All 11 upstream blocks exist | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-0786 | Config | P2 | – | `test_all_11_location_routes_exist` | All 11 location routes exist | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-0787 | Config | P2 | – | `test_rate_limiting_configured` | Rate limiting configured | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-0788 | Config | P2 | – | `test_cors_headers_configured` | Cors headers configured | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-0789 | Config | P2 | – | `test_proxy_headers_forwarded` | Proxy headers forwarded | `edura-infra/nginx/tests/test_nginx_config.py` | |
| TC-0790 | Config | P2 | – | `test_setup_rabbitmq_topology_mocked` | Unit test using mock pika blocking connection to test topology calls. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-0791 | Config | P2 | – | `test_obsolete_queues_are_removed` | Obsolete queues are removed | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-0792 | Config | P2 | – | `test_topology_is_consistent` | Every binding targets a declared queue; nothing is bound twice; every service has a queue. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-0793 | Config | P2 | – | `test_setup_idempotency` | Test that running setup multiple times is idempotent and produces no errors. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-0794 | Config | P2 | – | `test_topology_queues_and_exchange_declared` | Verify exchange and queues are passive-declared without error. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |
| TC-0795 | Config | P2 | – | `test_pub_sub_smoke` | Publish payment.success event and verify it reaches both enrollment.queue and notification.queue. | `edura-infra/rabbitmq/tests/test_rabbitmq_setup.py` | |

## End-to-end smoke (edura-tests/smoke)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0796 | E2E | P1 | – | `test_critical_path` | Pytest hook for running critical path test suite. | `edura-tests/smoke/critical_path.py` | |

## Frontend – Jest (edura-frontend)

| TC ID | Type | Priority | Class | Test | Description | Test file | Status |
|---|---|---|---|---|---|---|---|
| TC-0797 | Unit | P2 | access | `sends visitors to log in, keeping the query string` | sends visitors to log in, keeping the query string | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0798 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0799 | Unit | P2 | – | `sends non-admins home without loading courses` | sends non-admins home without loading courses | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0800 | Unit | P2 | list | `loads courses and streams` | loads courses and streams | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0801 | Unit | P2 | – | `shows each course card` | shows each course card | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0802 | Unit | P2 | – | `filters by title` | filters by title | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0803 | Unit | P2 | – | `offers to create the first course when there are none` | offers to create the first course when there are none | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0804 | Unit | P2 | – | `shows a failed load` | shows a failed load | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0805 | Unit | P2 | – | `opens and closes the access manager` | opens and closes the access manager | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0806 | Unit | P2 | – | `explains each course type and shows active A/L streams only for grades 12–13` | explains each course type and shows active A/L streams only for grades 12–13 | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0807 | Unit | P2 | – | `says when no streams exist` | says when no streams exist | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0808 | Unit | P2 | – | `creates an A/L exam course with the chosen streams` | creates an A/L exam course with the chosen streams | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0809 | Unit | P2 | – | `drops streams and grade for an ungated course, and unticks a stream` | drops streams and grade for an ungated course, and unticks a stream | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0810 | Unit | P2 | – | `uploads a thumbnail first` | uploads a thumbnail first | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0811 | Unit | P2 | – | `stops when the thumbnail upload fails` | stops when the thumbnail upload fails | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0812 | Unit | P2 | – | `validates the title and price` | validates the title and price | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0813 | Unit | P2 | – | `shows a failed create inside the modal` | shows a failed create inside the modal | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0814 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0815 | Unit | P2 | – | `prefills the form and locks the type once lessons exist` | prefills the form and locks the type once lessons exist | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0816 | Unit | P2 | – | `lets a course without lessons change type` | lets a course without lessons change type | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0817 | Unit | P2 | – | `keeps the current image and clears streams when the grade leaves A/L` | keeps the current image and clears streams when the grade leaves A/L | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0818 | Unit | P2 | – | `toggles streams while editing` | toggles streams while editing | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0819 | Unit | P2 | – | `replaces the image with a new upload` | replaces the image with a new upload | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0820 | Unit | P2 | – | `stops when the new image fails to upload` | stops when the new image fails to upload | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0821 | Unit | P2 | – | `validates and reports a failed save` | validates and reports a failed save | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0822 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0823 | Unit | P2 | publish and delete | `unpublishes a published course and publishes a draft` | unpublishes a published course and publishes a draft | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0824 | Unit | P2 | – | `shows a failed publish` | shows a failed publish | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0825 | Unit | P2 | – | `deletes only after confirming` | deletes only after confirming | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0826 | Unit | P2 | – | `shows a failed delete` | shows a failed delete | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0827 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0828 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0829 | Unit | P2 | – | `sends students home but lets super admins in` | sends students home but lets super admins in | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0830 | Unit | P2 | – | `loads courses when the store is empty` | loads courses when the store is empty | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0831 | Unit | P2 | – | `shows the course and its lessons` | shows the course and its lessons | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0832 | Unit | P2 | – | `shows a free course with no lessons` | shows a free course with no lessons | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0833 | Unit | P2 | – | `opens and closes the lesson access manager` | opens and closes the lesson access manager | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0834 | Unit | P2 | – | `creates a lesson with an image` | creates a lesson with an image | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0835 | Unit | P2 | – | `creates a lesson without an image` | creates a lesson without an image | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0836 | Unit | P2 | – | `needs a title` | needs a title | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0837 | Unit | P2 | – | `stops when the image upload fails` | stops when the image upload fails | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0838 | Unit | P2 | – | `needs a course id` | needs a course id | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0839 | Unit | P2 | – | `shows a failed create and closes` | shows a failed create and closes | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0840 | Unit | P2 | – | `prefills the form and keeps the current image` | prefills the form and keeps the current image | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0841 | Unit | P2 | – | `removes the image, with undo` | removes the image, with undo | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0842 | Unit | P2 | – | `replaces the image and deletes the old one` | replaces the image and deletes the old one | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0843 | Unit | P2 | – | `saves a lesson that never had an image` | saves a lesson that never had an image | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0844 | Unit | P2 | – | `stops when the new image fails to upload` | stops when the new image fails to upload | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0845 | Unit | P2 | – | `validates and reports a failed save` | validates and reports a failed save | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0846 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0847 | Unit | P2 | delete | `deletes the lesson and its image after confirming` | deletes the lesson and its image after confirming | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0848 | Unit | P2 | – | `skips the image for a lesson without one and shows failures` | skips the image for a lesson without one and shows failures | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0849 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0850 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0851 | Unit | P2 | – | `sends students home` | sends students home | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0852 | Unit | P2 | – | `loads courses when the store is empty` | loads courses when the store is empty | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0853 | Unit | P2 | – | `lists lessons in order` | lists lessons in order | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0854 | Unit | P2 | – | `shows an empty state when lessons fail to load` | shows an empty state when lessons fail to load | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0855 | Unit | P2 | – | `opens and closes the lesson access manager` | opens and closes the lesson access manager | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0856 | Unit | P2 | – | `creates a lesson with an image and reloads` | creates a lesson with an image and reloads | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0857 | Unit | P2 | – | `creates a lesson without an image` | creates a lesson without an image | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0858 | Unit | P2 | – | `needs a title and a course id` | needs a title and a course id | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0859 | Unit | P2 | – | `reports a missing course id` | reports a missing course id | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0860 | Unit | P2 | – | `stops when the image upload fails` | stops when the image upload fails | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0861 | Unit | P2 | – | `shows a failed create, then clears it when reopened` | shows a failed create, then clears it when reopened | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0862 | Unit | P2 | – | `keeps the current image and reloads` | keeps the current image and reloads | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0863 | Unit | P2 | – | `removes the image, with undo` | removes the image, with undo | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0864 | Unit | P2 | – | `replaces the image and deletes the old one` | replaces the image and deletes the old one | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0865 | Unit | P2 | – | `saves a lesson without an image` | saves a lesson without an image | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0866 | Unit | P2 | – | `stops when the new image fails to upload` | stops when the new image fails to upload | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0867 | Unit | P2 | – | `validates and reports a failed save` | validates and reports a failed save | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0868 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0869 | Unit | P2 | delete | `deletes the lesson and its image after confirming` | deletes the lesson and its image after confirming | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0870 | Unit | P2 | – | `shows a failed delete` | shows a failed delete | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0871 | Unit | P2 | – | `shows a spinner while analysing` | shows a spinner while analysing | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0872 | Unit | P2 | – | `renders nothing without a course` | renders nothing without a course | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0873 | Unit | P2 | – | `shows a failed analysis` | shows a failed analysis | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0874 | Unit | P2 | – | `summarises modules and papers` | summarises modules and papers | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0875 | Unit | P2 | – | `says when there is nothing to analyse` | says when there is nothing to analyse | `edura-frontend/src/app/__tests__/admin-course-pages.test.tsx` | |
| TC-0876 | Unit | P2 | access | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0877 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0878 | Unit | P2 | – | `sends students home` | sends students home | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0879 | Unit | P2 | – | `loads courses too when the store is empty` | loads courses too when the store is empty | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0880 | Unit | P2 | list | `shows this lesson's exams in order` | shows this lesson's exams in order | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0881 | Unit | P2 | – | `shows a loading state, then an empty lesson` | shows a loading state, then an empty lesson | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0882 | Unit | P2 | – | `shows a failed load` | shows a failed load | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0883 | Unit | P2 | – | `suggests the next order number and creates a scheduled exam` | suggests the next order number and creates a scheduled exam | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0884 | Unit | P2 | – | `creates an anytime exam with an image` | creates an anytime exam with an image | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0885 | Unit | P2 | – | `validates title and duration` | validates title and duration | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0886 | Unit | P2 | – | `stops when the image upload fails` | stops when the image upload fails | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0887 | Unit | P2 | – | `needs a lesson id` | needs a lesson id | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0888 | Unit | P2 | – | `shows a failed create and closes` | shows a failed create and closes | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0889 | Unit | P2 | – | `prefills the form and keeps the current image` | prefills the form and keeps the current image | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0890 | Unit | P2 | – | `leaves whole-hour durations without minutes and can clear the schedule` | leaves whole-hour durations without minutes and can clear the schedule | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0891 | Unit | P2 | – | `opens a sub-hour exam with minutes only` | opens a sub-hour exam with minutes only | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0892 | Unit | P2 | – | `removes the image, with undo` | removes the image, with undo | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0893 | Unit | P2 | – | `replaces the image and deletes the old one` | replaces the image and deletes the old one | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0894 | Unit | P2 | – | `stops when the new image fails to upload` | stops when the new image fails to upload | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0895 | Unit | P2 | – | `validates and reports a failed save` | validates and reports a failed save | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0896 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0897 | Unit | P2 | delete | `deletes the exam and its image after confirming` | deletes the exam and its image after confirming | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0898 | Unit | P2 | – | `shows a failed delete` | shows a failed delete | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0899 | Unit | P2 | – | `downloads the template` | downloads the template | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0900 | Unit | P2 | – | `logs a failed template download` | logs a failed template download | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0901 | Unit | P2 | – | `imports a ZIP, shows the summary and reloads exams` | imports a ZIP, shows the summary and reloads exams | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0902 | Unit | P2 | – | `does not reload when nothing was created` | does not reload when nothing was created | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0903 | Unit | P2 | – | `stays open while importing and shows failures` | stays open while importing and shows failures | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0904 | Unit | P2 | access | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0905 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0906 | Unit | P2 | – | `sends students home` | sends students home | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0907 | Unit | P2 | – | `loads the course and exams when the store is empty` | loads the course and exams when the store is empty | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0908 | Unit | P2 | list | `shows progress and each question` | shows progress and each question | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0909 | Unit | P2 | – | `counts remaining questions` | counts remaining questions | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0910 | Unit | P2 | – | `says when all questions exist` | says when all questions exist | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0911 | Unit | P2 | – | `shows loading, then an empty exam` | shows loading, then an empty exam | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0912 | Unit | P2 | – | `shows a failed load` | shows a failed load | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0913 | Unit | P2 | – | `defaults to four options when the course is unknown` | defaults to four options when the course is unknown | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0914 | Unit | P2 | – | `creates a question from the filled options` | creates a question from the filled options | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0915 | Unit | P2 | – | `uploads question and option images` | uploads question and option images | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0916 | Unit | P2 | – | `keeps going when an option image fails to upload` | keeps going when an option image fails to upload | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0917 | Unit | P2 | – | `stops when the question image fails to upload` | stops when the question image fails to upload | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0918 | Unit | P2 | – | `validates text, options and the correct answer` | validates text, options and the correct answer | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0919 | Unit | P2 | – | `shows a failed create and closes` | shows a failed create and closes | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0920 | Unit | P2 | – | `prefills the form and saves unchanged images` | prefills the form and saves unchanged images | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0921 | Unit | P2 | – | `pads options up to the grade count` | pads options up to the grade count | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0922 | Unit | P2 | – | `trims extra options for lower grades and fills blank questions` | trims extra options for lower grades and fills blank questions | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0923 | Unit | P2 | – | `removes the question image, with undo` | removes the question image, with undo | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0924 | Unit | P2 | – | `replaces the question image and deletes the old one` | replaces the question image and deletes the old one | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0925 | Unit | P2 | – | `stops when the new question image fails to upload` | stops when the new question image fails to upload | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0926 | Unit | P2 | – | `removes an option image, with undo` | removes an option image, with undo | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0927 | Unit | P2 | – | `replaces option images, deleting old ones, and skips failed uploads` | replaces option images, deleting old ones, and skips failed uploads | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0928 | Unit | P2 | – | `validates and reports a failed save` | validates and reports a failed save | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0929 | Unit | P2 | – | `needs exactly one correct answer` | needs exactly one correct answer | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0930 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0931 | Unit | P2 | delete | `deletes the question and its images after confirming` | deletes the question and its images after confirming | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0932 | Unit | P2 | – | `shows a failed delete` | shows a failed delete | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0933 | Unit | P2 | – | `imports, lists skipped rows and reloads` | imports, lists skipped rows and reloads | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0934 | Unit | P2 | – | `reports zero imports without skipped rows` | reports zero imports without skipped rows | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0935 | Unit | P2 | – | `needs a file and shows failed imports` | needs a file and shows failed imports | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0936 | Unit | P2 | – | `downloads the template` | downloads the template | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0937 | Unit | P2 | – | `shows a failed template download` | shows a failed template download | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0938 | Unit | P2 | – | `closes with Cancel or ✕` | closes with Cancel or ✕ | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0939 | Unit | P2 | – | `applies images, lists errors and reloads` | applies images, lists errors and reloads | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0940 | Unit | P2 | – | `shows a clean result without an error list` | shows a clean result without an error list | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0941 | Unit | P2 | – | `needs a file and shows failed uploads` | needs a file and shows failed uploads | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0942 | Unit | P2 | preview | `shows the paper as students see it, with an answer toggle` | shows the paper as students see it, with an answer toggle | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0943 | Unit | P2 | – | `omits grade details when the course is unknown` | omits grade details when the course is unknown | `edura-frontend/src/app/__tests__/admin-exam-pages.test.tsx` | |
| TC-0944 | Unit | P2 | Admin messages | `sends non-admins home and renders nothing` | sends non-admins home and renders nothing | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0945 | Unit | P2 | – | `groups conversations by unread and recency` | groups conversations by unread and recency | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0946 | Unit | P2 | – | `shows a loader while conversations sync` | shows a loader while conversations sync | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0947 | Unit | P2 | – | `searches by name and last message` | searches by name and last message | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0948 | Unit | P2 | – | `opens a conversation and its messages` | opens a conversation and its messages | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0949 | Unit | P2 | – | `closes the sidebar on small screens when a conversation is picked` | closes the sidebar on small screens when a conversation is picked | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0950 | Unit | P2 | – | `toggles the sidebar from the header` | toggles the sidebar from the header | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0951 | Unit | P2 | – | `leaves for the dashboard, clearing the selection` | leaves for the dashboard, clearing the selection | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0952 | Unit | P2 | – | `sends with the button and refreshes the list` | sends with the button and refreshes the list | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0953 | Unit | P2 | – | `sends on Enter but not Shift+Enter` | sends on Enter but not Shift+Enter | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0954 | Unit | P2 | – | `ignores blank replies` | ignores blank replies | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0955 | Unit | P2 | – | `puts the text back when sending fails` | puts the text back when sending fails | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0956 | Unit | P2 | deleting a conversation | `clears the open chat from the header` | clears the open chat from the header | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0957 | Unit | P2 | – | `deletes from the sidebar without opening the chat` | deletes from the sidebar without opening the chat | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0958 | Unit | P2 | – | `shows a failed delete in the dialog` | shows a failed delete in the dialog | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0959 | Unit | P2 | – | `cancel keeps the conversation` | cancel keeps the conversation | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0960 | Unit | P2 | starting a conversation | `finds the student's conversation and adds it to the list` | finds the student's conversation and adds it to the list | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0961 | Unit | P2 | – | `closes the search` | closes the search | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0962 | Unit | P2 | – | `refreshes conversations every 7s and the open chat every 5s` | refreshes conversations every 7s and the open chat every 5s | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0963 | Unit | P2 | – | `lists feedback and searches it` | lists feedback and searches it | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0964 | Unit | P2 | – | `shows empty and loading states` | shows empty and loading states | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0965 | Unit | P2 | – | `opens a feedback entry and marks it read` | opens a feedback entry and marks it read | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0966 | Unit | P2 | – | `shows read feedback without a mark-read button` | shows read feedback without a mark-read button | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0967 | Unit | P2 | – | `deletes feedback from the header` | deletes feedback from the header | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0968 | Unit | P2 | – | `deletes feedback from the list and shows failures` | deletes feedback from the list and shows failures | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0969 | Unit | P2 | – | `goes back to chats` | goes back to chats | `edura-frontend/src/app/__tests__/admin-messages-page.test.tsx` | |
| TC-0970 | Unit | P2 | Admin dashboard | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0971 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0972 | Unit | P2 | – | `sends non-admins home without loading stats` | sends non-admins home without loading stats | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0973 | Unit | P2 | – | `greets the admin and shows the stat cards` | greets the admin and shows the stat cards | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0974 | Unit | P2 | – | `highlights pending bank slips` | highlights pending bank slips | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0975 | Unit | P2 | – | `uses the singular for one pending slip and hides the banner for none` | uses the singular for one pending slip and hides the banner for none | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0976 | Unit | P2 | – | `links every quick action` | links every quick action | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0977 | Unit | P2 | – | `lists recent activity` | lists recent activity | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0978 | Unit | P2 | – | `shows placeholders while loading and an empty activity message` | shows placeholders while loading and an empty activity message | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0979 | Unit | P2 | – | `sends non-admins home` | sends non-admins home | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0980 | Unit | P2 | – | `loads analytics and stats and fills every panel` | loads analytics and stats and fills every panel | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0981 | Unit | P2 | – | `shows empty states` | shows empty states | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0982 | Unit | P2 | – | `shows placeholders while loading` | shows placeholders while loading | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0983 | Unit | P2 | – | `shows the load error` | shows the load error | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0984 | Unit | P2 | – | `sends non-admins home` | sends non-admins home | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0985 | Unit | P2 | – | `loads the exam list first and asks for an exam` | loads the exam list first and asks for an exam | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0986 | Unit | P2 | – | `loads the leaderboard for an exam and district` | loads the leaderboard for an exam and district | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0987 | Unit | P2 | – | `shows an empty board and clears filters` | shows an empty board and clears filters | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0988 | Unit | P2 | – | `shows the load error` | shows the load error | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0989 | Unit | P2 | Admin settings | `sends non-admins home` | sends non-admins home | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0990 | Unit | P2 | – | `shows account info and fills the name` | shows account info and fills the name | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0991 | Unit | P2 | – | `shows inactive accounts` | shows inactive accounts | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0992 | Unit | P2 | – | `reports profile saving as successful` | reports profile saving as successful | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0993 | Unit | P2 | – | `changes the password and clears the form` | changes the password and clears the form | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0994 | Unit | P2 | – | `checks the new passwords match and are long enough` | checks the new passwords match and are long enough | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0995 | Unit | P2 | – | `shows the server error` | shows the server error | `edura-frontend/src/app/__tests__/admin-overview-pages.test.tsx` | |
| TC-0996 | Unit | P2 | – | `sends non-admins to their dashboard` | sends non-admins to their dashboard | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-0997 | Unit | P2 | – | `loads pending slips and the course filter` | loads pending slips and the course filter | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-0998 | Unit | P2 | – | `opens the bank accounts page` | opens the bank accounts page | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-0999 | Unit | P2 | – | `shows all submissions and filters by course` | shows all submissions and filters by course | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1000 | Unit | P2 | – | `says when there is nothing to review` | says when there is nothing to review | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1001 | Unit | P2 | – | `shows the load error` | shows the load error | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1002 | Unit | P2 | – | `keeps working when the course list fails` | keeps working when the course list fails | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1003 | Unit | P2 | – | `shows the slip details with the image from the API host` | shows the slip details with the image from the API host | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1004 | Unit | P2 | – | `uses absolute image urls as they are` | uses absolute image urls as they are | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1005 | Unit | P2 | – | `shows no image without an API url configured` | shows no image without an API url configured | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1006 | Unit | P2 | – | `approves a slip` | approves a slip | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1007 | Unit | P2 | – | `needs a reason to reject` | needs a reason to reject | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1008 | Unit | P2 | – | `rejects with the reason` | rejects with the reason | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1009 | Unit | P2 | – | `shows a failed approval` | shows a failed approval | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1010 | Unit | P2 | – | `shows the rejection reason and no actions for processed slips` | shows the rejection reason and no actions for processed slips | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1011 | Unit | P2 | – | `closes the review` | closes the review | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1012 | Unit | P2 | – | `shows the global revenue summary` | shows the global revenue summary | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1013 | Unit | P2 | – | `breaks earnings down for one course` | breaks earnings down for one course | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1014 | Unit | P2 | – | `says when there is no analysis` | says when there is no analysis | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1015 | Unit | P2 | – | `sends non-admins to their dashboard` | sends non-admins to their dashboard | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1016 | Unit | P2 | – | `lists every account, active or not` | lists every account, active or not | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1017 | Unit | P2 | – | `shows a loader, then an empty state that opens the form` | shows a loader, then an empty state that opens the form | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1018 | Unit | P2 | – | `adds an account with a live preview` | adds an account with a live preview | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1019 | Unit | P2 | – | `edits an account` | edits an account | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1020 | Unit | P2 | – | `toggles an account on and off` | toggles an account on and off | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1021 | Unit | P2 | – | `deletes only after confirming` | deletes only after confirming | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1022 | Unit | P2 | – | `cancel closes the form` | cancel closes the form | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1023 | Unit | P2 | – | `shows the load error` | shows the load error | `edura-frontend/src/app/__tests__/admin-payment-pages.test.tsx` | |
| TC-1024 | Unit | P2 | – | `sends non-admins home without loading students` | sends non-admins home without loading students | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1025 | Unit | P2 | – | `lists students with their details` | lists students with their details | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1026 | Unit | P2 | – | `uses the singular for one student and shows an empty table` | uses the singular for one student and shows an empty table | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1027 | Unit | P2 | – | `sends each filter to the API` | sends each filter to the API | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1028 | Unit | P2 | – | `pages through results` | pages through results | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1029 | Unit | P2 | – | `a new filter goes back to the first page` | a new filter goes back to the first page | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1030 | Unit | P2 | – | `opens a student's progress` | opens a student's progress | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1031 | Unit | P2 | – | `toggles a student's status in place` | toggles a student's status in place | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1032 | Unit | P2 | – | `shows a failed toggle` | shows a failed toggle | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1033 | Unit | P2 | – | `deletes a student only after confirming` | deletes a student only after confirming | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1034 | Unit | P2 | – | `shows a failed delete` | shows a failed delete | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1035 | Unit | P2 | – | `shows skeleton rows while loading` | shows skeleton rows while loading | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1036 | Unit | P2 | – | `loads the student's progress` | loads the student's progress | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1037 | Unit | P2 | – | `shows the header, metrics, contacts and subject cards` | shows the header, metrics, contacts and subject cards | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1038 | Unit | P2 | – | `expands a subject to list its exams` | expands a subject to list its exams | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1039 | Unit | P2 | – | `lists attempt history and opens an attempt` | lists attempt history and opens an attempt | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1040 | Unit | P2 | – | `dispatches the report and toasts the result` | dispatches the report and toasts the result | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1041 | Unit | P2 | – | `uses a default success message` | uses a default success message | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1042 | Unit | P2 | – | `toasts a failed report` | toasts a failed report | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1043 | Unit | P2 | – | `shows a load error with a way back` | shows a load error with a way back | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1044 | Unit | P2 | – | `clears the error when leaving` | clears the error when leaving | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1045 | Unit | P2 | – | `loads and shows the attempt` | loads and shows the attempt | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1046 | Unit | P2 | – | `marks scores under 85% as not passed and navigates back` | marks scores under 85% as not passed and navigates back | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1047 | Unit | P2 | – | `shows the error` | shows the error | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1048 | Unit | P2 | – | `does nothing without both ids` | does nothing without both ids | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1049 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1050 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1051 | Unit | P2 | – | `sends a %s to the admin dashboard` | sends a %s to the admin dashboard | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1052 | Unit | P2 | – | `lists the other admins` | lists the other admins | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1053 | Unit | P2 | – | `shows an empty list and load errors` | shows an empty list and load errors | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1054 | Unit | P2 | – | `creates an admin and closes the form` | creates an admin and closes the form | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1055 | Unit | P2 | – | `shows a failed create in the form` | shows a failed create in the form | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1056 | Unit | P2 | – | `cancel and the backdrop close the form` | cancel and the backdrop close the form | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1057 | Unit | P2 | – | `removes an admin after confirming` | removes an admin after confirming | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1058 | Unit | P2 | – | `alerts when removing fails` | alerts when removing fails | `edura-frontend/src/app/__tests__/admin-people-pages.test.tsx` | |
| TC-1059 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1060 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1061 | Unit | P2 | – | `sends non-admins home` | sends non-admins home | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1062 | Unit | P2 | subjects tab | `lists Grade 10 subjects first and counts active ones` | lists Grade 10 subjects first and counts active ones | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1063 | Unit | P2 | – | `switches grade` | switches grade | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1064 | Unit | P2 | – | `adds a trimmed subject and reloads` | adds a trimmed subject and reloads | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1065 | Unit | P2 | – | `shows a failed add` | shows a failed add | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1066 | Unit | P2 | – | `edits a subject name and status` | edits a subject name and status | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1067 | Unit | P2 | – | `cancels an edit and reports a failed save` | cancels an edit and reports a failed save | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1068 | Unit | P2 | – | `deletes a subject only after confirming` | deletes a subject only after confirming | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1069 | Unit | P2 | – | `shows a failed delete and a failed load` | shows a failed delete and a failed load | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1070 | Unit | P2 | – | `lists streams with their subjects` | lists streams with their subjects | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1071 | Unit | P2 | – | `shows an empty state` | shows an empty state | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1072 | Unit | P2 | – | `creates a stream from comma-separated subjects` | creates a stream from comma-separated subjects | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1073 | Unit | P2 | – | `needs at least one real subject` | needs at least one real subject | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1074 | Unit | P2 | – | `shows a failed create` | shows a failed create | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1075 | Unit | P2 | – | `edits a stream, including its status` | edits a stream, including its status | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1076 | Unit | P2 | – | `needs a subject when editing and reports failures` | needs a subject when editing and reports failures | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1077 | Unit | P2 | – | `closes the modal with ✕ and Cancel` | closes the modal with ✕ and Cancel | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1078 | Unit | P2 | – | `deletes a stream after confirming, and shows failures` | deletes a stream after confirming, and shows failures | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1079 | Unit | P2 | – | `fetches the user when auth is not initialised` | fetches the user when auth is not initialised | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1080 | Unit | P2 | – | `sends visitors to log in and students to their courses` | sends visitors to log in and students to their courses | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1081 | Unit | P2 | – | `groups packages by level` | groups packages by level | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1082 | Unit | P2 | – | `filters by grade and status` | filters by grade and status | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1083 | Unit | P2 | – | `shows an empty state and the load error` | shows an empty state and the load error | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1084 | Unit | P2 | – | `reports a failed auto-generate` | reports a failed auto-generate | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1085 | Unit | P2 | – | `creates a package, naming it from the grade and stream` | creates a package, naming it from the grade and stream | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1086 | Unit | P2 | – | `drops the stream when the grade goes below A/L` | drops the stream when the grade goes below A/L | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1087 | Unit | P2 | – | `edits a package without renaming it` | edits a package without renaming it | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1088 | Unit | P2 | – | `keeps the form open with the error when saving fails` | keeps the form open with the error when saving fails | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1089 | Unit | P2 | – | `deletes a package after confirming in the dialog` | deletes a package after confirming in the dialog | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1090 | Unit | P2 | – | `reports a failed delete` | reports a failed delete | `edura-frontend/src/app/__tests__/admin-structure-pages.test.tsx` | |
| TC-1091 | Unit | P2 | access and loading | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1092 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1093 | Unit | P2 | – | `sends students home` | sends students home | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1094 | Unit | P2 | – | `loads the course list when the store is empty` | loads the course list when the store is empty | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1095 | Unit | P2 | – | `loads the lesson, its videos and materials` | loads the lesson, its videos and materials | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1096 | Unit | P2 | – | `shows a failed load` | shows a failed load | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1097 | Unit | P2 | – | `handles an unknown lesson with no content` | handles an unknown lesson with no content | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1098 | Unit | P2 | content list | `shows lesson-level materials` | shows lesson-level materials | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1099 | Unit | P2 | – | `shows videos in order with their details and materials` | shows videos in order with their details and materials | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1100 | Unit | P2 | – | `adds a video from a YouTube URL` | adds a video from a YouTube URL | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1101 | Unit | P2 | – | `treats blank numbers as zero` | treats blank numbers as zero | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1102 | Unit | P2 | – | `edits a video` | edits a video | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1103 | Unit | P2 | – | `opens a video without a stored duration` | opens a video without a stored duration | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1104 | Unit | P2 | – | `shows a failed save and closes` | shows a failed save and closes | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1105 | Unit | P2 | – | `deletes a video only after confirming` | deletes a video only after confirming | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1106 | Unit | P2 | – | `alerts when a delete fails` | alerts when a delete fails | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1107 | Unit | P2 | – | `needs a file for a new material` | needs a file for a new material | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1108 | Unit | P2 | – | `adds a lesson-level material` | adds a lesson-level material | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1109 | Unit | P2 | – | `adds a material to a video` | adds a material to a video | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1110 | Unit | P2 | – | `edits a material and keeps its file` | edits a material and keeps its file | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1111 | Unit | P2 | – | `replaces a material file and removes the old one, ignoring cleanup errors` | replaces a material file and removes the old one, ignoring cleanup errors | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1112 | Unit | P2 | – | `edits a lesson-level material without a stored public id or type` | edits a lesson-level material without a stored public id or type | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1113 | Unit | P2 | – | `shows a failed save and closes` | shows a failed save and closes | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1114 | Unit | P2 | – | `deletes a material and its file after confirming` | deletes a material and its file after confirming | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1115 | Unit | P2 | – | `deletes a lesson-level material without a stored file id` | deletes a lesson-level material without a stored file id | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1116 | Unit | P2 | – | `alerts when a delete fails` | alerts when a delete fails | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1117 | Unit | P2 | – | `lists the checkpoints for a video` | lists the checkpoints for a video | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1118 | Unit | P2 | – | `shows an empty video and logs failed loads` | shows an empty video and logs failed loads | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1119 | Unit | P2 | – | `downloads the CSV template and reports failures` | downloads the CSV template and reports failures | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1120 | Unit | P2 | – | `imports a CSV on top of existing quizzes` | imports a CSV on top of existing quizzes | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1121 | Unit | P2 | – | `shows a failed import` | shows a failed import | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1122 | Unit | P2 | – | `edits a checkpoint question and timing` | edits a checkpoint question and timing | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1123 | Unit | P2 | – | `updates timing only for a checkpoint without a question` | updates timing only for a checkpoint without a question | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1124 | Unit | P2 | – | `shows a failed checkpoint save and goes back to the list` | shows a failed checkpoint save and goes back to the list | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1125 | Unit | P2 | – | `leaves edit mode when the manager closes` | leaves edit mode when the manager closes | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1126 | Unit | P2 | – | `deletes a checkpoint after confirming` | deletes a checkpoint after confirming | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1127 | Unit | P2 | – | `alerts when a checkpoint delete fails` | alerts when a checkpoint delete fails | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1128 | Unit | P2 | – | `clears every checkpoint after confirming` | clears every checkpoint after confirming | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1129 | Unit | P2 | – | `alerts when clearing fails` | alerts when clearing fails | `edura-frontend/src/app/__tests__/admin-video-content-page.test.tsx` | |
| TC-1130 | Unit | P2 | – | `signs a student in and sends them to the callback URL` | signs a student in and sends them to the callback URL | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1131 | Unit | P2 | – | `sends admins to the admin dashboard` | sends admins to the admin dashboard | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1132 | Unit | P2 | – | `shows wrong credentials` | shows wrong credentials | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1133 | Unit | P2 | – | `offers to resend the verification email for an unverified account` | offers to resend the verification email for an unverified account | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1134 | Unit | P2 | – | `explains when the verification email cannot be sent` | explains when the verification email cannot be sent | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1135 | Unit | P2 | – | `toggles password visibility` | toggles password visibility | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1136 | Unit | P2 | – | `shows a busy state while signing in` | shows a busy state while signing in | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1137 | Unit | P2 | – | `signs in with Google` | signs in with Google | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1138 | Unit | P2 | – | `logs a failed Google sign-in` | logs a failed Google sign-in | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1139 | Unit | P2 | Forgot password page | `sends the reset link and shows a confirmation` | sends the reset link and shows a confirmation | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1140 | Unit | P2 | – | `shows an error when the request fails` | shows an error when the request fails | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1141 | Unit | P2 | – | `shows a busy state` | shows a busy state | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1142 | Unit | P2 | – | `needs a token from the email link` | needs a token from the email link | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1143 | Unit | P2 | – | `checks the passwords match and are long enough` | checks the passwords match and are long enough | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1144 | Unit | P2 | – | `rejects a short password before calling the server` | rejects a short password before calling the server | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1145 | Unit | P2 | – | `resets the password and returns to login` | resets the password and returns to login | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1146 | Unit | P2 | – | `goes to plain login without a callback` | goes to plain login without a callback | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1147 | Unit | P2 | – | `shows an expired-link error from the server` | shows an expired-link error from the server | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1148 | Unit | P2 | – | `shows a busy state` | shows a busy state | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1149 | Unit | P2 | Verify email page | `verifies the link from the email` | verifies the link from the email | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1150 | Unit | P2 | – | `explains a bad link and resends a new one` | explains a bad link and resends a new one | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1151 | Unit | P2 | – | `handles a link without a token and a failed resend` | handles a link without a token and a failed resend | `edura-frontend/src/app/__tests__/auth-pages.test.tsx` | |
| TC-1152 | Unit | P2 | robots and sitemap | `allows every crawler and points at the sitemap` | allows every crawler and points at the sitemap | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1153 | Unit | P2 | – | `lists the public pages with the home page first` | lists the public pages with the home page first | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1154 | Unit | P2 | Root layout metadata | `sets the title template, canonical url and theme colour` | sets the title template, canonical url and theme colour | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1155 | Unit | P2 | Thin wrapper pages | `both course pages render the shared course list` | both course pages render the shared course list | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1156 | Unit | P2 | – | `the old subjects page redirects to streams` | the old subjects page redirects to streams | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1157 | Unit | P2 | – | `the feedback page shows the form and its metadata` | the feedback page shows the form and its metadata | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1158 | Unit | P2 | Home page | `loads stats, ranking exams, streams and then the top three` | loads stats, ranking exams, streams and then the top three | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1159 | Unit | P2 | – | `shows popular courses with stream names, prices and links` | shows popular courses with stream names, prices and links | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1160 | Unit | P2 | – | `shows skeleton cards until stats arrive` | shows skeleton cards until stats arrive | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1161 | Unit | P2 | – | `shows the live leaderboard with medals` | shows the live leaderboard with medals | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1162 | Unit | P2 | – | `names the student count in the call to action` | names the student count in the call to action | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1163 | Unit | P2 | – | `does not refetch what the store already has` | does not refetch what the store already has | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1164 | Unit | P2 | – | `sends a signed-in %s to the admin dashboard` | sends a signed-in %s to the admin dashboard | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1165 | Unit | P2 | – | `stays at zero until the section scrolls into view` | stays at zero until the section scrolls into view | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1166 | Unit | P2 | – | `counts up to the real figures, abbreviating thousands` | counts up to the real figures, abbreviating thousands | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1167 | Unit | P2 | – | `leaves students on the home page` | leaves students on the home page | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1168 | Unit | P2 | Info page | `fetches platform stats and shows them` | fetches platform stats and shows them | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1169 | Unit | P2 | – | `shows dashes while stats are loading` | shows dashes while stats are loading | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1170 | Unit | P2 | – | `skips the fetch when stats are already loaded` | skips the fetch when stats are already loaded | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1171 | Unit | P2 | – | `lists the FAQs and contact details` | lists the FAQs and contact details | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1172 | Unit | P2 | – | `shows a loader until auth is initialised` | shows a loader until auth is initialised | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1173 | Unit | P2 | – | `sends visitors to log in, back to the dashboard` | sends visitors to log in, back to the dashboard | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1174 | Unit | P2 | – | `loads enrollments, attempts, referrals and badges` | loads enrollments, attempts, referrals and badges | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1175 | Unit | P2 | – | `fetches the profile when signed in without one` | fetches the profile when signed in without one | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1176 | Unit | P2 | – | `passes store data to the three columns` | passes store data to the three columns | `edura-frontend/src/app/__tests__/general-pages.test.tsx` | |
| TC-1177 | Unit | P2 | Payment page | `sends visitors to log in, back to this page` | sends visitors to log in, back to this page | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1178 | Unit | P2 | – | `needs a payment type and item` | needs a payment type and item | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1179 | Unit | P2 | – | `summarises the item and lists deposit banks, selecting the first` | summarises the item and lists deposit banks, selecting the first | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1180 | Unit | P2 | – | `starts a bank-slip payment with the chosen bank` | starts a bank-slip payment with the chosen bank | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1181 | Unit | P2 | – | `waits for bank accounts and lets the student go back` | waits for bank accounts and lets the student go back | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1182 | Unit | P2 | – | `shows a server error from a failed bank-account load` | shows a server error from a failed bank-account load | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1183 | Unit | P2 | – | `needs a payment id` | needs a payment id | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1184 | Unit | P2 | – | `loads the checkout and adds the PayHere script` | loads the checkout and adds the PayHere script | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1185 | Unit | P2 | – | `does not add the script when the checkout cannot be loaded` | does not add the script when the checkout cannot be loaded | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1186 | Unit | P2 | – | `shows the chosen bank and uploads the slip with the details` | shows the chosen bank and uploads the slip with the details | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1187 | Unit | P2 | – | `lets the student remove the chosen image` | lets the student remove the chosen image | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1188 | Unit | P2 | – | `needs a payment id before uploading` | needs a payment id before uploading | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1189 | Unit | P2 | – | `needs an image before uploading` | needs an image before uploading | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1190 | Unit | P2 | – | `shows an upload error, e.g. after a page refresh lost the pending payment` | shows an upload error, e.g. after a page refresh lost the pending payment | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1191 | Unit | P2 | – | `shows placeholder bank details until the list loads, and does not refetch a loaded list` | shows placeholder bank details until the list loads, and does not refetch a loaded list | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1192 | Unit | P2 | – | `goes back on cancel` | goes back on cancel | `edura-frontend/src/app/__tests__/payment-pages.test.tsx` | |
| TC-1193 | Unit | P2 | Profile page | `sends visitors to log in, back to the profile` | sends visitors to log in, back to the profile | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1194 | Unit | P2 | – | `shows a loader until auth is initialised` | shows a loader until auth is initialised | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1195 | Unit | P2 | – | `refreshes the user, enrollments and streams on load` | refreshes the user, enrollments and streams on load | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1196 | Unit | P2 | – | `shows the profile read-only with initials and subjects` | shows the profile read-only with initials and subjects | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1197 | Unit | P2 | – | `lists up to three enrolled courses and the exam count` | lists up to three enrolled courses and the exam count | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1198 | Unit | P2 | – | `saves edits, then reloads the user and their courses` | saves edits, then reloads the user and their courses | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1199 | Unit | P2 | – | `unticks a subject` | unticks a subject | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1200 | Unit | P2 | – | `shows the server error when saving fails` | shows the server error when saving fails | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1201 | Unit | P2 | – | `cancel throws away unsaved edits` | cancel throws away unsaved edits | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1202 | Unit | P2 | – | `warns about a missing NIC and opens the editor from the warning` | warns about a missing NIC and opens the editor from the warning | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1203 | Unit | P2 | – | `shows the stream name and loads subjects for it` | shows the stream name and loads subjects for it | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1204 | Unit | P2 | – | `rejects a badly formatted NIC without calling the API` | rejects a badly formatted NIC without calling the API | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1205 | Unit | P2 | – | `accepts NIC %s` | accepts NIC %s | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1206 | Unit | P2 | – | `offers only active streams and asks for one before listing subjects` | offers only active streams and asks for one before listing subjects | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1207 | Unit | P2 | photo upload | `uploads the chosen file and reloads the user` | uploads the chosen file and reloads the user | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1208 | Unit | P2 | – | `reports a failed upload` | reports a failed upload | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1209 | Unit | P2 | – | `shows the photo instead of initials when there is one` | shows the photo instead of initials when there is one | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1210 | Unit | P2 | – | `links password users to the reset flow` | links password users to the reset flow | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1211 | Unit | P2 | – | `hides the section until has_password is known` | hides the section until has_password is known | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1212 | Unit | P2 | – | `lets Google users set a password` | lets Google users set a password | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1213 | Unit | P2 | – | `checks the passwords match` | checks the passwords match | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1214 | Unit | P2 | – | `shows the server error when setting fails` | shows the server error when setting fails | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1215 | Unit | P2 | – | `loads the badge dashboard and shows earned, locked and percentage` | loads the badge dashboard and shows earned, locked and percentage | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1216 | Unit | P2 | – | `skips categories with no badges` | skips categories with no badges | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1217 | Unit | P2 | – | `shows a loader on first load` | shows a loader on first load | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1218 | Unit | P2 | – | `shows 0% when there are no badges at all` | shows 0% when there are no badges at all | `edura-frontend/src/app/__tests__/profile-pages.test.tsx` | |
| TC-1219 | Unit | P2 | – | `registers a student with their profile and asks them to verify` | registers a student with their profile and asks them to verify | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1220 | Unit | P2 | – | `keeps the button disabled until every rule passes` | keeps the button disabled until every rule passes | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1221 | Unit | P2 | – | `needs an A/L stream and a valid NIC from grade 12` | needs an A/L stream and a valid NIC from grade 12 | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1222 | Unit | P2 | – | `prefills a referral code from the link, upper-cased` | prefills a referral code from the link, upper-cased | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1223 | Unit | P2 | – | `shows a registration error and stays on the form` | shows a registration error and stays on the form | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1224 | Unit | P2 | – | `lets the student resend the verification email after the wait` | lets the student resend the verification email after the wait | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1225 | Unit | P2 | – | `toggles both password fields` | toggles both password fields | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1226 | Unit | P2 | – | `logs a failed Google sign-up` | logs a failed Google sign-up | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1227 | Unit | P2 | – | `logs a failed subject lookup` | logs a failed subject lookup | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1228 | Unit | P2 | – | `shows field hints after leaving invalid fields` | shows field hints after leaving invalid fields | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1229 | Unit | P2 | – | `sends visitors to log in first, keeping the page as the callback` | sends visitors to log in first, keeping the page as the callback | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1230 | Unit | P2 | – | `creates the profile for a new account` | creates the profile for a new account | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1231 | Unit | P2 | – | `fills in a Google-seeded profile without asking for the name again` | fills in a Google-seeded profile without asking for the name again | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1232 | Unit | P2 | – | `names an existing profile that has no name yet` | names an existing profile that has no name yet | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1233 | Unit | P2 | – | `updates instead when the profile appeared meanwhile` | updates instead when the profile appeared meanwhile | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1234 | Unit | P2 | – | `shows other save errors` | shows other save errors | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1235 | Unit | P2 | – | `asks A/L students for a stream and NIC` | asks A/L students for a stream and NIC | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1236 | Unit | P2 | – | `tolerates the stream and subject lookups failing` | tolerates the stream and subject lookups failing | `edura-frontend/src/app/__tests__/signup-pages.test.tsx` | |
| TC-1237 | Unit | P2 | CourseList | `shows only exam courses on the exam page` | shows only exam courses on the exam page | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1238 | Unit | P2 | – | `shows only video courses on the video page` | shows only video courses on the video page | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1239 | Unit | P2 | – | `renders a card with price, grade, streams and enrolment state` | renders a card with price, grade, streams and enrolment state | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1240 | Unit | P2 | – | `searches by title and clears the search` | searches by title and clears the search | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1241 | Unit | P2 | – | `filters by price and counts active filters` | filters by price and counts active filters | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1242 | Unit | P2 | – | `clear all resets filters and sorting` | clear all resets filters and sorting | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1243 | Unit | P2 | – | `shows an empty state whose button clears filters` | shows an empty state whose button clears filters | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1244 | Unit | P2 | – | `uses the mobile drawer for filters` | uses the mobile drawer for filters | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1245 | Unit | P2 | – | `closes the mobile drawer from its close button and its backdrop` | closes the mobile drawer from its close button and its backdrop | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1246 | Unit | P2 | – | `clears the search from the x inside the box` | clears the search from the x inside the box | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1247 | Unit | P2 | – | `filters by subject when courses carry one, and finds them by subject in search` | filters by subject when courses carry one, and finds them by subject in search | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1248 | Unit | P2 | – | `shows skeletons while loading and the error when loading fails` | shows skeletons while loading and the error when loading fails | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1249 | Unit | P2 | – | `renders nothing while the profile still needs completing` | renders nothing while the profile still needs completing | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1250 | Unit | P2 | – | `keeps working when profile completion finishes while mounted` | keeps working when profile completion finishes while mounted | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1251 | Unit | P2 | class packages | `does not look up packages for visitors` | does not look up packages for visitors | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1252 | Unit | P2 | – | `shows active and purchasable packages` | shows active and purchasable packages | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1253 | Unit | P2 | – | `enrols in a free package and refreshes the list` | enrols in a free package and refreshes the list | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1254 | Unit | P2 | – | `shows and dismisses an enrolment error` | shows and dismisses an enrolment error | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1255 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1256 | Unit | P2 | – | `shows the loader while enrollments load` | shows the loader while enrollments load | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1257 | Unit | P2 | – | `lists enrolled courses with type, progress and a classroom link` | lists enrolled courses with type, progress and a classroom link | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1258 | Unit | P2 | – | `filters by course type` | filters by course type | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1259 | Unit | P2 | – | `shows expiry badges` | shows expiry badges | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1260 | Unit | P2 | – | `shows an empty state` | shows an empty state | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1261 | Unit | P2 | – | `renders nothing while the profile still needs completing` | renders nothing while the profile still needs completing | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1262 | Unit | P2 | Class packages page | `fetches the user when auth is not initialised and renders nothing yet` | fetches the user when auth is not initialised and renders nothing yet | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1263 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1264 | Unit | P2 | – | `lists packages with level badges, descriptions and actions` | lists packages with level badges, descriptions and actions | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1265 | Unit | P2 | – | `enrols in a free package and refreshes` | enrols in a free package and refreshes | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1266 | Unit | P2 | – | `shows and dismisses errors` | shows and dismisses errors | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1267 | Unit | P2 | – | `shows a load error and an empty state` | shows a load error and an empty state | `edura-frontend/src/app/__tests__/student-catalog-pages.test.tsx` | |
| TC-1268 | Unit | P2 | – | `loads the course and shows a spinner meanwhile` | loads the course and shows a spinner meanwhile | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1269 | Unit | P2 | – | `shows the load error` | shows the load error | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1270 | Unit | P2 | – | `shows the header, price and locked lessons for visitors` | shows the header, price and locked lessons for visitors | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1271 | Unit | P2 | – | `goes back to the course list` | goes back to the course list | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1272 | Unit | P2 | – | `sends visitors to log in before buying` | sends visitors to log in before buying | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1273 | Unit | P2 | – | `takes signed-in students to payment` | takes signed-in students to payment | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1274 | Unit | P2 | – | `enrols in a free exam course and reloads it` | enrols in a free exam course and reloads it | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1275 | Unit | P2 | – | `enrols in a free video course with the video endpoint` | enrols in a free video course with the video endpoint | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1276 | Unit | P2 | – | `sends visitors to log in before a free enrolment` | sends visitors to log in before a free enrolment | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1277 | Unit | P2 | – | `shows overall progress and the exam actions` | shows overall progress and the exam actions | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1278 | Unit | P2 | – | `shows the end date when access lasts a while` | shows the end date when access lasts a while | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1279 | Unit | P2 | – | `marks future exams as scheduled` | marks future exams as scheduled | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1280 | Unit | P2 | – | `explains why an exam is locked` | explains why an exam is locked | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1281 | Unit | P2 | – | `shows a live countdown for an exam already in progress` | shows a live countdown for an exam already in progress | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1282 | Unit | P2 | video course | `locks lessons until enrolled, except ones bought on their own` | locks lessons until enrolled, except ones bought on their own | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1283 | Unit | P2 | – | `lets enrolled students continue the class` | lets enrolled students continue the class | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1284 | Unit | P2 | – | `says when there are no lessons yet` | says when there are no lessons yet | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1285 | Unit | P2 | – | `says when an exam course has no content yet` | says when an exam course has no content yet | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1286 | Unit | P2 | – | `renders nothing while the profile still needs completing` | renders nothing while the profile still needs completing | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1287 | Unit | P2 | – | `keeps working when profile completion finishes while mounted` | keeps working when profile completion finishes while mounted | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1288 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1289 | Unit | P2 | – | `fetches the user when signed in without one` | fetches the user when signed in without one | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1290 | Unit | P2 | – | `shows the course, progress and the first lesson of the first module` | shows the course, progress and the first lesson of the first module | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1291 | Unit | P2 | – | `starts the YouTube player for the current lesson` | starts the YouTube player for the current lesson | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1292 | Unit | P2 | – | `loads the YouTube script when the API is missing and starts once it is ready` | loads the YouTube script when the API is missing and starts once it is ready | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1293 | Unit | P2 | – | `switches lessons from the curriculum` | switches lessons from the curriculum | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1294 | Unit | P2 | – | `reuses a live player when switching lessons` | reuses a live player when switching lessons | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1295 | Unit | P2 | – | `lists the lesson's own and shared materials` | lists the lesson's own and shared materials | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1296 | Unit | P2 | – | `shows placeholder text and no materials for a bare lesson` | shows placeholder text and no materials for a bare lesson | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1297 | Unit | P2 | – | `collapses and expands modules` | collapses and expands modules | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1298 | Unit | P2 | – | `formats durations in the sidebar and header` | formats durations in the sidebar and header | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1299 | Unit | P2 | player controls | `plays, pauses and shows buffering from player events` | plays, pauses and shows buffering from player events | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1300 | Unit | P2 | – | `ignores play before the player exists` | ignores play before the player exists | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1301 | Unit | P2 | – | `rewinds ten seconds, not below zero` | rewinds ten seconds, not below zero | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1302 | Unit | P2 | – | `seeks and changes volume with the sliders` | seeks and changes volume with the sliders | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1303 | Unit | P2 | – | `shows the time under the cursor on the seek bar` | shows the time under the cursor on the seek bar | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1304 | Unit | P2 | – | `changes the playback speed` | changes the playback speed | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1305 | Unit | P2 | – | `toggles theater mode, hiding the curriculum` | toggles theater mode, hiding the curriculum | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1306 | Unit | P2 | – | `toggles fullscreen with inline styles` | toggles fullscreen with inline styles | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1307 | Unit | P2 | – | `hides the controls while playing after the mouse stops` | hides the controls while playing after the mouse stops | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1308 | Unit | P2 | completion | `marks a lesson complete with the course lesson count` | marks a lesson complete with the course lesson count | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1309 | Unit | P2 | – | `does not re-send completed lessons` | does not re-send completed lessons | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1310 | Unit | P2 | – | `keeps the lesson incomplete when saving fails` | keeps the lesson incomplete when saving fails | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1311 | Unit | P2 | – | `pauses at the earliest missed checkpoint and resumes after a correct answer` | pauses at the earliest missed checkpoint and resumes after a correct answer | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1312 | Unit | P2 | – | `clamps the clock to the lesson length` | clamps the clock to the lesson length | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1313 | Unit | P2 | – | `uses the live duration when the lesson has none` | uses the live duration when the lesson has none | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1314 | Unit | P2 | – | `renders nothing while the profile still needs completing` | renders nothing while the profile still needs completing | `edura-frontend/src/app/__tests__/student-course-pages.test.tsx` | |
| TC-1315 | Unit | P2 | Before the exam | `sends visitors to log in, back to the exam` | sends visitors to log in, back to the exam | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1316 | Unit | P2 | – | `checks access and shows the start modal with the exam details` | checks access and shows the start modal with the exam details | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1317 | Unit | P2 | – | `uses cached course data for the modal` | uses cached course data for the modal | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1318 | Unit | P2 | – | `blocks a locked exam from the cache without asking the server` | blocks a locked exam from the cache without asking the server | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1319 | Unit | P2 | – | `blocks an exam the server says is locked` | blocks an exam the server says is locked | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1320 | Unit | P2 | – | `still offers the exam when the access check fails` | still offers the exam when the access check fails | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1321 | Unit | P2 | – | `"later" goes back` | "later" goes back | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1322 | Unit | P2 | – | `resumes an attempt saved in this browser without the modal` | resumes an attempt saved in this browser without the modal | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1323 | Unit | P2 | – | `shows when a scheduled exam opens` | shows when a scheduled exam opens | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1324 | Unit | P2 | – | `blocks when starting hits a progression lock` | blocks when starting hits a progression lock | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1325 | Unit | P2 | – | `shows the last result when the exam was already attempted` | shows the last result when the exam was already attempted | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1326 | Unit | P2 | – | `returns to the modal after a general start failure` | returns to the modal after a general start failure | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1327 | Unit | P2 | – | `shows the last attempt, reading options from the review` | shows the last attempt, reading options from the review | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1328 | Unit | P2 | – | `falls back to the start modal when there is no previous attempt` | falls back to the start modal when there is no previous attempt | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1329 | Unit | P2 | During the exam | `shows questions, the timer, the watermark and saves the attempt locally` | shows questions, the timer, the watermark and saves the attempt locally | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1330 | Unit | P2 | – | `tracks answers and the unanswered count` | tracks answers and the unanswered count | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1331 | Unit | P2 | – | `shows hours for long exams` | shows hours for long exams | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1332 | Unit | P2 | submitting | `warns about unanswered questions and lets the student go back` | warns about unanswered questions and lets the student go back | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1333 | Unit | P2 | – | `sends every question, clears local state and shows the results` | sends every question, clears local state and shows the results | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1334 | Unit | P2 | – | `shows the result screen with the review` | shows the result screen with the review | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1335 | Unit | P2 | – | `links back to the dashboard and the course` | links back to the dashboard and the course | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1336 | Unit | P2 | – | `falls back to the course list when the result has no course` | falls back to the course list when the result has no course | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1337 | Unit | P2 | – | `auto-submits when time runs out` | auto-submits when time runs out | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1338 | Unit | P2 | – | `warns when the auto-submit fails, and clears the saved attempt` | warns when the auto-submit fails, and clears the saved attempt | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1339 | Unit | P2 | – | `wipes answers, reports and warns when the student leaves the tab` | wipes answers, reports and warns when the student leaves the tab | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1340 | Unit | P2 | – | `a click dismisses the violation overlay` | a click dismisses the violation overlay | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1341 | Unit | P2 | – | `does not penalise mobile devices for the screen turning off` | does not penalise mobile devices for the screen turning off | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1342 | Unit | P2 | – | `ignores ordinary keys and blocks the context menu` | ignores ordinary keys and blocks the context menu | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1343 | Unit | P2 | – | `stops watching once the paper is submitted` | stops watching once the paper is submitted | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1344 | Unit | P2 | Results PDF | `captures the summary and each review item into the PDF` | captures the summary and each review item into the PDF | `edura-frontend/src/app/__tests__/student-exam-page.test.tsx` | |
| TC-1345 | Unit | P2 | – | `sends visitors to log in` | sends visitors to log in | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1346 | Unit | P2 | – | `loads attempts and progress, showing a spinner meanwhile` | loads attempts and progress, showing a spinner meanwhile | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1347 | Unit | P2 | – | `shows the analytics summary and subject cards` | shows the analytics summary and subject cards | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1348 | Unit | P2 | – | `drills into a subject and back out` | drills into a subject and back out | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1349 | Unit | P2 | – | `groups raw attempts by exam and opens a review` | groups raw attempts by exam and opens a review | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1350 | Unit | P2 | – | `shows an empty raw-data tab` | shows an empty raw-data tab | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1351 | Unit | P2 | – | `loads the review for the attempt in the url` | loads the review for the attempt in the url | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1352 | Unit | P2 | – | `shows the title, score and pass badge` | shows the title, score and pass badge | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1353 | Unit | P2 | – | `marks a score under 85% as not passed` | marks a score under 85% as not passed | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1354 | Unit | P2 | – | `navigates back and to the results list` | navigates back and to the results list | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1355 | Unit | P2 | – | `shows the error with a way back` | shows the error with a way back | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1356 | Unit | P2 | – | `does nothing without an attempt id` | does nothing without an attempt id | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1357 | Unit | P2 | – | `captures each section into a paged A4 PDF` | captures each section into a paged A4 PDF | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1358 | Unit | P2 | – | `shortens long titles in the PDF header` | shortens long titles in the PDF header | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1359 | Unit | P2 | – | `shows an empty state when no exam has rankings` | shows an empty state when no exam has rankings | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1360 | Unit | P2 | – | `asks for an exam, grouping exams by subject and course` | asks for an exam, grouping exams by subject and course | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1361 | Unit | P2 | – | `loads the podium, the table and my rank for the chosen exam` | loads the podium, the table and my rank for the chosen exam | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1362 | Unit | P2 | – | `marks the current user on the podium` | marks the current user on the podium | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1363 | Unit | P2 | – | `shows times under a minute in seconds only` | shows times under a minute in seconds only | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1364 | Unit | P2 | – | `refetches for a district and clears filters` | refetches for a district and clears filters | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1365 | Unit | P2 | – | `shows placeholder rows while the board updates` | shows placeholder rows while the board updates | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1366 | Unit | P2 | – | `renders nothing while the profile still needs completing` | renders nothing while the profile still needs completing | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1367 | Unit | P2 | – | `keeps working when profile completion finishes while mounted` | keeps working when profile completion finishes while mounted | `edura-frontend/src/app/__tests__/student-results-pages.test.tsx` | |
| TC-1368 | Unit | P2 | StatusModal | `renders a %s message` | renders a %s message | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1369 | Unit | P2 | – | `defaults to an info dialog with a Close button` | defaults to an info dialog with a Close button | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1370 | Unit | P2 | – | `renders nothing without notifications` | renders nothing without notifications | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1371 | Unit | P2 | – | `auto-hides timed notifications and lets the user dismiss others` | auto-hides timed notifications and lets the user dismiss others | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1372 | Unit | P2 | – | `submits the chosen category and thanks the user` | submits the chosen category and thanks the user | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1373 | Unit | P2 | – | `prefills the signed-in user's address` | prefills the signed-in user's address | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1374 | Unit | P2 | – | `disables the button while sending` | disables the button while sending | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1375 | Unit | P2 | – | `shows the server error` | shows the server error | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1376 | Unit | P2 | – | `is hidden on admin pages` | is hidden on admin pages | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1377 | Unit | P2 | – | `creates a guest session id when there is none` | creates a guest session id when there is none | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1378 | Unit | P2 | – | `opens, loads history, polls, and sends as a guest` | opens, loads history, polls, and sends as a guest | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1379 | Unit | P2 | – | `sends as the signed-in user without a guest session` | sends as the signed-in user without a guest session | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1380 | Unit | P2 | – | `shows conversation bubbles and badges unread admin replies while closed` | shows conversation bubbles and badges unread admin replies while closed | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1381 | Unit | P2 | – | `caps the unread badge at 9+` | caps the unread badge at 9+ | `edura-frontend/src/components/__tests__/feedback-chat-notify.test.tsx` | |
| TC-1382 | Unit | P2 | Footer | `is hidden on %s` | is hidden on %s | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1383 | Unit | P2 | – | `links to the main areas elsewhere` | links to the main areas elsewhere | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1384 | Unit | P2 | Navbar | `is hidden on %s` | is hidden on %s | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1385 | Unit | P2 | – | `shows the admin console on admin pages` | shows the admin console on admin pages | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1386 | Unit | P2 | – | `offers sign in to visitors and highlights the current page` | offers sign in to visitors and highlights the current page | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1387 | Unit | P2 | – | `hides navigation until the profile is completed` | hides navigation until the profile is completed | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1388 | Unit | P2 | – | `opens and closes the mobile menu, closing it on navigation` | opens and closes the mobile menu, closing it on navigation | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1389 | Unit | P2 | – | `shows the portal in the mobile menu for signed-in users` | shows the portal in the mobile menu for signed-in users | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1390 | Unit | P2 | AdminNavbar | `lists the admin areas and marks the current one` | lists the admin areas and marks the current one | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1391 | Unit | P2 | – | `hides admin management from non-admins` | hides admin management from non-admins | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1392 | Unit | P2 | – | `has a mobile menu with settings` | has a mobile menu with settings | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1393 | Unit | P2 | Providers | `gives children the app store` | gives children the app store | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1394 | Unit | P2 | – | `shows initials, name, grade and wallet credits for a student` | shows initials, name, grade and wallet credits for a student | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1395 | Unit | P2 | – | `shows admin links and no wallet for admins` | shows admin links and no wallet for admins | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1396 | Unit | P2 | – | `shows a plain dashboard link for teachers` | shows a plain dashboard link for teachers | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1397 | Unit | P2 | – | `falls back to the email name` | falls back to the email name | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1398 | Unit | P2 | – | `closes when clicking outside` | closes when clicking outside | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1399 | Unit | P2 | – | `logs out locally even if the server call fails` | logs out locally even if the server call fails | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1400 | Unit | P2 | – | `shows a photo stored as profile_photo_url, and initials if it fails to load` | shows a photo stored as profile_photo_url, and initials if it fails to load | `edura-frontend/src/components/__tests__/layout.test.tsx` | |
| TC-1401 | Unit | P2 | GoogleAuthProvider | `wraps the app with the configured client id` | wraps the app with the configured client id | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1402 | Unit | P2 | – | `asks each question and resumes the video when all are right` | asks each question and resumes the video when all are right | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1403 | Unit | P2 | – | `lets the student try again after a wrong answer` | lets the student try again after a wrong answer | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1404 | Unit | P2 | – | `falls back to the icon and shows the unlock date when earned` | falls back to the icon and shows the unlock date when earned | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1405 | Unit | P2 | – | `greys out a badge not yet earned` | greys out a badge not yet earned | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1406 | Unit | P2 | – | `shows nothing without new badges` | shows nothing without new badges | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1407 | Unit | P2 | – | `celebrates each new badge in turn, then clears them` | celebrates each new badge in turn, then clears them | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1408 | Unit | P2 | – | `ActivityFeed greets the student and lists attempts` | ActivityFeed greets the student and lists attempts | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1409 | Unit | P2 | – | `ActivityFeed shows loading and empty states` | ActivityFeed shows loading and empty states | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1410 | Unit | P2 | – | `AchievementPanel shows up to four badges and the wallet` | AchievementPanel shows up to four badges and the wallet | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1411 | Unit | P2 | – | `AchievementPanel falls back to an icon for badges without artwork` | AchievementPanel falls back to an icon for badges without artwork | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1412 | Unit | P2 | – | `AchievementPanel shows loading and empty states` | AchievementPanel shows loading and empty states | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1413 | Unit | P2 | – | `shows the profile, links and enrolled courses` | shows the profile, links and enrolled courses | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1414 | Unit | P2 | – | `says when there are no courses and shows a stored photo` | says when there are no courses and shows a stored photo | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1415 | Unit | P2 | – | `uploads a new photo and reloads the user` | uploads a new photo and reloads the user | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1416 | Unit | P2 | – | `does not reload the user when the upload fails, or when no file is chosen` | does not reload the user when the upload fails, or when no file is chosen | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1417 | Unit | P2 | – | `PerformanceLineChart has a default colour` | PerformanceLineChart has a default colour | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1418 | Unit | P2 | – | `summarises the attempt and marks right and wrong answers` | summarises the attempt and marks right and wrong answers | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1419 | Unit | P2 | – | `prints the video link instead of embedding it when capturing a PDF` | prints the video link instead of embedding it when capturing a PDF | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1420 | Unit | P2 | – | `renders nothing when closed` | renders nothing when closed | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1421 | Unit | P2 | – | `searches after two characters, debounced, and selects a student` | searches after two characters, debounced, and selects a student | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1422 | Unit | P2 | – | `says when nothing matches and survives a failed search` | says when nothing matches and survives a failed search | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1423 | Unit | P2 | – | `shows progress while a chat is being opened` | shows progress while a chat is being opened | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1424 | Unit | P2 | – | `searches eligible students by name, school or district` | searches eligible students by name, school or district | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1425 | Unit | P2 | – | `exam access shows the backend's limitation as an error` | exam access shows the backend's limitation as an error | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1426 | Unit | P2 | – | `shows a loading state while the lists load` | shows a loading state while the lists load | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1427 | Unit | P2 | – | `shows a load error and closes` | shows a load error and closes | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1428 | Unit | P2 | – | `marks a visitor as initialized without calling the server` | marks a visitor as initialized without calling the server | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1429 | Unit | P2 | – | `restores a fresh session straight away and loads the user` | restores a fresh session straight away and loads the user | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1430 | Unit | P2 | – | `refreshes a token that is about to expire, keeping it where it was` | refreshes a token that is about to expire, keeping it where it was | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1431 | Unit | P2 | – | `treats a token without an expiry as valid` | treats a token without an expiry as valid | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1432 | Unit | P2 | – | `moves a guest chat onto the account` | moves a guest chat onto the account | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1433 | Unit | P2 | – | `keeps going when the chat sync fails` | keeps going when the chat sync fails | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1434 | Unit | P2 | – | `uses the loaded user's flag too, and leaves complete profiles alone` | uses the loaded user's flag too, and leaves complete profiles alone | `edura-frontend/src/components/__tests__/widgets.test.tsx` | |
| TC-1435 | Unit | P2 | getErrorMessage | `returns a string error as is` | returns a string error as is | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1436 | Unit | P2 | – | `reads the message of a local Error or a raw {error, message} object` | reads the message of a local Error or a raw {error, message} object | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1437 | Unit | P2 | – | `prefers the Edura detail.message, then detail.msg, then a plain detail` | prefers the Edura detail.message, then detail.msg, then a plain detail | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1438 | Unit | P2 | – | `joins Pydantic validation errors` | joins Pydantic validation errors | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1439 | Unit | P2 | – | `falls back to the axios message, then a generic one` | falls back to the axios message, then a generic one | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1440 | Unit | P2 | getInitials | `uses up to two initials of the name` | uses up to two initials of the name | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1441 | Unit | P2 | – | `falls back to the email, then "U"` | falls back to the email, then "U" | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1442 | Unit | P2 | – | `saves and reads back an attempt that is still running` | saves and reads back an attempt that is still running | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1443 | Unit | P2 | – | `drops an attempt whose time is up` | drops an attempt whose time is up | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1444 | Unit | P2 | – | `ignores corrupted entries` | ignores corrupted entries | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1445 | Unit | P2 | – | `lists only running attempts and ignores other keys` | lists only running attempts and ignores other keys | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1446 | Unit | P2 | – | `clears an attempt on submit` | clears an attempt on submit | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1447 | Unit | P2 | – | `counts seconds remaining, never below zero` | counts seconds remaining, never below zero | `edura-frontend/src/lib/__tests__/utils.test.ts` | |
| TC-1448 | Unit | P2 | – | `maps a student attempt review` | maps a student attempt review | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1449 | Unit | P2 | – | `maps student profiles and turns skip/limit into a page` | maps student profiles and turns skip/limit into a page | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1450 | Unit | P2 | – | `defaults missing profile fields` | defaults missing profile fields | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1451 | Unit | P2 | – | `filters by district, grade and status on the current page` | filters by district, grade and status on the current page | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1452 | Unit | P2 | – | `flips the active flag` | flips the active flag | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1453 | Unit | P2 | – | `deletes the profile and the login, tolerating a missing login` | deletes the profile and the login, tolerating a missing login | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1454 | Unit | P2 | – | `stops if the profile cannot be deleted` | stops if the profile cannot be deleted | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1455 | Unit | P2 | rankings | `lists nothing until an exam is chosen` | lists nothing until an exam is chosen | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1456 | Unit | P2 | – | `maps the course leaderboard of the chosen exam` | maps the course leaderboard of the chosen exam | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1457 | Unit | P2 | – | `lists all streams, including inactive ones` | lists all streams, including inactive ones | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1458 | Unit | P2 | – | `creates, updates and deletes streams` | creates, updates and deletes streams | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1459 | Unit | P2 | – | `manages grade subjects` | manages grade subjects | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1460 | Unit | P2 | – | `pages through every course` | pages through every course | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1461 | Unit | P2 | – | `stops after a short page` | stops after a short page | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1462 | Unit | P2 | – | `creates a course with course_service field names` | creates a course with course_service field names | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1463 | Unit | P2 | – | `updates a course, sending stream ids as numbers` | updates a course, sending stream ids as numbers | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1464 | Unit | P2 | – | `deletes a course` | deletes a course | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1465 | Unit | P2 | – | `lists, creates, updates and deletes modules` | lists, creates, updates and deletes modules | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1466 | Unit | P2 | – | `clears a lesson's exams before deleting the lesson` | clears a lesson's exams before deleting the lesson | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1467 | Unit | P2 | – | `lists exams only for a course` | lists exams only for a course | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1468 | Unit | P2 | – | `creates an exam, converting a local schedule to ISO` | creates an exam, converting a local schedule to ISO | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1469 | Unit | P2 | – | `creates an exam outside any lesson with no schedule` | creates an exam outside any lesson with no schedule | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1470 | Unit | P2 | – | `updates only the fields given` | updates only the fields given | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1471 | Unit | P2 | – | `deletes an exam and uploads question images` | deletes an exam and uploads question images | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1472 | Unit | P2 | – | `maps questions and marks the correct option` | maps questions and marks the correct option | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1473 | Unit | P2 | – | `creates an MCQ with option inputs` | creates an MCQ with option inputs | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1474 | Unit | P2 | – | `updates and deletes a question` | updates and deletes a question | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1475 | Unit | P2 | – | `imports questions from CSV and bulk-imports exams` | imports questions from CSV and bulk-imports exams | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1476 | Unit | P2 | uploads | `uploads an image and returns it under every field name callers use` | uploads an image and returns it under every field name callers use | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1477 | Unit | P2 | – | `uploads a material file` | uploads a material file | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1478 | Unit | P2 | – | `deletes an asset by public id` | deletes an asset by public id | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1479 | Unit | P2 | – | `maps videos and sends course_service field names` | maps videos and sends course_service field names | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1480 | Unit | P2 | – | `maps materials and pins or unpins them to a video` | maps materials and pins or unpins them to a video | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1481 | Unit | P2 | – | `manages in-video checkpoints` | manages in-video checkpoints | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1482 | Unit | P2 | – | `exam-level access lists are empty` | exam-level access lists are empty | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1483 | Unit | P2 | – | `grants and revokes with numeric ids` | grants and revokes with numeric ids | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1484 | Unit | P2 | admin accounts | `lists admins` | lists admins | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1485 | Unit | P2 | – | `splits the full name when creating an admin` | splits the full name when creating an admin | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1486 | Unit | P2 | – | `deletes an admin everywhere` | deletes an admin everywhere | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1487 | Unit | P2 | class packages | `drops empty filters` | drops empty filters | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1488 | Unit | P2 | – | `sends the stream as a number, null to clear, or omits it` | sends the stream as a number, null to clear, or omits it | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1489 | Unit | P2 | – | `lists, grants and revokes package holders` | lists, grants and revokes package holders | `edura-frontend/src/lib/api/__tests__/admin.test.ts` | |
| TC-1490 | Unit | P2 | login / register / google | `logs in with only email and password; the refresh token stays a cookie` | logs in with only email and password; the refresh token stays a cookie | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1491 | Unit | P2 | – | `registers as a student by default and sends the sign-up profile` | registers as a student by default and sends the sign-up profile | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1492 | Unit | P2 | – | `keeps an explicit role` | keeps an explicit role | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1493 | Unit | P2 | – | `exchanges a Google access token` | exchanges a Google access token | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1494 | Unit | P2 | – | `logs out with credentials so the refresh cookie is revoked` | logs out with credentials so the refresh cookie is revoked | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1495 | Unit | P2 | getCurrentUser | `needs a stored token` | needs a stored token | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1496 | Unit | P2 | – | `combines the token, the profile and /me` | combines the token, the profile and /me | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1497 | Unit | P2 | – | `retries a missing profile while user_service builds it` | retries a missing profile while user_service builds it | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1498 | Unit | P2 | – | `gives up after five tries and asks for profile completion` | gives up after five tries and asks for profile completion | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1499 | Unit | P2 | – | `does not retry other profile errors and tolerates /me failing` | does not retry other profile errors and tolerates /me failing | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1500 | Unit | P2 | – | `never asks staff for academic details` | never asks staff for academic details | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1501 | Unit | P2 | profile | `reads /me` | reads /me | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1502 | Unit | P2 | – | `creates the profile for the signed-in account` | creates the profile for the signed-in account | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1503 | Unit | P2 | – | `updates the profile of the user in the token` | updates the profile of the user in the token | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1504 | Unit | P2 | – | `refuses to update without a session` | refuses to update without a session | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1505 | Unit | P2 | – | `uploads a photo then stores both its URL and public id` | uploads a photo then stores both its URL and public id | `edura-frontend/src/lib/api/__tests__/auth.test.ts` | |
| TC-1506 | Unit | P2 | chat api | `sends a message, with the guest session only when there is one` | sends a message, with the guest session only when there is one | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1507 | Unit | P2 | – | `loads history for a guest session or the signed-in user` | loads history for a guest session or the signed-in user | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1508 | Unit | P2 | – | `syncs a guest thread on login` | syncs a guest thread on login | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1509 | Unit | P2 | – | `maps admin conversations` | maps admin conversations | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1510 | Unit | P2 | – | `reads, replies to and deletes a conversation` | reads, replies to and deletes a conversation | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1511 | Unit | P2 | – | `opens the thread with a student` | opens the thread with a student | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1512 | Unit | P2 | – | `submits feedback and maps optional fields` | submits feedback and maps optional fields | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1513 | Unit | P2 | – | `lists feedback with paging` | lists feedback with paging | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1514 | Unit | P2 | – | `marks read and deletes` | marks read and deletes | `edura-frontend/src/lib/api/__tests__/chat-feedback.test.ts` | |
| TC-1515 | Unit | P2 | – | `sends JSON to the gateway` | sends JSON to the gateway | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1516 | Unit | P2 | – | `attaches the session token, preferring sessionStorage` | attaches the session token, preferring sessionStorage | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1517 | Unit | P2 | – | `refreshes once on 401 and replays the request with the new token` | refreshes once on 401 and replays the request with the new token | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1518 | Unit | P2 | – | `stores a refreshed token where the session lives` | stores a refreshed token where the session lives | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1519 | Unit | P2 | – | `shares one refresh between concurrent 401s` | shares one refresh between concurrent 401s | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1520 | Unit | P2 | – | `signs out and goes to /login when the refresh fails` | signs out and goes to /login when the refresh fails | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1521 | Unit | P2 | – | `never refreshes for anonymous visitors` | never refreshes for anonymous visitors | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1522 | Unit | P2 | – | `never refreshes for the auth route %s` | never refreshes for the auth route %s | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1523 | Unit | P2 | – | `passes other errors straight through` | passes other errors straight through | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1524 | Unit | P2 | – | `does not retry a request that already failed after a refresh` | does not retry a request that already failed after a refresh | `edura-frontend/src/lib/api/__tests__/client.test.ts` | |
| TC-1525 | Unit | P2 | initiatePayment | `only supports whole-course payments` | only supports whole-course payments | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1526 | Unit | P2 | – | `starts a PayHere checkout at the real course price` | starts a PayHere checkout at the real course price | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1527 | Unit | P2 | – | `treats a missing price as free and a live gateway as non-sandbox` | treats a missing price as free and a live gateway as non-sandbox | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1528 | Unit | P2 | – | `refuses a PayHere config for an unknown order` | refuses a PayHere config for an unknown order | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1529 | Unit | P2 | bank slips | `defers the upload until the slip file is chosen, then sends one form` | defers the upload until the slip file is chosen, then sends one form | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1530 | Unit | P2 | – | `lists pending slips mapped for the admin screen` | lists pending slips mapped for the admin screen | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1531 | Unit | P2 | – | `shows "approved" receipts as verified` | shows "approved" receipts as verified | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1532 | Unit | P2 | – | `lists every slip without a filter and narrows by course` | lists every slip without a filter and narrows by course | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1533 | Unit | P2 | – | `finds one slip or fails` | finds one slip or fails | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1534 | Unit | P2 | – | `verifies a slip` | verifies a slip | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1535 | Unit | P2 | – | `maps payments for the UI` | maps payments for the UI | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1536 | Unit | P2 | – | `finds a payment by id or PayHere order id` | finds a payment by id or PayHere order id | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1537 | Unit | P2 | – | `filters all payments by status and method` | filters all payments by status and method | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1538 | Unit | P2 | – | `derives stats from payments and receipts` | derives stats from payments and receipts | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1539 | Unit | P2 | – | `groups earnings by course from successful payments only` | groups earnings by course from successful payments only | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1540 | Unit | P2 | – | `creates, updates and deletes accounts` | creates, updates and deletes accounts | `edura-frontend/src/lib/api/__tests__/payment.test.ts` | |
| TC-1541 | Unit | P2 | catalogue | `maps published courses and passes the viewer grade and stream` | maps published courses and passes the viewer grade and stream | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1542 | Unit | P2 | – | `browses without filters and copes with an empty answer` | browses without filters and copes with an empty answer | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1543 | Unit | P2 | – | `shows an outline without attempts when the student has no access` | shows an outline without attempts when the student has no access | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1544 | Unit | P2 | – | `unlocks a single granted lesson and counts passed exams` | unlocks a single granted lesson and counts passed exams | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1545 | Unit | P2 | – | `treats staff as having full access without asking the server` | treats staff as having full access without asking the server | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1546 | Unit | P2 | – | `treats an access-check failure as no access` | treats an access-check failure as no access | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1547 | Unit | P2 | – | `shows anonymous visitors only the outline and video counts` | shows anonymous visitors only the outline and video counts | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1548 | Unit | P2 | – | `loads videos, materials, checkpoints and progress for enrolled students` | loads videos, materials, checkpoints and progress for enrolled students | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1549 | Unit | P2 | – | `still lists videos when no progress was recorded` | still lists videos when no progress was recorded | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1550 | Unit | P2 | – | `getVideoClassDetails is the overview` | getVideoClassDetails is the overview | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1551 | Unit | P2 | exam lists | `lists a course's exams with lesson-level access` | lists a course's exams with lesson-level access | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1552 | Unit | P2 | – | `lists a lesson's exams, looking up access for their course` | lists a lesson's exams, looking up access for their course | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1553 | Unit | P2 | – | `returns nothing for an empty lesson` | returns nothing for an empty lesson | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1554 | Unit | P2 | – | `enrolls in a free course through payment_service` | enrolls in a free course through payment_service | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1555 | Unit | P2 | – | `lists active whole-course enrollments whose course still exists` | lists active whole-course enrollments whose course still exists | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1556 | Unit | P2 | – | `returns no enrollments when signed out` | returns no enrollments when signed out | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1557 | Unit | P2 | – | `is open for an enrolled student` | is open for an enrolled student | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1558 | Unit | P2 | – | `locks it for students who are not enrolled` | locks it for students who are not enrolled | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1559 | Unit | P2 | – | `locks it until the scheduled start` | locks it until the scheduled start | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1560 | Unit | P2 | taking an exam | `starts an attempt, packing the session into the attempt id` | starts an attempt, packing the session into the attempt id | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1561 | Unit | P2 | – | `submits answers by option text and maps the result` | submits answers by option text and maps the result | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1562 | Unit | P2 | – | `reports violations without ever failing the exam` | reports violations without ever failing the exam | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1563 | Unit | P2 | – | `loads the last attempt, or null when there is none` | loads the last attempt, or null when there is none | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1564 | Unit | P2 | – | `maps an attempt review with defaults` | maps an attempt review with defaults | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1565 | Unit | P2 | results and rankings | `lists my attempts with string ids` | lists my attempts with string ids | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1566 | Unit | P2 | – | `passes leaderboard filters only when set` | passes leaderboard filters only when set | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1567 | Unit | P2 | profile reference data and referrals | `needs a grade to list subjects` | needs a grade to list subjects | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1568 | Unit | P2 | – | `maps streams` | maps streams | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1569 | Unit | P2 | – | `lists referral events and applies a trimmed code` | lists referral events and applies a trimmed code | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1570 | Unit | P2 | – | `records video progress with defaults` | records video progress with defaults | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1571 | Unit | P2 | class packages | `filters packages by the student's grade, and stream from grade 12` | filters packages by the student's grade, and stream from grade 12 | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1572 | Unit | P2 | – | `ignores the stream below grade 12` | ignores the stream below grade 12 | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1573 | Unit | P2 | – | `shows every package to visitors and to students without a profile` | shows every package to visitors and to students without a profile | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1574 | Unit | P2 | – | `enrolls in a free package` | enrolls in a free package | `edura-frontend/src/lib/api/__tests__/student.test.ts` | |
| TC-1575 | Unit | P2 | – | `loads public streams into the same list` | loads public streams into the same list | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1576 | Unit | P2 | – | `fetches students with their total` | fetches students with their total | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1577 | Unit | P2 | – | `updates the toggled student when the ids match as strings` | updates the toggled student when the ids match as strings | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1578 | Unit | P2 | – | `records a failed toggle` | records a failed toggle | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1579 | Unit | P2 | – | `removes a deleted student and lowers the total` | removes a deleted student and lowers the total | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1580 | Unit | P2 | – | `sends a progress report` | sends a progress report | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1581 | Unit | P2 | admin slice — streams and admins | `adds, edits and removes streams` | adds, edits and removes streams | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1582 | Unit | P2 | – | `lists, adds and removes admins` | lists, adds and removes admins | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1583 | Unit | P2 | – | `stores and clears the PayHere config` | stores and clears the PayHere config | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1584 | Unit | P2 | – | `lists slips and updates one after review` | lists slips and updates one after review | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1585 | Unit | P2 | – | `lists all slips by default` | lists all slips by default | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1586 | Unit | P2 | – | `loads bank accounts for students or admins` | loads bank accounts for students or admins | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1587 | Unit | P2 | – | `adds, edits and removes bank accounts` | adds, edits and removes bank accounts | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1588 | Unit | P2 | – | `loads earnings for a course` | loads earnings for a course | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1589 | Unit | P2 | – | `defaults enrollment paging and attempt limits` | defaults enrollment paging and attempt limits | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1590 | Unit | P2 | – | `fetches platform stats once` | fetches platform stats once | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1591 | Unit | P2 | – | `records a failed stats load` | records a failed stats load | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1592 | Unit | P2 | – | `fetches ranking exams once` | fetches ranking exams once | `edura-frontend/src/lib/redux/__tests__/admin-payment-dashboard.test.ts` | |
| TC-1593 | Unit | P2 | ui slice | `queues notifications with unique ids, even in the same millisecond` | queues notifications with unique ids, even in the same millisecond | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1594 | Unit | P2 | – | `tracks a global loading message` | tracks a global loading message | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1595 | Unit | P2 | – | `stays quiet for an exam that was already attempted` | stays quiet for an exam that was already attempted | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1596 | Unit | P2 | – | `ignores other successes` | ignores other successes | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1597 | Unit | P2 | auth slice — login | `keeps a remembered session in localStorage only` | keeps a remembered session in localStorage only | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1598 | Unit | P2 | – | `keeps an unremembered session in this tab only` | keeps an unremembered session in this tab only | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1599 | Unit | P2 | – | `remembers which address still needs verifying` | remembers which address still needs verifying | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1600 | Unit | P2 | – | `reports wrong credentials` | reports wrong credentials | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1601 | Unit | P2 | auth slice — session | `loads the current user and whether the profile needs completing` | loads the current user and whether the profile needs completing | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1602 | Unit | P2 | – | `marks the app initialized even when there is no session` | marks the app initialized even when there is no session | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1603 | Unit | P2 | – | `logs out everywhere` | logs out everywhere | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1604 | Unit | P2 | – | `sets credentials, persisting only when asked` | sets credentials, persisting only when asked | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1605 | Unit | P2 | – | `has small flags for startup and profile completion` | has small flags for startup and profile completion | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1606 | Unit | P2 | auth slice — Google sign-in | `stores the session in this tab and loads the user` | stores the session in this tab and loads the user | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1607 | Unit | P2 | – | `reports a rejected Google token` | reports a rejected Google token | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1608 | Unit | P2 | auth slice — profile and passwords | `creating the profile clears the completion step` | creating the profile clears the completion step | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1609 | Unit | P2 | – | `creating a profile without a loaded user only clears the flag` | creating a profile without a loaded user only clears the flag | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1610 | Unit | P2 | – | `updating without a loaded user changes nothing` | updating without a loaded user changes nothing | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1611 | Unit | P2 | – | `forgot-password sends the address it was given` | forgot-password sends the address it was given | `edura-frontend/src/lib/redux/__tests__/auth-ui.test.ts` | |
| TC-1612 | Unit | P2 | courses slice — admin | `fetches, creates, updates and deletes courses` | fetches, creates, updates and deletes courses | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1613 | Unit | P2 | – | `ignores an update for a course that is not listed` | ignores an update for a course that is not listed | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1614 | Unit | P2 | – | `keeps lessons in sync with their course` | keeps lessons in sync with their course | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1615 | Unit | P2 | – | `ignores lesson changes for courses that are not loaded` | ignores lesson changes for courses that are not loaded | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1616 | Unit | P2 | – | `uploads and deletes images` | uploads and deletes images | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1617 | Unit | P2 | courses slice — student | `fetches the catalogue for the signed-in student's grade and stream` | fetches the catalogue for the signed-in student's grade and stream | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1618 | Unit | P2 | – | `browses without a grade when signed out` | browses without a grade when signed out | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1619 | Unit | P2 | – | `loads a course overview, clearing the previous one first` | loads a course overview, clearing the previous one first | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1620 | Unit | P2 | – | `reports a failed free video enrollment` | reports a failed free video enrollment | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1621 | Unit | P2 | – | `marks an exam attempted after submitting` | marks an exam attempted after submitting | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1622 | Unit | P2 | exams slice — admin | `fetches, creates, updates and deletes exams` | fetches, creates, updates and deletes exams | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1623 | Unit | P2 | – | `starts an attempt` | starts an attempt | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1624 | Unit | P2 | – | `announces new badges when a submit earns them` | announces new badges when a submit earns them | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1625 | Unit | P2 | – | `reports a failed submit` | reports a failed submit | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1626 | Unit | P2 | – | `loads the last attempt and the access check` | loads the last attempt and the access check | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1627 | Unit | P2 | – | `loads, adds, edits and removes questions` | loads, adds, edits and removes questions | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1628 | Unit | P2 | – | `imports a CSV without touching the list` | imports a CSV without touching the list | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1629 | Unit | P2 | video classes slice | `loads a video class` | loads a video class | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1630 | Unit | P2 | – | `creates a module and tracks admin errors` | creates a module and tracks admin errors | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1631 | Unit | P2 | – | `updateProgress marks a video watched when the payload names it` | updateProgress marks a video watched when the payload names it | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1632 | Unit | P2 | – | `createVideoAction surfaces the API error` | createVideoAction surfaces the API error | `edura-frontend/src/lib/redux/__tests__/content-slices.test.ts` | |
| TC-1633 | Unit | P2 | chat slice — student side | `remembers the guest session id in the browser` | remembers the guest session id in the browser | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1634 | Unit | P2 | – | `shows a spinner only for the first load, then polls quietly` | shows a spinner only for the first load, then polls quietly | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1635 | Unit | P2 | – | `appends a sent message` | appends a sent message | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1636 | Unit | P2 | – | `syncs a guest thread` | syncs a guest thread | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1637 | Unit | P2 | chat slice — admin inbox | `loads conversations, quietly when polling` | loads conversations, quietly when polling | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1638 | Unit | P2 | – | `opens a conversation and replies` | opens a conversation and replies | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1639 | Unit | P2 | – | `deleting the open conversation also closes it` | deleting the open conversation also closes it | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1640 | Unit | P2 | – | `keeps the open conversation when another is deleted` | keeps the open conversation when another is deleted | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1641 | Unit | P2 | – | `starting a chat with a student opens it and lists it once` | starting a chat with a student opens it and lists it once | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1642 | Unit | P2 | – | `submits feedback and reports success` | submits feedback and reports success | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1643 | Unit | P2 | – | `lists, marks read and deletes feedback` | lists, marks read and deletes feedback | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1644 | Unit | P2 | referral slice | `loads the summary and events` | loads the summary and events | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1645 | Unit | P2 | – | `defaults the events limit to 50` | defaults the events limit to 50 | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1646 | Unit | P2 | – | `applies a code then refreshes the summary and events` | applies a code then refreshes the summary and events | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1647 | Unit | P2 | badges slice | `loads the badge dashboard` | loads the badge dashboard | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1648 | Unit | P2 | – | `reports a failed dashboard load with the server detail or a fallback` | reports a failed dashboard load with the server detail or a fallback | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1649 | Unit | P2 | – | `loads earned badges` | loads earned badges | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
| TC-1650 | Unit | P2 | – | `queues and clears badge celebrations` | queues and clears badge celebrations | `edura-frontend/src/lib/redux/__tests__/social-slices.test.ts` | |
