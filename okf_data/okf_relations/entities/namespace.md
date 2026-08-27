---
id: okf-relations/entities/namespace
kind: entity
title: Namespace
description: A logical partition inside one cluster; most object kinds live inside
  exactly one Namespace and are isolated from others.
outgoing_relations:
- okf-relations/edges/027-namespace-pod
- okf-relations/edges/028-namespace-service
incoming_relations:
- okf-relations/edges/023-resource-quota-namespace
- okf-relations/edges/024-limit-range-namespace
primary_sources:
- concepts/overview/working-with-objects/namespaces.md
- concepts/workloads/pods/user-namespaces.md
source: concepts/overview/working-with-objects/namespaces.md
word_count: 32
---

Namespace: A logical partition inside one cluster; most object kinds live inside exactly one Namespace and are isolated from others. Namespace scopes Pod. Namespace scopes Service. ResourceQuota constrains Namespace. LimitRange constrains Namespace.
