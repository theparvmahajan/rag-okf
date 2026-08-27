---
id: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#verify-the-mac-address-and-productuuid-are-unique-for-every-node-verify-mac-address
kind: section
title: Verify the MAC address and product_uuid are unique for every node {#verify-mac-address}
source: setup/production-environment/tools/kubeadm/install-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
heading: Verify the MAC address and product_uuid are unique for every node {#verify-mac-address}
parent: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-your-os-version
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/install-kubeadm.md#check-network-adapters
word_count: 77
---

* You can get the MAC address of the network interfaces using the command `ip link` or `ifconfig -a`
* The product_uuid can be checked by using the command `sudo cat /sys/class/dmi/id/product_uuid`

It is very likely that hardware devices will have unique addresses, although some virtual machines may have
identical values. Kubernetes uses these values to uniquely identify the nodes in the cluster.
If these values are not unique to each node, the installation process
may fail.
