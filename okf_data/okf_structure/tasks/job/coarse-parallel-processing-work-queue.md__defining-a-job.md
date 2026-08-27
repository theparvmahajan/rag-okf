---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#defining-a-job
kind: section
title: Defining a Job
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Defining a Job
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#create-a-container-image
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#running-the-job
word_count: 75
---

Here is a manifest for a Job.  You'll need to make a copy of the Job manifest
(call it `./job.yaml`),
and edit the name of the container image to match the name you used.

In this example, each pod works on one item from the queue and then exits.
So, the completion count of the Job corresponds to the number of work items
done. That is why the example manifest has `.spec.completions` set to `8`.
