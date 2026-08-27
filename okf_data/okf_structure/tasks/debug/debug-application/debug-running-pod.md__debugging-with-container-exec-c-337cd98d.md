---
id: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-with-container-exec-container-exec
kind: section
title: Debugging with container exec {#container-exec}
source: tasks/debug/debug-application/debug-running-pod.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
heading: Debugging with container exec {#container-exec}
parent: okf-structure/tasks/debug/debug-application/debug-running-pod
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#examining-pod-logs-examine-pod-logs
next_sibling: okf-structure/tasks/debug/debug-application/debug-running-pod.md#debugging-with-an-ephemeral-debug-container-ephemeral-container
word_count: 125
---

If the container image includes
debugging utilities, as is the case with images built from Linux and Windows OS
base images, you can run commands inside a specific container with
`kubectl exec`:

```shell
kubectl exec ${POD_NAME} -c ${CONTAINER_NAME} -- ${CMD} ${ARG1} ${ARG2} ... ${ARGN}
```

`-c ${CONTAINER_NAME}` is optional. You can omit it for Pods that only contain a single container.

As an example, to look at the logs from a running Cassandra pod, you might run

```shell
kubectl exec cassandra -- cat /var/log/cassandra/system.log
```

You can run a shell that's connected to your terminal using the `-i` and `-t`
arguments to `kubectl exec`, for example:

```shell
kubectl exec -it cassandra -- sh
```

For more details, see Get a Shell to a Running Container.
