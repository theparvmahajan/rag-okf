---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#alternatives
kind: section
title: Alternatives
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Alternatives
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#running-the-job
next_sibling: null
word_count: 59
---

If running a queue service or modifying your containers to use a work queue is inconvenient, you may
want to consider one of the other
job patterns.

If you have a continuous stream of background processing work to run, then
consider running your background workers with a ReplicaSet instead,
and consider running a background processing library such as
https://github.com/resque/resque.
