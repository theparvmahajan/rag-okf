---
id: okf-structure/concepts/cluster-administration/node-autoscaling.md#node-provisioning-provisioning
kind: section
title: Node provisioning {#provisioning}
source: concepts/cluster-administration/node-autoscaling.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/
heading: Node provisioning {#provisioning}
parent: okf-structure/concepts/cluster-administration/node-autoscaling
children: []
prev_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/node-autoscaling.md#node-consolidation-consolidation
word_count: 435
---

If there are Pods in a cluster that can't be scheduled on existing Nodes, new Nodes can be
automatically added to the cluster—_provisioned_—to accommodate the Pods. This is
especially useful if the number of Pods changes over time, for example as a result of
combining horizontal workload with Node autoscaling.

Autoscalers provision the Nodes by creating and deleting cloud provider resources backing them. Most
commonly, the resources backing the Nodes are Virtual Machines.

The main goal of provisioning is to make all Pods schedulable. This goal is not always attainable
because of various limitations, including reaching configured provisioning limits, provisioning
configuration not being compatible with a particular set of pods, or the lack of cloud provider
capacity. While provisioning, Node autoscalers often try to achieve additional goals (for example
minimizing the cost of the provisioned Nodes or balancing the number of Nodes between failure
domains).

There are two main inputs to a Node autoscaler when determining Nodes to
provision—Pod scheduling constraints,
and Node constraints imposed by autoscaler configuration.

Autoscaler configuration may also include other Node provisioning triggers (for example the number
of Nodes falling below a configured minimum limit).

Provisioning was formerly known as _scale-up_ in Cluster Autoscaler.

### Pod scheduling constraints {#provisioning-pod-constraints}

Pods can express scheduling constraints to
impose limitations on the kind of Nodes they can be scheduled on. Node autoscalers take these
constraints into account to ensure that the pending Pods can be scheduled on the provisioned Nodes.

The most common kind of scheduling constraints are the resource requests specified by Pod
containers. Autoscalers will make sure that the provisioned Nodes have enough resources to satisfy
the requests. However, they don't directly take into account the real resource usage of the Pods
after they start running. In order to autoscale Nodes based on actual workload resource usage, you
can combine horizontal workload autoscaling with Node
autoscaling.

Other common Pod scheduling constraints include
Node affinity,
inter-Pod affinity,
or a requirement for a particular storage volume.

### Node constraints imposed by autoscaler configuration {#provisioning-node-constraints}

The specifics of the provisioned Nodes (for example the amount of resources, the presence of a given
label) depend on autoscaler configuration. Autoscalers can either choose them from a pre-defined set
of Node configurations, or use auto-provisioning.

### Auto-provisioning {#autoprovisioning}

Node auto-provisioning is a mode of provisioning in which a user doesn't have to fully configure the
specifics of the Nodes that can be provisioned. Instead, the autoscaler dynamically chooses the Node
configuration based on the pending Pods it's reacting to, as well as pre-configured constraints (for
example, the minimum amount of resources or the need for a given label).
