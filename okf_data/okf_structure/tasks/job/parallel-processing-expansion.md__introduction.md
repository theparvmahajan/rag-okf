---
id: okf-structure/tasks/job/parallel-processing-expansion.md#introduction
kind: section
title: Parallel Processing using Expansions
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: null
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#prerequisites
word_count: 64
---

This task demonstrates running multiple Jobs
based on a common template. You can use this approach to process batches of work in
parallel.

For this example there are only three items: _apple_, _banana_, and _cherry_.
The sample Jobs process each item by printing a string then pausing.

See using Jobs in real workloads to learn about how
this pattern fits more realistic use cases.
