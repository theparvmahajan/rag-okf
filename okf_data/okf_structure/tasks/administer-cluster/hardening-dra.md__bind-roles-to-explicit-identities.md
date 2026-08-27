---
id: okf-structure/tasks/administer-cluster/hardening-dra.md#bind-roles-to-explicit-identities
kind: section
title: Bind roles to explicit identities
source: tasks/administer-cluster/hardening-dra.md
url: https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/
heading: Bind roles to explicit identities
parent: okf-structure/tasks/administer-cluster/hardening-dra
children: []
prev_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#grant-least-privilege-permissions-for-synthetic-subresources
next_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#validate-and-monitor
word_count: 38
---

Create `ClusterRoleBinding` objects for each component identity, and avoid
sharing a broad role across unrelated DRA components.

Restrict `resourceclaims/driver` rules with `resourceNames` where possible so
an identity can only write status for the specific DRA driver it operates.
