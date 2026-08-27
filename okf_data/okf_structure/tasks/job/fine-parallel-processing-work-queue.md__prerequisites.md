---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#prerequisites
kind: section
title: Prerequisites
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Prerequisites
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#introduction
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#starting-redis
word_count: 60
---

You will need a container image registry where you can upload images to run in your cluster.
The example uses Docker Hub, but you could adapt it to a different
container image registry.

This task example also assumes that you have Docker installed locally. You use Docker to
build container images.

Be familiar with the basic,
non-parallel, use of Job.
