---
id: okf-structure/concepts/workloads/resource-managers.md#pod-level-resource-managers-pod-level-resource-managers
kind: section
title: Pod-level resource managers {#pod-level-resource-managers}
source: concepts/workloads/resource-managers.md
url: https://kubernetes.io/docs/concepts/workloads/resource-managers/
heading: Pod-level resource managers {#pod-level-resource-managers}
parent: okf-structure/concepts/workloads/resource-managers
children: []
prev_sibling: okf-structure/concepts/workloads/resource-managers.md#device-manager
next_sibling: okf-structure/concepts/workloads/resource-managers.md#whatsnext
word_count: 1509
---

Pod-level resource support for the existing resource managers (Topology, CPU,
and Memory) extends them to handle pod-level resource specifications. When
enabled (via the `PodLevelResources` and `PodLevelResourceManagers` feature
gates), the resource managers can use `.spec.resources` directly as the basis
for their allocation decisions, evolving from a strictly per-container
allocation model to a pod-centric one. This partitioning scheme introduces a
more flexible and powerful resource management model, particularly for
performance-sensitive workloads. It allows you to define hybrid allocation
models where some containers in a Pod receive exclusive, NUMA-aligned resources,
while others share the remaining resources from a pod-level shared pool.

It is important to differentiate between the capabilities offered by each
Topology Manager scope, and how this modifies the behavior of the resource
managers. The `pod` scope enables allocation based on the entire pod's budget,
creating a pod-level shared pool for non-Guaranteed containers, alongside
exclusive allocations. In contrast, the `container` scope allows for a hybrid
allocation model where individual containers can get exclusive, NUMA-aligned
resources while others run in the node's shared pool, without aligning the
entire pod as a single unit.

Both standard init containers and restartable init containers (sidecars) are
fully supported. They can be granted exclusive resource slices or utilize the
pod's shared pool, and their lifecycle rules (e.g., reusable resources for
standard init containers vs. persistent reservations for sidecars) are respected
by the pod-level resource managers.

### Glossary

Pod level resources specification
:   The resource budget defined at the Pod level in `.spec.resources`, that
    specifies the collective requests and limits for the entire pod.

Guaranteed Container
:   Within the context of this feature, a container is considered `Guaranteed`
    if it specifies resource requests equal to its limits for both CPU
    (exclusive CPU allocation requires a positive integer value) and Memory.
    This status makes it eligible for exclusive resource allocation from the
    resource managers.

Exclusive slice
:   A dedicated portion of resources (for example: specific CPUs or memory
    pages) allocated solely to a single container, ensuring isolation from other
    containers.

Pod shared pool
:   The subset of a pod's allocated resources that remains after all exclusive
    slices have been reserved. These resources are shared by all containers in
    the pod that do not receive an exclusive allocation. While containers in
    this pool share resources with each other, they are strictly isolated from
    the exclusive slices and the general node-wide shared pool.

### How pod-level resource managers work

The CPU and Memory resource managers operate differently depending on the
configured Topology Manager scope.

#### Topology manager's pod scope and pod-level resources

When the Topology Manager scope is set to `pod`, the Kubelet performs a single
NUMA alignment for the entire pod based on the resource budget defined in
`.spec.resources`.

The resulting NUMA-aligned resource pool is then partitioned:

1.  **Exclusive Slices:** Containers that specify `Guaranteed` resources
    (requests equal to limits for both CPU and memory, and the CPU request is a
    positive integer) are allocated exclusive slices from the pod's total
    allocation.
2.  **Pod Shared Pool:** The remaining resources form a shared pool that is
    shared among all other containers in the pod that do not receive an
    exclusive allocation. While containers in this pool share resources with
    each other, they are strictly isolated from the exclusive slices and the
    general node-wide shared pool.

Note that when standard init containers run to completion, their resources are
added to a per-pod reusable set, rather than being returned to the node's
resource pool. Because they run sequentially, these resources are made reusable
for subsequent app containers (either for their own exclusive slices or for the
shared pool).

This allows you to co-locate containers that require exclusive resources (for
example: a high-performance primary application) with those that do not (for
example: sidecars for logging or monitoring), all within a single NUMA-aligned
pod.

Consider the containers in the following pod spec, where the Topology Manager
scope is `pod` and the pod has a total budget of 4 CPUs. `main-app` requests an
exclusive 2 CPU slice, while the sidecars share the remaining 2 CPUs in the
pod's shared pool:

**Important considerations:**

When using pod-level resources with the Topology manager's pod scope, there are
some important considerations:

*   **Empty shared pool restriction:** This configuration does not allow pod
    specifications that would produce an empty pod shared pool if there are
    containers that require one. If the sum of resource requests from all
    containers that are `Guaranteed` exactly equals the total resource budget,
    and there is at least one other container that requires a shared pool, the
    pod will be rejected at admission.

    For example, the following pod asks for a pod-level budget of 4 CPUs.
    `main-app` requires an exclusive 3 CPUs and `metrics-sidecar` requires an
    exclusive 1 CPU. Because there are 0 CPUs left in the shared pool for
    `logging-sidecar`, this pod is rejected (the same validation is applied for
    memory):

    

*   **Wasted resources:** Any resources overallocated when using the `pod` scope
    (the total container requests sum to less than the pod-level budget and
    there are no shared pool containers, or the shared pool containers don't
    fully utilize the remaining amount) will be assigned and reserved for the
    pod, effectively being wasted during the whole execution of the pod.

*   **Persistent pool:** The pod's total resource pool (the NUMA alignment and
    total reserved capacity) is persistent. If a shared-pool container crashes
    and restarts, the pod's overall resource reservation remains safely anchored
    on the node. The resources are only released back to the node's general pool
    when the entire pod is terminated.

#### Topology manager's container scope and pod-level resources

When the Topology Manager scope is set to `container`, the Kubelet evaluates
each container individually for exclusive allocation.

If the overall pod achieves a `Guaranteed` QoS class (through of having
appropriate values in the Pod-level `.spec.resources`), you can mix and match
containers:

*   Containers with their own `Guaranteed` requests receive exclusive
    NUMA-aligned resources.
*   Other `non-Guaranteed` containers in the pod run in the node's shared pool.
*   The collective resource consumption of all containers is still enforced by
    the pod's `.spec.resources` limits.

This scope is useful when you have an infrastructure sidecar that needs to be
aligned to a specific NUMA node for device access, while the main workload can
run in the general node shared pool.

Consider the containers in the following pod spec, where the Topology Manager
scope is `container` and the pod represents a workload with an infrastructure
sidecar and two application workers, with a total budget of 4 CPUs. The
`infrastructure-sidecar` gets an exclusive, NUMA-aligned 2 CPU slice. The two
application workers (`worker-1` and `worker-2`) run in the general, node-wide
shared pool:

#### CPU quota (CFS)

When running mixed workloads within a pod, isolation is enforced differently
depending on the allocation:

*   **Exclusive Containers:** Containers granted exclusive CPU slices have their
    CPU CFS quota enforcement disabled, allowing them to run without being
    throttled by the Linux scheduler.
*   **Pod Shared Pool Containers:** Containers falling into the pod shared pool
    have CPU CFS quotas enabled, ensuring they do not consume more than the
    leftover pod budget and preventing them from interfering with the exclusive
    containers.

#### Persistent pool and restarts

The pod's total resource pool (the NUMA alignment and total reserved capacity)
is persistent. If a container utilizing the pod's shared pool crashes and
restarts, the pod's overall resource reservation remains safely anchored on the
node. The resources are only released back to the node's general pool when the
entire pod is terminated.

#### Kubelet downgrades and state checkpoints

Enabling the `PodLevelResourceManagers` feature introduces new state versions
for the CPU and Memory managers.

If you downgrade the Kubelet to a version that does not support this feature, or
if you explicitly disable the feature gates after they have been active, the
older Kubelet will fail to read the newer checkpoint files due to this version
incompatibility. To recover, administrators must drain the affected node,
manually delete the
internal state checkpoint files
(`cpu_manager_state` and `memory_manager_state`), and restart the Kubelet.

### Observability and metrics

You can monitor the behavior and health of the resource managers across both
container-level and pod-level allocations using the following Kubelet metrics
(enabled via the `PodLevelResourceManagers` feature gate):

*   `resource_manager_allocations_total`: Counts the total number of exclusive
    resource allocations performed by a manager. The `source` label ("pod" or
    "node") distinguishes between allocations drawn from the node-level pool
    versus a pre-allocated pod-level pool.
*   `resource_manager_allocation_errors_total`: Counts errors encountered during
    exclusive resource allocation, distinguished by the intended allocation
    `source` ("pod" or "node").
*   `resource_manager_container_assignments`: Tracks the cumulative number of
    containers that will be granted a specific type of resource assignment. The
    `assignment_type` label ("node_exclusive", "pod_exclusive", "pod_shared")
    provides visibility into how many containers are running with exclusive
    resources (from the node or pod pool) versus the pod-level shared pool.

### Limitations and caveats

*   The functionality is only implemented for the `static` CPU Manager policy
    and the `Static` Memory Manager policy. Note that the `BestEffort` policy is
    not supported for the Memory Manager.
*   This feature is only supported on Linux nodes. On Windows nodes, the
    resource managers will act as a no-op for pod-level allocations.
