---
id: okf-structure/tasks/debug/debug-cluster/local-debugging.md#connecting-your-local-machine-to-a-remote-kubernetes-cluster
kind: section
title: Connecting your local machine to a remote Kubernetes cluster
source: tasks/debug/debug-cluster/local-debugging.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/local-debugging/
heading: Connecting your local machine to a remote Kubernetes cluster
parent: okf-structure/tasks/debug/debug-cluster/local-debugging
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#prerequisites
next_sibling: okf-structure/tasks/debug/debug-cluster/local-debugging.md#developing-or-debugging-an-existing-service
word_count: 46
---

After installing `telepresence`, run `telepresence connect` to launch
its Daemon and connect your local workstation to the cluster.

```
$ telepresence connect
 
Launching Telepresence Daemon
...
Connected to context default (https://<cluster public IP>)
```

You can curl services using the Kubernetes syntax e.g. `curl -ik https://kubernetes.default`
