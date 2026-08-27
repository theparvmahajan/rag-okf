---
id: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#introduction
kind: section
title: Hardening Guide - Dynamic Resource Allocation
source: concepts/security/hardening-guide/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/
heading: null
parent: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#harden-dra-status-update-permissions
word_count: 46
---

Dynamic Resource Allocation (DRA) adds powerful scheduling and device management
capabilities. Because DRA components update `ResourceClaim` status, cluster
administrators should configure authorization for those updates with explicit,
least-privilege RBAC.

Starting in Kubernetes v1.36, DRA status updates use synthetic subresources and,
in some cases, specialized node-aware verbs.
