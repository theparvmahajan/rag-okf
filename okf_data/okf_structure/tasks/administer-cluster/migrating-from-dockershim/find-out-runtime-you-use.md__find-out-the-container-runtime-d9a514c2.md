---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#find-out-the-container-runtime-used-on-a-node
kind: section
title: Find out the container runtime used on a Node
source: tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/
heading: Find out the container runtime used on a Node
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use
children: []
prev_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#find-out-what-container-runtime-endpoint-you-use-which-endpoint
word_count: 134
---

Use `kubectl` to fetch and show node information:

```shell
kubectl get nodes -o wide
```

The output is similar to the following. The column `CONTAINER-RUNTIME` outputs
the runtime and its version.

For Docker Engine, the output is similar to this:

```none
NAME         STATUS   VERSION    CONTAINER-RUNTIME
node-1       Ready    v1.16.15   docker://19.3.1
node-2       Ready    v1.16.15   docker://19.3.1
node-3       Ready    v1.16.15   docker://19.3.1
```
If your runtime shows as Docker Engine, you still might not be affected by the
removal of dockershim in Kubernetes v1.24.
Check the runtime endpoint to see if you use dockershim.
If you don't use dockershim, you aren't affected. 

For containerd, the output is similar to this:

```none
NAME         STATUS   VERSION   CONTAINER-RUNTIME
node-1       Ready    v1.19.6   containerd://1.4.1
node-2       Ready    v1.19.6   containerd://1.4.1
node-3       Ready    v1.19.6   containerd://1.4.1
```

Find out more information about container runtimes
on Container Runtimes
page.
