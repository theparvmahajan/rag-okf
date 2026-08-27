---
id: okf-structure/concepts/architecture/cloud-controller.md#cloud-controller-manager-functions-functions-of-the-ccm
kind: section
title: Cloud controller manager functions {#functions-of-the-ccm}
source: concepts/architecture/cloud-controller.md
url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
heading: Cloud controller manager functions {#functions-of-the-ccm}
parent: okf-structure/concepts/architecture/cloud-controller
children: []
prev_sibling: okf-structure/concepts/architecture/cloud-controller.md#design
next_sibling: okf-structure/concepts/architecture/cloud-controller.md#authorization
word_count: 271
---

The controllers inside the cloud controller manager include:

### Node controller

The node controller is responsible for updating Node objects
when new servers are created in your cloud infrastructure. The node controller obtains information about the
hosts running inside your tenancy with the cloud provider. The node controller performs the following functions:

1. Update a Node object with the corresponding server's unique identifier obtained from the cloud provider API.
1. Annotating and labelling the Node object with cloud-specific information, such as the region the node
   is deployed into and the resources (CPU, memory, etc) that it has available.
1. Obtain the node's hostname and network addresses.
1. Verifying the node's health. In case a node becomes unresponsive, this controller checks with
   your cloud provider's API to see if the server has been deactivated / deleted / terminated.
   If the node has been deleted from the cloud, the controller deletes the Node object from your Kubernetes
   cluster.

Some cloud provider implementations split this into a node controller and a separate node
lifecycle controller.

### Route controller

The route controller is responsible for configuring routes in the cloud
appropriately so that containers on different nodes in your Kubernetes
cluster can communicate with each other.

Depending on the cloud provider, the route controller might also allocate blocks
of IP addresses for the Pod network.

### Service controller

Services integrate with cloud
infrastructure components such as managed load balancers, IP addresses, network
packet filtering, and target health checking. The service controller interacts with your
cloud provider's APIs to set up load balancers and other infrastructure components
when you declare a Service resource that requires them.
