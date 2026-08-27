---
id: okf-relations/edges/003-stateful-set-pod
kind: relation
subject: StatefulSet
predicate: owns
object: Pod
subject_entity: okf-relations/entities/stateful-set
object_entity: okf-relations/entities/pod
grounding_sources:
- source: tutorials/stateful-application/basic-stateful-set.md
  score: 790
  subject_hits: 165
  object_hits: 191
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 709
  subject_hits: 3
  object_hits: 350
- source: concepts/workloads/controllers/statefulset.md
  score: 509
  subject_hits: 97
  object_hits: 129
source: tutorials/stateful-application/basic-stateful-set.md
word_count: 22
---

StatefulSet owns Pod. A StatefulSet creates Pods directly (no intermediate ReplicaSet) with a stable name, ordinal index, and persistent identity across rescheduling.
