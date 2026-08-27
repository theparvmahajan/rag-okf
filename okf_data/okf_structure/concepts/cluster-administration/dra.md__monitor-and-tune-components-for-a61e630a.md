---
id: okf-structure/concepts/cluster-administration/dra.md#monitor-and-tune-components-for-higher-load-especially-in-high-scale-environments
kind: section
title: Monitor and tune components for higher load, especially in high scale environments
source: concepts/cluster-administration/dra.md
url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
heading: Monitor and tune components for higher load, especially in high scale environments
parent: okf-structure/concepts/cluster-administration/dra
children: []
prev_sibling: okf-structure/concepts/cluster-administration/dra.md#dra-driver-deployment-and-maintenance
next_sibling: okf-structure/concepts/cluster-administration/dra.md#whatsnext
word_count: 715
---

Control plane component kube-scheduler and the internal ResourceClaim controller
orchestrated by the component kube-controller-manager do the
heavy lifting during scheduling of Pods with claims based on metadata stored in
the DRA APIs. Compared to non-DRA scheduled Pods, the number of API server
calls, memory, and CPU utilization needed by these components is increased for
Pods using DRA claims. In addition, node local components like the DRA driver
and kubelet utilize DRA APIs to allocated the hardware request at Pod sandbox
creation time. Especially in high scale environments where clusters have many
nodes, and/or deploy many workloads that heavily utilize DRA defined resource
claims, the cluster administrator should configure the relevant components to
anticipate the increased load. 

The effects of mistuned components can have direct or snowballing affects
causing different symptoms during the Pod lifecycle. If the `kube-scheduler`
component's QPS and burst configurations are too low, the scheduler might
quickly identify a suitable node for a Pod but take longer to bind the Pod to
that node. With DRA, during Pod scheduling, the QPS and Burst parameters in the
client-go configuration within `kube-controller-manager` are critical.

The specific values to tune your cluster to depend on a variety of factors like
number of nodes/pods, rate of pod creation, churn, even in non-DRA environments;
see the SIG Scalability README on Kubernetes scalability
 thresholds
for more information. In scale tests performed against a DRA enabled cluster
with 100 nodes, involving 720 long-lived pods (90% saturation) and 80 churn pods
(10% churn, 10 times), with a job creation QPS of 10, `kube-controller-manager`
QPS could be set to as low as 75 and Burst to 150 to meet equivalent metric
targets for non-DRA deployments. At this lower bound, it was observed that the
client side rate limiter was triggered enough to protect the API server from
explosive burst but was high enough that pod startup SLOs were not impacted.
While this is a good starting point, you can get a better idea of how to tune
the different components that have the biggest effect on DRA performance for
your deployment by monitoring the following metrics. For more information on all
the stable metrics in Kubernetes, see the Kubernetes Metrics
Reference.

### `kube-controller-manager` metrics

The following metrics look closely at the internal ResourceClaim controller
managed by the `kube-controller-manager` component.

* Workqueue Add Rate: Monitor  sum(rate(workqueue_adds_total{name="resource_claim"}[5m]))  to gauge how quickly items are added to the ResourceClaim controller.
* Workqueue Depth: Track
  sum(workqueue_depth{endpoint="kube-controller-manager",
  name="resource_claim"}) to identify any backlogs in the ResourceClaim
  controller.
* Workqueue Work Duration: Observe histogram_quantile(0.99,
  sum(rate(workqueue_work_duration_seconds_bucket{name="resource_claim"}[5m]))
  by (le)) to understand the speed at which the ResourceClaim controller
  processes work.

If you are experiencing low Workqueue Add Rate, high Workqueue Depth, and/or
high Workqueue Work Duration, this suggests the controller isn't performing
optimally. Consider tuning parameters like QPS, burst, and CPU/memory
configurations.

If you are experiencing high Workequeue Add Rate, high Workqueue Depth, but
reasonable Workqueue Work Duration, this indicates the controller is processing
work, but concurrency might be insufficient. Concurrency is hardcoded in the
controller, so as a cluster administrator, you can tune for this by reducing the
pod creation QPS, so the add rate to the resource claim workqueue is more
manageable.

### `kube-scheduler` metrics

The following scheduler metrics are high level metrics aggregating performance
across all Pods scheduled, not just those using DRA. It is important to note
that the end-to-end metrics are ultimately influenced by the
`kube-controller-manager`'s performance in creating ResourceClaims from
ResourceClainTemplates in deployments that heavily use ResourceClainTemplates.

* Scheduler End-to-End Duration: Monitor histogram_quantile(0.99,
  sum(increase(scheduler_pod_scheduling_sli_duration_seconds_bucket[5m])) by
  (le)).
* Scheduler Algorithm Latency: Track histogram_quantile(0.99,
  sum(increase(scheduler_scheduling_algorithm_duration_seconds_bucket[5m])) by
  (le)).

### `kubelet` metrics

When a Pod bound to a node must have a ResourceClaim satisfied, kubelet calls
the `NodePrepareResources` and `NodeUnprepareResources` methods of the DRA
driver. You can observe this behavior from the kubelet's point of view with the
following metrics.

* Kubelet NodePrepareResources: Monitor histogram_quantile(0.99,
  sum(rate(dra_operations_duration_seconds_bucket{operation_name="PrepareResources"}[5m]))
  by (le)).
* Kubelet NodeUnprepareResources: Track histogram_quantile(0.99,
  sum(rate(dra_operations_duration_seconds_bucket{operation_name="UnprepareResources"}[5m]))
  by (le)).

### DRA kubeletplugin operations

DRA drivers implement the `kubeletplugin` package
interface
which surfaces its own metric for the underlying gRPC operation
`NodePrepareResources` and `NodeUnprepareResources`. You can observe this
behavior from the point of view of the internal kubeletplugin with the following
metrics.

* DRA kubeletplugin gRPC NodePrepareResources operation: Observe histogram_quantile(0.99,
  sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodePrepareResources"}[5m]))
  by (le)).
* DRA kubeletplugin gRPC NodeUnprepareResources operation: Observe  histogram_quantile(0.99,
  sum(rate(dra_grpc_operations_duration_seconds_bucket{method_name=~".*NodeUnprepareResources"}[5m]))
  by (le)).
