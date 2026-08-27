---
id: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#example-scenario
kind: section
title: Example Scenario
source: tasks/administer-cluster/reserve-compute-resources.md
url: https://kubernetes.io/docs/tasks/administer-cluster/reserve-compute-resources/
heading: Example Scenario
parent: okf-structure/tasks/administer-cluster/reserve-compute-resources
children: []
prev_sibling: okf-structure/tasks/administer-cluster/reserve-compute-resources.md#general-guidelines
next_sibling: null
word_count: 162
---

Here is an example to illustrate Node Allocatable computation:

* Node has `32Gi` of `memory`, `16 CPUs` and `100Gi` of `Storage`
* `kubeReserved` is set to `{cpu: 1000m, memory: 2Gi, ephemeral-storage: 1Gi}`
* `systemReserved` is set to `{cpu: 500m, memory: 1Gi, ephemeral-storage: 1Gi}`
* `evictionHard` is set to `{memory.available: "<500Mi", nodefs.available: "<10%"}`

Under this scenario, 'Allocatable' will be 14.5 CPUs, 28.5Gi of memory and
`88Gi` of local storage.
Scheduler ensures that the total memory `requests` across all pods on this node does
not exceed 28.5Gi and storage doesn't exceed 88Gi.
Kubelet evicts pods whenever the overall memory usage across pods exceeds 28.5Gi,
or if overall disk usage exceeds 88Gi. If all processes on the node consume as
much CPU as they can, pods together cannot consume more than 14.5 CPUs.

If `kubeReserved` and/or `systemReserved` is not enforced and system daemons
exceed their reservation, `kubelet` evicts pods whenever the overall node memory
usage is higher than 31.5Gi or `storage` is greater than 90Gi.
