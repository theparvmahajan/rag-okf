---
id: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#configuring-pod-schedulinggates
kind: section
title: Configuring Pod schedulingGates
source: concepts/scheduling-eviction/pod-scheduling-readiness.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
heading: Configuring Pod schedulingGates
parent: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/pod-scheduling-readiness.md#usage-example
word_count: 63
---

The `schedulingGates` field contains a list of strings, and each string literal is perceived as a
criteria that Pod should be satisfied before considered schedulable. This field can be initialized
only when a Pod is created (either by the client, or mutated during admission). After creation,
each schedulingGate can be removed in arbitrary order, but addition of a new scheduling gate is disallowed.
