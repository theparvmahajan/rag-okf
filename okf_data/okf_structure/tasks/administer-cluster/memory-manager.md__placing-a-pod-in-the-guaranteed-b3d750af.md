---
id: okf-structure/tasks/administer-cluster/memory-manager.md#placing-a-pod-in-the-guaranteed-qos-class
kind: section
title: Placing a Pod in the Guaranteed QoS class
source: tasks/administer-cluster/memory-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/memory-manager/
heading: Placing a Pod in the Guaranteed QoS class
parent: okf-structure/tasks/administer-cluster/memory-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#reserved-memory-configuration-reserved-memory-flag
next_sibling: okf-structure/tasks/administer-cluster/memory-manager.md#whatsnext
word_count: 172
---

If the selected policy is anything other than `None`, the Memory Manager identifies pods
that are in the `Guaranteed` QoS class.
The Memory Manager provides specific topology hints to the Topology Manager for each `Guaranteed` pod.
For pods in a QoS class other than `Guaranteed`, the Memory Manager provides default topology hints
to the Topology Manager.

The following excerpts from pod manifests assign a pod to the `Guaranteed` QoS class.

A Pod with integer CPU(s) runs in the `Guaranteed` QoS class, when `requests` are equal to `limits`:

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      limits:
        memory: "200Mi"
        cpu: "2"
        example.com/device: "1"
      requests:
        memory: "200Mi"
        cpu: "2"
        example.com/device: "1"
```

Also, a pod sharing CPU(s) runs in the `Guaranteed` QoS class, when `requests` are equal to `limits`.

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      limits:
        memory: "200Mi"
        cpu: "300m"
        example.com/device: "1"
      requests:
        memory: "200Mi"
        cpu: "300m"
        example.com/device: "1"
```

Notice that both CPU and memory requests must be specified for a Pod to lend it to Guaranteed QoS class.
