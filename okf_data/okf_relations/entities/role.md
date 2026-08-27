---
id: okf-relations/entities/role
kind: entity
title: Role
description: A namespaced set of permissions (verbs on resources) within the Kubernetes
  RBAC system.
outgoing_relations: []
incoming_relations:
- okf-relations/edges/019-role-binding-role
primary_sources:
- concepts/security/rbac-good-practices.md
source: concepts/security/rbac-good-practices.md
word_count: 17
---

Role: A namespaced set of permissions (verbs on resources) within the Kubernetes RBAC system. RoleBinding grants Role.
