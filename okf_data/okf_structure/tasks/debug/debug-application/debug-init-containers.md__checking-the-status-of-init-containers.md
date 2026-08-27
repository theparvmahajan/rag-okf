---
id: okf-structure/tasks/debug/debug-application/debug-init-containers.md#checking-the-status-of-init-containers
kind: section
title: Checking the status of Init Containers
source: tasks/debug/debug-application/debug-init-containers.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-init-containers/
heading: Checking the status of Init Containers
parent: okf-structure/tasks/debug/debug-application/debug-init-containers
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#prerequisites
next_sibling: okf-structure/tasks/debug/debug-application/debug-init-containers.md#getting-details-about-init-containers
word_count: 53
---

Display the status of your pod:

```shell
kubectl get pod <pod-name>
```

For example, a status of `Init:1/2` indicates that one of two Init Containers
has completed successfully:

```
NAME         READY     STATUS     RESTARTS   AGE
<pod-name>   0/1       Init:1/2   0          7s
```

See Understanding Pod status for more examples of
status values and their meanings.
