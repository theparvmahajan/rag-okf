---
id: okf-structure/concepts/configuration/manage-resources-containers.md#how-pods-with-resource-requests-are-scheduled
kind: section
title: How Pods with resource requests are scheduled
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: How Pods with resource requests are scheduled
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#pod-resources-example-example-2
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#how-kubernetes-applies-resource-requests-and-limits-how-pods-with-resource-limits-are-run
word_count: 119
---

When you create a Pod, the Kubernetes scheduler selects a node for the Pod to
run on. Each node has a maximum capacity for each of the resource types: the
amount of CPU and memory it can provide for Pods. The scheduler ensures that,
for each resource type, the sum of the resource requests of the scheduled
containers is less than the capacity of the node.
Note that although actual memory
or CPU resource usage on nodes is very low, the scheduler still refuses to place
a Pod on a node if the capacity check fails. This protects against a resource
shortage on a node when resource usage later increases, for example, during a
daily peak in request rate.
