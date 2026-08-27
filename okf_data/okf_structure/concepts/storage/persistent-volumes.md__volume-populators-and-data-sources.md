---
id: okf-structure/concepts/storage/persistent-volumes.md#volume-populators-and-data-sources
kind: section
title: Volume populators and data sources
source: concepts/storage/persistent-volumes.md
url: https://kubernetes.io/docs/concepts/storage/persistent-volumes/
heading: Volume populators and data sources
parent: okf-structure/concepts/storage/persistent-volumes
children: []
prev_sibling: okf-structure/concepts/storage/persistent-volumes.md#volume-cloning
next_sibling: okf-structure/concepts/storage/persistent-volumes.md#writing-portable-configuration
word_count: 75
---

Volume cloning and
snapshot restore pre-populate
a new volume from a built-in _data source_. _Volume populators_ extend this mechanism so that
a PersistentVolumeClaim can be pre-populated from other kinds of source (a custom resource),
referenced through its `dataSourceRef` field:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: populated-pvc
spec:
  dataSourceRef:
    name: example-name
    kind: ExampleDataSource
    apiGroup: example.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```

For details, including cross-namespace data sources, see
Volume Populators and Data Sources.
