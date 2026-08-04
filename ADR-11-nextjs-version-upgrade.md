# Architectural Decision Record (ADR)
## ADR-11: Upgrade Next.js to Version 15 and React to Version 19

### Status
Decided / Approved

### Context
The original repository was configured to use **Next.js 14** as the client-side framework. However, during the implementation of the CI/CD pipeline (**DDP-#03**), running security checks (`npm audit --audit-level=high`) failed because Next.js 14 has multiple active, high-severity CVEs (including image optimization vulnerability `CVE-2025-66478`) that are no longer patched under Next.js 14. 

To satisfy the strict security scan criteria:
1. The framework must be updated to a secure release.
2. The nested peer dependencies like `postcss` (moderate vulnerability) and `minimatch` (high vulnerability) also need to be overridden.

### Decision
We will upgrade the frontend repository dependencies to:
- **Next.js 15.5.20** (or latest stable Next 15 release)
- **React 19.2.7** and **React-DOM 19.2.7** (required for Next 15)
- **ESLint Config Next 15.5.20**

Additionally, we will configure package overrides in `package.json` to lock transitive dependencies to non-vulnerable versions:
```json
  "overrides": {
    "postcss": "^8.5.10",
    "minimatch": "^9.0.8"
  }
```

### Consequences
- **Security Check Compliance**: The `npm audit --audit-level=high` command now reports **0 vulnerabilities** and passes the security scan stage in the GitHub Actions CI/CD pipeline cleanly.
- **Future-proofing**: Moving to Next.js 15 and React 19 keeps the EDURA Learning Management System up-to-date with modern APIs and performance upgrades.
- **Compatibility**: All page components, Redux configurations, and custom styles remain compatible with the updated rendering APIs.
