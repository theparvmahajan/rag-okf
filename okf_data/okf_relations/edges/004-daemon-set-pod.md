---
id: okf-relations/edges/004-daemon-set-pod
kind: relation
subject: DaemonSet
predicate: owns
object: Pod
subject_entity: okf-relations/entities/daemon-set
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/scheduling-eviction/assign-pod-node.md
  score: 406
  subject_hits: 5
  object_hits: 195
- source: concepts/workloads/pods/_index.md
  score: 402
  subject_hits: 2
  object_hits: 199
- source: concepts/workloads/controllers/daemonset.md
  score: 328
  subject_hits: 74
  object_hits: 84
source: concepts/scheduling-eviction/assign-pod-node.md
word_count: 28
---

DaemonSet owns Pod. A DaemonSet ensures one matching Pod runs on every Node (or every Node matching a selector), adding or removing Pods as Nodes join or leave.
