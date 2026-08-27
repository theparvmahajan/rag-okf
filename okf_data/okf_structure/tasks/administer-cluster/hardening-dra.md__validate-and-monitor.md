---
id: okf-structure/tasks/administer-cluster/hardening-dra.md#validate-and-monitor
kind: section
title: Validate and monitor
source: tasks/administer-cluster/hardening-dra.md
url: https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/
heading: Validate and monitor
parent: okf-structure/tasks/administer-cluster/hardening-dra
children: []
prev_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#bind-roles-to-explicit-identities
next_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#whatsnext
word_count: 31
---

1. Verify each identity has only the required verbs and subresources.
1. Confirm DRA status updates work after rollout.
1. Watch API server audit events for denied `resourceclaims/binding` and
   `resourceclaims/driver` requests.
