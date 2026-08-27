---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#retrieve-the-qos-class-for-a-pod
kind: section
title: Retrieve the QoS class for a Pod
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: Retrieve the QoS class for a Pod
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-has-two-containers
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#clean-up
word_count: 27
---

Rather than see all the fields, you can view just the field you need:

```bash
kubectl --namespace=qos-example get pod qos-demo-4 -o jsonpath='{ .status.qosClass}{"\n"}'
```

```none
Burstable
```
