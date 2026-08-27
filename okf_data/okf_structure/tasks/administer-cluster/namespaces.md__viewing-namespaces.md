---
id: okf-structure/tasks/administer-cluster/namespaces.md#viewing-namespaces
kind: section
title: Viewing namespaces
source: tasks/administer-cluster/namespaces.md
url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
heading: Viewing namespaces
parent: okf-structure/tasks/administer-cluster/namespaces
children: []
prev_sibling: okf-structure/tasks/administer-cluster/namespaces.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/namespaces.md#creating-a-new-namespace
word_count: 303
---

List the current namespaces in a cluster using:

```shell
kubectl get namespaces
```
```console
NAME              STATUS   AGE
default           Active   11d
kube-node-lease   Active   11d
kube-public       Active   11d
kube-system       Active   11d
```

Kubernetes starts with four initial namespaces:

* `default` The default namespace for objects with no other namespace
* `kube-node-lease` This namespace holds Lease objects associated with each node. Node leases allow the kubelet to send heartbeats so that the control plane can detect node failure.
* `kube-public` This namespace is created automatically and is readable by all users
  (including those not authenticated). This namespace is mostly reserved for cluster usage,
  in case that some resources should be visible and readable publicly throughout the whole cluster.
  The public aspect of this namespace is only a convention, not a requirement.
* `kube-system` The namespace for objects created by the Kubernetes system

You can also get the summary of a specific namespace using:

```shell
kubectl get namespaces <name>
```

Or you can get detailed information with:

```shell
kubectl describe namespaces <name>
```
```console
Name:           default
Labels:         <none>
Annotations:    <none>
Status:         Active

No resource quota.

Resource Limits
 Type       Resource    Min Max Default
 ----               --------    --- --- ---
 Container          cpu         -   -   100m
```

Note that these details show both resource quota (if present) as well as resource limit ranges.

Resource quota tracks aggregate usage of resources in the Namespace and allows cluster operators
to define *Hard* resource usage limits that a Namespace may consume.

A limit range defines min/max constraints on the amount of resources a single entity can consume in
a Namespace.

See Admission control: Limit Range

A namespace can be in one of two phases:

* `Active` the namespace is in use
* `Terminating` the namespace is being deleted, and cannot be used for new objects

For more details, see Namespace
in the API reference.
