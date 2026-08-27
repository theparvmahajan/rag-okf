---
id: okf-structure/concepts/workloads/controllers/statefulset.md#update-strategies
kind: section
title: Update strategies
source: concepts/workloads/controllers/statefulset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
heading: Update strategies
parent: okf-structure/concepts/workloads/controllers/statefulset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#deployment-and-scaling-guarantees
next_sibling: okf-structure/concepts/workloads/controllers/statefulset.md#rolling-updates
word_count: 96
---

A StatefulSet's `.spec.updateStrategy` field allows you to configure
and disable automated rolling updates for containers, labels, resource request/limits, and
annotations for the Pods in a StatefulSet. There are two possible values:

`OnDelete`
: When a StatefulSet's `.spec.updateStrategy.type` is set to `OnDelete`,
  the StatefulSet controller will not automatically update the Pods in a
  StatefulSet. Users must manually delete Pods to cause the controller to
  create new Pods that reflect modifications made to a StatefulSet's `.spec.template`.

`RollingUpdate`
: The `RollingUpdate` update strategy implements automated, rolling updates for the Pods in a
  StatefulSet. This is the default update strategy.
