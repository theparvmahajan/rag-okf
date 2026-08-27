---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-alpha-features-alpha-features
kind: section
title: DRA alpha features {#alpha-features}
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: DRA alpha features {#alpha-features}
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#dra-beta-features-beta-features
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#whatsnext
word_count: 5135
---

The following sections describe DRA features that are available in the Alpha
feature stage.
They depend on enabling feature gates and may depend on additional
API groups.
For more information, see
Set up DRA in the cluster.

### Extended resource allocation by DRA {#extended-resource}

You can provide an extended resource name for a DeviceClass. The scheduler will then
select the devices matching the class for the extended resource requests.
This allows users to continue using extended resource requests in a pod to request
either extended resources provided by device plugin, or DRA devices.
The same extended resource can be provided either by device plugin, or DRA on one single cluster node.
The same extended resource can be provided by device plugin on some nodes, and DRA on other nodes in the same cluster.

In the example below, the DeviceClass is given an extendedResourceName `example.com/gpu`.
If a pod requested for the extended resource `example.com/gpu: 2`, it can be scheduled to
a node with two or more devices matching the DeviceClass.

```yaml
apiVersion: resource.k8s.io/v1
kind: DeviceClass
metadata:
  name: gpu.example.com
spec:
  selectors:
  - cel:
      expression: device.driver == 'gpu.example.com' && device.attributes['gpu.example.com'].type
        == 'gpu'
  extendedResourceName: example.com/gpu
```

In addition, users can use a special extended resource to allocate devices without
having to explicitly create a ResourceClaim. Using the extended resource name
prefix `deviceclass.resource.kubernetes.io/` and the DeviceClass name.
This works for any DeviceClass, even if it does not specify an extended resource name.
The resulting ResourceClaim will contain a request for an `ExactCount` of the
specified number of devices of that DeviceClass.

Extended resource allocation by DRA is a *beta feature* and is enabled by default with the 
`DRAExtendedResource` feature gate
in the kube-apiserver, kube-scheduler, kube-controller-manager, and kubelet.

### Partitionable devices {#partitionable-devices}

Devices represented in DRA don't necessarily have to be a single unit connected to a single machine,
but can also be a logical device comprised of multiple devices connected to multiple machines.
These devices might consume overlapping resources of the underlying phyical devices,
meaning that when one logical device is allocated other devices will no longer be available.

In the ResourceSlice API, this is represented as a list of named CounterSets, each of which
contains a set of named counters. The counters represent the resources available on the physical
device that are used by the logical devices advertised through DRA.

Logical devices can specify the ConsumesCounters list. Each entry contains a reference to a CounterSet
and a set of named counters with the amounts they will consume. So for a device to be allocatable,
the referenced counter sets must have sufficient quantity for the counters referenced by the device.

CounterSets must be specified in separate ResourceSlices from devices.
Devices can consume counters from any CounterSet defined in the same resource pool as the device.

Here is an example of two devices, each consuming 6Gi of memory from a shared counter with 8Gi of memory.
Thus, only one of the devices can be allocated at any point in time.
The scheduler handles this and it is transparent to the consumer as the ResourceClaim API is not affected.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-countersets
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  sharedCounters:
  - name: gpu-1-counters
    counters:
      memory:
        value: 8Gi
---
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: resourceslice-with-devices
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 2
  driver: dra.example.com
  devices:
  - name: device-1
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
  - name: device-2
    consumesCounters:
    - counterSet: gpu-1-counters
      counters:
        memory:
          value: 6Gi
```

Partitionable devices is a *beta feature* and enabled when the
`DRAPartitionableDevices` feature gate
is kept enabled in the kube-apiserver and kube-scheduler.

### Consumable capacity

The consumable capacity feature allows the same devices to be consumed by multiple independent ResourceClaims,
with the Kubernetes scheduler managing how much of the device's capacity is used up by each claim.
This is analogous to how Pods can share the resources on a Node; ResourceClaims can share the resources on a Device.

The device driver can set `allowMultipleAllocations` field added in `.spec.devices` of `ResourceSlice`
to allow allocating that device to multiple independent ResourceClaims or to multiple requests within a ResourceClaim.

Users can set `capacity` field added in `spec.devices.requests` of `ResourceClaim` to specify the device resource requirements for each allocation.

For the device that allows multiple allocations, the requested capacity is drawn from — or consumed from — its total capacity,
a concept known as **consumable capacity**.
Then, the scheduler ensures that the aggregate consumed capacity across all claims does not exceed the device’s overall capacity.
Furthermore, driver authors can use the `requestPolicy` constraints on individual device capacities to control
how those capacities are consumed.
For example, the driver author can specify that a given capacity is only consumed in increments of 1Gi.

Here is an example of a network device which allows multiple allocations and contains a consumable bandwidth capacity.

```yaml
kind: ResourceSlice
apiVersion: resource.k8s.io/v1
metadata:
  name: resourceslice
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 1
  driver: dra.example.com
  devices:
  - name: eth1
    allowMultipleAllocations: true
    attributes:
      name:
        string: "eth1"
    capacity:
      bandwidth:
        requestPolicy:
          default: "1M"
          validRange:
            min: "1M"
            step: "8"
        value: "10G"
```

The consumable capacity can be requested as shown in the below example.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaimTemplate
metadata:
  name: bandwidth-claim-template
spec:
  spec:
    devices:
      requests:
      - name: req-0
        exactly:
          deviceClassName: resource.example.com
          capacity:
            requests:
              bandwidth: 1G
```

The allocation result will include the consumed capacity and the identifier of the share.

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
...
status:
  allocation:
    devices:
      results:
      - consumedCapacity:
          bandwidth: 1G
        device: eth1
        shareID: "a671734a-e8e5-11e4-8fde-42010af09327"
```

In this example, a multiply-allocatable device was chosen. However, any `resource.example.com` device
with at least the requested 1G bandwidth could have met the requirement.
If a non-multiply-allocatable device were chosen, the allocation would have resulted in the entire device.
To force the use of a only multiply-allocatable devices, you can use the CEL criteria `device.allowMultipleAllocations == true`.

#### DistinctAttribute constraint

When requesting multiple devices in a ResourceClaim, you can use the DistinctAttribute
constraint to ensure that each allocated device has a different value for a specified
attribute. This constraint was introduced with the consumable capacity feature.

The DistinctAttribute constraint is particularly useful when working with
multiply-allocatable devices. It prevents the scheduler from allocating the same
device multiple times within a single ResourceClaim, even when that device allows
multiple allocations.

Beyond preventing duplicate allocations, this constraint helps optimize performance
by ensuring devices are distributed based on their attributes. For example, you can
use it to distribute devices across different NUMA nodes to optimize memory bandwidth
and reduce contention.

### Device taints and tolerations {#device-taints-and-tolerations}

Device taints are similar to node taints: a taint has a string key, a string value, and an effect.
The effect is applied to the ResourceClaim which is using a tainted device and to all Pods referencing that ResourceClaim.
The "NoSchedule" effect prevents scheduling those Pods.
Tainted devices are ignored when trying to allocate a ResourceClaim because using them would prevent scheduling of Pods.

The "NoExecute" effect implies "NoSchedule" and in addition causes eviction of all Pods
which have been scheduled already.
This eviction is implemented in the device taint eviction controller in kube-controller-manager by deleting affected Pods.

The "None" effect is ignored by the scheduler and eviction controller.
DRA drivers can use it to communicate exceptions to admins or other controllers,
like for example degraded health of a device. Admins can also use it to
do dry-runs of pod eviction in DeviceTaintRules (more on that below).

ResourceClaims can tolerate taints. If a taint is tolerated, its effect does not apply.
An empty toleration matches all taints. A toleration can be limited to certain effects
and/or match certain key/value pairs.
A toleration can check that a certain key exists, regardless which value it has, or it can check
for specific values of a key.
For more information on this matching see the
node taint concepts.

Eviction can be delayed by tolerating a taint for a certain duration.
That delay starts at the time when a taint gets added to a device, which is recorded in a field of the taint.

Taints apply as described above also to ResourceClaims allocating "all" devices on a node.
All devices must be untainted or all of their taints must be tolerated.
Allocating a device with admin access (described above)
is not exempt either. An admin using that mode must explicitly tolerate all taints
to access tainted devices.

Device taints and tolerations is a *beta feature* and enabled when the
`DRADeviceTaints` feature gate
is kept enabled in the kube-apiserver, kube-controller-manager and kube-scheduler.
To use DeviceTaintRules, the `resource.k8s.io/v1beta2` API version must be
enabled together with the `DRADeviceTaintRules` feature gate.
In contrast to `DRADeviceTaints`, `DRADeviceTaintRules` is off by default because of this dependency
on the beta API group, which has to be off by default.

You can add taints to devices in the following ways, by using the DeviceTaintRule API kind.

#### Taints set by the driver

A DRA driver can add taints to the device information that it publishes in ResourceSlices.
Consult the documentation of a DRA driver to learn whether the driver uses taints and what their keys and values are.

#### Taints set by an admin

An admin or a control plane component can taint devices without having to tell
the DRA driver to include taints in its device information in ResourceSlices.
They do that by creating DeviceTaintRules.
Each DeviceTaintRule adds one taint to devices which match the device selector.
Without such a selector, no devices are tainted.
This makes it harder to accidentally evict all pods using ResourceClaims when leaving out the selector by mistake.

Devices can be selected by giving the name of a DeviceClass, driver, pool, and/or device.
The DeviceClass selects all devices that are selected by the selectors in that DeviceClass.
With just the driver name, an admin can taint all devices managed by that driver,
for example while doing some kind of maintenance of that driver across the entire cluster.
Adding a pool name can limit the taint to a single node, if the driver manages node-local devices.

Finally, adding the device name can select one specific device.
The device name and pool name can also be used alone, if desired.
For example, drivers for node-local devices are encouraged to use the node name as their pool name.
Then tainting with that pool name automatically taints all devices on a node.

Drivers might use stable names like "gpu-0" that hide which specific device is currently assigned to that name.
To support tainting a specific hardware instance, CEL selectors can be used in a DeviceTaintRule
to match a vendor-specific unique ID attribute, if the driver supports one for its hardware.

The taint applies as long as the DeviceTaintRule exists.
It can be modified and and removed at any time.
Here is one example of a DeviceTaintRule for a fictional DRA driver:

```yaml
apiVersion: resource.k8s.io/v1beta2
kind: DeviceTaintRule
metadata:
  name: example
spec:
  # The entire hardware installation for this
  # particular driver is broken.
  # Evict all pods and don't schedule new ones.
  deviceSelector:
    driver: dra.example.com
  taint:
    key: dra.example.com/unhealthy
    value: Broken
    effect: NoExecute
```

The kube-apiserver automatically tracks when this taint was created by setting the
`timeAdded` field in the `spec`. The toleration period starts at that time
stamp. During updates which change the effect (see simulated eviction flow
below), the kube-apiserver automatically updates the time stamp. Users can control
the time stamp explicitly by setting the field when creating a DeviceTaintRule and
by changing it to some different value when updating.

The status contains a condition added by the eviction controller:

```
kubectl describe devicetaintrules
```

```
Name:         example
...
Spec:
  Device Selector:
    Driver:  dra.example.com
  Taint:
    Effect:      NoExecute
    Key:         dra.example.com/unhealthy
    Time Added:  2025-11-05T18:15:37Z
    Value:       Broken
Status:
  Conditions:
    Last Transition Time:  2025-11-05T18:15:37Z
    Message:               1 pod evicted since starting the controller.
    Observed Generation:   1
    Reason:                Completed
    Status:                False
    Type:                  EvictionInProgress
Events:                    <none>
```

Pods get evicted by deleting them. Usually this happens very quickly,
except when a toleration for the taint delays it for a certain period or
when there are very many pods which need to be evicted. When it takes
longer, the message provides information about the current status:

    2 pods need to be evicted in 2 different namespaces. 1 pod evicted since starting the controller.

The condition can be used to check whether an eviction is currently active:

    kubectl wait --for=condition=EvictionInProgress=false DeviceTaintRule/example

Beware of the potential race between scheduler and controller observing the new
taint at different times, which can lead to pods still being scheduled at a
time when the controller thinks that there are none which need to be evicted
and thus sets this condition to `False`. In practice, this race is made very
unlikely by updating the status only after an intentional delay of a few
seconds.

For `effect: None`, the message provides information about the number of
affected devices, how many of those are allocated, and how many pods would be
evicted if the effect was `NoExecute`. This can be used to do a dry-run before
actually triggering eviction:

- Create a DeviceTaintRule with the desired selectors and `effect: None`.

- Review the message:

  ```
  3 published devices selected. 1 allocated device selected.
  1 pod would be evicted in 1 namespace if the effect was NoExecute.
  This information will not be updated again. Recreate the DeviceTaintRule to trigger an update.
  ```

  Published devices are those listed in ResourceSlices. Tainting them
  prevents allocation for new pods. Only allocated devices cause
  eviction of the pods using them.

- Edit the DeviceTaintRule and change the effect into `NoExecute`.

### Resource pool status {#resource-pool-status}

You can query the availability of devices in resource pools using the
ResourcePoolStatusRequest API. This provides visibility into how many devices
are available, allocated, or unavailable across your cluster's DRA resource pools.

To check resource pool status:

1. Create a ResourcePoolStatusRequest specifying the driver name (required) and
   optionally a limit on the number of pools returned. You can also limit it to a single pool by specifying a pool name:

   ```yaml
   apiVersion: resource.k8s.io/v1beta2
   kind: ResourcePoolStatusRequest
   metadata:
     name: check-gpus
   spec:
     driver: example.com/gpu
     # Optional: filter to a specific pool
     # poolName: my-pool
     # Optional: limit number of pools returned (default: 100, max: 1000)
     # limit: 10
   ```

1. Wait for the controller to process the request:

   ```shell
   kubectl wait --for=condition=Complete resourcepoolstatusrequest/check-gpus --timeout=30s
   ```

1. Read the status to see pool availability:

   ```shell
   kubectl get resourcepoolstatusrequest/check-gpus -o yaml
   ```

   The status includes:
   - `poolCount`: total number of pools matching the filter (may exceed the number
     of pools listed if truncated by the limit).
   - `pools`: a list of pool details, each containing:
     - `driver` and `poolName`: identify the pool.
     - `generation`: the latest pool generation observed across ResourceSlices.
     - `resourceSliceCount`: the number of ResourceSlices making up the pool.
     - `totalDevices`: total devices in the pool.
     - `allocatedDevices`: devices currently allocated to claims.
     - `availableDevices`: devices available for allocation
       (totalDevices - allocatedDevices - unavailableDevices).
     - `unavailableDevices`: devices not available due to taints or other conditions.
     - `nodeName`: the node associated with the pool, if any.
     - `validationError`: set when the pool's data could not be fully validated
       (for example, during a generation rollout). When set, device count fields
       may be unset.
   - `conditions`: includes `Complete` (success) or `Failed` (error) condition types.

1. Delete the request when done:

   ```shell
   kubectl delete resourcepoolstatusrequest/check-gpus
   ```

ResourcePoolStatusRequest objects are processed once by a controller in
kube-controller-manager. The spec is immutable once created, and the entire
object becomes immutable once the status is populated. To get updated
availability data, delete and recreate the request. Completed requests are
automatically cleaned up after 1 hour.

This feature requires explicit RBAC permissions on the ResourcePoolStatusRequest
resource. No default ClusterRoles include this permission.

Resource pool status is an *alpha feature* and only enabled when the
`DRAResourcePoolStatus` feature gate
is enabled in the kube-apiserver and kube-controller-manager.

### Device binding conditions

Device Binding Conditions allow the Kubernetes scheduler to delay Pod binding until
external resources, such as fabric-attached GPUs or reprogrammable FPGAs, are confirmed
to be ready.

This waiting behavior is implemented in the 
PreBind phase
of the scheduling framework.
During this phase, the scheduler checks whether all required device conditions are
satisfied before proceeding with binding.

This improves scheduling reliability by avoiding premature binding and enables coordination
with external device controllers.

To use this feature, device drivers (typically managed by driver owners) must publish the
following fields in the `Device` section of a `ResourceSlice`. Cluster administrators
must enable the `DRADeviceBindingConditions` and `DRAResourceClaimDeviceStatus` feature
gates for the scheduler to honor these fields.

`bindingConditions`
: A list of _condition types_ that must be set to True (in the `.status.conditions` field of the associated ResourceClaim) before the Pod can be bound. These conditions typically represent readiness signals, such as DeviceAttached or DeviceInitialized.

`bindingFailureConditions`
: A list of condition types that, if set to True in
  status.conditions field of the associated ResourceClaim, indicate a failure state.
  If any of these conditions are True, the scheduler will abort binding and reschedule the Pod.

`bindsToNode`
: if set to `true`, the scheduler records the selected node name in the
  `status.allocation.nodeSelector` field of the ResourceClaim.
  This does not affect the Pod's `spec.nodeSelector`. Instead, it sets a node selector
  inside the ResourceClaim, which external controllers can use to perform node-specific
  operations such as device attachment or preparation.

All condition types listed in bindingConditions and bindingFailureConditions are evaluated
from the `status.conditions` field of the ResourceClaim.
External controllers are responsible for updating these conditions using standard Kubernetes
condition semantics (`type`, `status`, `reason`, `message`, `lastTransitionTime`).

The scheduler waits up to **600 seconds** (default) for all `bindingConditions` to become `True`.
If the timeout is reached or any `bindingFailureConditions` are `True`, the scheduler
clears the allocation and reschedules the Pod.
A cluster administration can configure this timeout duration by editing the kube-scheduler configuration file.

An example of configuring this timeout in `KubeSchedulerConfiguration` is given below:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- schedulerName: default-scheduler
  pluginConfig:
  - name: DynamicResources
    args:
      apiVersion: kubescheduler.config.k8s.io/v1
      kind: DynamicResourcesArgs
      bindingTimeout: 60s
```

#### Example {#device-binding-conditions-example}

Here is an example of a ResourceSlice that you might see in a cluster where there's a DRA driver in use, and that driver supports binding conditions:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: gpu-slice-1
spec:
  driver: dra.example.com
  nodeSelector:
    nodeSelectorTerms:
    - matchExpressions:
      - key: accelerator-type
        operator: In
        values:
        - "high-performance"
  pool:
    name: gpu-pool
    generation: 1
    resourceSliceCount: 1
  devices:
    - name: gpu-1
      attributes:
        vendor:
          string: "example"
        model:
          string: "example-gpu"
      bindsToNode: true
      bindingConditions:
        - dra.example.com/is-prepared
      bindingFailureConditions:
        - dra.example.com/preparing-failed
```
This example ResourceSlice has the following properties:

- The ResourceSlice targets nodes labeled with `accelerator-type=high-performance`, 
so that the scheduler uses only a specific set of eligible nodes.
- The scheduler selects one node from the selected group (for example, `node-3`) and sets 
the `status.allocation.nodeSelector` field in the ResourceClaim to that node name.
- The `dra.example.com/is-prepared` binding condition indicates that the device `gpu-1`
must be prepared (the `is-prepared` condition has a status of `True`) before binding. 
- If the `gpu-1` device preparation fails (the `preparing-failed` condition has a status of `True`), the scheduler aborts binding.
- The scheduler waits up to 600 seconds (default) for the device to become ready.
- External controllers can use the node selector in the ResourceClaim to perform
node-specific setup on the selected node.

Device binding conditions is a *beta feature* and is enabled by default, controlled by the
`DRADeviceBindingConditions` feature gate
in the kube-apiserver and kube-scheduler.

### Node allocatable resources {#node-allocatable-resources}

Devices managed by DRA can have an underlying footprint composed of node-allocatable
resources, such as `cpu`, `memory`, `hugepages`, or `ephemeral-storage`.
This feature integrates these DRA-based requests into the scheduler's standard
accounting alongside regular Pod `spec` requests for these resources.

Users (PodSpec authors) can use a mixture of Pod-level resources, container-level resources, 
and resource claims with associated node-allocatable resources. These devices represent 
resources like CPUs or memory directly, or they could be accelerators, network interface cards,
or other devices that require some host resources when allocated. The DRA driver will 
populate information in the ResourceSlice that tells the scheduler how to calculate the
node allocatable resources when the device is allocated to a ResourceClaim.
PodSpec authors do not need to make that calculation themselves.

When authoring a PodSpec using claims for these types of devices, there are a few things to be aware of:

*   When Pod-level resources are used, the sum of all container and claim resources 
    must not exceed the Pod-level resources; otherwise, the Pod will fail to schedule.
*   A container's total resource requirement is the sum of its container-level resources
    and any node-allocatable resources from its associated resource claims.
*   Claims that consume node allocatable resources cannot be shared between Pods.

#### Details for DRA Driver Authors

DRA drivers declare this node allocatable resource footprint using the
`nodeAllocatableResourceMappings` field on devices within a ResourceSlice.
This mapping translates the requested DRA device or capacity into standard
resources that are tracked in the node's `status.allocatable` (note that extended
resources are not supported for this mapping). This is useful both for drivers that directly
expose native resources (like a CPU or Memory DRA driver) and for devices that
require auxiliary node dependencies (like an accelerator that needs host memory).

This mapping defines the translation of the requested DRA device or capacity
units to the corresponding quantity of the node-allocatable resource. The
scheduler calculates the exact quantity using:

*   **Device-based scaling:** If `capacityKey` is not set, the
    `allocationMultiplier` multiplies the device count allocated to the claim.
    The `allocationMultiplier` defaults to 1 if not specified.
*   **Capacity-based scaling:** If `capacityKey` is set, it references a
    capacity name defined in the device's `capacity` map. The scheduler looks
    up the amount of that capacity consumed by the claim and multiplies it by
    the `allocationMultiplier`.

##### Example: CPU DRA Driver (Capacity-based scaling)

Here is an example where a CPU DRA driver exposes a CPU socket as a pool of 128
CPUs using DRA consumable capacity. The `capacityKey` links the consumed
`cpu.example.com/cpu` capacity directly to the node's standard `cpu`
allocatable resource:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: my-node-cpus
spec:
  driver: cpu.example.com
  nodeName: my-node
  pool:
    name: socket-cpus
    generation: 1
    resourceSliceCount: 1
  devices:
  - name: socket0cpus
    allowMultipleAllocations: true
    capacity:
      "cpu.example.com/cpu": "128"
    nodeAllocatableResourceMappings:
      cpu:
        capacityKey: "cpu.example.com/cpu"
        # allocationMultiplier defaults to 1 if omitted
  - name: socket1cpus
    allowMultipleAllocations: true
    capacity:
      "cpu.example.com/cpu": "128"
    nodeAllocatableResourceMappings:
      cpu:
        capacityKey: "cpu.example.com/cpu"
        # allocationMultiplier defaults to 1 if omitted
```

##### Example: Accelerator with Auxiliary Resources (Device-based scaling)

Here is an example of a resource slice where an accelerator requires an
additional 8Gi of memory per device instance to function:

```yaml
apiVersion: resource.k8s.io/v1
kind: ResourceSlice
metadata:
  name: my-node-xpus
spec:
  driver: xpu.example.com
  nodeName: my-node
  pool:
    name: xpu-pool
    generation: 1
    resourceSliceCount: 1
  devices:
  - name: xpu-model-x-001
    attributes:
      example.com/model:
        string: "model-x"
    nodeAllocatableResourceMappings:
      memory:
        allocationMultiplier: "8Gi"
```

After a Pod is successfully bound to the node, the exact quantities of 
node-allocatable resources allocated via DRA are included in the Pod's
`status.nodeAllocatableResourceClaimStatuses` field.

Node-allocatable resources is an alpha feature and is enabled when the
`DRANodeAllocatableResources` feature gate is enabled in the kube-apiserver,
kube-scheduler, and kubelet. In the alpha phase, the kubelet does not account
for these resources when determining QoS classes, configuring cgroups, or making
eviction decisions.

### DRA device metadata in containers {#device-metadata}

DRA drivers can expose device metadata such as device attributes (PCI bus
addresses or mdevUUID for mediated devices) or network configuration directly
to containers as JSON files.
This lets applications inside the container discover information about allocated
devices without querying the Kubernetes API or building custom controllers.

KEP-5304 defines a
device metadata protocol that drivers must
follow so applications inside the container see a consistent layout across
drivers and clusters. The
DRA kubelet plugin library
implements this protocol for you; the rest of this section describes how to
use it.

Device metadata follows the same rules as device access: it is available inside
a container only when that container requests the device in its container
specification, and not otherwise. For how to request DRA devices in Pods and
containers, see
Request devices in workloads using DRA.

#### Device metadata protocol {#device-metadata-protocol}

The protocol consists of four rules:

1. **File paths.** Metadata files live inside containers under
   `/var/run/kubernetes.io/dra-device-attributes`. For a directly referenced
   ResourceClaim the path is
   `resourceclaims/<claimName>/<requestName>/<driverName>-metadata.json`; for a
   claim created from a ResourceClaimTemplate the path is
   `resourceclaimtemplates/<podClaimName>/<requestName>/<driverName>-metadata.json`
   (where `podClaimName` is `pod.spec.resourceClaims[].name`).

   In cases where the ResourceClaim request uses the
   prioritized list feature, only the top-level request
   name is used for the `<requestName>` segment in the file path (that is,
   the `/<subrequest>` portion is dropped). Inside the
   JSON file, the `requests[].name` field carries the full
   `<request>/<subrequest>` reference (for example, `gpu/high-memory`) so
   that consumers can identify which alternative was allocated.

   The path constants are defined in
   `k8s.io/dynamic-resource-allocation/api/metadata`.

1. **JSON API.** Each file is a stream of one or more
   `DeviceMetadata`
   objects serialized as versioned JSON with `apiVersion` and `kind`, following
   Kubernetes API conventions. The same metadata is encoded once per supported
   API version (newest first). All objects in the stream are semantically
   equivalent; consumers should use the first object they can decode.

1. **Generation.** When a driver updates a metadata file the embedded
   `metadata.generation` field must increase so consumers can detect changes.

1. **Container exposure.** Files are typically exposed via
   CDI bind-mounts, but other
   mechanisms are permitted as long as the file appears at the correct path and
   is read-only inside the container.

#### How device metadata works {#device-metadata-how-it-works}

Device metadata is a driver-side feature that does not require any Kubernetes
API changes or feature gates. Using the DRA kubelet plugin library is a common
way to implement a driver, but drivers can be built in other ways as well.
Drivers that use the kubelet plugin enable this feature by passing the
`EnableDeviceMetadata` and `MetadataVersions`
options
when starting the plugin. `MetadataVersions` specifies which API versions are
serialized into the metadata file and must be set explicitly by the driver.
Check the documentation of your DRA driver to learn whether device metadata is
supported and how to enable it.

When device metadata is enabled, the driver generates metadata files and CDI
bind-mount specifications while preparing the allocated devices for the pod,
before the consuming containers start. The metadata appears inside containers at
the well-known paths as defined above.

When a single request allocates devices from multiple DRA drivers, each driver
writes its own metadata file. Containers enumerate `*-metadata.json` files in
the request directory to discover all devices.

The Go package
`k8s.io/dynamic-resource-allocation/devicemetadata`
provides utilities for reading and decoding these metadata files by applications
inside the container.

#### Metadata schema {#device-metadata-schema}

Each metadata file conforms to the
`DeviceMetadata`
API (`metadata.resource.k8s.io/v1alpha1`).
The following example shows a metadata file for a GPU device allocated through
a ResourceClaimTemplate:

```json
{
  "kind": "DeviceMetadata",
  "apiVersion": "metadata.resource.k8s.io/v1alpha1",
  "metadata": {
    "name": "pod0-gpu-2kqrd",
    "namespace": "gpu-test1",
    "uid": "c7e7b22e-239b-4498-b27c-7f1344481e14",
    "generation": 1
  },
  "podClaimName": "gpu",
  "requests": [
    {
      "name": "gpu",
      "devices": [
        {
          "driver": "gpu.example.com",
          "pool": "worker-0",
          "name": "gpu-0",
          "attributes": {
            "driverVersion": {
              "version": "1.0.0"
            },
            "index": {
              "int": 0
            },
            "model": {
              "string": "LATEST-GPU-MODEL"
            },
            "uuid": {
              "string": "gpu-18db0e85-99e9-c746-8531-ffeb86328b39"
            }
          }
        }
      ]
    }
  ]
}
```

#### Immediate and deferred metadata {#device-metadata-lifecycle}

Drivers provide metadata in one of two ways:

Immediate
: The driver populates metadata while preparing the claim on the
  node and writes the metadata file before the container starts. This is
  typical for GPU drivers where device information is known at preparation time.

Deferred
: In some cases, for example a network driver, the device information is
  not available during device allocation time but becomes available after the
  pod sandbox is created. In those cases the driver creates the CDI mount with
  an empty metadata file and writes the actual metadata later via an NRI hook
  that runs before the container starts. This ensures applications never see a
  missing or partially written file. Each update must increment
  `metadata.generation` so consumers can detect changes. The `MetadataUpdater`
  API in the DRA kubelet plugin library handles generation bookkeeping
  automatically for driver authors.

In both cases, metadata remains available to each consuming container for the
lifetime of that container. Metadata files are cleaned up after all containers
in the Pod have terminated.

To learn how to use device metadata in your workloads, see
Access DRA device metadata.

#### Custom drivers {#device-metadata-custom-drivers}

Custom, hand-crafted drivers that do not use the DRA kubelet plugin library
must implement the device metadata protocol
themselves. That means writing `DeviceMetadata` JSON at the correct file paths,
incrementing `metadata.generation` on every update, and exposing the files
read-only inside the container through CDI or an equivalent mechanism.

### List type attributes {#list-type-attributes}

This feature improves the ResourceSlice API, allowing DRA drivers to specify list values for device attributes instead of only scalars.
This is useful for modeling more complex internal node topologies, for example when a CPU has adjacency to multiple PCIe roots.

For ResourceClaim authors (end users), this means that the `matchAttribute` and `distinctAttribute` work better for these cases. 

- `matchAttribute` — the two attributes must have a *non-empty list intersection*, rather than be identical (scalar values are treated as single-item lists). 
  This just means that if one driver publishes a single value for, say, the PCIe root, and another driver publishes a list, the constraint is met as long as 
  the single value appears somewhere in the list.
- `distinctAttribute` — the attribute values must be *pairwise-disjoint* (no value shared between any two devices)

To help ResourceClaim authors use attributes that may be lists inside CEL expressions, this feature also introduces an `includes()` CEL function.

```
# Scalar attribute (backward compatible)
# assume: device.attributes["dra.example.com"].model = "model-a"
device.attributes["dra.example.com"].model.includes("model-a")  # true
device.attributes["dra.example.com"].model.includes("model-b")  # false

# List-type attribute (requires DRAListTypeAttributes)
# assume: device.attributes["dra.example.com"].supported-models= ["model-a", "model-b"]
device.attributes["dra.example.com"].supported-models.includes("model-a")  # true
device.attributes["dra.example.com"].supported-models.includes("model-c")  # false
```

#### Details for DRA Driver Authors

By default, each `DeviceAttribute` holds exactly one scalar value: a boolean, an integer,
a string, or a semantic version string. The `DRAListTypeAttributes` feature gate extends
`DeviceAttribute` with four list-type fields, allowing a device to advertise multiple
values for a single attribute:

- **`bools`** — a list of boolean values
- **`ints`** — a list of 64-bit integer values
- **`strings`** — a list of strings (each at most 64 characters)
- **`versions`** — a list of semantic version strings per semver.org spec 2.0.0
  (each at most 64 characters)

The total number of individual attribute values per device (scalar fields plus all list
elements combined) is limited to **48**. When any device in a ResourceSlice uses this feature or other advanced features such as taints,
the ResourceSlice will be limited to at most **64** devices.
use list-type attributes or other advanced features such as taints.

Here is an example of a device advertising multiple supported models using a list-type
string attribute:

```yaml
kind: ResourceSlice
apiVersion: resource.k8s.io/v1
metadata:
  name: example-resourceslice
spec:
  nodeName: worker-1
  pool:
    name: pool
    generation: 1
    resourceSliceCount: 1
  driver: dra.example.com
  devices:
  - name: gpu-0
    attributes:
      dra.example.com/supported-models:
        strings:
        - model-a
        - model-b
```

List type attributes is an *alpha feature* and only enabled when the
`DRAListTypeAttributes` feature gate
is enabled in the kube-apiserver and kube-scheduler.
