---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#metrics-and-observability
kind: section
title: Metrics and observability
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: Metrics and observability
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#limitations
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#whatsnext
word_count: 41
---

The kubelet exports two prometheus metrics specific to user-namespaces:
 * `started_user_namespaced_pods_total`: a counter that tracks the number of user namespaced pods that are attempted to be created.
 * `started_user_namespaced_pods_errors_total`: a counter that tracks the number of errors creating user namespaced pods.
