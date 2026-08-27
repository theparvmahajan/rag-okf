---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-implementation
kind: section
title: Device plugin implementation
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: Device plugin implementation
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-registration
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-deployment
word_count: 850
---

The general workflow of a device plugin includes the following steps:

1. Initialization. During this phase, the device plugin performs vendor-specific
   initialization and setup to make sure the devices are in a ready state.

1. The plugin starts a gRPC service, with a Unix socket under the host path
   `/var/lib/kubelet/device-plugins/` (this path is hardcoded and is not
   affected by the kubelet's `--root-dir` or any other configuration), that
   implements the following interfaces:

   ```gRPC
   service DevicePlugin {
         // GetDevicePluginOptions returns options to be communicated with Device Manager.
         rpc GetDevicePluginOptions(Empty) returns (DevicePluginOptions) {}

         // ListAndWatch returns a stream of List of Devices
         // Whenever a Device state change or a Device disappears, ListAndWatch
         // returns the new list
         rpc ListAndWatch(Empty) returns (stream ListAndWatchResponse) {}

         // Allocate is called during container creation so that the Device
         // Plugin can run device specific operations and instruct Kubelet
         // of the steps to make the Device available in the container
         rpc Allocate(AllocateRequest) returns (AllocateResponse) {}

         // GetPreferredAllocation returns a preferred set of devices to allocate
         // from a list of available ones. The resulting preferred allocation is not
         // guaranteed to be the allocation ultimately performed by the
         // devicemanager. It is only designed to help the devicemanager make a more
         // informed allocation decision when possible.
         rpc GetPreferredAllocation(PreferredAllocationRequest) returns (PreferredAllocationResponse) {}

         // PreStartContainer is called, if indicated by Device Plugin during registration phase,
         // before each container start. Device plugin can run device specific operations
         // such as resetting the device before making devices available to the container.
         rpc PreStartContainer(PreStartContainerRequest) returns (PreStartContainerResponse) {}
   }
   ```

   
   Plugins are not required to provide useful implementations for
   `GetPreferredAllocation()` or `PreStartContainer()`. Flags indicating
   the availability of these calls, if any, should be set in the `DevicePluginOptions`
   message sent back by a call to `GetDevicePluginOptions()`. The `kubelet` will
   always call `GetDevicePluginOptions()` to see which optional functions are
   available, before calling any of them directly.
   

1. The plugin registers itself with the kubelet through the Unix socket at host
   path `/var/lib/kubelet/device-plugins/kubelet.sock`.

   
   The ordering of the workflow is important. A plugin MUST start serving gRPC
   service before registering itself with kubelet for successful registration.
   

1. After successfully registering itself, the device plugin runs in serving mode, during which it keeps
   monitoring device health and reports back to the kubelet upon any device state changes.
   It is also responsible for serving `Allocate` gRPC requests. During `Allocate`, the device plugin may
   do device-specific preparation; for example, GPU cleanup or QRNG initialization.
   If the operations succeed, the device plugin returns an `AllocateResponse` that contains container
   runtime configurations for accessing the allocated devices. The kubelet passes this information
   to the container runtime.

   An `AllocateResponse` contains zero or more `ContainerAllocateResponse` objects. In these, the
   device plugin defines modifications that must be made to a container's definition to provide
   access to the device. These modifications include:

   * Annotations
   * device nodes
   * environment variables
   * mounts
   * fully-qualified CDI device names

   
   The processing of the fully-qualified CDI device names by the Device Manager requires
   that the `DevicePluginCDIDevices` feature gate
   is enabled for both the kubelet and the kube-apiserver. This was added as an alpha feature in Kubernetes
   v1.28, graduated to beta in v1.29 and to GA in v1.31.
   

### Handling kubelet restarts

A device plugin is expected to detect kubelet restarts and re-register itself with the new
kubelet instance. A new kubelet instance deletes all the existing Unix sockets under
`/var/lib/kubelet/device-plugins` (the hardcoded path for device plugins) when it starts. A device plugin can monitor the deletion
of its Unix socket and re-register itself upon such an event.

### Device plugin and unhealthy devices

There are cases when devices fail or are shut down. The responsibility of the Device Plugin
in this case is to notify the kubelet about the situation using the `ListAndWatchResponse` API.

Once a device is marked as unhealthy, the kubelet will decrease the allocatable count
for this resource on the Node to reflect how many devices can be used for scheduling new pods.
Capacity count for the resource will not change.

Pods that were assigned to the failed devices will continue be assigned to this device.
It is typical that code relying on the device will start failing and Pod may get
into Failed phase if `restartPolicy` for the Pod was not `Always` or enter the crash loop
otherwise.

Before Kubernetes v1.31, the way to know whether or not a Pod is associated with the
failed device is to use the PodResources API.

When the feature gate `ResourceHealthStatus` is enabled (beta and enabled by default since v1.36),
the field `allocatedResourcesStatus`
is added to each container status, within the `.status` for each Pod. The `allocatedResourcesStatus`
field reports health information for each device assigned to the container.
Each resource health entry can include an optional `message` field with additional
human readable context about the health status, such as error details or failure reasons.

For a failed Pod, or where you suspect a fault, you can use this status to understand whether
the Pod behavior may be associated with device failure. For example, if an accelerator is reporting
an over-temperature event, the `allocatedResourcesStatus` field may report this.
