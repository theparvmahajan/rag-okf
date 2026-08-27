---
id: okf-structure/tasks/job/indexed-parallel-processing-static.md#introduction
kind: section
title: Indexed Job for Parallel Processing with Static Work Assignment
source: tasks/job/indexed-parallel-processing-static.md
url: https://kubernetes.io/docs/tasks/job/indexed-parallel-processing-static/
heading: null
parent: okf-structure/tasks/job/indexed-parallel-processing-static
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/job/indexed-parallel-processing-static.md#prerequisites
word_count: 159
---

In this example, you will run a Kubernetes Job that uses multiple parallel
worker processes.
Each worker is a different container running in its own Pod. The Pods have an
_index number_ that the control plane sets automatically, which allows each Pod
to identify which part of the overall task to work on.

The pod index is available in the annotation
`batch.kubernetes.io/job-completion-index` as a string representing its
decimal value. In order for the containerized task process to obtain this index,
you can publish the value of the annotation using the downward API
mechanism.
For convenience, the control plane automatically sets the downward API to
expose the index in the `JOB_COMPLETION_INDEX` environment variable.

Here is an overview of the steps in this example:

1. **Define a Job manifest using indexed completion**.
   The downward API allows you to pass the pod index annotation as an
   environment variable or file to the container.
2. **Start an `Indexed` Job based on that manifest**.
