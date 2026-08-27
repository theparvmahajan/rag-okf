---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#introduction
kind: section
title: Configure Quality of Service for Pods
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: null
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#prerequisites
word_count: 102
---

This page shows how to configure Pods so that they will be assigned particular
Quality of Service (QoS) classes.
Kubernetes uses QoS classes to make decisions about evicting Pods when Node resources are exceeded.

When Kubernetes creates a Pod it assigns one of these QoS classes to the Pod:

* Guaranteed
* Burstable
* BestEffort

Kubernetes assigns the QoS class when the Pod is created, and it remains unchanged
for the lifetime of the Pod. If you attempt to
resize the Pod's resources
to values that would result in a different QoS class, control plane rejects your request with an error message.
