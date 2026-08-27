---
id: okf-structure/concepts/storage/volume-populators-and-data-sources.md#cross-namespace-data-sources
kind: section
title: Cross namespace data sources
source: concepts/storage/volume-populators-and-data-sources.md
url: https://kubernetes.io/docs/concepts/storage/volume-populators-and-data-sources/
heading: Cross namespace data sources
parent: okf-structure/concepts/storage/volume-populators-and-data-sources
children: []
prev_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#data-source-references
next_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#whatsnext
word_count: 224
---

Kubernetes supports cross namespace volume data sources.
To use cross namespace volume data sources, you must enable the `AnyVolumeDataSource`
and `CrossNamespaceVolumeDataSource`
feature gates for
the kube-apiserver and kube-controller-manager.
Also, you must enable the `CrossNamespaceVolumeDataSource` feature gate for the csi-provisioner.

Enabling the `CrossNamespaceVolumeDataSource` feature gate allows you to specify
a namespace in the dataSourceRef field.

When you specify a namespace for a volume data source, Kubernetes checks for a
ReferenceGrant in the other namespace before accepting the reference.
ReferenceGrant is part of the `gateway.networking.k8s.io` extension APIs.
See ReferenceGrant
in the Gateway API documentation for details.
This means that you must extend your Kubernetes cluster with at least ReferenceGrant from the
Gateway API before you can use this mechanism.

### Using a cross-namespace volume data source

Create a ReferenceGrant to allow the namespace owner to accept the reference.
You define a populated volume by specifying a cross namespace volume data source
using the `dataSourceRef` field. You must already have a valid ReferenceGrant
in the source namespace:

   ```yaml
   apiVersion: gateway.networking.k8s.io/v1beta1
   kind: ReferenceGrant
   metadata:
     name: allow-ns1-pvc
     namespace: default
   spec:
     from:
     - group: ""
       kind: PersistentVolumeClaim
       namespace: ns1
     to:
     - group: snapshot.storage.k8s.io
       kind: VolumeSnapshot
       name: new-snapshot-demo
   ```

   ```yaml
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: foo-pvc
     namespace: ns1
   spec:
     storageClassName: example
     accessModes:
     - ReadWriteOnce
     resources:
       requests:
         storage: 1Gi
     dataSourceRef:
       apiGroup: snapshot.storage.k8s.io
       kind: VolumeSnapshot
       name: new-snapshot-demo
       namespace: default
     volumeMode: Filesystem
   ```
