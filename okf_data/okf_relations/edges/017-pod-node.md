---
id: okf-relations/edges/017-pod-node
kind: relation
subject: Pod
predicate: scheduled onto
object: Node
subject_entity: okf-relations/entities/pod
object_entity: okf-relations/entities/node
grounding_sources:
- source: concepts/scheduling-eviction/assign-pod-node.md
  score: 1330
  subject_hits: 195
  object_hits: 179
- source: concepts/scheduling-eviction/taint-and-toleration.md
  score: 981
  subject_hits: 77
  object_hits: 148
- source: concepts/scheduling-eviction/dynamic-resource-allocation.md
  score: 962
  subject_hits: 182
  object_hits: 104
source: concepts/scheduling-eviction/assign-pod-node.md
word_count: 31
---

Pod scheduled onto Node. The scheduler assigns a Pod to a Node that satisfies its resource requests, node selector/affinity rules, and any taints the Node has that the Pod must tolerate.
