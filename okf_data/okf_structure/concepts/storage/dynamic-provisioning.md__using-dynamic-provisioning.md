---
id: okf-structure/concepts/storage/dynamic-provisioning.md#using-dynamic-provisioning
kind: section
title: Using Dynamic Provisioning
source: concepts/storage/dynamic-provisioning.md
url: https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/
heading: Using Dynamic Provisioning
parent: okf-structure/concepts/storage/dynamic-provisioning
children: []
prev_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#enabling-dynamic-provisioning
next_sibling: okf-structure/concepts/storage/dynamic-provisioning.md#defaulting-behavior
word_count: 118
---

Users request dynamically provisioned storage by including a storage class in
their `PersistentVolumeClaim`. Before Kubernetes v1.6, this was done via the
`volume.beta.kubernetes.io/storage-class` annotation. However, this annotation
is deprecated since v1.9. Users now can and should instead use the
`storageClassName` field of the `PersistentVolumeClaim` object. The value of
this field must match the name of a `StorageClass` configured by the
administrator (see Enabling Dynamic Provisioning).

To select the "fast" storage class, for example, a user would create the
following PersistentVolumeClaim:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: claim1
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: fast
  resources:
    requests:
      storage: 30Gi
```

This claim results in an SSD-like Persistent Disk being automatically
provisioned. When the claim is deleted, the volume is destroyed.
