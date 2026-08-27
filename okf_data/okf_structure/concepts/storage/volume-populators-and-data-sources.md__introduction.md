---
id: okf-structure/concepts/storage/volume-populators-and-data-sources.md#introduction
kind: section
title: Volume Populators and Data Sources
source: concepts/storage/volume-populators-and-data-sources.md
url: https://kubernetes.io/docs/concepts/storage/volume-populators-and-data-sources/
heading: null
parent: okf-structure/concepts/storage/volume-populators-and-data-sources
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/volume-populators-and-data-sources.md#volume-populators-and-data-sources
word_count: 126
---

This document describes _volume populators_ and _data sources_ in Kubernetes.
Familiarity with persistent volumes
is suggested.

When you create a PersistentVolumeClaim,
the volume that Kubernetes provisions for it normally starts empty. A _data source_
lets you instead request that the new volume be pre-populated with existing data.
_Volume populators_ are the controllers that carry out that population, based on the
data source that the PersistentVolumeClaim references.

Kubernetes has built-in support for data sources that
clone an existing volume or that
restore a volume snapshot. Custom volume
populators extend this mechanism. The data source is a custom resource, that is, an object
whose type is defined by a
CustomResourceDefinition.
A populator controller watches for PersistentVolumeClaims that reference such a resource
and fills the new volume from it.
