---
id: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#node-aware-dra-verbs
kind: section
title: Node-aware DRA verbs
source: concepts/security/hardening-guide/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/
heading: Node-aware DRA verbs
parent: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#harden-dra-status-update-permissions
next_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#example-rbac-patterns
word_count: 49
---

When authorizing updates to `resourceclaims/driver`, use the appropriate
specialized verb prefix:

- **`associated-node:<verb>`** (for example, `associated-node:update`)
  - For node-local drivers.
  - The API server verifies node association for the requesting driver.
- **`arbitrary-node:<verb>`** (for example, `arbitrary-node:patch`)
  - For control-plane or multi-node controllers that may update claims from
    any node.
