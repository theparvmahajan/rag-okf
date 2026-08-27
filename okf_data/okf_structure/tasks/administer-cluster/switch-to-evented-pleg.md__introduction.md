---
id: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#introduction
kind: section
title: Switching from Polling to CRI Event-based Updates to Container Status
source: tasks/administer-cluster/switch-to-evented-pleg.md
url: https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/
heading: null
parent: okf-structure/tasks/administer-cluster/switch-to-evented-pleg
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/switch-to-evented-pleg.md#prerequisites
word_count: 70
---

This page shows how to migrate nodes to use event based updates for container status. The event-based
implementation reduces node resource consumption by the kubelet, compared to the legacy approach
that relies on polling.
You may know this feature as _evented Pod lifecycle event generator (PLEG)_. That's the name used
internally within the Kubernetes project for a key implementation detail.

The polling based approach is referred to as _generic PLEG_.
