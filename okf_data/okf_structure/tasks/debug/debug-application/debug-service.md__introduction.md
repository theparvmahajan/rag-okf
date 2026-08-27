---
id: okf-structure/tasks/debug/debug-application/debug-service.md#introduction
kind: section
title: Debug Services
source: tasks/debug/debug-application/debug-service.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
heading: null
parent: okf-structure/tasks/debug/debug-application/debug-service
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#running-commands-in-a-pod
word_count: 58
---

An issue that comes up rather frequently for new installations of Kubernetes is
that a Service is not working properly.  You've run your Pods through a
Deployment (or other workload controller) and created a Service, but you
get no response when you try to access it.  This document will hopefully help
you to figure out what's going wrong.
