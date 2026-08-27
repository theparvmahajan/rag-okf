---
id: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#prerequisites
kind: section
title: Prerequisites
source: tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/
heading: Prerequisites
parent: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#access-device-metadata-with-a-resourceclaim-access-metadata-resourceclaim
word_count: 61
---

* Ensure that your cluster admin has set up DRA, attached devices, and installed
  drivers. For more information, see
  Set Up DRA in a Cluster.
* Ensure that the DRA driver deployed in your cluster supports device metadata.
  Drivers that use the DRA kubelet plugin enable the `EnableDeviceMetadata` and
  `MetadataVersions` options when starting the plugin. Check the driver's
  documentation for details.
