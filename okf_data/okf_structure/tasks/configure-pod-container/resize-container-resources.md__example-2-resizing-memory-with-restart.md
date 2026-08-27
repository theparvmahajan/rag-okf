---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#example-2-resizing-memory-with-restart
kind: section
title: 'Example 2: Resizing memory with restart'
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: 'Example 2: Resizing memory with restart'
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#example-1-resizing-cpu-without-restart
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#troubleshooting-infeasible-resize-request
word_count: 92
---

Now, resize the memory for the *same* pod by increasing it to `300Mi`.
Since the memory `resizePolicy` is `RestartContainer`, the container is expected to restart.

```shell
kubectl patch pod resize-demo -n qos-example --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"memory":"300Mi"}, "limits":{"memory":"300Mi"}}}]}}'
```

Check the pod status shortly after patching:

```shell
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

You should now observe:
* `spec.containers[0].resources` shows `memory: 300Mi`.
* `status.containerStatuses[0].resources` also shows `memory: 300Mi`.
* `status.containerStatuses[0].restartCount` has increased to `1` (or more, if restarts happened previously),
  indicating the container was restarted to apply the memory change.
