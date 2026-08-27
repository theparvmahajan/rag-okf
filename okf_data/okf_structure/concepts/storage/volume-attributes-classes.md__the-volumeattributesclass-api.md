---
id: okf-structure/concepts/storage/volume-attributes-classes.md#the-volumeattributesclass-api
kind: section
title: The VolumeAttributesClass API
source: concepts/storage/volume-attributes-classes.md
url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
heading: The VolumeAttributesClass API
parent: okf-structure/concepts/storage/volume-attributes-classes
children: []
prev_sibling: okf-structure/concepts/storage/volume-attributes-classes.md#introduction
next_sibling: okf-structure/concepts/storage/volume-attributes-classes.md#parameters
word_count: 321
---

Each VolumeAttributesClass contains the `driverName` and `parameters`, which are
used when a PersistentVolume (PV) belonging to the class needs to be dynamically provisioned
or modified.

The name of a VolumeAttributesClass object is significant and is how users can request a particular class.
Administrators set the name and other parameters of a class when first creating VolumeAttributesClass objects.
While the name of a VolumeAttributesClass object in a `PersistentVolumeClaim` is mutable, the parameters in an existing class are immutable.

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: silver
driverName: pd.csi.storage.gke.io
parameters:
  provisioned-iops: "3000"
  provisioned-throughput: "50" 
```

### Provisioner

Each VolumeAttributesClass has a provisioner that determines what volume plugin is used for
provisioning PVs. The field `driverName` must be specified.

The feature support for VolumeAttributesClass is implemented in
kubernetes-csi/external-provisioner.

You are not restricted to specifying the kubernetes-csi/external-provisioner.
You can also run and specify external provisioners,
which are independent programs that follow a specification defined by Kubernetes.
Authors of external provisioners have full discretion over where their code lives, how
the provisioner is shipped, how it needs to be run, what volume plugin it uses, etc.

To understand how the provisioner works with VolumeAttributesClass, refer to 
the CSI external-provisioner documentation.

### Resizer

Each VolumeAttributesClass has a resizer that determines what volume plugin is used
for modifying PVs. The field `driverName` must be specified.

The modifying volume feature support for VolumeAttributesClass is implemented in
kubernetes-csi/external-resizer.

For example, an existing PersistentVolumeClaim is using a VolumeAttributesClass named silver:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: silver
  …
```

A new VolumeAttributesClass gold is available in the cluster:

```yaml
apiVersion: storage.k8s.io/v1
kind: VolumeAttributesClass
metadata:
  name: gold
driverName: pd.csi.storage.gke.io
parameters:
  iops: "4000"
  throughput: "60"
```

The end user can update the PVC with the new VolumeAttributesClass gold and apply:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test-pv-claim
spec:
  …
  volumeAttributesClassName: gold
  …
```

To understand how the resizer works with VolumeAttributesClass, refer to 
the CSI external-resizer documentation.
