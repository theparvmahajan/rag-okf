---
id: okf-structure/concepts/policy/resource-quotas.md#quota-scopes
kind: section
title: Quota scopes
source: concepts/policy/resource-quotas.md
url: https://kubernetes.io/docs/concepts/policy/resource-quotas/
heading: Quota scopes
parent: okf-structure/concepts/policy/resource-quotas
children: []
prev_sibling: okf-structure/concepts/policy/resource-quotas.md#quota-and-cluster-capacity
next_sibling: okf-structure/concepts/policy/resource-quotas.md#whatsnext
word_count: 1437
---

Each quota can have an associated set of `scopes`. A quota will only measure usage for a resource if it matches
the intersection of enumerated scopes.

When a scope is added to the quota, it limits the number of resources it supports to those that pertain to the scope.
Resources specified on the quota outside of the allowed set results in a validation error.

Kubernetes  supports the following scopes:

| Scope | Description |
| ----- | ----------- |
| `BestEffort` | Match pods that have best effort quality of service. |
| `CrossNamespacePodAffinity` | Match pods that have cross-namespace pod (anti)affinity terms. |
| `NotBestEffort` | Match pods that do not have best effort quality of service. |
| `NotTerminating` | Match pods where `.spec.activeDeadlineSeconds` is `nil` |
| `PriorityClass` | Match pods that references the specified priority class. |
| `Terminating` | Match pods where `.spec.activeDeadlineSeconds` >= `0` |
| `VolumeAttributesClass` | Match PersistentVolumeClaims that reference the specified volume attributes class. |

ResourceQuotas with a scope set can also have a optional `scopeSelector` field. You define one or more _match expressions_
that specify an `operators` and, if relevant, a set of `values` to match. For example:

```yaml
  scopeSelector:
    matchExpressions:
      - scopeName: BestEffort # Match pods that have best effort quality of service
        operator: Exists # optional; "Exists" is implied for BestEffort scope
```

The `scopeSelector` supports the following values in the `operator` field:

* `In`
* `NotIn`
* `Exists`
* `DoesNotExist`

If the `operator` is `In` or `NotIn`, the `values` field must have at least
one value. For example:

```yaml
  scopeSelector:
    matchExpressions:
      - scopeName: PriorityClass
        operator: In
        values:
          - middle
```

If the `operator` is `Exists` or `DoesNotExist`, the `values` field must *NOT* be
specified.

### Best effort Pods scope {#quota-scope-best-effort}

This scope only tracks quota consumed by Pods.
It only matches pods that have the best effort
QoS class.

The `operator` for a `scopeSelector` must be `Exists`.

### Not-best-effort Pods scope {#quota-scope-non-best-effort}

This scope only tracks quota consumed by Pods.
It only matches pods that have the Guaranteed
or Burstable
QoS class.

The `operator` for a `scopeSelector` must be `Exists`.

### Non-terminating Pods scope {#quota-scope-non-terminating}

This scope only tracks quota consumed by Pods that are not terminating. The `operator` for a `scopeSelector`
must be `Exists`.

A Pod is not terminating if the `.spec.activeDeadlineSeconds` field is unset.

You can use a ResourceQuota with this scope to manage the following resources:

* `count.pods`
* `pods`
* `cpu`
* `memory`
* `requests.cpu`
* `requests.memory`
* `limits.cpu`
* `limits.memory`

### Terminating Pods scope {#quota-scope-terminating}

This scope only tracks quota consumed by Pods that are terminating. The `operator` for a `scopeSelector`
must be `Exists`.

A Pod is considered as _terminating_ if the `.spec.activeDeadlineSeconds` field is set to any number.

You can use a ResourceQuota with this scope to manage the following resources:

* `count.pods`
* `pods`
* `cpu`
* `memory`
* `requests.cpu`
* `requests.memory`
* `limits.cpu`
* `limits.memory`

### Cross-namespace pod affinity scope
 

You can use `CrossNamespacePodAffinity` quota scope to limit which namespaces are allowed to
have pods with affinity terms that cross namespaces. Specifically, it controls which pods are allowed
to set `namespaces` or `namespaceSelector` fields in pod (anti)affinity terms.

Preventing users from using cross-namespace affinity terms might be desired since a pod
with anti-affinity constraints can block pods from all other namespaces
from getting scheduled in a failure domain.

Using this scope, you (as a cluster administrator) can prevent certain namespaces - such as `foo-ns` in the example below -
from having pods that use cross-namespace pod affinity. You configure this creating a ResourceQuota object in
that namespace with `CrossNamespacePodAffinity` scope and hard limit of 0:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: disable-cross-namespace-affinity
  namespace: foo-ns
spec:
  hard:
    pods: "0"
  scopeSelector:
    matchExpressions:
    - scopeName: CrossNamespacePodAffinity
      operator: Exists
```

If you want to disallow using `namespaces` and `namespaceSelector` by default, and
only allow it for specific namespaces, you could configure `CrossNamespacePodAffinity`
as a limited resource by setting the kube-apiserver flag `--admission-control-config-file`
to the path of the following configuration file:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: "ResourceQuota"
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: ResourceQuotaConfiguration
    limitedResources:
    - resource: pods
      matchScopes:
      - scopeName: CrossNamespacePodAffinity
        operator: Exists
```

With the above configuration, pods can use `namespaces` and `namespaceSelector` in pod affinity only
if the namespace where they are created have a resource quota object with
`CrossNamespacePodAffinity` scope and a hard limit greater than or equal to the number of pods using those fields.

### PriorityClass scope {#resource-quota-per-priorityclass}

A ResourceQuota with a PriorityClass scope only matches Pods that have a particular
priority class, and only
if any `scopeSelector` in the quota spec selects a particular Pod.

Pods can be created at a specific priority.
You can control a pod's consumption of system resources based on a pod's priority, by using the `scopeSelector`
field in the quota spec.

When quota is scoped for PriorityClass using the `scopeSelector` field, the ResourceQuota
can only track (and limit) the following resources:

* `pods`
* `cpu`
* `memory`
* `ephemeral-storage`
* `limits.cpu`
* `limits.memory`
* `limits.ephemeral-storage`
* `requests.cpu`
* `requests.memory`
* `requests.ephemeral-storage`

#### Example {#quota-scope-priorityclass-example}

This example creates a ResourceQuota matches it with pods at specific priorities. The example
works as follows:

- Pods in the cluster have one of the three PriorityClasses, "low", "medium", "high".
  - If you want to try this out, use a testing cluster and set up those three PriorityClasses before you continue.
- One quota object is created for each priority.

Inspect this set of ResourceQuotas:

Apply the YAML using `kubectl create`.

```shell
kubectl create -f https://k8s.io/examples/policy/quota.yaml
```

```
resourcequota/pods-high created
resourcequota/pods-medium created
resourcequota/pods-low created
```

Verify that `Used` quota is `0` using `kubectl describe quota`.

```shell
kubectl describe quota
```

```
Name:       pods-high
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     1k
memory      0     200Gi
pods        0     10

Name:       pods-low
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     5
memory      0     10Gi
pods        0     10

Name:       pods-medium
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     10
memory      0     20Gi
pods        0     10
```

Create a pod with priority "high".

To create the Pod:

```shell
kubectl create -f https://k8s.io/examples/policy/high-priority-pod.yaml

```

Verify that "Used" stats for "high" priority quota, `pods-high`, has changed and that
the other two quotas are unchanged.

```shell
kubectl describe quota
```

```
Name:       pods-high
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         500m  1k
memory      10Gi  200Gi
pods        1     10

Name:       pods-low
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     5
memory      0     10Gi
pods        0     10

Name:       pods-medium
Namespace:  default
Resource    Used  Hard
--------    ----  ----
cpu         0     10
memory      0     20Gi
pods        0     10
```

#### Limiting PriorityClass consumption by default

It may be desired that pods at a particular priority, such as "cluster-services",
should be allowed in a namespace, if and only if, a matching quota object exists.

With this mechanism, operators are able to restrict usage of certain high
priority classes to a limited number of namespaces and not every namespace
will be able to consume these priority classes by default.

To enforce this, `kube-apiserver` flag `--admission-control-config-file` should be
used to pass path to the following configuration file:

```yaml
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
- name: "ResourceQuota"
  configuration:
    apiVersion: apiserver.config.k8s.io/v1
    kind: ResourceQuotaConfiguration
    limitedResources:
    - resource: pods
      matchScopes:
      - scopeName: PriorityClass
        operator: In
        values: ["cluster-services"]
```

Then, create a resource quota object in the `kube-system` namespace:

```shell
kubectl apply -f https://k8s.io/examples/policy/priority-class-resourcequota.yaml -n kube-system
```

```none
resourcequota/pods-cluster-services created
```

In this case, a pod creation will be allowed if:

1. the Pod's `priorityClassName` is not specified.
1. the Pod's `priorityClassName` is specified to a value other than `cluster-services`.
1. the Pod's `priorityClassName` is set to `cluster-services`, it is to be created
   in the `kube-system` namespace, and it has passed the resource quota check.

A Pod creation request is rejected if its `priorityClassName` is set to `cluster-services`
and it is to be created in a namespace other than `kube-system`.

### VolumeAttributesClass scope {#quota-scope-volume-attributes-class}

This scope only tracks quota consumed by PersistentVolumeClaims.

PersistentVolumeClaims can be created with a specific
VolumeAttributesClass, and might be modified after creation.
You can control a PVC's consumption of storage resources based on the associated
VolumeAttributesClasses, by using the `scopeSelector` field in the quota spec.

The PVC references the associated VolumeAttributesClass by the following fields:

* `spec.volumeAttributesClassName`
* `status.currentVolumeAttributesClassName`
* `status.modifyVolumeStatus.targetVolumeAttributesClassName`

A relevant ResourceQuota is matched and consumed only if the ResourceQuota has a `scopeSelector` that selects the PVC.

When the quota is scoped for the volume attributes class using the `scopeSelector` field, the quota object is restricted to track only the following resources:

* `persistentvolumeclaims`
* `requests.storage`

Read Limit Storage Consumption to learn more about this.
