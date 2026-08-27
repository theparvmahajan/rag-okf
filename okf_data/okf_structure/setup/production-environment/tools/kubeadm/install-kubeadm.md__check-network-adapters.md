---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-network-adapters
kind: section
title: Check network adapters
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Check network adapters
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#verify-the-mac-address-and-productuuid-are-unique-for-every-node-verify-mac-address
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-required-ports-check-required-ports
word_count: 34
---

If you have more than one network adapter, and your Kubernetes components are not reachable on the default
route, we recommend you add IP route(s) so Kubernetes cluster addresses go via the appropriate adapter.
