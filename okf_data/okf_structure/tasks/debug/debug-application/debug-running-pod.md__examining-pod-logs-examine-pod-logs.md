---
id: okf-structure/tasks/debug/debug-application/debug-running-pod.md#examining-pod-logs-examine-pod-logs
kind: section
title: Examining pod logs {#examine-pod-logs}
source: tasks/debug/debug-application/debug-running-pod.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
heading: Examining pod logs {#examine-pod-logs}
parent: okf-structure/tasks/debug/debug-application/debug-running-pod
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#example-debugging-pending-pods
next_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-with-container-exec-container-exec
word_count: 39
---

First, look at the logs of the affected container:

```shell
kubectl logs ${POD_NAME} -c ${CONTAINER_NAME}
```

If your container has previously crashed, you can access the previous container's crash log with:

```shell
kubectl logs ${POD_NAME} -c ${CONTAINER_NAME} --previous
```
