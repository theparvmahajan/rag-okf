---
id: okf-structure/tasks/debug/debug-application/debug-service.md#any-network-policy-ingress-rules-affecting-the-target-pods
kind: section
title: Any Network Policy Ingress rules affecting the target Pods?
source: tasks/debug/debug-application/debug-service.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-service/
heading: Any Network Policy Ingress rules affecting the target Pods?
parent: okf-structure/tasks/debug/debug-application/debug-service
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#does-the-service-exist
next_sibling: okf-structure/tasks/debug/debug-application/debug-service.md#does-the-service-work-by-dns-name
word_count: 30
---

If you have deployed any Network Policy Ingress rules which may affect incoming
traffic to `hostnames-*` Pods, these need to be reviewed.

Please refer to Network Policies for more details.
