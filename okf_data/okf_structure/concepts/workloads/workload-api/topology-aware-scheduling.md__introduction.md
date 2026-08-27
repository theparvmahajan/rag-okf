---
id: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling.md#introduction
kind: section
title: Topology-Aware Workload Scheduling
source: concepts/workloads/workload-api/topology-aware-scheduling.md
url: https://kubernetes.io/docs/concepts/workloads/workload-api/topology-aware-scheduling/
heading: null
parent: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/workload-api/topology-aware-scheduling.md#topology-aware-scheduling-with-gang-scheduling-policy
word_count: 55
---

*Topology-Aware Scheduling* (TAS) is a feature of the Workload API that optimizes the placement of
pods within the cluster.

TAS ensures that all pods within a PodGroup are co-located into a specific topology domain,
such as a single server rack or zone. This minimizes inter-pod communication latency and prevents
workload fragmentation across the cluster infrastructure.
