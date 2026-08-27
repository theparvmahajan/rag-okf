---
id: okf-structure/setup/best-practices/cluster-large.md#prioritizing-cluster-essential-components
kind: section
title: Prioritizing cluster-essential components
source: setup/best-practices/cluster-large.md
url: https://kubernetes.io/docs/setup/best-practices/cluster-large/
heading: Prioritizing cluster-essential components
parent: okf-structure/setup/best-practices/cluster-large
children: []
prev_sibling: okf-structure/setup/best-practices/cluster-large.md#addon-resources
next_sibling: okf-structure/setup/best-practices/cluster-large.md#whatsnext
word_count: 36
---

To ensure cluster-essential components (such as CoreDNS, metrics-server, and other critical add-ons) are scheduled ahead of other workloads and are not preempted by lower-priority pods, run them with a system PriorityClass, such as `system-cluster-critical` or `system-node-critical`.
