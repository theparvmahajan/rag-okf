---
id: okf-structure/concepts/security/hardening-guide/scheduler.md#disallow-labeling-nodes
kind: section
title: Disallow labeling nodes
source: concepts/security/hardening-guide/scheduler.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/scheduler/
heading: Disallow labeling nodes
parent: okf-structure/concepts/security/hardening-guide/scheduler
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/scheduler.md#scheduling-configurations-for-custom-schedulers
next_sibling: null
word_count: 30
---

A cluster administrator should ensure that cluster users cannot label the nodes. 
A malicious actor can use `nodeSelector` to schedule workloads on nodes where those workloads should not be present.
