---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#drain-the-node
kind: section
title: Drain the node
source: tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/
heading: Drain the node
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#stop-the-docker-daemon
word_count: 17
---

```shell
kubectl drain <node-to-drain> --ignore-daemonsets
```

Replace `<node-to-drain>` with the name of your node you are draining.
