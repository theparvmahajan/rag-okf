---
id: okf-structure/concepts/workloads/pods/pod-qos.md#introduction
kind: section
title: Pod Quality of Service Classes
source: concepts/workloads/pods/pod-qos.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
heading: null
parent: okf-structure/concepts/workloads/pods/pod-qos
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#quality-of-service-classes
word_count: 60
---

This page introduces _Quality of Service (QoS) classes_ in Kubernetes, and explains
how Kubernetes assigns a QoS class to each Pod as a consequence of the resource
constraints that you specify for the containers in that Pod. Kubernetes relies on this
classification to make decisions about which Pods to evict when there are not enough
available resources on a Node.
