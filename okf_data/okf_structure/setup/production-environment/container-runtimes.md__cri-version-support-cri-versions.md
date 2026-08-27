---
id: okf-structure/setup/production-environment/container-runtimes.md#cri-version-support-cri-versions
kind: section
title: CRI version support {#cri-versions}
source: setup/production-environment/container-runtimes.md
url: https://kubernetes.io/docs/setup/production-environment/container-runtimes/
heading: CRI version support {#cri-versions}
parent: okf-structure/setup/production-environment/container-runtimes
children: []
prev_sibling: okf-structure/setup/production-environment/container-runtimes.md#cgroup-drivers
next_sibling: okf-structure/setup/production-environment/container-runtimes.md#container-runtimes
word_count: 40
---

Your container runtime must support v1 of the container runtime interface.

Kubernetes starting v1.26
_only works_ with v1 of the CRI API. If a container runtime does not support the v1 API,
the kubelet will not register as a node.
