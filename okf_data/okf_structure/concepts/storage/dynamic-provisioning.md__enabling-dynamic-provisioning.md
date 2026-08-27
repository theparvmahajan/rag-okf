---
id: okf-structure/concepts/storage/dynamic-provisioning.md#enabling-dynamic-provisioning
kind: section
title: Enabling Dynamic Provisioning
source: concepts/storage/dynamic-provisioning.md
url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
heading: Enabling Dynamic Provisioning
parent: okf-structure/concepts/storage/dynamic-provisioning
children: []
prev_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#background
next_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#using-dynamic-provisioning
word_count: 107
---

To enable dynamic provisioning, a cluster administrator needs to pre-create
one or more StorageClass objects for users.
StorageClass objects define which provisioner should be used and what parameters
should be passed to that provisioner when dynamic provisioning is invoked.
The name of a StorageClass object must be a valid
DNS subdomain name.

The following manifest creates a storage class "slow" which provisions standard
disk-like persistent disks.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: slow
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-standard
```

The following manifest creates a storage class "fast" which provisions
SSD-like persistent disks.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd
parameters:
  type: pd-ssd
```
