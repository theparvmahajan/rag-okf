---
id: okf-structure/concepts/workloads/pods/downward-api.md#available-fields
kind: section
title: Available fields
source: concepts/workloads/pods/downward-api.md
url: https://kubernetes.io/docs/concepts/workloads/pods/downward-api/
heading: Available fields
parent: okf-structure/concepts/workloads/pods/downward-api
children: []
prev_sibling: okf-structure/concepts/workloads/pods/downward-api.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/downward-api.md#whatsnext
word_count: 453
---

Only some Kubernetes API fields are available through the downward API. This
section lists which fields you can make available.

You can pass information from available Pod-level fields using `fieldRef`.
At the API level, the `spec` for a Pod always defines at least one
Container.
You can pass information from available Container-level fields using
`resourceFieldRef`.

### Information available via `fieldRef` {#downwardapi-fieldRef}

For some Pod-level fields, you can provide them to a container either as
an environment variable or using a `downwardAPI` volume. The fields available
via either mechanism are:

`metadata.name`
: the pod's name

`metadata.namespace`
: the pod's namespace

`metadata.uid`
: the pod's unique ID

`metadata.annotations['<KEY>']`
: the value of the pod's annotation named `<KEY>` (for example, `metadata.annotations['myannotation']`)

`metadata.labels['<KEY>']`
: the text value of the pod's label named `<KEY>` (for example, `metadata.labels['mylabel']`)

The following information is available through environment variables
**but not as a downwardAPI volume fieldRef**:

`spec.serviceAccountName`
: the name of the pod's service account

`spec.nodeName`
: the name of the node where the Pod is executing

`status.hostIP`
: the primary IP address of the node to which the Pod is assigned

`status.hostIPs`
: the IP addresses is a dual-stack version of `status.hostIP`, the first is always the same as `status.hostIP`.

`status.podIP`
: the pod's primary IP address (usually, its IPv4 address)

`status.podIPs`
: the IP addresses is a dual-stack version of `status.podIP`, the first is always the same as `status.podIP`

The following information is available through a `downwardAPI` volume 
`fieldRef`, **but not as environment variables**:

`metadata.labels`
: all of the pod's labels, formatted as `label-key="escaped-label-value"` with one label per line

`metadata.annotations`
: all of the pod's annotations, formatted as `annotation-key="escaped-annotation-value"` with one annotation per line  

### Information available via `resourceFieldRef` {#downwardapi-resourceFieldRef}

These container-level fields allow you to provide information about
requests and limits
for resources such as CPU and memory.

Container CPU and memory resources can be resized while the container is running.
If this happens, a downward API volume will be updated,
but environment variables will not be updated unless the container restarts.
See Resize CPU and Memory Resources assigned to Containers
for more details.

`resource: limits.cpu`
: A container's CPU limit

`resource: requests.cpu`
: A container's CPU request

`resource: limits.memory`
: A container's memory limit

`resource: requests.memory`
: A container's memory request

`resource: limits.hugepages-*`
: A container's hugepages limit

`resource: requests.hugepages-*`
: A container's hugepages request

`resource: limits.ephemeral-storage`
: A container's ephemeral-storage limit

`resource: requests.ephemeral-storage`
: A container's ephemeral-storage request

#### Fallback information for resource limits

If CPU and memory limits are not specified for a container, and you use the
downward API to try to expose that information, then the
kubelet defaults to exposing the maximum allocatable value for CPU and memory
based on the node allocatable
calculation.
