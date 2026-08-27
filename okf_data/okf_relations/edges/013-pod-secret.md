---
id: okf-relations/edges/013-pod-secret
kind: relation
subject: Pod
predicate: mounts
object: Secret
subject_entity: okf-relations/entities/pod
object_entity: okf-relations/entities/secret
grounding_sources:
- source: concepts/storage/volumes.md
  score: 1870
  subject_hits: 130
  object_hits: 40
- source: concepts/configuration/secret.md
  score: 1415
  subject_hits: 61
  object_hits: 237
- source: concepts/storage/persistent-volumes.md
  score: 1279
  subject_hits: 72
  object_hits: 2
source: concepts/storage/volumes.md
word_count: 32
---

Pod mounts Secret. A Pod can consume a Secret the same way it consumes a ConfigMap - mounted files or environment variables - with extra handling conventions since the data is sensitive.
