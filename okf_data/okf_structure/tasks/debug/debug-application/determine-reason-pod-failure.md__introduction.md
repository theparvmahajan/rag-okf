---
id: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#introduction
kind: section
title: Determine the Reason for Pod Failure
source: tasks/debug/debug-application/determine-reason-pod-failure.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/
heading: null
parent: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-application/determine-reason-pod-failure.md#prerequisites
word_count: 63
---

This page shows how to write and read a Container termination message.

Termination messages provide a way for containers to write
information about fatal events to a location where it can
be easily retrieved and surfaced by tools like dashboards
and monitoring software. In most cases, information that you
put in a termination message should also be written to
the general
Kubernetes logs.
