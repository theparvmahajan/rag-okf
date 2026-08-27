---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#restart-the-kubelet
kind: section
title: Restart the kubelet
source: tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd/
heading: Restart the kubelet
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#configure-the-kubelet-to-use-containerd-as-its-container-runtime
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/change-runtime-containerd.md#verify-that-the-node-is-healthy
word_count: 5
---

```shell
systemctl start kubelet
```
