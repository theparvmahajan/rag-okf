---
id: okf-relations/entities/job
kind: entity
title: Job
description: Runs Pods to completion for a finite task, retrying on failure up to
  a configured limit.
outgoing_relations:
- okf-relations/edges/005-job-pod
incoming_relations:
- okf-relations/edges/006-cron-job-job
primary_sources:
- concepts/workloads/controllers/cron-jobs.md
- concepts/workloads/controllers/job.md
source: concepts/workloads/controllers/cron-jobs.md
word_count: 23
---

Job: Runs Pods to completion for a finite task, retrying on failure up to a configured limit. Job owns Pod. CronJob creates Job.
