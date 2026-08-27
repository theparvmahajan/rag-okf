---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#example-1-resizing-cpu-without-restart
kind: section
title: 'Example 1: Resizing CPU without restart'
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: 'Example 1: Resizing CPU without restart'
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#create-a-namespace
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#example-2-resizing-memory-with-restart
word_count: 201
---

First, create a Pod designed for in-place CPU resize and restart-required memory resize.

Create the pod:

```shell
kubectl create -f pod-resize.yaml -n qos-example
```

This pod starts in the Guaranteed QoS class. Verify its initial state:

```shell
# Wait a moment for the pod to be running
kubectl get pod resize-demo --output=yaml -n qos-example
```

Observe the `spec.containers[0].resources` and `status.containerStatuses[0].resources`.
They should match the manifest (700m CPU, 200Mi memory). Note the `status.containerStatuses[0].restartCount` (should be 0).

Now, increase the CPU request and limit to `800m`. You use `kubectl patch` with the `--subresource resize` command line argument.

```shell
kubectl patch pod resize-demo -n qos-example --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"800m"}, "limits":{"cpu":"800m"}}}]}}'

# Alternative methods:
# kubectl -n qos-example edit pod resize-demo --subresource resize
# kubectl -n qos-example apply -f <updated-manifest> --subresource resize --server-side
```

The `--subresource resize` command line argument requires `kubectl` client version v1.32.0 or later.
Older versions will report an `invalid subresource` error.

Check the pod status again after patching:

```shell
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

You should see:
* `spec.containers[0].resources` now shows `cpu: 800m`.
* `status.containerStatuses[0].resources` also shows `cpu: 800m`, indicating the resize was successful on the node.
* `status.containerStatuses[0].restartCount` remains `0`, because the CPU `resizePolicy` was `NotRequired`.
