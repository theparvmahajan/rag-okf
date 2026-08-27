---
id: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-policies
kind: section
title: Topology manager policies
source: tasks/administer-cluster/topology-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/topology-manager/
heading: Topology manager policies
parent: okf-structure/tasks/administer-cluster/topology-manager
children: []
prev_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-scopes
next_sibling: okf-structure/tasks/administer-cluster/topology-manager.md#topology-manager-policy-options
word_count: 457
---

The Topology Manager supports four allocation policies. You can set a policy via a kubelet flag,
`--topology-manager-policy`. There are four supported policies:

* `none` (default)
* `best-effort`
* `restricted`
* `single-numa-node`

If the Topology Manager is configured with the **pod** scope, the container, which is considered by
the policy, is reflecting requirements of the entire pod, and thus each container from the pod
will result with **the same** topology alignment decision.

### `none` policy {#policy-none}

This is the default policy and does not perform any topology alignment.

### `best-effort` policy {#policy-best-effort}

For each container in a Pod, the kubelet, with `best-effort` topology management policy, calls
each Hint Provider to discover their resource availability. Using this information, the Topology
Manager stores the preferred NUMA Node affinity for that container. If the affinity is not
preferred, the Topology Manager will store this and admit the pod to the node anyway.

The *Hint Providers* can then use this information when making the
resource allocation decision.

### `restricted` policy {#policy-restricted}

For each container in a Pod, the kubelet, with `restricted` topology management policy, calls each
Hint Provider to discover their resource availability. Using this information, the Topology
Manager stores the preferred NUMA Node affinity for that container. If the affinity is not
preferred, the Topology Manager will reject this pod from the node. This will result in a pod entering a
`Terminated` state with a pod admission failure.

Once the pod is in a `Terminated` state, the Kubernetes scheduler will **not** attempt to
reschedule the pod. It is recommended to use a ReplicaSet or Deployment to trigger a redeployment of
the pod. An external control loop could be also implemented to trigger a redeployment of pods that
have the `Topology Affinity` error.

If the pod is admitted, the *Hint Providers* can then use this information when making the
resource allocation decision.

### `single-numa-node` policy {#policy-single-numa-node}

For each container in a Pod, the kubelet, with `single-numa-node` topology management policy,
calls each Hint Provider to discover their resource availability. Using this information, the
Topology Manager determines if a single NUMA Node affinity is possible. If it is, Topology
Manager will store this and the *Hint Providers* can then use this information when making the
resource allocation decision. If, however, this is not possible then the Topology Manager will
reject the pod from the node. This will result in a pod in a `Terminated` state with a pod
admission failure.

Once the pod is in a `Terminated` state, the Kubernetes scheduler will **not** attempt to
reschedule the pod. It is recommended to use a Deployment with replicas to trigger a redeployment of
the Pod. An external control loop could be also implemented to trigger a redeployment of pods
that have the `Topology Affinity` error.
