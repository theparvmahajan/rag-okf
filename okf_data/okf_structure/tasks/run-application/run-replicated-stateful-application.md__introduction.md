---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#introduction
kind: section
title: Run a Replicated Stateful Application
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: null
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#prerequisites
word_count: 60
---

This page shows how to run a replicated stateful application using a
statefulset.
This application is a replicated MySQL database. The example topology has a
single primary server and multiple replicas, using asynchronous row-based
replication.

**This is not a production configuration**. MySQL settings remain on insecure defaults to keep the focus
on general patterns for running stateful applications in Kubernetes.
