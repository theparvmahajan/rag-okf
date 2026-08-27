---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#verify-that-the-node-is-healthy
kind: section
title: Verify that the node is healthy
source: tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/
heading: Verify that the node is healthy
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#restart-the-kubelet
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#remove-docker-engine
word_count: 18
---

Run `kubectl get nodes -o wide` and containerd appears as the runtime for the node we just changed.
