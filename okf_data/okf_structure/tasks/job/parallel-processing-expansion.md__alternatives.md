---
id: okf-structure/tasks/job/parallel-processing-expansion.md#alternatives
kind: section
title: Alternatives
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: Alternatives
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#labels-on-jobs-and-pods
next_sibling: null
word_count: 125
---

If you plan to create a large number of Job objects, you may find that:

- Even using labels, managing so many Jobs is cumbersome.
- If you create many Jobs in a batch, you might place high load
  on the Kubernetes control plane. Alternatively, the Kubernetes API
  server could rate limit you, temporarily rejecting your requests with a 429 status.
- You are limited by a resource quota
  on Jobs: the API server permanently rejects some of your requests
  when you create a great deal of work in one batch.

There are other job patterns
that you can use to process large amounts of work without creating very many Job
objects.

You could also consider writing your own controller
to manage Job objects automatically.
