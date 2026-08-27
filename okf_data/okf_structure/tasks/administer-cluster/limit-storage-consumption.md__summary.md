---
id: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#summary
kind: section
title: Summary
source: tasks/administer-cluster/limit-storage-consumption.md
url: https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/
heading: Summary
parent: okf-structure/tasks/administer-cluster/limit-storage-consumption
children: []
prev_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#resourcequota-to-limit-pvc-count-and-cumulative-storage-capacity
next_sibling: null
word_count: 53
---

A limit range can put a ceiling on how much storage is requested while a resource quota can effectively cap the storage
consumed by a namespace through claim counts and cumulative storage capacity. The allows a cluster-admin to plan their
cluster's storage budget without risk of any one project going over their allotment.
