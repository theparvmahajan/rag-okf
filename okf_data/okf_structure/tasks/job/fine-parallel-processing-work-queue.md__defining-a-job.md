---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#defining-a-job
kind: section
title: Defining a Job
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Defining a Job
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#create-a-container-image-create-an-image
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#running-the-job
word_count: 135
---

Here is a manifest for the Job you will create:

Be sure to edit the manifest to
change `gcr.io/myproject` to your own path.

In this example, each pod works on several items from the queue and then exits when there are no more items.
Since the workers themselves detect when the workqueue is empty, and the Job controller does not
know about the workqueue, it relies on the workers to signal when they are done working.
The workers signal that the queue is empty by exiting with success.  So, as soon as **any** worker
exits with success, the controller knows the work is done, and that the Pods will exit soon.
So, you need to leave the completion count of the Job unset. The job controller will wait for
the other pods to complete too.
