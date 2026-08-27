---
id: okf-structure/tasks/administer-cluster/cpu-management-policies.md#configuring-cpu-management-policies
kind: section
title: Configuring CPU management policies
source: tasks/administer-cluster/cpu-management-policies.md
url: https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/
heading: Configuring CPU management policies
parent: okf-structure/tasks/administer-cluster/cpu-management-policies
children: []
prev_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/cpu-management-policies.md#windows-support
word_count: 87
---

By default, the kubelet uses CFS quota
to enforce pod CPU limits.  When the node runs many CPU-bound pods,
the workload can move to different CPU cores depending on
whether the pod is throttled and which CPU cores are available at
scheduling time. Many workloads are not sensitive to this migration and thus
work fine without any intervention.

However, in workloads where CPU cache affinity and scheduling latency
significantly affect workload performance, the kubelet allows alternative CPU
management policies to determine some placement preferences on the node.
