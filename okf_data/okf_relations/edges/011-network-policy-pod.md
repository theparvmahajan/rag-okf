---
id: okf-relations/edges/011-network-policy-pod
kind: relation
subject: NetworkPolicy
predicate: selects
object: Pod
subject_entity: okf-relations/entities/network-policy
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/services-networking/network-policies.md
  score: 676
  subject_hits: 57
  object_hits: 125
- source: concepts/security/multi-tenancy.md
  score: 87
  subject_hits: 1
  object_hits: 41
- source: concepts/services-networking/_index.md
  score: 69
  subject_hits: 4
  object_hits: 26
source: concepts/services-networking/network-policies.md
word_count: 22
---

NetworkPolicy selects Pod. A NetworkPolicy applies to the Pods matched by its pod selector, restricting the ingress/egress traffic those Pods are allowed.
