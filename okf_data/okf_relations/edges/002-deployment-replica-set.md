---
id: okf-relations/edges/002-deployment-replica-set
kind: relation
subject: Deployment
predicate: manages rollout via
object: ReplicaSet
subject_entity: okf-relations/entities/deployment
object_entity: okf-relations/entities/replica-set
grounding_sources:
- source: concepts/workloads/controllers/deployment.md
  score: 1662
  subject_hits: 428
  object_hits: 130
- source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
  score: 462
  subject_hits: 22
  object_hits: 5
- source: tasks/run-application/update-deployment-rolling.md
  score: 325
  subject_hits: 87
  object_hits: 2
source: concepts/workloads/controllers/deployment.md
word_count: 29
---

Deployment manages rollout via ReplicaSet. Updating a Deployment's Pod template creates a new ReplicaSet and gradually scales it up while scaling the old ReplicaSet down - a rolling update.
