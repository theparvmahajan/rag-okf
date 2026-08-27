---
id: okf-relations/edges/026-pod-container
kind: relation
subject: Pod
predicate: contains
object: Container
subject_entity: okf-relations/entities/pod
object_entity: okf-relations/entities/container
grounding_sources:
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 2210
  subject_hits: 350
  object_hits: 299
- source: concepts/workloads/pods/_index.md
  score: 914
  subject_hits: 199
  object_hits: 102
- source: concepts/storage/volumes.md
  score: 906
  subject_hits: 130
  object_hits: 125
source: concepts/workloads/pods/pod-lifecycle.md
word_count: 21
---

Pod contains Container. A Pod's spec lists one or more Containers that share the Pod's network namespace and, optionally, its volumes.
