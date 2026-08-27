---
id: okf-structure/setup/best-practices/cluster-large.md#control-plane-components
kind: section
title: Control plane components
source: setup/best-practices/cluster-large.md
url: https://kubernetes.io/docs/setup/best-practices/cluster-large/
heading: Control plane components
parent: okf-structure/setup/best-practices/cluster-large
children: []
prev_sibling: okf-structure/setup/best-practices/cluster-large.md#cloud-provider-resource-quotas-quota-issues
next_sibling: okf-structure/setup/best-practices/cluster-large.md#addon-resources
word_count: 248
---

For a large cluster, you need a control plane with sufficient compute and other
resources.

Typically you would run one or two control plane instances per failure zone,
scaling those instances vertically first and then scaling horizontally after reaching
the point of falling returns to (vertical) scale.

You should run at least one instance per failure zone to provide fault-tolerance. Kubernetes
nodes do not automatically steer traffic towards control-plane endpoints that are in the
same failure zone; however, your cloud provider might have its own mechanisms to do this.

For example, using a managed load balancer, you configure the load balancer to send traffic
that originates from the kubelet and Pods in failure zone _A_, and direct that traffic only
to the control plane hosts that are also in zone _A_. If a single control-plane host or
endpoint failure zone _A_ goes offline, that means that all the control-plane traffic for
nodes in zone _A_ is now being sent between zones. Running multiple control plane hosts in
each zone makes that outcome less likely.

### etcd storage

To improve performance of large clusters, you can store Event objects in a separate
dedicated etcd instance.

When creating a cluster, you can (using custom tooling):

* start and configure additional etcd instance
* configure the API server to use it for storing events

See Operating etcd clusters for Kubernetes and
Set up a High Availability etcd cluster with kubeadm
for details on configuring and managing etcd for a large cluster.
