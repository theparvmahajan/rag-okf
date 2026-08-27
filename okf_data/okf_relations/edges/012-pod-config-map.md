---
id: okf-relations/edges/012-pod-config-map
kind: relation
subject: Pod
predicate: mounts
object: ConfigMap
subject_entity: okf-relations/entities/pod
object_entity: okf-relations/entities/config-map
grounding_sources:
- source: concepts/storage/volumes.md
  score: 1760
  subject_hits: 130
  object_hits: 18
- source: tasks/configure-pod-container/configure-pod-configmap.md
  score: 1662
  subject_hits: 103
  object_hits: 236
- source: tutorials/configuration/updating-configuration-via-a-configmap.md
  score: 1275
  subject_hits: 75
  object_hits: 168
source: concepts/storage/volumes.md
word_count: 17
---

Pod mounts ConfigMap. A Pod can consume a ConfigMap as mounted files, environment variables, or command-line arguments.
