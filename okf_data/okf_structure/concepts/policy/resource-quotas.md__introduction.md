---
id: okf-structure/concepts/policy/resource-quotas.md#introduction
kind: section
title: Resource Quotas
source: concepts/policy/resource-quotas.md
url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
heading: null
parent: okf-structure/concepts/policy/resource-quotas
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/policy/resource-quotas.md#how-kubernetes-resourcequotas-work
word_count: 108
---

When several users or teams share a cluster with a fixed number of nodes,
there is a concern that one team could use more than its fair share of resources.

_Resource quotas_ are a tool for administrators to address this concern.

A resource quota, defined by a ResourceQuota object, provides constraints that limit
aggregate resource consumption per namespace. A ResourceQuota can also
limit the quantity of objects that can be created in a namespace by API kind, as well as the total
amount of infrastructure resources that may be consumed by
API objects found in that namespace.

Neither contention nor changes to quota will affect already created resources.
