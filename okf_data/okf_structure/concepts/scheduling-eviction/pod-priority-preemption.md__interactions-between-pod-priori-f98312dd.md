---
id: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#interactions-between-pod-priority-and-quality-of-service-interactions-of-pod-priority-and-qos
kind: section
title: Interactions between Pod priority and quality of service {#interactions-of-pod-priority-and-qos}
source: concepts/scheduling-eviction/pod-priority-preemption.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/
heading: Interactions between Pod priority and quality of service {#interactions-of-pod-priority-and-qos}
parent: okf-structure/concepts/scheduling-eviction/pod-priority-preemption
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#troubleshooting
next_sibling: okf-structure/concepts/scheduling-eviction/pod-priority-preemption.md#whatsnext
word_count: 204
---

Pod priority and QoS class
are two orthogonal features with few interactions and no default restrictions on
setting the priority of a Pod based on its QoS classes. The scheduler's
preemption logic does not consider QoS when choosing preemption targets.
Preemption considers Pod priority and attempts to choose a set of targets with
the lowest priority. Higher-priority Pods are considered for preemption only if
the removal of the lowest priority Pods is not sufficient to allow the scheduler
to schedule the preemptor Pod, or if the lowest priority Pods are protected by
`PodDisruptionBudget`.

The kubelet uses Priority to determine pod order for node-pressure eviction.
You can use the QoS class to estimate the order in which pods are most likely
to get evicted. The kubelet ranks pods for eviction based on the following factors:

  1. Whether the starved resource usage exceeds requests
  1. Pod Priority
  1. Amount of resource usage relative to requests

See Pod selection for kubelet eviction
for more details.

kubelet node-pressure eviction does not evict Pods when their
usage does not exceed their requests. If a Pod with lower priority is not
exceeding its requests, it won't be evicted. Another Pod with higher priority
that exceeds its requests may be evicted.
