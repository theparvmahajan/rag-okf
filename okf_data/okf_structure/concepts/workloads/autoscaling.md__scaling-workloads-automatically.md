---
id: okf-structure/concepts/workloads/autoscaling.md#scaling-workloads-automatically
kind: section
title: Scaling workloads automatically
source: concepts/workloads/autoscaling.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/
heading: Scaling workloads automatically
parent: okf-structure/concepts/workloads/autoscaling
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling.md#scaling-workloads-manually
next_sibling: okf-structure/concepts/workloads/autoscaling.md#scaling-cluster-infrastructure
word_count: 508
---

Kubernetes also supports _automatic scaling_ of workloads, which is the focus of this page.

The concept of _Autoscaling_ in Kubernetes refers to the ability to automatically update an
object that manages a set of Pods (for example a
Deployment).

### Scaling workloads horizontally

In Kubernetes, you can automatically scale a workload horizontally using a HorizontalPodAutoscaler (HPA).

It is implemented as a Kubernetes API resource and a controller
and periodically adjusts the number of replicas
in a workload to match observed resource utilization such as CPU or memory usage.

There is a walkthrough tutorial of configuring a HorizontalPodAutoscaler for a Deployment.

### Scaling workloads vertically

You can automatically scale a workload vertically using a VerticalPodAutoscaler (VPA).
Unlike the HPA, the VPA doesn't come with Kubernetes by default, but is a an add-on that you or a cluster administrator may need to deploy before you can use it.

Once installed, it allows you to create CustomResourceDefinitions
(CRDs) for your workloads which define _how_ and _when_ to scale the resources of the managed replicas.

You will need to have the Metrics Server
installed to your cluster for the VPA to work.

#### In-place pod vertical scaling

As of Kubernetes , VPA does not support resizing pods in-place,
but this integration is being worked on.
For manually resizing pods in-place, see Resize Container Resources In-Place.

### Autoscaling based on cluster size

For workloads that need to be scaled based on the size of the cluster (for example
`cluster-dns` or other system components), you can use the
_Cluster Proportional Autoscaler_.
Just like the VPA, it is not part of the Kubernetes core, but hosted as its
own project on GitHub.

The Cluster Proportional Autoscaler watches the number of schedulable nodes
and cores and scales the number of replicas of the target workload accordingly.

If the number of replicas should stay the same, you can scale your workloads vertically according to the cluster size using
the _Cluster Proportional Vertical Autoscaler_.
The project is **currently in beta** and can be found on GitHub.

While the Cluster Proportional Autoscaler scales the number of replicas of a workload,
the Cluster Proportional Vertical Autoscaler adjusts the resource requests for a workload
(for example a Deployment or DaemonSet) based on the number of nodes and/or cores in the cluster.

### Event driven Autoscaling

It is also possible to scale workloads based on events, for example using the
_Kubernetes Event Driven Autoscaler_ (**KEDA**).

KEDA is a CNCF-graduated project enabling you to scale your workloads based on the number
of events to be processed, for example the amount of messages in a queue. There exists
a wide range of adapters for different event sources to choose from.

### Autoscaling based on schedules

Another strategy for scaling your workloads is to **schedule** the scaling operations, for example in order to
reduce resource consumption during off-peak hours.

Similar to event driven autoscaling, such behavior can be achieved using KEDA in conjunction with
its `Cron` scaler.
The `Cron` scaler allows you to define schedules (and time zones) for scaling your workloads in or out.
