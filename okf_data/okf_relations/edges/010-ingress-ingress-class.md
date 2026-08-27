---
id: okf-relations/edges/010-ingress-ingress-class
kind: relation
subject: Ingress
predicate: implemented by
object: IngressClass
subject_entity: okf-relations/entities/ingress
object_entity: okf-relations/entities/ingress-class
grounding_sources:
- source: concepts/services-networking/ingress.md
  score: 613
  subject_hits: 151
  object_hits: 34
- source: concepts/services-networking/ingress-controllers.md
  score: 327
  subject_hits: 76
  object_hits: 8
- source: tasks/configure-pod-container/migrate-from-psp.md
  score: 46
  subject_hits: 1
  object_hits: 1
source: concepts/services-networking/ingress.md
word_count: 25
---

Ingress implemented by IngressClass. An Ingress references an IngressClass to say which controller implementation should handle it, since a cluster can run more than one.
