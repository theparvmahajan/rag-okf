---
id: okf-structure/concepts/storage/persistent-volumes.md#volume-cloning
kind: section
title: Volume Cloning
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: Volume Cloning
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#volume-snapshot-and-restore-volume-from-snapshot-support
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#volume-populators-and-data-sources
word_count: 40
---

Volume Cloning
only available for CSI volume plugins.

### Create PersistentVolumeClaim from an existing PVC {#create-persistent-volume-claim-from-an-existing-pvc}

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: cloned-pvc
spec:
  storageClassName: my-csi-plugin
  dataSource:
    name: existing-src-pvc-name
    kind: PersistentVolumeClaim
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```
