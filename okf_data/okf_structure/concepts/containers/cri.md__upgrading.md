---
id: okf-structure/concepts/containers/cri.md#upgrading
kind: section
title: Upgrading
source: concepts/containers/cri.md
url: https://kubernetes.io/docs/concepts/containers/cri/
heading: Upgrading
parent: okf-structure/concepts/containers/cri
children: []
prev_sibling: okf-structure/concepts/containers/cri.md#the-api-api
next_sibling: okf-structure/concepts/containers/cri.md#list-streaming-list-streaming
word_count: 73
---

When upgrading the Kubernetes version on a node, the kubelet restarts. If the
container runtime does not support the `v1` CRI API, the kubelet will fail to
register and report an error. If a gRPC re-dial is required because the container
runtime has been upgraded, the runtime must support the `v1` CRI API for the
connection to succeed. This might require a restart of the kubelet after the
container runtime is correctly configured.
