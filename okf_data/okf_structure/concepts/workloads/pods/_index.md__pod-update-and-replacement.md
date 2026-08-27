---
id: okf-structure/concepts/workloads/pods/_index.md#pod-update-and-replacement
kind: section
title: Pod update and replacement
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Pod update and replacement
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#working-with-pods
next_sibling: okf-structure/concepts/workloads/pods/_index.md#resource-sharing-and-communication
word_count: 610
---

As mentioned in the previous section, when the Pod template for a workload
resource is changed, the controller creates new Pods based on the updated
template instead of updating or patching the existing Pods.

Kubernetes doesn't prevent you from managing Pods directly. It is possible to
update some fields of a running Pod, in place. However, Pod update operations
like
`patch`, and
`replace`
have some limitations:

- Most of the metadata about a Pod is immutable. For example, you cannot
  change the `namespace`, `name`, `uid`, or `creationTimestamp` fields.

- If the `metadata.deletionTimestamp` is set, no new entry can be added to the
  `metadata.finalizers` list.
- Pod updates may not change fields other than `spec.containers[*].image`,
  `spec.initContainers[*].image`, `spec.activeDeadlineSeconds`, `spec.terminationGracePeriodSeconds`,
  `spec.tolerations` or `spec.schedulingGates`. For `spec.tolerations`, you can only add new entries.
- When updating the `spec.activeDeadlineSeconds` field, two types of updates
  are allowed:

  1. setting the unassigned field to a positive number;
  1. updating the field from a positive number to a smaller, non-negative
     number.

### Pod subresources

The above update rules apply to regular pod updates, but other pod fields can be updated through _subresources_.

- **Resize:** The `resize` subresource allows container resources (`spec.containers[*].resources`) to be updated.
  See Resize Container Resources for more details.
- **Ephemeral Containers:** The `ephemeralContainers` subresource allows
  ephemeral containers
  to be added to a Pod.
  See Ephemeral Containers for more details.
- **Status:** The `status` subresource allows the pod status to be updated.
  This is typically only used by the Kubelet and other system controllers.
- **Binding:** The `binding` subresource allows setting the pod's `spec.nodeName` via a `Binding` request.
  This is typically only used by the scheduler.

### Pod generation

- The `metadata.generation` field is unique. It will be automatically set by the
  system such that new pods have a `metadata.generation` of 1, and every update to
  mutable fields in the pod's spec will increment the `metadata.generation` by 1.

- `observedGeneration` is a field that is captured in the `status` section of the Pod
  object. The Kubelet will set `status.observedGeneration`
  to track the pod state to the current pod status. The pod's `status.observedGeneration` will reflect the
  `metadata.generation` of the pod at the point that the pod status is being reported.

The `status.observedGeneration` field is managed by the kubelet and external controllers should **not** modify this field.

Different status fields may either be associated with the `metadata.generation` of the current sync loop, or with the
`metadata.generation` of the previous sync loop. The key distinction is whether a change in the `spec` is reflected
directly in the `status` or is an indirect result of a running process.

#### Direct Status Updates

For status fields where the allocated spec is directly reflected, the `observedGeneration` will
be associated with the current `metadata.generation` (Generation N).

This behavior applies to:

- **Resize Status**: The status of a resource resize operation.
- **Allocated Resources**: The resources allocated to the Pod after a resize.
- **Ephemeral Containers**: When a new ephemeral container is added, and it is in `Waiting` state.

#### Indirect Status Updates

For status fields that are an indirect result of running the spec, the `observedGeneration` will be associated
with the `metadata.generation` of the previous sync loop (Generation N-1).

This behavior applies to:

- **Container Image**: The `ContainerStatus.ImageID` reflects the image from the previous generation until the new image
  is pulled and the container is updated.
- **Actual Resources**: During an in-progress resize, the actual resources in use still belong to the previous generation's
  request.
- **Container state**: During an in-progress resize, with require restart policy reflects the previous generation's
  request.
- **activeDeadlineSeconds** & **terminationGracePeriodSeconds** & **deletionTimestamp**: The effects of these fields on the
  Pod's status are a result of the previously observed specification.
