---
id: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#harden-dra-status-update-permissions
kind: section
title: Harden DRA status update permissions
source: concepts/security/hardening-guide/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/
heading: Harden DRA status update permissions
parent: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#introduction
next_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#node-aware-dra-verbs
word_count: 116
---

For DRA status updates,In addition to granting `update` permissions on the
`resourceclaims/status` subresource, cluster administrators must grant permissions on
specific "synthetic" subresources based on the exact fields a component needs to modify.
This enforces the principle of least privilege between the scheduler, custom controllers,
and DRA drivers.

The DRA authorization checks are divided into two synthetic subresources:

- **`resourceclaims/binding`**
  - Required to modify `status.allocation` and `status.reservedFor`.
  - Typically granted to the kube-scheduler and custom allocation controllers.
  - Uses standard `update` and `patch` verbs.
- **`resourceclaims/driver`**
  - Required to modify `status.devices`.
  - This check is performed per-driver to drivers from tampering with devices on different
  nodes and/or from other drivers.
  - Uses node-aware verbs for stricter scope.
