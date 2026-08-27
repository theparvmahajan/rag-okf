---
id: okf-structure/setup/best-practices/multiple-zones.md#storage-access-for-zones
kind: section
title: Storage access for zones
source: setup/best-practices/multiple-zones.md
url: https://kubernetes.io/docs/setup/best-practices/multiple-zones/
heading: Storage access for zones
parent: okf-structure/setup/best-practices/multiple-zones
children: []
prev_sibling: okf-structure/setup/best-practices/multiple-zones.md#manual-zone-assignment-for-pods
next_sibling: okf-structure/setup/best-practices/multiple-zones.md#networking
word_count: 117
---

When persistent volumes are created, Kubernetes automatically adds zone labels 
to any PersistentVolumes that are linked to a specific zone.
The scheduler then ensures,
through its `NoVolumeZoneConflict` predicate, that pods which claim a given PersistentVolume
are only placed into the same zone as that volume.

Please note that the method of adding zone labels can depend on your 
cloud provider and the storage provisioner you’re using. Always refer to the specific 
documentation for your environment to ensure correct configuration.

You can specify a StorageClass
for PersistentVolumeClaims that specifies the failure domains (zones) that the
storage in that class may use.
To learn about configuring a StorageClass that is aware of failure domains or zones,
see Allowed topologies.
