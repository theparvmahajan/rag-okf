---
id: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#introduction
kind: section
title: HorizontalPodAutoscaler Walkthrough
source: tasks/run-application/horizontal-pod-autoscale-walkthrough.md
url: https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/
heading: null
parent: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/run-application/horizontal-pod-autoscale-walkthrough.md#prerequisites
word_count: 130
---

A HorizontalPodAutoscaler
(HPA for short)
automatically updates a workload resource (such as
a Deployment or
StatefulSet), with the
aim of automatically scaling the workload to match demand.

Horizontal scaling means that the response to increased load is to deploy more
Pods.
This is different from _vertical_ scaling, which for Kubernetes would mean
assigning more resources (for example: memory or CPU) to the Pods that are already
running for the workload.

If the load decreases, and the number of Pods is above the configured minimum,
the HorizontalPodAutoscaler instructs the workload resource (the Deployment, StatefulSet,
or other similar resource) to scale back down.

This document walks you through an example of enabling HorizontalPodAutoscaler to
automatically manage scale for an example web app. This example workload is Apache
httpd running some PHP code.
