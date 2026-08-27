---
id: okf-structure/concepts/workloads/pods/_index.md#whatsnext
kind: section
title: Whatsnext
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Whatsnext
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#container-probes
next_sibling: null
word_count: 151
---

* Learn about the lifecycle of a Pod.
* Read about PodDisruptionBudget
  and how you can use it to manage application availability during disruptions.
* Pod is a top-level resource in the Kubernetes REST API.
  The 
  object definition describes the object in detail.
* The Distributed System Toolkit: Patterns for Composite Containers explains common layouts for Pods with more than one container.
* Read about Pod topology spread constraints
* Read Advanced Pod Configuration to learn the topic in detail.
  That page covers aspects of Pod configuration beyond the essentials, including:
  * PriorityClasses
  * RuntimeClasses
  * advanced ways to configure _scheduling_: the way that Kubernetes decides which node a Pod should run on.

To understand the context for why Kubernetes wraps a common Pod API in other resources
(such as StatefulSets or
Deployments),
you can read about the prior art, including:

* Aurora
* Borg
* Marathon
* Omega
* Tupperware.
