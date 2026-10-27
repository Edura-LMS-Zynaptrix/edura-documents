# Architectural Decision Record (ADR)
## ADR-15: The documents repository uses `main` only, without a `develop` branch

### Status
Proposed. Needs supervisor review within one sprint (development guideline §1.3).

### Context
The development guideline (§3.2) defines a Git Flow style branch strategy: `main` holds production-ready code and only accepts merges through an approved pull request, while `develop` is the integration branch where features are merged first and from which releases are cut. Appendix C asks for a `develop` branch, set as the default, on the **code repositories**.

`edura-documents` is the `documents` repository from SENG 31242 (guideline §3.1: "Continued from SENG 31242"). It holds the SRS, SDS, ADRs, meeting notes, sprint plans, retrospectives and testing and security evidence. It contains no source code, no build and no deployable artefact:

- There is no release to prepare and no version to bump or tag; documents are not shipped.
- There is no integration or staging environment, so nothing is deployed from `develop` to staging or from `main` to production.
- No CI pipeline runs on this repository.
- Every change is already submitted as a feature branch and reviewed in a pull request, and the repository has been used this way since the design phase.

### Decision
`edura-documents` keeps **`main` as its only long-lived branch** and as its default branch. A `develop` branch is **not** created.

The rest of the guideline's workflow still applies:

- Work happens on short-lived branches named `feature/<ticket-id>-<slug>` or `fix/<ticket-id>-<slug>` (guideline §3.2).
- Every change reaches `main` through a pull request with at least **one approving review** (guideline §5.3, §8.2) and all review comments resolved.
- Commit messages follow Conventional Commits and reference the issue (guideline §3.4), for example `docs(adr): add ADR-15`.
- `main` is protected; direct pushes are not allowed.

The code repositories (`edura-backend`, `edura-frontend`, `edura-infra`, `edura-tests`) are unaffected and use `main` and `develop` as the guideline requires.

### Consequences
**Positive**
- Simpler workflow for documentation: one merge instead of two (feature to `develop`, then `develop` to `main`), with no release branch that would carry nothing.
- `main` always shows the latest approved version of every document, which is what supervisors and the final submission (guideline §10.1: `documents/...`) need.
- No risk of documents drifting between two long-lived branches.

**Negative / trade-offs**
- There is no staging area for documents. Everything on `main` has already been reviewed, but there is no second branch to hold work that is approved but not yet "published".
- This is a deviation from Appendix C for one repository. It is limited to a repository without code, and is recorded here.
- Branch protection on `main` is the only guard. It should be kept strict: require a pull request and one approval, require conversation resolution, and apply the rule to administrators. At the time of writing the rule on `main` does not yet apply to administrators; enabling it is a follow-up.

### Follow-up
1. On `main` in `edura-documents`, enable **Do not allow bypassing the above settings** and **Require conversation resolution before merging**.
2. Add a note to the repository README that `main` is the only long-lived branch and that changes go through pull requests from `feature/` branches.
3. Mention this decision in the final report under repository setup (guideline §3.1 and §10.4, chapter 4).
4. If the repository ever gains code or a CI pipeline (for example a document build), revisit this decision and create `develop`.
