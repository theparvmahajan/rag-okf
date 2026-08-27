---
id: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#example-resizing-pod-level-resources
kind: section
title: 'Example: Resizing Pod-Level Resources'
source: tasks/configure-pod-container/resize-pod-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
heading: 'Example: Resizing Pod-Level Resources'
parent: okf-structure/tasks/configure-pod-container/resize-pod-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#limitations
next_sibling: okf-structure/tasks/configure-pod-container/resize-pod-resources.md#clean-up
word_count: 325
---

First, create a Pod designed for in-place CPU resize and restart-required memory resize.

Create the pod:

```shell
kubectl create -f pod-level-resize.yaml
```

This pod starts in the Guaranteed QoS class as pod-level requests are equal to limits. Verify its initial state:

```shell
# Wait a moment for the pod to be running
kubectl get pod pod-level-resize-demo --output=yaml
```

Observe the `spec.resources`(200m CPU, 200Mi memory). Note the
`status.containerStatuses[0].restartCount` (should be 0) and
`status.containerStatuses[1].restartCount` (should be 0).

Now, increase the pod-level CPU request and limit to `300m`. You use `kubectl patch` with the `--subresource resize` command line argument.

```shell
kubectl patch pod pod-level-resize-demo --subresource resize --patch \
  '{"spec":{"resources":{"requests":{"cpu":"300m"}, "limits":{"cpu":"300m"}}}}'

# Alternative methods:
# kubectl edit pod pod-level-resize-demo --subresource resize
# kubectl apply -f <updated-manifest> --subresource resize --server-side
```

The `--subresource resize` command line argument requires `kubectl` client version v1.32.0 or later.
Older versions will report an `invalid subresource` error.

Check the pod status again after patching:

```shell
kubectl get pod pod-level-resize-demo --output=yaml
```

You should see:
* `spec.resources.requests` and `spec.resources.limits` now show `cpu: 300m`.
* `status.containerStatuses[0].restartCount` remains `0`, because the CPU
  `resizePolicy` was `NotRequired`.
* `status.containerStatuses[1].restartCount` increased to `1` indicating the
  container was restarted to apply the CPU change. The restart occurred in Container 1 despite the resize being applied at the Pod level, due to the intricate relationship between Pod-level limits and container-level policies. Because Container 1 did not specify an explicit CPU limit, its underlying resource configuration (For example, cgroups) implicitly adopted the Pod's overall CPU limit as its effective maximum consumption boundary. When the Pod-level CPU limit was patched from 200m to 300m, this action consequently changed the implicit limit enforced on Container 1. Since Container 1 had its resizePolicy explicitly set to RestartContainer for CPU, the `kubelet` was obligated to restart the container to correctly apply this change in the underlying resource enforcement mechanism, thus confirming that altering Pod-level limits can trigger container restart policies even when container limits are not directly defined.
