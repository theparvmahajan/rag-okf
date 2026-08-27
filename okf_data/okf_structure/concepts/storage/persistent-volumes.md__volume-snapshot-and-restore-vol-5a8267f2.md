---
id: okf-structure/concepts/storage/persistent-volumes.md#volume-snapshot-and-restore-volume-from-snapshot-support
kind: section
title: Volume Snapshot and Restore Volume from Snapshot Support
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: Volume Snapshot and Restore Volume from Snapshot Support
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#raw-block-volume-support
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#volume-cloning
word_count: 67
---

Volume snapshots only support the out-of-tree CSI volume plugins.
For details, see Volume Snapshots.
In-tree volume plugins are deprecated. You can read about the deprecated volume
plugins in the
Volume Plugin FAQ.

### Create a PersistentVolumeClaim from a Volume Snapshot {#create-persistent-volume-claim-from-volume-snapshot}

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: restore-pvc
spec:
  storageClassName: csi-hostpath-sc
  dataSource:
    name: new-snapshot-test
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```
