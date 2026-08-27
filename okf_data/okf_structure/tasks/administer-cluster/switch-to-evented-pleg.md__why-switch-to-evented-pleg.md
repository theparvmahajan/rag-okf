---
id: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#why-switch-to-evented-pleg
kind: section
title: Why switch to Evented PLEG?
source: tasks/administer-cluster/switch-to-evented-pleg.md
url: https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/
heading: Why switch to Evented PLEG?
parent: okf-structure/tasks/administer-cluster/switch-to-evented-pleg
children: []
prev_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#switching-to-evented-pleg
word_count: 54
---

* The _Generic PLEG_ incurs non-negligible overhead due to frequent polling of container statuses.
* This overhead is exacerbated by Kubelet's parallelized polling of container states, thus limiting
  its scalability and causing poor performance and reliability problems.
* The goal of _Evented PLEG_ is to reduce unnecessary work during inactivity
  by replacing periodic polling.
