# Performance Test Report

Guideline reference: §10.1 item 9 (performance test results). Requirements tested: SRS NFR-001 (response time) and NFR-009 (scalability).

- **Date:** 2026-10-28
- **Environment:** staging, `https://staging.eduralms.com` (AKS, namespace `edura-staging`: one replica per service, shared Neon Postgres).
- **Client:** one laptop in Sri Lanka, one IP address. The servers are in Azure East US, so about 240 ms of every response is network travel.
- **Tool:** `edura-tests/performance/load_test.py` (asyncio and httpx). Read-only GET requests to public endpoints; nothing was created or changed.

## Requirements

| ID | Requirement | Target |
|---|---|---|
| NFR-001 | 95% of standard user interface interactions processed and rendered in under 2.0 s under normal load | p95 below 2.0 s |
| NFR-009 | Support at least 500 concurrent user sessions with no more than 20% degradation | 500 concurrent users |

## Test 1: response time (NFR-001)

Method: 20 requests per endpoint, 0.8 s apart (about 75 requests per minute, under the gateway's limit), after one warm-up request that is not counted.

| Endpoint | Requests | Errors | p50 ms | p95 ms | p99 ms | Under 2 s |
|---|---|---|---|---|---|---|
| `GET /api/courses/` | 20 | 0 | 247 | 1,816 | 2,742 | 95.0% |
| `GET /api/courses/11` | 20 | 0 | 240 | 325 | 429 | 100.0% |
| `GET /api/analytics/platform-stats` | 20 | 0 | 246 | 319 | 394 | 100.0% |
| `GET /api/enrollments/class-packages` | 20 | 0 | 246 | 326 | 343 | 100.0% |

**Result: met for these endpoints.** Typical responses take about 250 ms. The course list is the weak point: its p95 is 1.8 s, just inside the target, and its slowest request took 2.7 s. It returns the whole catalogue (20 or more courses per call), so it is the first place to look if the 2 s target is missed. With 20 samples per endpoint, a p95 is one request; treat it as an indication, not a guarantee.

## Test 2: concurrent load through the gateway (NFR-009)

Method: closed-loop workers sending requests continuously for 15 s per step to `GET /api/courses/11` and `GET /api/analytics/platform-stats`.

| Concurrent users | Requests | Errors | Throughput req/s | p50 ms | p95 ms | p99 ms |
|---|---|---|---|---|---|---|
| 1 | 50 | 8 (16.0%, 8 rate-limited) | 3.3 | 235 | 310 | 2,040 |
| 5 | 275 | 241 (87.6%, 241 rate-limited) | 18.0 | 250 | 328 | 812 |
| 10 | 560 | 527 (94.1%, 527 rate-limited) | 36.9 | 247 | 370 | 856 |

Every error was HTTP 429 from the gateway's rate limit (100 requests per minute per IP, burst 20). **No request failed with a server error (5xx) and none timed out.** Requests that were answered kept a p50 of about 250 ms at every step, so the gateway protected the services as designed.

## What these results do and do not show

- **NFR-001 (response time): met** for the endpoints tested, at normal load.
- **NFR-009 (500 concurrent users): not verified.** The 429 responses show that one client IP cannot load the system through the gateway, so Test 2 measures the rate limit, not the services' capacity. Students on different networks have different IPs and are limited separately, but students sharing one IP (a school or institute network) would share the 100 requests per minute. That deserves a decision from the client.
- Only public read endpoints were tested. Sign-in (bcrypt hashing), exam submission and payment webhooks, which are heavier, were not load tested.
- Staging runs one replica per service on a small cluster, so it is not a measure of what production can do.

## Gaps and next steps

| # | Gap | Suggested action |
|---|---|---|
| 1 | 500-concurrent-user target not verified | Load test a service directly from inside the cluster (for example `kubectl port-forward` to one service, or a short-lived load pod) with `PERF_BASE_URL` set accordingly. Needs approval, because it loads the shared staging database. |
| 2 | Course list p95 is 1.8 s | Add paging or caching to the course list in a later release (application change, deferred). |
| 3 | Heavy endpoints not tested | Add sign-in, exam start and submit to the script using a throw-away account. |
| 4 | Report is Markdown; deliverable list asks for PDF | Export as `performance-report.pdf` for the final submission. |
