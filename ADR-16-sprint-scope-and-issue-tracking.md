# Architectural Decision Record (ADR)
## ADR-16: Sprint backlog scope, untracked demo activities and no formal sprint capacity

### Status
Proposed. Needs supervisor review within one sprint (development guideline §1.3).

### Context
The development guideline sets expectations for how sprints are planned and tracked:

- Appendix C: "Sprint 5 backlog populated with at least 15 development issues", "Sprint capacity calculated per member", and "all issues have: assignee, estimate, priority label, epic label, acceptance criteria".
- §4.1 and §4.3: every development task is an issue on the project board with a technical description and acceptance criteria.

The team's sprint plan (Sprints 5 to 8) numbers its work items DDP-#01 to DDP-#48. In practice the project differs from these expectations in three ways:

1. **Sprint 5 has 14 issues, not 15.** The sprint plan assigns DDP-#01 to #12, #18 and #25 to Sprint 5. Those 14 issues cover the whole Foundation and Infrastructure theme: repositories, Docker Compose, CI, service skeletons, data layer, RabbitMQ, Nginx and the AKS cluster. The scope was sized to the work the team needed, and no filler issue was added to reach 15.
2. **Five planned items were never created as GitHub issues:** DDP-#38, #43, #44, #46 and #47. They describe activities and not deliverables:

   | Plan item | Activity |
   |---|---|
   | DDP-#38 | Fix P1-Critical bugs found in the demo walkthrough. Each bug is already tracked as its own issue (DDP-#37 logs failures as bug issues), so a second umbrella issue would duplicate them. |
   | DDP-#43 | First full demo rehearsal on the production URL |
   | DDP-#44 | Second rehearsal with Q&A preparation |
   | DDP-#46 | Pre-demo verification of the production URL and demo accounts |
   | DDP-#47 | The live panel demonstration |

   None produces a code, test or document change that a pull request could close.
3. **Sprint capacity was not calculated per member.** The sprint plan estimates about 62 hours per member across 16 weeks (about 3.9 hours per week) and assigns service ownership, but no per-sprint capacity figure was recorded.

### Decision
- Sprint 5 stays at **14 issues**, matched to its planned scope, and this ADR is the record of the shortfall against Appendix C.
- DDP-#38, #43, #44, #46 and #47 **are not created as issues**. They stay in the sprint plan as scheduled activities. Any defect they uncover is raised as an ordinary bug issue.
- Sprint capacity is **not retroactively calculated** for Sprints 5 to 8. The per-member hour estimates in the sprint plan stand as the capacity assumption.
- Every issue that does exist keeps the required fields: assignee, estimate, priority label, epic label and acceptance criteria.

### Consequences
**Positive**
- The board holds only real, closable work, and bugs are not tracked twice.
- No effort is spent creating issues that would only be opened and closed.

**Negative / trade-offs**
- Sprint 5 is one issue short of Appendix C, and the DDP numbering has gaps (38, 43, 44, 46, 47), which a reader of the board may question.
- Without a recorded capacity, velocity can be compared with planned hours only at the whole-project level, not per sprint and per member.
- Rehearsal and demo activities leave no board history beyond the sprint plan and the retrospectives.

### Follow-up
1. Reference this ADR in the final report under project management (guideline §10.4).
2. Mention the gaps in DDP numbering in the Sprint 8 retrospective.
3. If a later sprint plan is made, record planned hours per member for each sprint at planning time.
