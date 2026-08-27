---
id: okf-structure/tasks/administer-cluster/hardening-dra.md#grant-least-privilege-permissions-for-synthetic-subresources
kind: section
title: Grant least-privilege permissions for synthetic subresources
source: tasks/administer-cluster/hardening-dra.md
url: https://kubernetes.io/docs/tasks/administer-cluster/hardening-dra/
heading: Grant least-privilege permissions for synthetic subresources
parent: okf-structure/tasks/administer-cluster/hardening-dra
children: []
prev_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#identify-dra-components-that-write-status
next_sibling: okf-structure/tasks/administer-cluster/hardening-dra.md#bind-roles-to-explicit-identities
word_count: 143
---

Starting in Kubernetes v1.36, DRA status updates require synthetic subresource
permissions in addition to `resourceclaims/status`.

### Grant scheduler and allocation-controller permissions

Apply a role that allows binding-related updates:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dra-binding-updater
rules:
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/status"]
    verbs: ["get", "patch", "update"]
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/binding"]
    verbs: ["patch", "update"]
```

### Grant node-local driver permissions

Use node-aware verbs for node-local drivers:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dra-node-driver-status-updater
rules:
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/status"]
    verbs: ["get", "patch", "update"]
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/driver"]
    verbs: ["associated-node:patch", "associated-node:update"]
    resourceNames: ["dra.example.com"]
```

### Grant multi-node controller permissions only when needed

Use `arbitrary-node:*` only for components that must update from any node:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: dra-multinode-status-updater
rules:
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/status"]
    verbs: ["get", "patch", "update"]
  - apiGroups: ["resource.k8s.io"]
    resources: ["resourceclaims/driver"]
    verbs: ["arbitrary-node:patch", "arbitrary-node:update"]
    resourceNames: ["dra.example.com"]
```
