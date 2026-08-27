---
id: okf-relations/edges/009-ingress-service
kind: relation
subject: Ingress
predicate: routes to
object: Service
subject_entity: okf-relations/entities/ingress
object_entity: okf-relations/entities/service
grounding_sources:
- source: concepts/services-networking/ingress.md
  score: 746
  subject_hits: 151
  object_hits: 42
- source: concepts/services-networking/service.md
  score: 636
  subject_hits: 12
  object_hits: 264
- source: tasks/debug/debug-application/debug-service.md
  score: 405
  subject_hits: 2
  object_hits: 79
source: concepts/services-networking/ingress.md
word_count: 22
---

Ingress routes to Service. An Ingress defines host/path rules that an ingress controller uses to forward external traffic to a named Service.
