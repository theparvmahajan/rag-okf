---
id: okf-structure/concepts/workloads/pods/pod-qos.md#quality-of-service-classes
kind: section
title: Quality of Service classes
source: concepts/workloads/pods/pod-qos.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
heading: Quality of Service classes
parent: okf-structure/concepts/workloads/pods/pod-qos
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/pod-qos.md#memory-qos-with-cgroup-v2
word_count: 670
---

Kubernetes classifies the Pods that you run and allocates each Pod into a specific
_quality of service (QoS) class_. Kubernetes uses that classification to influence how different
pods are handled. Kubernetes does this classification based on the
resource requests
of the Containers in that Pod, along with
how those requests relate to resource limits.
This is known as Quality of Service
(QoS) class. Kubernetes assigns every Pod a QoS class based on the resource requests
and limits of its component Containers. QoS classes are used by Kubernetes to decide
which Pods to evict from a Node experiencing
Node Pressure. The possible
QoS classes are `Guaranteed`, `Burstable`, and `BestEffort`. When a Node runs out of resources,
Kubernetes will first evict `BestEffort` Pods running on that Node, followed by `Burstable` and
finally `Guaranteed` Pods. When this eviction is due to resource pressure, only Pods exceeding
resource requests are candidates for eviction.

### Guaranteed

Pods that are `Guaranteed` have the strictest resource limits and are least likely
to face eviction. They are guaranteed not to be killed until they exceed their limits
or there are no lower-priority Pods that can be preempted from the Node. They may
not acquire resources beyond their specified limits. These Pods can also make
use of exclusive CPUs using the
`static` CPU management policy.

#### Criteria

For a Pod to be given a QoS class of `Guaranteed`:

* Every Container in the Pod must have a memory limit and a memory request, both greater than zero.
* For every Container in the Pod, the memory limit must equal the memory request.
* Every Container in the Pod must have a CPU limit and a CPU request, both greater than zero.
* For every Container in the Pod, the CPU limit must equal the CPU request.

If instead the Pod uses Pod-level resources:

* The Pod must have a Pod-level memory limit and memory request, and their values must be equal.
* The Pod must have a Pod-level CPU limit and CPU request, and their values must be equal.

### Burstable

Pods that are `Burstable` have some lower-bound resource guarantees based on the request, but
do not require a specific limit. If a limit is not specified, it defaults to a
limit equivalent to the capacity of the Node, which allows the Pods to flexibly increase
their resources if resources are available. In the event of Pod eviction due to Node
resource pressure, these Pods are evicted only after all `BestEffort` Pods are evicted.
Because a `Burstable` Pod can include a Container that has no resource limits or requests, a Pod
that is `Burstable` can try to use any amount of node resources.

#### Criteria

A Pod is given a QoS class of `Burstable` if:

* The Pod does not meet the criteria for QoS class `Guaranteed`.
* At least one Container in the Pod has a memory or CPU request or limit,
  or the Pod has a Pod-level memory or CPU request or limit.

### BestEffort

Pods in the `BestEffort` QoS class can use node resources that aren't specifically assigned
to Pods in other QoS classes. For example, if you have a node with 16 CPU cores available to the
kubelet, and you assign 4 CPU cores to a `Guaranteed` Pod, then a Pod in the `BestEffort`
QoS class can try to use any amount of the remaining 12 CPU cores.

The kubelet prefers to evict `BestEffort` Pods if the node comes under resource pressure.

#### Criteria

A Pod has a QoS class of `BestEffort` if it doesn't meet the criteria for either `Guaranteed`
or `Burstable`. In other words, a Pod is `BestEffort` only if none of the Containers in the Pod have a
memory limit or a memory request, and none of the Containers in the Pod have a
CPU limit or a CPU request, and the Pod does not have any Pod-level memory or CPU limits or requests.
Containers in a Pod can request other resources (not CPU or memory) and still be classified as
`BestEffort`.
