---
id: okf-structure/concepts/workloads/pods/probes.md#introduction
kind: section
title: Liveness, Readiness, and Startup Probes
source: concepts/workloads/pods/probes.md
url: https://kubernetes.io/docs/concepts/workloads/pods/probes/
heading: null
parent: okf-structure/concepts/workloads/pods/probes
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/probes.md#types-of-probe-types-of-probe
word_count: 65
---

Kubernetes lets you define _probes_ to continuously monitor the health
of containers in a Pod. A probe is a diagnostic performed periodically
by the kubelet on a container.
To perform a diagnostic, the kubelet either executes code within
the container or makes a network request.

Based on the probe results, Kubernetes can restart unhealthy containers
or stop sending traffic to containers that are not ready.
