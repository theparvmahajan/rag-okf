---
id: okf-structure/concepts/policy/resource-quotas.md#enabling-resource-quota
kind: section
title: Enabling Resource Quota
source: concepts/policy/resource-quotas.md
url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
heading: Enabling Resource Quota
parent: okf-structure/concepts/policy/resource-quotas
children: []
prev_sibling: okf-structure/concepts/policy/resource-quotas.md#how-kubernetes-resourcequotas-work
next_sibling: okf-structure/concepts/policy/resource-quotas.md#types-of-resource-quota
word_count: 43
---

ResourceQuota support is enabled by default for many Kubernetes distributions. It is
enabled when the API server
`--enable-admission-plugins=` flag has `ResourceQuota` as
one of its arguments.

A resource quota is enforced in a particular namespace when there is a
ResourceQuota in that namespace.
