---
id: okf-structure/concepts/storage/volume-attributes-classes.md#introduction
kind: section
title: Volume Attributes Classes
source: concepts/storage/volume-attributes-classes.md
url: https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/
heading: null
parent: okf-structure/concepts/storage/volume-attributes-classes
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/volume-attributes-classes.md#the-volumeattributesclass-api
word_count: 89
---

This page assumes that you are familiar with StorageClasses,
volumes and PersistentVolumes
in Kubernetes.

A VolumeAttributesClass provides a way for administrators to describe the mutable
"classes" of storage they offer. Different classes might map to different quality-of-service levels.
Kubernetes itself is un-opinionated about what these classes represent.

This feature is generally available (GA) as of version 1.34, and users have the option to disable it.

You can also only use VolumeAttributesClasses with storage backed by
Container Storage Interface, and only where the
relevant CSI driver implements the `ModifyVolume` API.
