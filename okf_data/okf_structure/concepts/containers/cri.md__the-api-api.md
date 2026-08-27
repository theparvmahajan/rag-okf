---
id: okf-structure/concepts/containers/cri.md#the-api-api
kind: section
title: The API {#api}
source: concepts/containers/cri.md
url: https://kubernetes.io/docs/concepts/containers/cri/
heading: The API {#api}
parent: okf-structure/concepts/containers/cri
children: []
prev_sibling: okf-structure/concepts/containers/cri.md#introduction
next_sibling: okf-structure/concepts/containers/cri.md#upgrading
word_count: 77
---

The kubelet acts as a client when connecting to the container runtime via gRPC.
The runtime and image service endpoints have to be available in the container
runtime, which can be configured separately within the kubelet by using the
`--container-runtime-endpoint`
command line flag.

For Kubernetes v1.26 and later, the kubelet requires that the container runtime
supports the `v1` CRI API. If a container runtime does not support the `v1` API,
the kubelet will not register the node.
