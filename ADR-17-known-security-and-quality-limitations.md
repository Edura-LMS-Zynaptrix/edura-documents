# Architectural Decision Record (ADR)
## ADR-17: Known security and quality limitations accepted in the deployed release

### Status
Proposed. Needs supervisor review within one sprint (development guideline §1.3).

### Context
The OWASP Top 10 review (`security/owasp-checklist.md`) and the test coverage report (`testing/coverage-report.md`) compared the implemented system with the development guideline (§6.4, §8.1, §8.2). Most requirements are met, but the review found items that are not implemented or not demonstrated. Fixing several of them means changing the application code of the services, and the staging deployment is already running and used for the demonstration (§9.1). The team decided not to change the running application close to the demonstration, to avoid introducing new defects.

Items that need an application code change:

| # | Limitation | OWASP / guideline | Current behaviour |
|---|---|---|---|
| 1 | No account lockout after repeated failed logins | A07 | A wrong password returns `INVALID_CREDENTIALS`; failures are not counted. The gateway rate limit (100 requests per minute per IP) is the only brake. |
| 2 | Authentication events are not logged; recipient email addresses appear in logs | A09 | `auth_service` logs only start-up messages; `notification_service` logs `to_email` / `email`. |
| 3 | Fallback `SECRET_KEY` in code | A02 | `shared/auth.py` and `auth_service/config.py` fall back to a fixed development key if the variable is unset. Every environment sets its own key. |
| 4 | bcrypt work factor is the library default | A02 | The default is 12, which meets the minimum, but it is not set explicitly. |
| 5 | No Python lock file | A08 | `requirements.txt` files mix pinned and unpinned versions. |
| 6 | No threat model in the SDS | A04 | The SDS has a project risk register only. |

Items that need no application code change are being handled separately: response security headers at the edge (configuration), branch coverage reporting in CI (pipeline), and the RabbitMQ default credentials (secrets).

### Decision
The release keeps the six limitations above. They are **accepted and recorded**, not fixed, until after the final demonstration:

- No application code is changed for items 1 to 5 in this release.
- The limitations are listed in the OWASP checklist, in the final report under limitations and future work, and in the demonstration's "Limitations & Future Work" section (§9.2).
- The threat model (item 6) is documentation only and is added to the SDS security section.
- For item 3, a **configuration check** replaces the code change: each environment's `SECRET_KEY` is verified to differ from the fallback value.

### Consequences
**Positive**
- The running system, which has been tested end to end, stays unchanged before the demonstration.
- The limitations are visible and owned, not hidden.

**Negative / trade-offs**
- Repeated password guessing is slowed only by the gateway rate limit.
- Security investigations after an incident would lack authentication-event logs, and logs hold personal data (email addresses).
- If a deployment ever starts without `SECRET_KEY`, tokens would be signed with a publicly known key.
- Python builds are not fully reproducible.

### Follow-up
1. Verify, with someone who holds the secrets, that the staging and production `SECRET_KEY` values differ from the fallback in the code.
2. After the demonstration, create issues for items 1 to 5 and schedule them in the next release (account lockout, authentication-event logging with masked emails, removing the key fallback so a missing key fails at start-up, explicit bcrypt rounds, pinned dependencies).
3. Add the threat model to the SDS security section.
4. Re-run the OWASP review after those changes and update `security/owasp-checklist.md`.
5. Revisit this ADR when any of the items is fixed.
