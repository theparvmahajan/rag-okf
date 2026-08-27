---
id: okf-relations/edges/015-persistent-volume-claim-persistent-volume
kind: relation
subject: PersistentVolumeClaim
predicate: binds
object: PersistentVolume
subject_entity: okf-relations/entities/persistent-volume-claim
object_entity: okf-relations/entities/persistent-volume
grounding_sources:
- source: concepts/storage/persistent-volumes.md
  score: 1208
  subject_hits: 47
  object_hits: 110
- source: concepts/scheduling-eviction/dynamic-resource-allocation.md
  score: 860
  subject_hits: 2
  object_hits: 2
- source: tutorials/configuration/configure-persistent-volume-storage.md
  score: 435
  subject_hits: 22
  object_hits: 53
source: concepts/storage/persistent-volumes.md
word_count: 22
---

PersistentVolumeClaim binds PersistentVolume. A PersistentVolumeClaim is matched and bound to a PersistentVolume whose capacity, access mode, and class satisfy the claim's request.
