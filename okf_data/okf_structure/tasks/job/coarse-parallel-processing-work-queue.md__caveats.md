---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#caveats
kind: section
title: Caveats
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Caveats
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#alternatives
next_sibling: null
word_count: 178
---

If the number of completions is set to less than the number of items in the queue, then
not all items will be processed.

If the number of completions is set to more than the number of items in the queue,
then the Job will not appear to be completed, even though all items in the queue
have been processed.  It will start additional pods which will block waiting
for a message.
You would need to make your own mechanism to spot when there is work
to do and measure the size of the queue, setting the number of completions to match.

There is an unlikely race with this pattern.  If the container is killed in between the time
that the message is acknowledged by the `amqp-consume` command and the time that the container
exits with success, or if the node crashes before the kubelet is able to post the success of the pod
back to the API server, then the Job will not appear to be complete, even though all items
in the queue have been processed.
