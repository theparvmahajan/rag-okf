---
id: okf-relations/edges/008-service-endpoint-slice
kind: relation
subject: Service
predicate: backed by
object: EndpointSlice
subject_entity: okf-relations/entities/service
object_entity: okf-relations/entities/endpoint-slice
grounding_sources:
- source: concepts/services-networking/service.md
  score: 716
  subject_hits: 264
  object_hits: 37
- source: concepts/services-networking/endpoint-slices.md
  score: 366
  subject_hits: 20
  object_hits: 64
- source: tasks/debug/debug-application/debug-service.md
  score: 188
  subject_hits: 79
  object_hits: 6
source: concepts/services-networking/service.md
word_count: 26
---

Service backed by EndpointSlice. The endpoints controller watches a Service's selector and keeps a matching EndpointSlice updated with the current set of Pod IPs and ports.
