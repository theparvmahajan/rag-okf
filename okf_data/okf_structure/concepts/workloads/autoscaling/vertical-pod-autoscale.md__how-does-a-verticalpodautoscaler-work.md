---
id: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#how-does-a-verticalpodautoscaler-work
kind: section
title: How does a VerticalPodAutoscaler work?
source: concepts/workloads/autoscaling/vertical-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/
heading: How does a VerticalPodAutoscaler work?
parent: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#api-object
next_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#update-modes
word_count: 454
---

Kubernetes implements vertical pod autoscaling through multiple cooperating components that run intermittently (it is not a continuous process). The VPA consists of three main components: 

* The _recommender_, which analyzes resource usage and provides recommendations.
* The _updater_, that Pod resource requests either by evicting Pods or modifying them in place.
* And the VPA _admission controller_ webhook, which applies resource recommendations to new or recreated Pods.

Once during each period, the Recommender queries the resource utilization for Pods targeted by each VerticalPodAutoscaler definition. The Recommender finds the target resource defined by the `targetRef`, then selects the pods based on the target resource's `.spec.selector` labels, and obtains the metrics from the resource metrics API to analyze actual CPU and memory consumption.

The Recommender analyzes both current and historical resource usage data (CPU and memory) for each Pod targeted by the VerticalPodAutoscaler. It examines:
- Historical consumption patterns over time to identify trends
- Peak usage and variance to ensure sufficient headroom
- Out-of-memory (OOM) events and other resource-related incidents

Based on this analysis, the Recommender calculates three types of recommendations:
- Target recommendation (optimal resources for typical usage)
- Lower bound (minimum viable resources)
- Upper bound (maximum reasonable resources).

These recommendations are stored in the VerticalPodAutoscaler resource's `.status.recommendation` field.

The _updater_ component monitors the VerticalPodAutoscaler resources and compares current Pod resource requests with the recommendations. When the difference exceeds configured thresholds and the update policy allows it, the updater can either:

- Evict Pods, triggering their recreation with new resource requests (traditional approach)
- Update Pod resources in place without eviction, when the cluster supports in-place Pod resource updates

The chosen method depends on the configured update mode, cluster capabilities, and the type of resource change needed. In-place updates, when available, avoid Pod disruption but may have limitations on which resources can be modified. The updater respects PodDisruptionBudgets to minimize service impact.

The _admission controller_ operates as a mutating webhook that intercepts Pod creation requests. It
checks if the Pod is targeted by a VerticalPodAutoscaler and, if so, applies the recommended
resource requests and limits before the Pod is created. More specifically, the admission controller uses the Target recommendation in the VerticalPodAutoscaler resource's `.status.recommendation` stanza as the new resource requests. The admission controller ensures new Pods start with appropriately sized resource allocations, whether they're created during initial deployment, after an eviction by the updater, or due to scaling operations.

The VerticalPodAutoscaler requires a metrics source, such as Kubernetes' Metrics Server add-on,
to be installed in the cluster.
The VPA components fetch metrics from the `metrics.k8s.io` API. The Metrics Server needs to be launched separately as it is not deployed by default in most clusters. For more information about resource metrics, see Metrics Server.
