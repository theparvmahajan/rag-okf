---
id: okf-relations/edges/007-service-pod
kind: relation
subject: Service
predicate: selects
object: Pod
subject_entity: okf-relations/entities/service
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 718
  subject_hits: 9
  object_hits: 350
- source: concepts/workloads/controllers/job.md
  score: 705
  subject_hits: 4
  object_hits: 341
- source: concepts/services-networking/service.md
  score: 638
  subject_hits: 264
  object_hits: 52
source: concepts/workloads/pods/pod-lifecycle.md
word_count: 22
---

Service selects Pod. A Service finds the Pods it load-balances to via a label selector matched against Pod labels, not owner references.
