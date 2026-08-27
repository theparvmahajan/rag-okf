---
id: okf-structure/concepts/policy/resource-quotas.md#quota-and-cluster-capacity
kind: section
title: Quota and Cluster Capacity
source: concepts/policy/resource-quotas.md
url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
heading: Quota and Cluster Capacity
parent: okf-structure/concepts/policy/resource-quotas
children: []
prev_sibling: okf-structure/concepts/policy/resource-quotas.md#viewing-and-setting-quotas
next_sibling: okf-structure/concepts/policy/resource-quotas.md#quota-scopes
word_count: 141
---

ResourceQuotas are independent of the cluster capacity. They are
expressed in absolute units. So, if you add nodes to your cluster, this does *not*
automatically give each namespace the ability to consume more resources.

Sometimes more complex policies may be desired, such as:

- Proportionally divide total cluster resources among several teams.
- Allow each tenant to grow resource usage as needed, but have a generous
  limit to prevent accidental resource exhaustion.
- Detect demand from one namespace, add nodes, and increase quota.

Such policies could be implemented using `ResourceQuotas` as building blocks, by
writing a "controller" that watches the quota usage and adjusts the quota
hard limits of each namespace according to other signals.

Note that resource quota divides up aggregate cluster resources, but it creates no
restrictions around nodes: pods from several namespaces may run on the same node.
