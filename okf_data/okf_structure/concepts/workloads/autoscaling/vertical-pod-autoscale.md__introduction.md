---
id: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#introduction
kind: section
title: Vertical Pod Autoscaling
source: concepts/workloads/autoscaling/vertical-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/
heading: null
parent: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#api-object
word_count: 192
---

In Kubernetes, a _VerticalPodAutoscaler_ automatically updates a workload management resource (such as
a Deployment or
StatefulSet), with the
aim of automatically adjusting infrastructure resource
requests and limits to match actual usage.

Vertical scaling means that the response to increased resource demand is to assign more resources (for example: memory or CPU) 
to the Pods that are already running for the workload.
This is also known as _rightsizing_, or sometimes _autopilot_.
This is different from horizontal scaling, which for Kubernetes would mean deploying more Pods to distribute the load.

If the resource usage decreases, and the Pod resource requests are above optimal levels, 
the VerticalPodAutoscaler instructs the workload resource (the Deployment, StatefulSet, or other similar resource) 
to adjust resource requests back down, preventing resource waste.

The VerticalPodAutoscaler is implemented as a Kubernetes API resource and a 
controller.
The resource determines the behavior of the controller. 
The vertical pod autoscaling controller, running within the Kubernetes data plane,
periodically adjusts the resource requests and limits of its target (for example, a Deployment)
based on analysis of historical resource utilization,
the amount of resources available in the cluster, and real-time events such as out-of-memory (OOM) conditions.
