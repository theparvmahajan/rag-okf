---
id: okf-relations/edges/024-limit-range-namespace
kind: relation
subject: LimitRange
predicate: constrains
object: Namespace
subject_entity: okf-relations/entities/limit-range
object_entity: okf-relations/entities/namespace
grounding_sources:
- source: concepts/policy/resource-quotas.md
  score: 590
  subject_hits: 3
  object_hits: 94
- source: concepts/workloads/controllers/job.md
  score: 399
  subject_hits: 1
  object_hits: 5
- source: concepts/policy/limit-range.md
  score: 370
  subject_hits: 23
  object_hits: 33
source: concepts/policy/resource-quotas.md
word_count: 20
---

LimitRange constrains Namespace. A LimitRange sets default and min/max per-Pod or per-Container resource constraints for everything created in one Namespace.
