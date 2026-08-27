---
id: okf-relations/edges/000-deployment-replica-set
kind: relation
subject: Deployment
predicate: owns
object: ReplicaSet
subject_entity: okf-relations/entities/deployment
object_entity: okf-relations/entities/replica-set
grounding_sources:
- source: concepts/workloads/controllers/deployment.md
  score: 1116
  subject_hits: 428
  object_hits: 130
- source: concepts/workloads/controllers/replicaset.md
  score: 213
  subject_hits: 14
  object_hits: 88
- source: tasks/run-application/update-deployment-rolling.md
  score: 178
  subject_hits: 87
  object_hits: 2
source: concepts/workloads/controllers/deployment.md
word_count: 29
---

Deployment owns ReplicaSet. A Deployment creates and owns ReplicaSets via an owner reference; the garbage collector uses that reference, not labels, to cascade-delete ReplicaSets when the Deployment is deleted.
