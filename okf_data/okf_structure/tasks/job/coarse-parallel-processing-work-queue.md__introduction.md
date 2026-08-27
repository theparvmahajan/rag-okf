---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#introduction
kind: section
title: Coarse Parallel Processing Using a Work Queue
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: null
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#prerequisites
word_count: 149
---

In this example, you will run a Kubernetes Job with multiple parallel
worker processes.

In this example, as each pod is created, it picks up one unit of work
from a task queue, completes it, deletes it from the queue, and exits.

Here is an overview of the steps in this example:

1. **Start a message queue service.**  In this example, you use RabbitMQ, but you could use another
   one.  In practice you would set up a message queue service once and reuse it for many jobs.
1. **Create a queue, and fill it with messages.**  Each message represents one task to be done.  In
   this example, a message is an integer that we will do a lengthy computation on.
1. **Start a Job that works on tasks from the queue**.  The Job starts several pods.  Each pod takes
   one task from the message queue, processes it, and exits.
