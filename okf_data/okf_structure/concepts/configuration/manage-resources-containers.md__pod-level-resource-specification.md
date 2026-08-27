---
id: okf-structure/concepts/configuration/manage-resources-containers.md#pod-level-resource-specification
kind: section
title: Pod-level resource specification
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: Pod-level resource specification
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#resource-requests-and-limits-of-pod-and-container
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#resource-units-in-kubernetes
word_count: 129
---

Provided your cluster has the `PodLevelResources`
feature gate enabled,
you can specify resource requests and limits at
the Pod level. At the Pod level, Kubernetes 
only supports resource requests or limits for specific resource types: `cpu` and /
or `memory` and / or `hugepages`. With this feature, Kubernetes allows you to declare an overall resource
budget for the Pod, which is especially helpful when dealing with a large number of
containers where it can be difficult to accurately gauge individual resource needs.
Additionally, it enables containers within a Pod to share idle resources with each
other, improving resource utilization.

For a Pod, you can specify resource limits and requests for CPU and memory by including the following:
* `spec.resources.limits.cpu`
* `spec.resources.limits.memory`
* `spec.resources.limits.hugepages-<size>`
* `spec.resources.requests.cpu`
* `spec.resources.requests.memory`
* `spec.resources.requests.hugepages-<size>`
