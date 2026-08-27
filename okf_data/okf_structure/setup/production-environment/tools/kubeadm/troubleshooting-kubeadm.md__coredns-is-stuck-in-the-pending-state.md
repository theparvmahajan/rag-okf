---
id: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#coredns-is-stuck-in-the-pending-state
kind: section
title: '`coredns` is stuck in the `Pending` state'
source: setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
heading: '`coredns` is stuck in the `Pending` state'
parent: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm
children: []
prev_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#pods-in-runcontainererror-crashloopbackoff-or-error-state
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm.md#hostport-services-do-not-work
word_count: 46
---

This is **expected** and part of the design. kubeadm is network provider-agnostic, so the admin
should install the pod network add-on
of choice. You have to install a Pod Network
before CoreDNS may be deployed fully. Hence the `Pending` state before the network is set up.
