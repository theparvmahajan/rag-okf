---
id: okf-structure/concepts/workloads/pods/_index.md#container-probes
kind: section
title: Container probes
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Container probes
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#pods-with-multiple-containers-how-pods-manage-multiple-containers
next_sibling: okf-structure/concepts/workloads/pods/_index.md#whatsnext
word_count: 58
---

A _probe_ is a diagnostic performed periodically by the kubelet on a container.
To perform a diagnostic, the kubelet can invoke different actions:

- `ExecAction` (performed with the help of the container runtime)
- `TCPSocketAction` (checked directly by the kubelet)
- `HTTPGetAction` (checked directly by the kubelet)

You can read more about probes
in the Pod Lifecycle documentation.
