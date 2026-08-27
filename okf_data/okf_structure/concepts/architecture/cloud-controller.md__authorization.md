---
id: okf-structure/concepts/architecture/cloud-controller.md#authorization
kind: section
title: Authorization
source: concepts/architecture/cloud-controller.md
url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
heading: Authorization
parent: okf-structure/concepts/architecture/cloud-controller
children: []
prev_sibling: okf-structure/concepts/architecture/cloud-controller.md#cloud-controller-manager-functions-functions-of-the-ccm
next_sibling: okf-structure/concepts/architecture/cloud-controller.md#whatsnext
word_count: 287
---

This section breaks down the access that the cloud controller manager requires
on various API objects, in order to perform its operations.

### Node controller {#authorization-node-controller}

The Node controller only works with Node objects. It requires full access
to read and modify Node objects.

`v1/Node`:

- get
- list
- create
- update
- patch
- watch
- delete

### Route controller {#authorization-route-controller}

The route controller listens to Node object creation and configures
routes appropriately. It requires Get access to Node objects.

`v1/Node`:

- get

### Service controller {#authorization-service-controller}

The service controller watches for Service object **create**, **update** and **delete** events and then
configures load balancers for those Services appropriately.

To access Services, it requires **list**, and **watch** access. To update Services, it requires
**patch** and **update** access to the `status` subresource.

`v1/Service`:

- list
- get
- watch
- patch
- update

### Others {#authorization-miscellaneous}

The implementation of the core of the cloud controller manager requires access to create Event
objects, and to ensure secure operation, it requires access to create ServiceAccounts.

`v1/Event`:

- create
- patch
- update

`v1/ServiceAccount`:

- create

The RBAC ClusterRole for the cloud
controller manager looks like:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: cloud-controller-manager
rules:
- apiGroups:
  - ""
  resources:
  - events
  verbs:
  - create
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - '*'
- apiGroups:
  - ""
  resources:
  - nodes/status
  verbs:
  - patch
- apiGroups:
  - ""
  resources:
  - services
  verbs:
  - list
  - watch
- apiGroups:
  - ""
  resources:
  - services/status
  verbs:
  - patch
  - update
- apiGroups:
  - ""
  resources:
  - serviceaccounts
  verbs:
  - create
- apiGroups:
  - ""
  resources:
  - persistentvolumes
  verbs:
  - get
  - list
  - update
  - watch
```
