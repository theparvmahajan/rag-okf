---
id: okf-structure/tasks/debug/debug-cluster/kubectl-node-debug.md#cleanup
kind: section
title: Cleanup
source: tasks/debug/debug-cluster/kubectl-node-debug.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/kubectl-node-debug/
heading: Cleanup
parent: okf-structure/tasks/debug/debug-cluster/kubectl-node-debug
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/kubectl-node-debug.md#debugging-a-node-using-kubectl-debug-node
next_sibling: null
word_count: 75
---

When you finish using the debugging Pod, delete it:

```shell
kubectl get pods
```

```none
NAME                          READY   STATUS       RESTARTS   AGE
node-debugger-mynode-pdx84    0/1     Completed    0          8m1s
```	

```shell
# Change the pod name accordingly
kubectl delete pod node-debugger-mynode-pdx84 --now
```	

```none
pod "node-debugger-mynode-pdx84" deleted
```

The `kubectl debug node` command won't work if the Node is down (disconnected
from the network, or kubelet dies and won't restart, etc.).
Check debugging a down/unreachable node 
in that case.
