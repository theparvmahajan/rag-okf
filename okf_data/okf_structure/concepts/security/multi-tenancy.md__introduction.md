---
id: okf-structure/concepts/security/multi-tenancy.md#introduction
kind: section
title: Multi-tenancy
source: concepts/security/multi-tenancy.md
url: https://kubernetes.io/docs/concepts/security/multi-tenancy/
heading: null
parent: okf-structure/concepts/security/multi-tenancy
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/multi-tenancy.md#use-cases
word_count: 113
---

This page provides an overview of available configuration options and best practices for cluster
multi-tenancy.

Sharing clusters saves costs and simplifies administration. However, sharing clusters also
presents challenges such as security, fairness, and managing _noisy neighbors_.

Clusters can be shared in many ways. In some cases, different applications may run in the same
cluster. In other cases, multiple instances of the same application may run in the same cluster,
one for each end user. All these types of sharing are frequently described using the umbrella term
_multi-tenancy_.

While Kubernetes does not have first-class concepts of end users or tenants, it provides several
features to help manage different tenancy requirements. These are discussed below.
