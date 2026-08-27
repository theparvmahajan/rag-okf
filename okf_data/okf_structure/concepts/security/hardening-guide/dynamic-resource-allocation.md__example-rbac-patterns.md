---
id: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#example-rbac-patterns
kind: section
title: Example RBAC patterns
source: concepts/security/hardening-guide/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/dynamic-resource-allocation/
heading: Example RBAC patterns
parent: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#node-aware-dra-verbs
next_sibling: okf-structure/concepts/security/hardening-guide/dynamic-resource-allocation.md#related-cluster-administrator-task
word_count: 101
---

### Scheduler and allocation controller permissions

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

### Node-local DRA driver permissions

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

### Multi-node status controller permissions

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
