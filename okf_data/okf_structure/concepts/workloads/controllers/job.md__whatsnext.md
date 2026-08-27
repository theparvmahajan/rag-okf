---
id: okf-structure/concepts/workloads/controllers/job.md#whatsnext
kind: section
title: Whatsnext
source: concepts/workloads/controllers/job.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/job/
heading: Whatsnext
parent: okf-structure/concepts/workloads/controllers/job
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/job.md#alternatives
next_sibling: null
word_count: 183
---

* Learn about Pods.
* Read about different ways of running Jobs:
  * Coarse Parallel Processing Using a Work Queue
  * Fine Parallel Processing Using a Work Queue
  * Use an indexed Job for parallel processing with static work assignment
  * Create multiple Jobs based on a template: Parallel Processing using Expansions
* Follow the links within Clean up finished jobs automatically
  to learn more about how your cluster can clean up completed and / or failed tasks.
* `Job` is part of the Kubernetes REST API.
  Read the 
  object definition to understand the API for jobs.
* Read about `CronJob`, which you
  can use to define a series of Jobs that will run based on a schedule, similar to
  the UNIX tool `cron`.
* Practice how to configure handling of retriable and non-retriable pod failures
  using `podFailurePolicy`, based on the step-by-step examples.
* Learn about gang scheduling
  for all-or-nothing scheduling of parallel Jobs.

[Indexed Job with Static Work Assignment]: /docs/tasks/job/indexed-parallel-processing-static/
[Job Template Expansion]: /docs/tasks/job/parallel-processing-expansion/
[Job with Pod-to-Pod Communication]: /docs/tasks/job/job-with-pod-to-pod-communication/
[Queue with Pod Per Work Item]: /docs/tasks/job/coarse-parallel-processing-work-queue/
[Queue with Variable Pod Count]: /docs/tasks/job/fine-parallel-processing-work-queue/
