---
id: okf-relations/edges/025-priority-class-pod
kind: relation
subject: PriorityClass
predicate: assigns priority to
object: Pod
subject_entity: okf-relations/entities/priority-class
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/scheduling-eviction/pod-priority-preemption.md
  score: 1065
  subject_hits: 42
  object_hits: 180
- source: concepts/workloads/pods/_index.md
  score: 406
  subject_hits: 1
  object_hits: 199
- source: concepts/policy/resource-quotas.md
  score: 389
  subject_hits: 15
  object_hits: 115
source: concepts/scheduling-eviction/pod-priority-preemption.md
word_count: 25
---

PriorityClass assigns priority to Pod. A Pod references a PriorityClass to get a priority value the scheduler uses to decide preemption order under resource pressure.
