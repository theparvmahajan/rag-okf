---
id: okf-relations/edges/001-replica-set-pod
kind: relation
subject: ReplicaSet
predicate: owns
object: Pod
subject_entity: okf-relations/entities/replica-set
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/workloads/controllers/deployment.md
  score: 1179
  subject_hits: 130
  object_hits: 140
- source: concepts/workloads/controllers/replicaset.md
  score: 753
  subject_hits: 88
  object_hits: 131
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 711
  subject_hits: 1
  object_hits: 350
source: concepts/workloads/controllers/deployment.md
word_count: 23
---

ReplicaSet owns Pod. A ReplicaSet creates and owns the Pods matching its selector via an owner reference, and recreates them if they disappear.
