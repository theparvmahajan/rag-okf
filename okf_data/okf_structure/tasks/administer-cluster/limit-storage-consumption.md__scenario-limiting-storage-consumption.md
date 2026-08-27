---
id: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#scenario-limiting-storage-consumption
kind: section
title: 'Scenario: Limiting Storage Consumption'
source: tasks/administer-cluster/limit-storage-consumption.md
url: https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/
heading: 'Scenario: Limiting Storage Consumption'
parent: okf-structure/tasks/administer-cluster/limit-storage-consumption
children: []
prev_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#limitrange-to-limit-requests-for-storage
word_count: 66
---

The cluster-admin is operating a cluster on behalf of a user population and the admin wants to control
how much storage a single namespace can consume in order to control cost.

The admin would like to limit:

1. The number of persistent volume claims in a namespace
2. The amount of storage each claim can request
3. The amount of cumulative storage the namespace can have
