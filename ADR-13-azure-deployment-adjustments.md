# Architectural Decision Record (ADR)
## ADR-13: Azure AKS Deployment — Region, Node Size, TLS Edge and CI/CD Tooling

### Status
Proposed — to be reviewed with the supervisor (SENG 34213 §1.3)

### Context
SDS Chapter 8 (Deployment Design) and issues DDP-#12 / DDP-#18 describe the target deployment:
AKS + ACR in `eastasia`, `Standard_D4s_v3 × 2` nodes for staging, the Nginx gateway doing TLS
termination, managed Azure Cache for Redis, and Azure DevOps pipelines with canary releases.

While implementing DDP-#12 and DDP-#18, several of these turned out not to fit the project's real constraints:

1. **Database location.** All 11 per-service databases are Neon PostgreSQL projects in AWS `us-east-1`
   (Virginia, USA). A service in `eastasia` (Hong Kong) would pay ~200 ms per database round trip, and a
   single API request makes several queries. The users being in Sri Lanka matters far less than the
   app being next to its data.
2. **Subscription quota.** The team's Azure subscription is a free trial, limited to 4 vCPUs per region.
   `Standard_D4s_v3 × 2` needs 8 vCPUs, so `az aks create` would be rejected.
3. **HTTPS is mandatory.** auth_service sets its refresh-token cookie with `Secure`, and Google Sign-In only
   accepts `https://` origins for real domains. Staging therefore needs a trusted certificate from day one.
4. **CI/CD tooling.** The course guideline (SENG 34213 Chapter 7, LO4) requires **GitHub Actions**, and the
   team's CI already runs there. The SDS names Azure DevOps.
5. **Budget.** Azure Cache for Redis and separate clusters per environment would exhaust the free credit quickly.

### Decision
| Area | SDS / issue | Implemented |
|---|---|---|
| Region | `eastasia` | **`eastus`**, co-located with the Neon databases (AWS `us-east-1`) |
| Node pool | `Standard_D4s_v3 × 2` (frontend D4s, backend D8s, analytics E4s in SDS §8.2) | **`Standard_D2als_v7 × 1`** (2 vCPU, 4 GB, 30 GB OS disk; free-trial subscriptions can't use B-series for AKS), the minimum that runs all 11 services + frontend + RabbitMQ + Redis; scale with `az aks scale` / `NODE_SKU` |
| Environments | separate dev / staging / prod | **One AKS cluster, namespace per environment.** Only `edura-staging` runs (auto-deployed from `develop`); `edura-production` (from `main`, manual approval) is wired into the pipeline but disabled until the `ENABLE_PRODUCTION` variable is set |
| URLs | `staging.edura.lk` | **`https://staging.eduralms.com`** and **`https://eduralms.com`** (the team owns `eduralms.com`) |
| TLS | Nginx gateway | **Caddy** edge in front of the unchanged Nginx gateway, with automatic Let's Encrypt certificates on a static public IP per environment. The Nginx gateway still does routing and rate limiting (SDS §2.1). |
| Redis | Azure Cache for Redis | **In-cluster Redis** pod (cache/OTP only, no persistence needed) |
| RabbitMQ | — | In-cluster StatefulSet with a persistent disk; topology created by the `rabbitmq-setup` Job |
| CI/CD | Azure DevOps, canary | **GitHub Actions** (`edura-infra/.github/workflows/deploy.yml`), rolling updates; production gated by a required reviewer on the GitHub `production` environment |
| Azure auth from CI | Workload Identity / `KUBE_CONFIG_DATA` | **OIDC federated credentials** (`azure/login` + `azure/aks-set-context`); no kubeconfig or password stored in GitHub |
| Secrets | Azure Key Vault | **GitHub environment secrets** (one per service `.env`) → Kubernetes Secrets at deploy time. Key Vault remains future work. |

### Consequences
- **Performance:** Database queries stay inside one geographic region. Users in Sri Lanka add roughly 250 ms
  per page request instead of per query.
- **Cost:** About US$95/month (1 VM, load balancer, 2 IPs, small disks, ACR Basic), versus ~US$280+ for the SDS
  sizing. The cluster can be stopped (`az aks stop`) when idle.
- **Capacity:** One node is a single point of failure, and pods are packed tightly (memory requests lowered to fit
  4 GB). Enough for UAT and the panel demo, not for real production load.
- **Compliance with the guideline:** Staging auto-deploys on merge to `develop`. Production deploys on merge to
  `main` with manual approval (Chapter 7.2). The panel demo runs on the staging URL (§9.1).
- **Trade-offs:** No canary releases and no multi-zone high availability, so the production SLA in SDS §8.4 is
  not met. Redis data is lost if its pod restarts, which only affects in-flight OTPs and caches.
- **Reversibility:** Region, node size and Redis can be changed without code changes. Moving to `eastasia` would
  first require moving the Neon databases to an Asia region.
- **The SDS must be updated** (Chapter 8) to reflect this design before the final submission.
