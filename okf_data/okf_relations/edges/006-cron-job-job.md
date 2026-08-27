---
id: okf-relations/edges/006-cron-job-job
kind: relation
subject: CronJob
predicate: creates
object: Job
subject_entity: okf-relations/entities/cron-job
object_entity: okf-relations/entities/job
grounding_sources:
- source: concepts/workloads/controllers/job.md
  score: 1001
  subject_hits: 8
  object_hits: 464
- source: concepts/workloads/controllers/cron-jobs.md
  score: 707
  subject_hits: 57
  object_hits: 136
- source: tasks/extend-kubernetes/custom-resources/custom-resource-definitions.md
  score: 418
  subject_hits: 2
  object_hits: 3
source: concepts/workloads/controllers/job.md
word_count: 23
---

CronJob creates Job. A CronJob creates a new Job object on each scheduled trigger; the Job then owns its own Pods as usual.
