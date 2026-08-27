---
id: okf-structure/concepts/storage/storage-classes.md#introduction
kind: section
title: Storage Classes
source: concepts/storage/storage-classes.md
url: https://kubernetes.io/docs/concepts/storage/storage-classes/
heading: null
parent: okf-structure/concepts/storage/storage-classes
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/storage-classes.md#storageclass-objects
word_count: 78
---

This document describes the concept of a StorageClass in Kubernetes. Familiarity
with volumes and
persistent volumes is suggested.

A StorageClass provides a way for administrators to describe the _classes_ of
storage they offer. Different classes might map to quality-of-service levels,
or to backup policies, or to arbitrary policies determined by the cluster
administrators. Kubernetes itself is unopinionated about what classes
represent.

The Kubernetes concept of a storage class is similar to “profiles” in some other
storage system designs.
