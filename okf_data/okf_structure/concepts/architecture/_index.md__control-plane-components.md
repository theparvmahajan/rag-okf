---
id: okf-structure/concepts/architecture/_index.md#control-plane-components
kind: section
title: Control plane components
source: concepts/architecture/_index.md
url: https://kubernetes.io/docs/concepts/architecture/
heading: Control plane components
parent: okf-structure/concepts/architecture/_index
children: []
prev_sibling: okf-structure/concepts/architecture/_index.md#introduction
next_sibling: okf-structure/concepts/architecture/_index.md#node-components
word_count: 309
---

The control plane's components make global decisions about the cluster (for example, scheduling),
as well as detecting and responding to cluster events (for example, starting up a new
pod when a Deployment's
`replicas` field is unsatisfied).

Control plane components can be run on any machine in the cluster. However, for simplicity, setup scripts
typically start all control plane components on the same machine, and do not run user containers on this machine.
See Creating Highly Available clusters with kubeadm
for an example control plane setup that runs across multiple machines.

### kube-apiserver

### etcd

### kube-scheduler

### kube-controller-manager

There are many different types of controllers. Some examples of them are:

- Node controller: Responsible for noticing and responding when nodes go down.
- Job controller: Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion.
- EndpointSlice controller: Populates EndpointSlice objects (to provide a link between Services and Pods).
- ServiceAccount controller: Create default ServiceAccounts for new namespaces.

The above is not an exhaustive list.

### cloud-controller-manager

The cloud-controller-manager only runs controllers that are specific to your cloud provider.
If you are running Kubernetes on your own premises, or in a learning environment inside your
own PC, the cluster does not have a cloud controller manager.

As with the kube-controller-manager, the cloud-controller-manager combines several logically
independent control loops into a single binary that you run as a single process. You can scale
horizontally (run more than one copy) to improve performance or to help tolerate failures.

The following controllers can have cloud provider dependencies:

- Node controller: For checking the cloud provider to determine if a node has been
  deleted in the cloud after it stops responding
- Route controller: For setting up routes in the underlying cloud infrastructure
- Service controller: For creating, updating and deleting cloud provider load balancers

---
