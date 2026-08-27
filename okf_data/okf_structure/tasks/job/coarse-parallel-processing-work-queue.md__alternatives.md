---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#alternatives
kind: section
title: Alternatives
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Alternatives
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#running-the-job
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#caveats
word_count: 173
---

This approach has the advantage that you do not need to modify your "worker" program to be
aware that there is a work queue. You can include the worker program unmodified in your container
image.

Using this approach does require that you run a message queue service.
If running a queue service is inconvenient, you may
want to consider one of the other job patterns.

This approach creates a pod for every work item.  If your work items only take a few seconds,
though, creating a Pod for every work item may add a lot of overhead.  Consider another
design, such as in the fine parallel work queue example,
that executes multiple work items per Pod.

In this example, you used the `amqp-consume` utility to read the message
from the queue and run the actual program.  This has the advantage that you
do not need to modify your program to be aware of the queue.
The fine parallel work queue example
shows how to communicate with the work queue using a client library.
