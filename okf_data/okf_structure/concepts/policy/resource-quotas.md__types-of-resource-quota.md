---
id: okf-structure/concepts/policy/resource-quotas.md#types-of-resource-quota
kind: section
title: Types of resource quota
source: concepts/policy/resource-quotas.md
url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
heading: Types of resource quota
parent: okf-structure/concepts/policy/resource-quotas
children: []
prev_sibling: okf-structure/concepts/policy/resource-quotas.md#enabling-resource-quota
next_sibling: okf-structure/concepts/policy/resource-quotas.md#viewing-and-setting-quotas
word_count: 1261
---

The ResourceQuota mechanism lets you enforce different kinds of limits. This
section describes the types of limit that you can enforce.

### Quota for infrastructure resources {#compute-resource-quota}

You can limit the total sum of
compute resources
that can be requested in a given namespace.

The following resource types are supported:

| Resource Name | Description |
| ------------- | ----------- |
| `limits.cpu` | Across all pods in a non-terminal state, the sum of CPU limits cannot exceed this value. |
| `limits.memory` | Across all pods in a non-terminal state, the sum of memory limits cannot exceed this value. |
| `requests.cpu` | Across all pods in a non-terminal state, the sum of CPU requests cannot exceed this value. |
| `requests.memory` | Across all pods in a non-terminal state, the sum of memory requests cannot exceed this value. |
| `hugepages-<size>` | Across all pods in a non-terminal state, the number of huge page requests of the specified size cannot exceed this value. |
| `cpu` | Same as `requests.cpu` |
| `memory` | Same as `requests.memory` |

### Quota for extended resources

In addition to the resources mentioned above, in release 1.10, quota support for
extended resources is added.

As overcommit is not allowed for extended resources, it makes no sense to specify both `requests`
and `limits` for the same extended resource in a quota. So for extended resources, only quota items
with prefix `requests.` are allowed.

Take the GPU resource as an example, if the resource name is `nvidia.com/gpu`, and you want to
limit the total number of GPUs requested in a namespace to 4, you can define a quota as follows:

* `requests.nvidia.com/gpu: 4`

See Viewing and Setting Quotas for more details.

### Quota for DRA resource claims

DRA (Dynamic Resource Allocation) resource claims can request DRA resources by device class. For an example
device class named `examplegpu`, you want to limit the total number of GPUs requested in a namespace to 4,
you can define a quota as follows:

* `examplegpu.deviceclass.resource.k8s.io/devices: 4`

When Extended Resource allocation by DRA
is enabled, the same device class named `examplegpu` can be requested via extended resource either explicitly
when the device class's ExtendedResourceName field is given, say, `example.com/gpu`, then you can define a quota as follows:

* `requests.example.com/gpu: 4`

or implicitly using the derived extended resource name from device class name `examplegpu`, you can define
a quota as follows:

* `requests.deviceclass.resource.kubernetes.io/examplegpu: 4`

All devices requested from resource claims or extended resources are counted towards all three quotas
listed above. The extended resource quota e.g. `requests.example.com/gpu: 4`, also counts the devices provided
by device plugin.

See Viewing and Setting Quotas for more details.

### Quota for storage

You can limit the total sum of storage for volumes
that can be requested in a given namespace.

In addition, you can limit consumption of storage resources based on associated
StorageClass.

| Resource Name | Description |
| ------------- | ----------- |
| `requests.storage` | Across all persistent volume claims, the sum of storage requests cannot exceed this value. |
| `persistentvolumeclaims` | The total number of PersistentVolumeClaims that can exist in the namespace. |
| `<storage-class-name>.storageclass.storage.k8s.io/requests.storage` | Across all persistent volume claims associated with the `<storage-class-name>`, the sum of storage requests cannot exceed this value. |
| `<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` | Across all persistent volume claims associated with the `<storage-class-name>`, the total number of persistent volume claims that can exist in the namespace. |

For example, if you want to quota storage with `gold` StorageClass separate from
a `bronze` StorageClass, you can define a quota as follows:

* `gold.storageclass.storage.k8s.io/requests.storage: 500Gi`
* `bronze.storageclass.storage.k8s.io/requests.storage: 100Gi`

#### Quota for local ephemeral storage

| Resource Name | Description |
| ------------- | ----------- |
| `requests.ephemeral-storage` | Across all pods in the namespace, the sum of local ephemeral storage requests cannot exceed this value. |
| `limits.ephemeral-storage` | Across all pods in the namespace, the sum of local ephemeral storage limits cannot exceed this value. |
| `ephemeral-storage` | Same as `requests.ephemeral-storage`. |

When using a CRI container runtime, container logs will count against the ephemeral storage quota.
This can result in the unexpected eviction of pods that have exhausted their storage quotas.

Refer to Logging Architecture for details.

### Quota on object count

You can set quota for *the total number of one particular resource kind* in the Kubernetes API,
using the following syntax:

* `count/<resource>.<group>` for resources from non-core API groups
* `count/<resource>` for resources from the core API group

For example, the PodTemplate API is in the core API group and so if you want to limit the number of
PodTemplate objects in a namespace, you use `count/podtemplates`.

These types of quotas are useful to protect against exhaustion of control plane storage. For example, you may
want to limit the number of Secrets in a server given their large size. Too many Secrets in a cluster can
actually prevent servers and controllers from starting. You can set a quota for Jobs to protect against
a poorly configured CronJob. CronJobs that create too many Jobs in a namespace can lead to a denial of service.

If you define a quota this way, it applies to Kubernetes' APIs that are part of the API server, and
to any custom resources backed by a CustomResourceDefinition.
For example, to create a quota on a `widgets` custom resource in the `example.com` API group,
use `count/widgets.example.com`.
If you use API aggregation to
add additional, custom APIs that are not defined as CustomResourceDefinitions, the core Kubernetes
control plane does not enforce quota for the aggregated API. The extension API server is expected to
provide quota enforcement if that's appropriate for the custom API.

##### Generic syntax {#resource-quota-object-count-generic}

This is a list of common examples of object kinds that you may want to put under object count quota,
listed by the configuration string that you would use.

* `count/pods`
* `count/persistentvolumeclaims`
* `count/services`
* `count/secrets`
* `count/configmaps`
* `count/deployments.apps`
* `count/replicasets.apps`
* `count/statefulsets.apps`
* `count/jobs.batch`
* `count/cronjobs.batch`

##### Specialized syntax {#resource-quota-object-count-specialized}

There is another syntax only to set the same type of quota, that only works for certain API kinds.
The following types are supported:

| Resource Name | Description |
| ------------- | ----------- |
| `configmaps` | The total number of ConfigMaps that can exist in the namespace. |
| `persistentvolumeclaims` | The total number of PersistentVolumeClaims that can exist in the namespace. |
| `pods` | The total number of Pods in a non-terminal state that can exist in the namespace. A pod is in a terminal state if `.status.phase in (Failed, Succeeded)` is true. |
| `replicationcontrollers` | The total number of ReplicationControllers that can exist in the namespace. |
| `resourcequotas` | The total number of ResourceQuotas that can exist in the namespace. |
| `services` | The total number of Services that can exist in the namespace. |
| `services.loadbalancers` | The total number of Services of type `LoadBalancer` that can exist in the namespace. |
| `services.nodeports` | The total number of `NodePorts` allocated to Services of type `NodePort` or `LoadBalancer` that can exist in the namespace. |
| `secrets` | The total number of Secrets that can exist in the namespace. |

For example, `pods` quota counts and enforces a maximum on the number of `pods`
created in a single namespace that are not terminal. You might want to set a `pods`
quota on a namespace to avoid the case where a user creates many small pods and
exhausts the cluster's supply of Pod IPs.

You can find more examples on Viewing and Setting Quotas.
