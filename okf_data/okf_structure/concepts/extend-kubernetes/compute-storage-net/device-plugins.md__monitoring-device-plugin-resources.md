---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#monitoring-device-plugin-resources
kind: section
title: Monitoring device plugin resources
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: Monitoring device plugin resources
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#api-compatibility
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-integration-with-the-topology-manager
word_count: 1050
---

In order to monitor resources provided by device plugins, monitoring agents need to be able to
discover the set of devices that are in-use on the node and obtain metadata to describe which
container the metric should be associated with. Prometheus metrics
exposed by device monitoring agents should follow the
Kubernetes Instrumentation Guidelines,
identifying containers using `pod`, `namespace`, and `container` prometheus labels.

The kubelet provides a gRPC service to enable discovery of in-use devices, and to provide metadata
for these devices:

```gRPC
// PodResourcesLister is a service provided by the kubelet that provides information about the
// node resources consumed by pods and containers on the node
service PodResourcesLister {
    rpc List(ListPodResourcesRequest) returns (ListPodResourcesResponse) {}
    rpc GetAllocatableResources(AllocatableResourcesRequest) returns (AllocatableResourcesResponse) {}
    rpc Get(GetPodResourcesRequest) returns (GetPodResourcesResponse) {}
}
```

### `List` gRPC endpoint {#grpc-endpoint-list}

The `List` endpoint provides information on resources of running pods, with details such as the
id of exclusively allocated CPUs, device id as it was reported by device plugins and id of
the NUMA node where these devices are allocated. Also, for NUMA-based machines, it contains the
information about memory and hugepages reserved for a container.

Starting from Kubernetes v1.27, the `List` endpoint can provide information on resources
of running pods allocated in `ResourceClaims` by the `DynamicResourceAllocation` API.
Starting from Kubernetes v1.34, this feature is enabled by default.

```gRPC
// ListPodResourcesResponse is the response returned by List function
message ListPodResourcesResponse {
    repeated PodResources pod_resources = 1;
}

// PodResources contains information about the node resources assigned to a pod
message PodResources {
    string name = 1;
    string namespace = 2;
    repeated ContainerResources containers = 3;
}

// ContainerResources contains information about the resources assigned to a container
message ContainerResources {
    string name = 1;
    repeated ContainerDevices devices = 2;
    repeated int64 cpu_ids = 3;
    repeated ContainerMemory memory = 4;
    repeated DynamicResource dynamic_resources = 5;
}

// ContainerMemory contains information about memory and hugepages assigned to a container
message ContainerMemory {
    string memory_type = 1;
    uint64 size = 2;
    TopologyInfo topology = 3;
}

// Topology describes hardware topology of the resource
message TopologyInfo {
        repeated NUMANode nodes = 1;
}

// NUMA representation of NUMA node
message NUMANode {
        int64 ID = 1;
}

// ContainerDevices contains information about the devices assigned to a container
message ContainerDevices {
    string resource_name = 1;
    repeated string device_ids = 2;
    TopologyInfo topology = 3;
}

// DynamicResource contains information about the devices assigned to a container by Dynamic Resource Allocation
message DynamicResource {
    string class_name = 1;
    string claim_name = 2;
    string claim_namespace = 3;
    repeated ClaimResource claim_resources = 4;
}

// ClaimResource contains per-plugin resource information
message ClaimResource {
    repeated CDIDevice cdi_devices = 1 [(gogoproto.customname) = "CDIDevices"];
}

// CDIDevice specifies a CDI device information
message CDIDevice {
    // Fully qualified CDI device name
    // for example: vendor.com/gpu=gpudevice1
    // see more details in the CDI specification:
    // https://github.com/container-orchestrated-devices/container-device-interface/blob/main/SPEC.md
    string name = 1;
}
```

cpu_ids in the `ContainerResources` in the `List` endpoint correspond to exclusive CPUs allocated
to a particular container. If the goal is to evaluate CPUs that belong to the shared pool, the `List`
endpoint needs to be used in conjunction with the `GetAllocatableResources` endpoint as explained
below:
1. Call `GetAllocatableResources` to get a list of all the allocatable CPUs
2. Call `GetCpuIds` on all `ContainerResources` in the system
3. Subtract out all of the CPUs from the `GetCpuIds` calls from the `GetAllocatableResources` call

### `GetAllocatableResources` gRPC endpoint {#grpc-endpoint-getallocatableresources}

GetAllocatableResources provides information on resources initially available on the worker node.
It provides more information than kubelet exports to APIServer.

`GetAllocatableResources` should only be used to evaluate allocatable
resources on a node. If the goal is to evaluate free/unallocated resources it should be used in
conjunction with the List() endpoint. The result obtained by `GetAllocatableResources` would remain
the same unless the underlying resources exposed to kubelet change. This happens rarely but when
it does (for example: hotplug/hotunplug, device health changes), client is expected to call
`GetAllocatableResources` endpoint.

However, calling `GetAllocatableResources` endpoint is not sufficient in case of cpu and/or memory
update and Kubelet needs to be restarted to reflect the correct resource capacity and allocatable.

```gRPC
// AllocatableResourcesResponses contains information about all the devices known by the kubelet
message AllocatableResourcesResponse {
    repeated ContainerDevices devices = 1;
    repeated int64 cpu_ids = 2;
    repeated ContainerMemory memory = 3;
}
```

`ContainerDevices` do expose the topology information declaring to which NUMA cells the device is
affine. The NUMA cells are identified using a opaque integer ID, which value is consistent to
what device plugins report
when they register themselves to the kubelet.

The gRPC service is served over a unix socket at `pod-resources/kubelet.sock` within the
kubelet's root directory (typically `/var/lib/kubelet/pod-resources/kubelet.sock`).
Monitoring agents for device plugin resources can be deployed as a daemon, or as a DaemonSet.
The canonical directory `pod-resources` within the kubelet root directory (typically
`/var/lib/kubelet/pod-resources`) requires privileged access, so monitoring
agents must run in a privileged security context. If a device monitoring agent is running as a
DaemonSet, the `pod-resources` directory must be mounted as a
volume in the device monitoring agent's
PodSpec.

When accessing the `pod-resources/kubelet.sock` from DaemonSet
or any other app deployed as a container on the host, which is mounting socket as
a volume, it is a good practice to mount the `pod-resources` directory
instead of the socket file itself. This will ensure
that after kubelet restart, the container will be able to re-connect to this socket.

On a typical Linux node, this means mounting `/var/lib/kubelet/pod-resources/`
instead of `/var/lib/kubelet/pod-resources/kubelet.sock`.

Container mounts are managed by inode referencing the socket or directory,
depending on what was mounted. When kubelet restarts, the socket is deleted
and a new socket is created, while the directory stays untouched.
So the original inode for the socket becomes unusable. The inode to the directory
will continue working.

### `Get` gRPC endpoint {#grpc-endpoint-get}

The `Get` endpoint provides information on resources of a running Pod. It exposes information
similar to those described in the `List` endpoint. The `Get` endpoint requires `PodName`
and `PodNamespace` of the running Pod.

```gRPC
// GetPodResourcesRequest contains information about the pod
message GetPodResourcesRequest {
    string pod_name = 1;
    string pod_namespace = 2;
}
```

The `Get` endpoint can provide Pod information related to dynamic resources
allocated by the dynamic resource allocation API.
Starting from Kubernetes v1.34, this feature is enabled by default.
