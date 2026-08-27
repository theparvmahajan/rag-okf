---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#hostport-services-do-not-work
kind: section
title: '`HostPort` services do not work'
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: '`HostPort` services do not work'
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#coredns-is-stuck-in-the-pending-state
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#pods-are-not-accessible-via-their-service-ip
word_count: 75
---

The `HostPort` and `HostIP` functionality is available depending on your Pod Network
provider. Please contact the author of the Pod Network add-on to find out whether
`HostPort` and `HostIP` functionality are available.

Calico, Canal, and Flannel CNI providers are verified to support HostPort.

For more information, see the
CNI portmap documentation.

If your network provider does not support the portmap CNI plugin, you may need to use the
NodePort feature of services
or use `HostNetwork=true`.
