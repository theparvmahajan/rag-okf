---
id: okf-relations/edges/016-persistent-volume-claim-storage-class
kind: relation
subject: PersistentVolumeClaim
predicate: provisioned via
object: StorageClass
subject_entity: okf-relations/entities/persistent-volume-claim
object_entity: okf-relations/entities/storage-class
grounding_sources:
- source: concepts/storage/persistent-volumes.md
  score: 473
  subject_hits: 47
  object_hits: 68
- source: concepts/storage/storage-classes.md
  score: 405
  subject_hits: 8
  object_hits: 55
- source: concepts/storage/dynamic-provisioning.md
  score: 166
  subject_hits: 7
  object_hits: 22
source: concepts/storage/persistent-volumes.md
word_count: 21
---

PersistentVolumeClaim provisioned via StorageClass. If no PersistentVolume already matches a claim, the claim's StorageClass tells its provisioner to create one dynamically.
