---
id: okf-structure/concepts/containers/cri.md#list-streaming-list-streaming
kind: section
title: List streaming {#list-streaming}
source: concepts/containers/cri.md
url: https://kubernetes.io/docs/concepts/containers/cri/
heading: List streaming {#list-streaming}
parent: okf-structure/concepts/containers/cri
children: []
prev_sibling: okf-structure/concepts/containers/cri.md#upgrading
next_sibling: okf-structure/concepts/containers/cri.md#whatsnext
word_count: 131
---

The standard CRI list RPCs (`ListContainers`, `ListPodSandbox`, `ListImages`) return
all results in a single unary response. On nodes with a large number of containers
(for example, more than roughly 10,000 including both running and stopped), these
responses can exceed gRPC's default 16 MiB message size limit, causing the kubelet
to fail when reconciling state with the container runtime.

With the `CRIListStreaming` feature gate enabled, the kubelet uses server-side
streaming RPCs (such as `StreamContainers`, `StreamPodSandboxes`,
`StreamImages`) that allow the container runtime to divide results across
multiple response messages, bypassing the per-message size limit. This is
particularly useful for:

- High container churn environments (CI/CD systems)
- Large-scale batch processing workloads

If the container runtime does not support streaming RPCs, the kubelet
automatically falls back to the standard unary RPCs for backward
compatibility.
