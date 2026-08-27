---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#about-dra-about-dra
kind: section
title: About DRA {#about-dra}
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: About DRA {#about-dra}
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-terminology-terminology
word_count: 383
---

Allocating resources with DRA is a similar experience to
dynamic volume provisioning,
in which you use PersistentVolumeClaims to claim storage capacity from storage classes
and request the claimed capacity in your Pods.

### Benefits of DRA {#dra-benefits}

DRA provides a flexible way to categorize, request, and use devices in your cluster.
Using DRA provides benefits like the following:

* **Flexible device filtering**: use common expression language (CEL) to perform
  fine-grained filtering for specific device attributes.
* **Device sharing**: share the same resource with multiple containers or Pods
  by referencing the corresponding resource claim.
* **Centralized device categorization**: device drivers and cluster admins can
  use device classes to provide app operators with hardware categories that are
  optimized for various use cases. For example, you can create a cost-optimized
  device class for general-purpose workloads, and a high-performance device
  class for critical jobs.
* **Simplified Pod requests**: with DRA, app operators don't need to specify
  device quantities in Pod resource requests. Instead, the Pod references a
  resource claim, and the device configuration in that claim applies to the Pod.

These benefits provide significant improvements in the device allocation
workflow when compared to
device plugins,
which require per-container device requests, don't support device sharing, and
don't support expression-based device filtering.

### Types of DRA users {#dra-user-types}

The workflow of using DRA to allocate devices involves the following types of users:

* **Device owner**: responsible for devices. Device owners might be commercial
  vendors, the cluster operator, or another entity. To use DRA, devices must
  have DRA-compatible drivers that do the following:

  * Create ResourceSlices that provide Kubernetes with information about
    nodes and resources.
  * Update ResourceSlices when resource capacity in the cluster changes.
  * Optionally, create DeviceClasses that workload operators can use to
    claim devices.

* **Cluster admin**: responsible for configuring clusters and nodes,
  attaching devices, installing drivers, and similar tasks. To use DRA,
  cluster admins do the following:

  * Attach devices to nodes.
  * Install device drivers that support DRA.
  * Optionally, create DeviceClasses that workload operators can use to claim devices.

* **Workload operator**: responsible for deploying and managing workloads in the
  cluster. To use DRA to allocate devices to Pods, workload operators do the following:

  * Create ResourceClaims or ResourceClaimTemplates to request specific
    configurations within DeviceClasses.
  * Deploy workloads that use specific ResourceClaims or ResourceClaimTemplates.
