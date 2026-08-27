---
id: okf-relations/edges/021-horizontal-pod-autoscaler-deployment
kind: relation
subject: HorizontalPodAutoscaler
predicate: scales
object: Deployment
subject_entity: okf-relations/entities/horizontal-pod-autoscaler
object_entity: okf-relations/entities/deployment
grounding_sources:
- source: concepts/workloads/controllers/deployment.md
  score: 1515
  subject_hits: 1
  object_hits: 428
- source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
  score: 739
  subject_hits: 37
  object_hits: 22
- source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
  score: 558
  subject_hits: 30
  object_hits: 21
source: concepts/workloads/controllers/deployment.md
word_count: 24
---

HorizontalPodAutoscaler scales Deployment. An HPA watches metrics (e.g. CPU utilization) and adjusts the replica count on the Deployment (or other scalable controller) it targets.
