---
id: okf-structure/tasks/job/parallel-processing-expansion.md#using-jobs-in-real-workloads
kind: section
title: Using Jobs in real workloads
source: tasks/job/parallel-processing-expansion.md
url: https://kubernetes.io/docs/tasks/job/parallel-processing-expansion/
heading: Using Jobs in real workloads
parent: okf-structure/tasks/job/parallel-processing-expansion
children: []
prev_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#use-advanced-template-parameters
next_sibling: okf-structure/tasks/job/parallel-processing-expansion.md#labels-on-jobs-and-pods
word_count: 140
---

In a real use case, each Job performs some substantial computation, such as rendering a frame
of a movie, or processing a range of rows in a database. If you were rendering a movie
you would set `$ITEM` to the frame number. If you were processing rows from a database
table, you would set `$ITEM` to represent the range of database rows to process.

In the task, you ran a command to collect the output from Pods by fetching
their logs. In a real use case, each Pod for a Job writes its output to
durable storage before completing. You can use a PersistentVolume for each Job,
or an external storage service. For example, if you are rendering frames for a movie,
use HTTP to `PUT` the rendered frame data to a URL, using a different URL for each
frame.
