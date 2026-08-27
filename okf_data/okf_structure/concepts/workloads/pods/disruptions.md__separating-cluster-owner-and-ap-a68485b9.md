---
id: okf-structure/concepts/workloads/pods/disruptions.md#separating-cluster-owner-and-application-owner-roles
kind: section
title: Separating Cluster Owner and Application Owner Roles
source: concepts/workloads/pods/disruptions.md
url: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
heading: Separating Cluster Owner and Application Owner Roles
parent: okf-structure/concepts/workloads/pods/disruptions
children: []
prev_sibling: okf-structure/concepts/workloads/pods/disruptions.md#pod-disruption-conditions-pod-disruption-conditions
next_sibling: okf-structure/concepts/workloads/pods/disruptions.md#how-to-perform-disruptive-actions-on-your-cluster
word_count: 99
---

Often, it is useful to think of the Cluster Manager
and Application Owner as separate roles with limited knowledge
of each other.   This separation of responsibilities
may make sense in these scenarios:

- when there are many application teams sharing a Kubernetes cluster, and
  there is natural specialization of roles
- when third-party tools or services are used to automate cluster management

Pod Disruption Budgets support this separation of roles by providing an
interface between the roles.

If you do not have such a separation of responsibilities in your organization,
you may not need to use Pod Disruption Budgets.
