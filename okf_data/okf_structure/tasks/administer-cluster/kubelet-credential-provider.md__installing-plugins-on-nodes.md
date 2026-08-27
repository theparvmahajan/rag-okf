---
id: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#installing-plugins-on-nodes
kind: section
title: Installing Plugins on Nodes
source: tasks/administer-cluster/kubelet-credential-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-credential-provider/
heading: Installing Plugins on Nodes
parent: okf-structure/tasks/administer-cluster/kubelet-credential-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kubelet-credential-provider.md#configuring-the-kubelet
word_count: 43
---

A credential provider plugin is an executable binary that will be run by the kubelet. Ensure that the plugin binary exists on
every node in your cluster and stored in a known directory. The directory will be required later when configuring kubelet flags.
