---
id: okf-structure/concepts/storage/volume-populators-and-data-sources.md#volume-populators-and-data-sources
kind: section
title: Volume populators and data sources
source: concepts/storage/volume-populators-and-data-sources.md
url: https://kubernetes.io/docs/concepts/storage/volume-populators-and-data-sources/
heading: Volume populators and data sources
parent: okf-structure/concepts/storage/volume-populators-and-data-sources
children: []
prev_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#introduction
next_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#data-source-references
word_count: 88
---

Kubernetes supports custom volume populators.
To use custom volume populators, you must enable the `AnyVolumeDataSource`
feature gate for
the kube-apiserver and kube-controller-manager.

Volume populators take advantage of a PVC spec field called `dataSourceRef`. Unlike the
`dataSource` field, which can only contain either a reference to another PersistentVolumeClaim
or to a VolumeSnapshot, the `dataSourceRef` field can contain a reference to any object in the
same namespace, except for core objects other than PVCs. For clusters that have the feature
gate enabled, use of the `dataSourceRef` is preferred over `dataSource`.
