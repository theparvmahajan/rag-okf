---
id: okf-relations/edges/023-resource-quota-namespace
kind: relation
subject: ResourceQuota
predicate: constrains
object: Namespace
subject_entity: okf-relations/entities/resource-quota
object_entity: okf-relations/entities/namespace
grounding_sources:
- source: concepts/policy/resource-quotas.md
  score: 1282
  subject_hits: 43
  object_hits: 94
- source: tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md
  score: 368
  subject_hits: 12
  object_hits: 28
- source: concepts/configuration/manage-resources-containers.md
  score: 355
  subject_hits: 4
  object_hits: 10
source: concepts/policy/resource-quotas.md
word_count: 22
---

ResourceQuota constrains Namespace. A ResourceQuota caps the total resources (CPU, memory, object counts) that can be consumed by everything inside one Namespace.
