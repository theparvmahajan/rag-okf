---
id: okf-structure/concepts/policy/_index.md#apply-policies-using-kubelet-configurations
kind: section
title: Apply policies using Kubelet configurations
source: concepts/policy/_index.md
url: https://kubernetes.io/docs/concepts/policy/
heading: Apply policies using Kubelet configurations
parent: okf-structure/concepts/policy/_index
children: []
prev_sibling: okf-structure/concepts/policy/_index.md#apply-policies-using-dynamic-admission-control
next_sibling: null
word_count: 45
---

Kubernetes allows configuring the Kubelet on each worker node.  Some Kubelet configurations act as policies:
* Process ID limits and reservations are used to limit and reserve allocatable PIDs.
* Node Resource Managers can manage compute, memory, and device resources for latency-critical and high-throughput workloads.
