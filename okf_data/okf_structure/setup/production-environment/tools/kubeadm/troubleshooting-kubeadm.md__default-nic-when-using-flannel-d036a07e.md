---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#default-nic-when-using-flannel-as-the-pod-network-in-vagrant
kind: section
title: Default NIC When using flannel as the pod network in Vagrant
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: Default NIC When using flannel as the pod network in Vagrant
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#kubelet-client-certificate-rotation-fails-kubelet-client-cert
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#non-public-ip-used-for-containers
word_count: 123
---

The following error might indicate that something was wrong in the pod network:

```sh
Error from server (NotFound): the server could not find the requested resource
```

- If you're using flannel as the pod network inside Vagrant, then you will have to
  specify the default interface name for flannel.

  Vagrant typically assigns two interfaces to all VMs. The first, for which all hosts
  are assigned the IP address `10.0.2.15`, is for external traffic that gets NATed.

  This may lead to problems with flannel, which defaults to the first interface on a host.
  This leads to all hosts thinking they have the same public IP address. To prevent this,
  pass the `--iface eth1` flag to flannel so that the second interface is chosen.
