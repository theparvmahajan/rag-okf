---
id: okf-structure/tasks/configure-pod-container/resize-container-resources.md#troubleshooting-infeasible-resize-request
kind: section
title: 'Troubleshooting: Infeasible resize request'
source: tasks/configure-pod-container/resize-container-resources.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/
heading: 'Troubleshooting: Infeasible resize request'
parent: okf-structure/tasks/configure-pod-container/resize-container-resources
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#example-2-resizing-memory-with-restart
next_sibling: okf-structure/tasks/configure-pod-container/resize-container-resources.md#clean-up
word_count: 159
---

Next, try requesting an unreasonable amount of CPU, such as 1000 full cores (written as `"1000"` instead of `"1000m"` for millicores), which likely exceeds node capacity.

```shell
# Attempt to patch with an excessively large CPU request
kubectl patch pod resize-demo -n qos-example --subresource resize --patch \
  '{"spec":{"containers":[{"name":"pause", "resources":{"requests":{"cpu":"1000"}, "limits":{"cpu":"1000"}}}]}}'
```

Query the Pod's details:

```shell
kubectl get pod resize-demo --output=yaml --namespace=qos-example
```

You'll see changes indicating the problem:

* The `spec.containers[0].resources` reflects the *desired* state (`cpu: "1000"`).
* A condition with `type: PodResizePending` and `reason: Infeasible` was added to the Pod.
* The condition's `message` will explain why (`Node didn't have enough capacity: cpu, requested: 800000, capacity: ...`)
* Crucially, `status.containerStatuses[0].resources` will *still show the previous values* (`cpu: 800m`, `memory: 300Mi`),
  because the infeasible resize was not applied by the Kubelet.
* The `restartCount` will not have changed due to this failed attempt.

To fix this, you would need to patch the pod again with feasible resource values.
