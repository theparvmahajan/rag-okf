---
id: okf-structure/concepts/storage/volume-populators-and-data-sources.md#data-source-references
kind: section
title: Data source references
source: concepts/storage/volume-populators-and-data-sources.md
url: https://kubernetes.io/docs/concepts/storage/volume-populators-and-data-sources/
heading: Data source references
parent: okf-structure/concepts/storage/volume-populators-and-data-sources
children: []
prev_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#volume-populators-and-data-sources
next_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#cross-namespace-data-sources
word_count: 431
---

The `dataSourceRef` field behaves almost the same as the `dataSource` field. If one is
specified while the other is not, the API server will give both fields the same value. Neither
field can be changed after creation, and attempting to specify different values for the two
fields will result in a validation error. Therefore the two fields will always have the same
contents.

There are two differences between the `dataSourceRef` field and the `dataSource` field that
users should be aware of:

* The `dataSource` field ignores invalid values (as if the field was blank) while the
  `dataSourceRef` field never ignores values and will cause an error if an invalid value is
  used. Invalid values are any core object (objects with no apiGroup) except for PVCs.
* The `dataSourceRef` field may contain different types of objects, while the `dataSource` field
  only allows PVCs and VolumeSnapshots.

When the `CrossNamespaceVolumeDataSource` feature is enabled, there are additional differences:

* The `dataSource` field only allows local objects, while the `dataSourceRef` field allows
  objects in any namespaces.
* When namespace is specified, `dataSource` and `dataSourceRef` are not synced.

Users should always use `dataSourceRef` on clusters that have the feature gate enabled, and
fall back to `dataSource` on clusters that do not. It is not necessary to look at both fields
under any circumstance. The duplicated values with slightly different semantics exist only for
backwards compatibility. In particular, a mixture of older and newer controllers are able to
interoperate because the fields are the same.

### Using volume populators

Volume populators are controllers that can
create non-empty volumes, where the contents of the volume are determined by a Custom Resource.
Users create a populated volume by referring to a Custom Resource using the `dataSourceRef` field:

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

Because volume populators are external components, attempts to create a PVC that uses one
can fail if not all the correct components are installed. External controllers should generate
events on the PVC to provide feedback on the status of the creation, including warnings if
the PVC cannot be created due to some missing component.

You can install the alpha volume data source validator
controller into your cluster. That controller generates warning Events on a PVC in the case that no populator
is registered to handle that kind of data source. When a suitable populator is installed for a PVC, it's the
responsibility of that populator controller to report Events that relate to volume creation and issues during
the process.
