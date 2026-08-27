---
id: okf-structure/concepts/workloads/pods/advanced-pod-config.md#priorityclasses
kind: section
title: PriorityClasses
source: concepts/workloads/pods/advanced-pod-config.md
url: https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/
heading: PriorityClasses
parent: okf-structure/concepts/workloads/pods/advanced-pod-config
children: []
prev_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#runtimeclasses
word_count: 196
---

_PriorityClasses_ allow you to set the importance of Pods relative to other Pods.
If you assign a priority class to a Pod, Kubernetes sets the `.spec.priority` field for that Pod
based on the PriorityClass you specified (you cannot set `.spec.priority` directly).
If or when a Pod cannot be scheduled, and the problem is due to a lack of resources, the kube-scheduler
tries to preempt lower priority
Pods, in order to make scheduling of the higher priority Pod possible.

A PriorityClass is a cluster-scoped API object that maps a priority class name to an integer priority value. Higher numbers indicate higher priority.

### Defining a PriorityClass

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: high-priority
value: 10000
globalDefault: false
description: "Priority class for high-priority workloads"
```

### Specify pod priority using a PriorityClass

apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  priorityClassName: high-priority

### Built-in PriorityClasses

Kubernetes provides two built-in PriorityClasses:
- `system-cluster-critical`: For system components that are critical to the cluster
- `system-node-critical`: For system components that are critical to individual nodes. This is the highest priority that Pods can have in Kubernetes.

For more information, see Pod Priority and Preemption.
