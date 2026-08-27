---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#introduction
kind: section
title: Reconfiguring a kubeadm cluster
source: tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-reconfigure/
heading: null
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-reconfigure.md#prerequisites
word_count: 61
---

kubeadm does not support automated ways of reconfiguring components that
were deployed on managed nodes. One way of automating this would be
by using a custom operator.

To modify the components configuration you must manually edit associated cluster
objects and files on disk.

This guide shows the correct sequence of steps that need to be performed
to achieve kubeadm cluster reconfiguration.
