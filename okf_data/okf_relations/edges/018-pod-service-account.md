---
id: okf-relations/edges/018-pod-service-account
kind: relation
subject: Pod
predicate: authenticates as
object: ServiceAccount
subject_entity: okf-relations/entities/pod
object_entity: okf-relations/entities/service-account
grounding_sources:
- source: tasks/configure-pod-container/configure-service-account.md
  score: 685
  subject_hits: 46
  object_hits: 73
- source: concepts/security/service-accounts.md
  score: 611
  subject_hits: 45
  object_hits: 58
- source: concepts/configuration/secret.md
  score: 409
  subject_hits: 61
  object_hits: 22
source: tasks/configure-pod-container/configure-service-account.md
word_count: 26
---

Pod authenticates as ServiceAccount. Every Pod runs under a ServiceAccount identity (default one if none is specified) used for API server authentication from inside the Pod.
