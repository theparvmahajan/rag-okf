---
id: okf-structure/concepts/workloads/pods/pod-condition.md#introduction
kind: section
title: Pod Conditions
source: concepts/workloads/pods/pod-condition.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
heading: null
parent: okf-structure/concepts/workloads/pods/pod-condition
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#structure-of-a-pod-condition
word_count: 133
---

In Kubernetes, many objects have _conditions_. 
Conditions are markers for some aspect of the actual state of the thing the object represents.
Pods have conditions, and Kubernetes Pod conditions are an important aspect of how controllers
(and people doing troubleshooting) can understand the health of a Pod.

A Pod's phase provides a high-level
summary of where the Pod is in its lifecycle, but a single value cannot capture the full
picture. For example, a Pod may be in the `Running` phase but not yet ready to serve traffic.
Pod conditions complement the phase by tracking multiple aspects of the Pod's state
independently, such as whether it has been scheduled, whether its containers are ready,
whether a resize is in progress, or whether the Pod is about to be disrupted due to a
taint.
