---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#introduction
kind: section
title: Fine Parallel Processing Using a Work Queue
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: null
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#prerequisites
word_count: 221
---

In this example, you will run a Kubernetes Job that runs multiple parallel
tasks as worker processes, each running as a separate Pod.

In this example, as each pod is created, it picks up one unit of work
from a task queue, processes it, and repeats until the end of the queue is reached.

Here is an overview of the steps in this example:

1. **Start a storage service to hold the work queue.**  In this example, you will use Redis to store
   work items.  In the previous example,
   you used RabbitMQ.  In this example, you will use Redis and a custom work-queue client library;
   this is because AMQP does not provide a good way for clients to
   detect when a finite-length work queue is empty.  In practice you would set up a store such
   as Redis once and reuse it for the work queues of many jobs, and other things.
1. **Create a queue, and fill it with messages.**  Each message represents one task to be done.  In
   this example, a message is an integer that we will do a lengthy computation on.
1. **Start a Job that works on tasks from the queue**.  The Job starts several pods.  Each pod takes
   one task from the message queue, processes it, and repeats until the end of the queue is reached.
