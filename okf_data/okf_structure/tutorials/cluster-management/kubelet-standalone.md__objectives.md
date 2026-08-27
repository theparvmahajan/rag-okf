---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#objectives
kind: section
title: Objectives
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: Objectives
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#introduction
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#prerequisites
word_count: 66
---

* Install `cri-o`, and `kubelet` on a Linux system and run them as `systemd` services.
* Launch a Pod running `nginx` that listens to requests on TCP port 80 on the Pod's IP address.
* Learn how the different components of the solution interact among themselves.

The kubelet configuration used for this tutorial is insecure by design and should
_not_ be used in a production environment.
