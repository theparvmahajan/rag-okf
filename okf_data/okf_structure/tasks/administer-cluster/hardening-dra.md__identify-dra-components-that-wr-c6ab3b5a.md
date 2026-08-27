---
id: okf-structure/tasks/administer-cluster/hardening-dra.md#identify-dra-components-that-write-status
kind: section
title: Identify DRA components that write status
source: tasks/administer-cluster/hardening-dra.md
url: https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/
heading: Identify DRA components that write status
parent: okf-structure/tasks/administer-cluster/hardening-dra
children: []
prev_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#grant-least-privilege-permissions-for-synthetic-subresources
word_count: 30
---

Document which identities (usually ServiceAccounts) update ResourceClaim
status in your cluster. Typical writers are:

- kube-scheduler or a custom allocation controller
- node-local DRA drivers
- multi-node DRA status controllers
