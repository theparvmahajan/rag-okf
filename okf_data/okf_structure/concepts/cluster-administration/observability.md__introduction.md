---
id: okf-structure/concepts/cluster-administration/observability.md#introduction
kind: section
title: Observability
source: concepts/cluster-administration/observability.md
url: https://kubernetes.io/docs/concepts/cluster-administration/observability/
heading: null
parent: okf-structure/concepts/cluster-administration/observability
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/observability.md#metrics
word_count: 127
---

In Kubernetes, observability is the process of collecting and analyzing metrics, logs, and traces—often referred to as the three pillars of observability—in order to obtain a better understanding of the internal state, performance, and health of the cluster.

Kubernetes control plane components, as well as many add-ons, generate and emit these signals. By aggregating and correlating them, you can gain a unified picture of the control plane, add-ons, and applications across the cluster.

Figure 1 outlines how cluster components emit the three primary signal types.

flowchart LR
    A[Cluster components] --> M[Metrics pipeline]
    A --> L[Log pipeline]
    A --> T[Trace pipeline]
    M --> S[(Storage and analysis)]
    L --> S
    T --> S
    S --> O[Operators and automation]

*Figure 1. High-level signals emitted by cluster components and their consumers.*
