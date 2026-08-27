---
id: okf-relations/edges/028-namespace-service
kind: relation
subject: Namespace
predicate: scopes
object: Service
subject_entity: okf-relations/entities/namespace
object_entity: okf-relations/entities/service
grounding_sources:
- source: concepts/services-networking/service.md
  score: 665
  subject_hits: 7
  object_hits: 264
- source: concepts/policy/resource-quotas.md
  score: 538
  subject_hits: 94
  object_hits: 22
- source: concepts/services-networking/dns-pod-service.md
  score: 475
  subject_hits: 33
  object_hits: 32
source: concepts/services-networking/service.md
word_count: 23
---

Namespace scopes Service. A Service is namespaced; Pods in other Namespaces must use its qualified DNS name to reach it across the boundary.
