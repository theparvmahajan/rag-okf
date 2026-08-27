---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#pods-are-not-accessible-via-their-service-ip
kind: section
title: Pods are not accessible via their Service IP
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: Pods are not accessible via their Service IP
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#hostport-services-do-not-work
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#tls-certificate-errors
word_count: 92
---

- Many network add-ons do not yet enable hairpin mode
  which allows pods to access themselves via their Service IP. This is an issue related to
  CNI. Please contact the network
  add-on provider to get the latest status of their support for hairpin mode.

- If you are using VirtualBox (directly or via Vagrant), you will need to
  ensure that `hostname -i` returns a routable IP address. By default, the first
  interface is connected to a non-routable host-only network. A work around
  is to modify `/etc/hosts`, see this
  Vagrantfile
  for an example.
