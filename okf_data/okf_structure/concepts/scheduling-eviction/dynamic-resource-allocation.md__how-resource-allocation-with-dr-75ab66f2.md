---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#how-resource-allocation-with-dra-works-how-it-works
kind: section
title: How resource allocation with DRA works {#how-it-works}
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: How resource allocation with DRA works {#how-it-works}
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-terminology-terminology
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#observability-of-dynamic-resources-observability-dynamic-resources
word_count: 365
---

The following sections describe the workflow for the various
types of DRA users and for the Kubernetes system during
dynamic resource allocation.

### Workflow for users {#user-workflow}

1. **Driver creation**: device owners or third-party entities create drivers
   that can create and manage ResourceSlices in the cluster. These drivers
   optionally also create DeviceClasses that define a category of devices and
   how to request them.
1. **Cluster configuration**: cluster admins create clusters, attach devices to
   nodes, and install the DRA device drivers. Cluster admins optionally create
   DeviceClasses that define categories of devices and how to request them.
1. **Resource claims**: workload operators create ResourceClaimTemplates or
   ResourceClaims that request specific device configurations within a
   DeviceClass. In the same step, workload operators modify their Kubernetes
   manifests to request those ResourceClaimTemplates or ResourceClaims.

### Workflow for Kubernetes {#kubernetes-workflow}

1. **ResourceSlice creation**: drivers in the cluster create ResourceSlices that
   represent one or more devices in a managed pool of similar devices.
1. **Workload creation**: the cluster control plane checks new workloads for
   references to ResourceClaimTemplates or to specific ResourceClaims.

   * If the workload uses a ResourceClaimTemplate, a controller named the
     `resourceclaim-controller` generates ResourceClaims for the workload.
   * If the workload uses a specific ResourceClaim, Kubernetes checks whether
     that ResourceClaim exists in the cluster. If the ResourceClaim doesn't
     exist, the Pods won't deploy.

1. **ResourceSlice filtering**: for every Pod, Kubernetes checks the
   ResourceSlices in the cluster to find a device that satisfies all of the
   following criteria:

   * The nodes that can access the resources are eligible to run the Pod.
   * The ResourceSlice has unallocated resources that match the requirements of
     the Pod's ResourceClaim.

1. **Resource allocation**: after finding an eligible ResourceSlice for a
   Pod's ResourceClaim, the Kubernetes scheduler updates the ResourceClaim
   with the allocation details. The scheduler uses a first-fit strategy and
   evaluates pools and ResourceSlices in lexicographical order by their names.
   Drivers can prioritize specific slices or pools by naming them appropriately.
   For details, see Naming and prioritization.
1. **Pod scheduling**: when resource allocation is complete, the scheduler
   places the Pod on a node that can access the allocated resource. The device
   driver and the kubelet on that node configure the device and the Pod's access
   to the device.
