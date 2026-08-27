---
id: okf-relations/edges/027-namespace-pod
kind: relation
subject: Namespace
predicate: scopes
object: Pod
subject_entity: okf-relations/entities/namespace
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 715
  subject_hits: 3
  object_hits: 350
- source: concepts/policy/resource-quotas.md
  score: 709
  subject_hits: 94
  object_hits: 115
- source: concepts/workloads/controllers/job.md
  score: 707
  subject_hits: 5
  object_hits: 341
source: concepts/workloads/pods/pod-lifecycle.md
word_count: 21
---

Namespace scopes Pod. A Pod exists inside exactly one Namespace, which isolates it (by name) from same-named objects in other Namespaces.
