# Architectural Decision Record (ADR)
## ADR-14: Accept known high and critical vulnerabilities in the frontend dependencies

### Status
Proposed. Needs supervisor review within one sprint (development guideline §1.3).

### Context
The development guideline requires "no known high or critical vulnerabilities in dependencies" (§8.2) and a dependency scan in CI (§7.2, OWASP A06). The frontend `Security Scan` job runs `npm audit`.

`npm audit` on the frontend lockfile (`edura-frontend`, `next@15.5.20`) reports **10 vulnerable packages: 2 critical, 7 high, 1 moderate**, covering 22 high or critical advisories (table below).

- `npm audit fix` fixes most of them without a major version change, including a patch update of `next` inside 15.x.
- The remaining PostCSS issue (bundled inside Next) can only be fixed by upgrading to Next 16, a breaking change.
- The frontend is **already deployed to production** (AKS, Docker image built from `next start` on `node:20-alpine`). When a dependency update was tried, the Jest suite failed and there was no time to regression-test the live system before the demo.

### Decision
**Do not change the frontend dependency tree before the final demonstration.** The 22 high and critical advisories are accepted as known risks, listed by ID in `edura-frontend/audit-ci.jsonc`. The `Security Scan` job runs `audit-ci` with that list, so:

- the listed advisories no longer fail the build;
- **any new high or critical advisory still fails the build**;
- every listed advisory is visible in the repository and in this record.

### Advisories accepted
| Package | Advisory | Severity | Summary |
|---|---|---|---|
| brace-expansion | [GHSA-6j4f-fj2g-mc7p](https://github.com/advisories/GHSA-6j4f-fj2g-mc7p) | high | brace-expansion: DoS via uncontrolled recursion in parseCommaParts causing stack exhaustion |
| brace-expansion | [GHSA-qhr7-859c-m2p7](https://github.com/advisories/GHSA-qhr7-859c-m2p7) | high | brace-expansion: DoS via uncontrolled recursion on nested brace groups causing stack exhaustion |
| dompurify | [GHSA-cg2g-xh64-v4q7](https://github.com/advisories/GHSA-cg2g-xh64-v4q7) | critical | DOMPurify SAFE_FOR_TEMPLATES bypass: split template expressions survive in attached shadow root content on DOM output modes |
| dompurify | [GHSA-mrv2-3pqr-j5jr](https://github.com/advisories/GHSA-mrv2-3pqr-j5jr) | high | DOMPurify IN_PLACE: hook that removes a parent or sibling leaves the detached subtree's event handlers armed (incomplete fix for GHSA-p98j-92pf-mc4p) |
| follow-redirects | [GHSA-8r9p-f939-6h3c](https://github.com/advisories/GHSA-8r9p-f939-6h3c) | high | follow-redirects sensitiveHeaders regex escaping can expose credential headers |
| follow-redirects | [GHSA-q3jh-wrc6-jgq8](https://github.com/advisories/GHSA-q3jh-wrc6-jgq8) | high | follow-redirects array-form headers bypass cross-origin credential stripping |
| js-yaml | [GHSA-2883-xcg3-v3hh](https://github.com/advisories/GHSA-2883-xcg3-v3hh) | high | js-yaml: maxTotalMergeKeys does not limit CPU use for empty merge sources |
| js-yaml | [GHSA-5p4m-2wfm-xmqj](https://github.com/advisories/GHSA-5p4m-2wfm-xmqj) | high | JS-YAML: Quadratic CPU consumption in !!omap resolution (3.x and 4.x) — CVE-2026-59870 fix not backported |
| nanoid | [GHSA-2v37-7h3g-55p8](https://github.com/advisories/GHSA-2v37-7h3g-55p8) | high | nanoid: custom generators can loop indefinitely when size is zero |
| next | [GHSA-2464-fhr4-w9xw](https://github.com/advisories/GHSA-2464-fhr4-w9xw) | critical | Next.js: Unauthenticated Remote Code Execution in Image Optimization API when SVG files are used |
| next | [GHSA-2xp9-vwfh-vxw4](https://github.com/advisories/GHSA-2xp9-vwfh-vxw4) | critical | Next.js: Unauthenticated Remote Code Execution in Image Optimization API when AVIF files are used |
| next | [GHSA-89xv-2m56-2m9x](https://github.com/advisories/GHSA-89xv-2m56-2m9x) | high | Next.js: Server-Side Request Forgery in Server Actions on custom servers |
| next | [GHSA-m99w-x7hq-7vfj](https://github.com/advisories/GHSA-m99w-x7hq-7vfj) | high | Next.js: Denial of Service in App Router using Server Actions |
| next | [GHSA-p293-qw3h-jr36](https://github.com/advisories/GHSA-p293-qw3h-jr36) | critical | Next.js: Unauthenticated Remote Code Execution on windows-hosted servers |
| next | [GHSA-p3m5-59mp-jv5r](https://github.com/advisories/GHSA-p3m5-59mp-jv5r) | high | Next.js: Denial of Service in App Router using Server Actions |
| next | [GHSA-p9j2-gv94-2wf4](https://github.com/advisories/GHSA-p9j2-gv94-2wf4) | high | Next.js: Server-Side Request Forgery in rewrites via attacker-controlled destination hostname |
| postcss | [GHSA-6g55-p6wh-862q](https://github.com/advisories/GHSA-6g55-p6wh-862q) | high | PostCSS: Arbitrary file read and information disclosure via attacker-controlled sourceMappingURL in CSS comments |
| postcss | [GHSA-r28c-9q8g-f849](https://github.com/advisories/GHSA-r28c-9q8g-f849) | high | PostCSS: Path Traversal in Previous Source Map Auto-Loading (sourceMappingURL) leads to Arbitrary .map File Disclosure |
| sharp | [GHSA-f88m-g3jw-g9cj](https://github.com/advisories/GHSA-f88m-g3jw-g9cj) | high | sharp inherited vulnerabilities in libvips: CVE-2026-33327, CVE-2026-33328, CVE-2026-35590, CVE-2026-35591 |
| sharp | [GHSA-rgj7-g3m4-5g8c](https://github.com/advisories/GHSA-rgj7-g3m4-5g8c) | high | sharp: Vulnerabilities in libheif: GHSA-g89c-p67h-r497 and GHSA-2jg2-4ch7-h545 |
| sharp | [GHSA-wq5f-xc86-pv6w](https://github.com/advisories/GHSA-wq5f-xc86-pv6w) | high | sharp : Vulnerability in librsvg dependency CVE-2026-96889 |
| source-map-js | [GHSA-68fv-2mgg-jv7q](https://github.com/advisories/GHSA-68fv-2mgg-jv7q) | high | source-map-js allows event-loop denial of service through indexed source-map section offsets |

### Exposure assessment
Based on how the frontend is built and run (`next.config.js`, `Dockerfile`). **Review each line against the advisory text before submitting; the third and fourth rows are not confirmed.**

| Area | Finding |
|---|---|
| Server Actions (`m99w-x7hq-7vfj`, `p3m5-59mp-jv5r`, `89xv-2m56-2m9x`) | No `'use server'` code exists in `src`, so the Server Actions advisories should not be reachable. |
| Windows or custom server (`p293-qw3h-jr36`, `89xv-2m56-2m9x`) | Production runs on Linux with `next start`, not a custom server and not Windows. |
| Image Optimization (`2464-fhr4-w9xw`, `2xp9-vwfh-vxw4`, critical) | **Possibly exposed.** `next.config.js` enables image optimization (`images.remotePatterns`, avif/webp) and `next/image` is used on the landing page and course list. This is the highest-risk item. |
| Rewrites SSRF (`p9j2-gv94-2wf4`) | Not checked. The gateway (nginx) does routing, but `next.config.js` has no rewrites. |
| `dompurify`, `follow-redirects`, `js-yaml`, `brace-expansion`, `nanoid`, `source-map-js`, `sharp`, `postcss` | Transitive dependencies. Several are build-time only. Not individually checked. |

### Mitigations while the risk is accepted
- The browser reaches the frontend only through the nginx gateway; the Next.js server is not exposed directly.
- Image sources are limited to `res.cloudinary.com` through `remotePatterns`.
- Dependabot or a manual `npm audit` re-check after the demonstration.

### Consequences
**Positive**
- The deployed system is unchanged, so the demonstrated system stays the one that was tested.
- CI stays meaningful: new vulnerabilities still fail the build.

**Negative / risks**
- The system knowingly runs with 2 critical and 7 high advisories. The guideline's A06 expectation ("no high/critical vulnerabilities") is **not met** and is recorded as a deviation.
- The Image Optimization advisories may be exploitable on the public site.

### Follow-up (after the demonstration)
1. Run `npm audit fix` on a branch, run the full test suite and deploy it to staging first.
2. Plan the upgrade to Next 16 as its own ticket.
3. Remove each fixed ID from `audit-ci.jsonc`.
4. Quick option if the Image Optimization risk matters sooner: set `images.unoptimized: true` in `next.config.js` (removes the optimizer endpoint, costs image performance).

### Where this is referenced
- `edura-frontend/audit-ci.jsonc` (the accepted list)
- OWASP checklist, A06 Vulnerable Components: mark as "partially met, deviation recorded in ADR-14"
- Final report, 6. Evaluation: "Limitations and known defects"
