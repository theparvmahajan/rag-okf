---
id: okf-structure/concepts/configuration/manage-resources-containers.md#pod-resources-example-example-2
kind: section
title: Pod resources example {#example-2}
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: Pod resources example {#example-2}
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#container-resources-example-example-1
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#how-pods-with-resource-requests-are-scheduled
word_count: 72
---

This feature can be enabled by setting the `PodLevelResources` 
feature gate.
The following Pod has an explicit request of 1 CPU and 100 MiB of memory, and an
explicit limit of 1 CPU and 200 MiB of memory. The `pod-resources-demo-ctr-1`
container has explicit requests and limits set. However, the
`pod-resources-demo-ctr-2` container will simply share the resources available
within the Pod resource boundaries, as it does not have explicit requests and limits
set.
