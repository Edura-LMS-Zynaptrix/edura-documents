# Architectural Decision Record (ADR)
## ADR-13: Azure deployment adjustments to SDS Chapter 8

### Status
Proposed. Needs supervisor review within one sprint (development guideline §1.3).

Note: this ADR was written after the deployment was built. `edura-infra` (README, `docs/AZURE-DEPLOYMENT.md`, `scripts/provision-aks.sh`, `.github/workflows/ci.yml`) already refers to "ADR-13" for these decisions, so the number 13 was reserved for it.

### Context
SDS Chapter 8 (Deployment Design) describes the intended hosting:

- **8.1:** Azure Kubernetes Service (AKS) for the containers, PostgreSQL on Neon, **Azure Cache for Redis**, Cloudinary.
- **8.2:** separate node pools: frontend `Standard_D4s_v3` (4 vCPU, 16 GB), backend `Standard_D8s_v3` (8 vCPU, 32 GB), data processing `Standard_E4s_v3` (4 vCPU, 32 GB).
- **8.4:** three environments: development, staging (a production mirror for UAT) and production (high availability, multi-zone, 99.9% uptime SLA).
- **8.5:** **Azure DevOps** pipelines with Snyk/Trivy scans, staging deployed on merge, and production deployed with manual approval and a **canary** strategy.

The team deployed EDURA on a free-trial Azure subscription with limited credit, using GitHub (where the code and issues already live). Deploying the SDS sizing would cost roughly US$280 or more per month, against about US$95 for the setup below, and free-trial subscriptions cannot use B-series VM sizes for AKS.

### Decision
The deployment differs from SDS Chapter 8 as follows.

| Topic | SDS Chapter 8 | Implemented | Reason |
|---|---|---|---|
| Cluster size | Several node pools (D4s_v3, D8s_v3, E4s_v3) | **One** `Standard_D2als_v7` node (2 vCPU, 4 GB, 30 GB OS disk) | Cost; the cheapest 2-vCPU size the free trial allows. Can be scaled without code changes. |
| Region | Not stated | **eastus** | Close to the Neon databases in AWS us-east-1. |
| Redis | Azure Cache for Redis | **Redis inside the cluster** (`k8s/base/10-redis.yaml`) | Redis only holds short-lived data (OTPs, rate counters, cache), so durability is not required; avoids a paid service. |
| RabbitMQ | Not specified for Azure | **StatefulSet inside the cluster** | Event bus for ADR-12; no managed service needed at this scale. |
| TLS / public entry | Gateway TLS (8.1, security chapter) | **Caddy** in front of the Nginx gateway, free Let's Encrypt certificates | No cost; automatic renewal. |
| CI/CD | Azure DevOps | **GitHub Actions** (`deploy.yml`), signing in to Azure with OIDC | The code, reviews and issues are on GitHub; no extra tool or credentials to store. |
| Environments | Development, staging, production | **Staging only**; production is fully wired but switched off | One 4 GB node cannot hold two environments. Local development uses `docker-compose.yml`. |
| Production deploy | Manual approval plus canary | Manual approval through the GitHub `production` environment (required reviewers); **rolling update, no canary** | Canary needs a traffic-splitting component and more capacity. Rollback is `kubectl rollout undo`. |
| Pipeline scans | Pylint/ESLint, Snyk/Trivy | Ruff + Black, ESLint + Prettier; `pip-audit` and `audit-ci` | Free tools that fit the Python and Node code; accepted advisories follow ADR-14. |

Production is enabled by setting the organisation variable `ENABLE_PRODUCTION` to `true` and adding capacity; see `edura-infra/docs/AZURE-DEPLOYMENT.md`, Part F.

### Consequences
**Positive**
- Runs EDURA for about US$95 per month, within the free-trial credit.
- The pipeline, manifests and scripts already support production, so scaling up needs configuration, not code.
- One tool (GitHub) for code, reviews, issues and deployment.

**Negative / trade-offs**
- **No high availability:** a single node means one failure takes the whole environment down, and there is no multi-zone redundancy or 99.9% SLA.
- **Limited capacity:** the 4 GB node can fill up; pods may be evicted or stay `Pending` (see the troubleshooting table in `AZURE-DEPLOYMENT.md`).
- **Redis in the cluster is not durable:** cached data and OTPs are lost if the pod is rescheduled.
- **No canary releases,** so a bad release reaches all users at once; rollback is manual.
- **Staging is not a production mirror:** it is the only running environment, so there is no UAT environment separate from the demo.
- The free-trial subscription is disabled after 30 days or when the credit runs out, unless upgraded to pay-as-you-go.

### Follow-up
1. Update SDS Chapter 8 (sections 8.1, 8.2, 8.4 and 8.5) to match this ADR (guideline §1.3). This is also item 5 under "Known gaps" in `edura-infra/docs/AZURE-DEPLOYMENT.md`.
2. Review this ADR with the supervisor within one sprint.
3. Before the final demo, upgrade the Azure subscription or confirm the cluster start date, and check the staging URL two hours before the panel.
4. If production is switched on, add a node (or larger VMs) and revisit the single-node and Redis decisions.
5. Mention these deviations in the final report under deployment (guideline §10.4).
