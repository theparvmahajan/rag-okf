---
id: okf-relations/edges/005-job-pod
kind: relation
subject: Job
predicate: owns
object: Pod
subject_entity: okf-relations/entities/job
object_entity: okf-relations/entities/pod
grounding_sources:
- source: concepts/workloads/controllers/job.md
  score: 1733
  subject_hits: 464
  object_hits: 341
- source: concepts/workloads/pods/pod-lifecycle.md
  score: 715
  subject_hits: 6
  object_hits: 350
- source: concepts/workloads/pods/_index.md
  score: 406
  subject_hits: 4
  object_hits: 199
source: concepts/workloads/controllers/job.md
word_count: 24
---

Job owns Pod. A Job creates one or more Pods and tracks them to completion, retrying failed Pods up to a configured backoff limit.
