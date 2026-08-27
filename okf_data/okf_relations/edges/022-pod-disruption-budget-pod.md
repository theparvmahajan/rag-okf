---
id: okf-relations/edges/022-pod-disruption-budget-pod
kind: relation
subject: PodDisruptionBudget
predicate: protects
object: Pod
subject_entity: okf-relations/entities/pod-disruption-budget
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 714
  subject_hits: 1
  object_hits: 350
- source: concepts/scheduling-eviction/node-pressure-eviction.md
  score: 493
  subject_hits: 2
  object_hits: 81
- source: concepts/workloads/pods/_index.md
  score: 400
  subject_hits: 1
  object_hits: 199
source: concepts/workloads/pods/pod-lifecycle.md
word_count: 29
---

PodDisruptionBudget protects Pod. A PodDisruptionBudget caps how many of a matching set of Pods can be evicted at once during voluntary disruptions like a Node drain or cluster upgrade.
