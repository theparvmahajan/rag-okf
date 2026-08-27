---
id: okf-structure/concepts/storage/volume-pvc-datasource.md#provisioning
kind: section
title: Provisioning
source: concepts/storage/volume-pvc-datasource.md
url: https://kubernetes.io/docs/concepts/storage/volume-pvc-datasource/
heading: Provisioning
parent: okf-structure/concepts/storage/volume-pvc-datasource
children: []
prev_sibling: okf-structure/concepts/storage/volume-pvc-datasource.md#introduction-2
next_sibling: okf-structure/concepts/storage/volume-pvc-datasource.md#usage
word_count: 96
---

Clones are provisioned like any other PVC with the exception of adding a dataSource
that references an existing PVC in the same namespace.

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
    name: clone-of-pvc-1
    namespace: myns
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: cloning
  resources:
    requests:
      storage: 5Gi
  dataSource:
    kind: PersistentVolumeClaim
    name: pvc-1
```

You must specify a capacity value for `spec.resources.requests.storage`, and the
value you specify must be the same or larger than the capacity of the source volume.

The result is a new PVC with the name `clone-of-pvc-1` that has the exact same
content as the specified source `pvc-1`.
