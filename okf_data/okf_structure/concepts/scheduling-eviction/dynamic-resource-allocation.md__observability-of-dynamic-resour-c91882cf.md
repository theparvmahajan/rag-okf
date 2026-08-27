---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#observability-of-dynamic-resources-observability-dynamic-resources
kind: section
title: Observability of dynamic resources {#observability-dynamic-resources}
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: Observability of dynamic resources {#observability-dynamic-resources}
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#how-resource-allocation-with-dra-works-how-it-works
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#pre-scheduled-pods
word_count: 512
---

You can check the status of dynamically allocated resources by using any of the
following methods:

* kubelet device metrics
* ResourceClaim status
* Device health monitoring

### kubelet device metrics {#monitoring-resources}

The `PodResourcesLister` kubelet gRPC service lets you monitor in-use devices.
The `DynamicResource` message provides information that's specific to dynamic
resource allocation, such as the device name and the claim name. For details,
see
Monitoring device plugin resources.

### ResourceClaim device status {#resourceclaim-device-status}

DRA drivers can report driver-specific
device status
data for each allocated device in the `status.devices` field of a ResourceClaim.
For example, the driver might list the IP addresses that are assigned to a
network interface device. Updating this field requires specific synthetic RBAC permissions,
see
Hardening Guide - Dynamic Resource Allocation
and
Harden Dynamic Resource Allocation in Your Cluster.

The accuracy of the information that a driver adds to a ResourceClaim
`status.devices` field depends on the driver. Evaluate drivers to decide whether
you can rely on this field as the only source of device information.

If you disable the
`DRAResourceClaimDeviceStatus` feature gate, the
`status.devices` field automatically gets cleared when storing the ResourceClaim.
A ResourceClaim device status is supported when it is possible, from a DRA
driver, to update an existing ResourceClaim where the `status.devices` field is
set.

For details about the `status.devices` field, see the
 API reference.

### Device Health Monitoring {#device-health-monitoring}

Kubernetes provides a mechanism for monitoring and reporting the health of dynamically allocated infrastructure resources.
For stateful applications running on specialized hardware, it is critical to know when a device has failed or become unhealthy. It is also helpful to find out if the device recovers.

To use this functionality, the `ResourceHealthStatus` feature gate must be enabled (beta and enabled by default since v1.36), and the DRA driver must implement the `DRAResourceHealth` gRPC service.

When a DRA driver detects that an allocated device has become unhealthy, it reports this status back to the kubelet. This health information is then exposed directly in the Pod's status. The kubelet populates the `allocatedResourcesStatus` field in the status of each container, detailing the health of each device assigned to that container. Each resource health entry can include an optional `message` field with additional human-readable context about the health status, such as error details or failure reasons.

If the kubelet does not receive a health update from a DRA driver within a timeout period, the device's health status is marked as "Unknown". DRA drivers can configure this timeout on a per-device basis by setting the `health_check_timeout_seconds` field in the `DeviceHealth` gRPC message. If not specified, the kubelet uses a default timeout of 30 seconds. This allows different hardware types (for example, GPUs, FPGAs, or storage devices) to use appropriate timeout values based on their health-reporting characteristics.

This provides crucial visibility for users and controllers to react to hardware failures.
For a Pod that is failing, you can inspect this status to determine if the failure was related to an unhealthy device.

Device health status is not updated in the Pod status after a Pod has terminated (for example, in Failed state).
