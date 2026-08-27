---
id: okf-structure/tasks/job/parallel-processing-expansion.md#labels-on-jobs-and-pods
kind: section
title: Labels on Jobs and Pods
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: Labels on Jobs and Pods
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#using-jobs-in-real-workloads
next_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#alternatives
word_count: 129
---

After you create a Job, Kubernetes automatically adds additional
labels that
distinguish one Job's pods from another Job's pods.

In this example, each Job and its Pod template have a label:
`jobgroup=jobexample`.

Kubernetes itself pays no attention to labels named `jobgroup`. Setting a label
for all the Jobs you create from a template makes it convenient to operate on all
those Jobs at once.
In the first example you used a template to
create several Jobs. The template ensures that each Pod also gets the same label, so
you can check on all Pods for these templated Jobs with a single command.

The label key `jobgroup` is not special or reserved.
You can pick your own labelling scheme.
There are recommended labels
that you can use if you wish.
