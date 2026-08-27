---
id: okf-relations/edges/014-pod-persistent-volume-claim
kind: relation
subject: Pod
predicate: claims storage via
object: PersistentVolumeClaim
subject_entity: okf-relations/entities/pod
object_entity: okf-relations/entities/persistent-volume-claim
grounding_sources:
- source: concepts/storage/persistent-volumes.md
  score: 1765
  subject_hits: 72
  object_hits: 47
- source: concepts/storage/volumes.md
  score: 1276
  subject_hits: 130
  object_hits: 10
- source: concepts/scheduling-eviction/dynamic-resource-allocation.md
  score: 1121
  subject_hits: 182
  object_hits: 2
source: concepts/storage/persistent-volumes.md
word_count: 25
---

Pod claims storage via PersistentVolumeClaim. A Pod references a PersistentVolumeClaim by name in its volumes list to get durable storage that outlives the Pod itself.
