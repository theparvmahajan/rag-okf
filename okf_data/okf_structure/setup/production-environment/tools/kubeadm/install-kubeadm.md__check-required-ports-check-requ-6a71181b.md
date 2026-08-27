---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-required-ports-check-required-ports
kind: section
title: Check required ports {#check-required-ports}
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Check required ports {#check-required-ports}
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-network-adapters
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#swap-configuration-swap-configuration
word_count: 74
---

These required ports
need to be open in order for Kubernetes components to communicate with each other.
You can use tools like netcat to check if a port is open. For example:

```shell
nc 127.0.0.1 6443 -zv -w 2
```

The pod network plugin you use may also require certain ports to be
open. Since this differs with each pod network plugin, please see the
documentation for the plugins about what port(s) those need.
