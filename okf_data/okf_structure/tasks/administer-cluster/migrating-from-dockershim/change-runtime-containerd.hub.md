---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd
kind: hub
title: Changing the Container Runtime on a Node from Docker Engine to containerd
source: tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/
heading: null
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim
children:
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#introduction
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#prerequisites
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#drain-the-node
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#stop-the-docker-daemon
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#install-containerd
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#configure-the-kubelet-to-use-containerd-as-its-container-runtime
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#restart-the-kubelet
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#verify-that-the-node-is-healthy
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#remove-docker-engine
- okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#uncordon-the-node
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/_index
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/check-if-dockershim-removal-affects-you
word_count: 494
---


