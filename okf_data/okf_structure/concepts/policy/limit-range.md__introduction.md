---
id: okf-structure/concepts/policy/limit-range.md#introduction
kind: section
title: Limit Ranges
source: concepts/policy/limit-range.md
url: https://kubernetes.io/docs/concepts/policy/limit-range/
heading: null
parent: okf-structure/concepts/policy/limit-range
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/policy/limit-range.md#constraints-on-resource-limits-and-requests
word_count: 222
---

By default, containers run with unbounded
compute resources on a Kubernetes cluster.
Using  Kubernetes resource quotas,
administrators (also termed _cluster operators_) can restrict consumption and creation
of cluster resources (such as CPU time, memory, and persistent storage) within a specified
namespace.
Within a namespace, a Pod can consume as much CPU and memory as is allowed by the ResourceQuotas that apply to that namespace.
As a cluster operator, or as a namespace-level administrator, you might also be concerned
about making sure that a single object cannot monopolize all available resources within a namespace.

A LimitRange is a policy to constrain the resource allocations (limits and requests) that you can specify for
each applicable object kind (such as Pod or PersistentVolumeClaim) in a namespace.

A _LimitRange_ provides constraints that can:

- Enforce minimum and maximum compute resources usage per Pod or Container in a namespace.
- Enforce minimum and maximum storage request per
  PersistentVolumeClaim in a namespace.
- Enforce a ratio between request and limit for a resource in a namespace.
- Set default request/limit for compute resources in a namespace and automatically
  inject them to Containers at runtime.

Kubernetes constrains resource allocations to Pods in a particular namespace
whenever there is at least one LimitRange object in that namespace.

The name of a LimitRange object must be a valid
DNS subdomain name.
