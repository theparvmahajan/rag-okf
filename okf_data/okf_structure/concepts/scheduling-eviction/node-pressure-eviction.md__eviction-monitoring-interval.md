---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#eviction-monitoring-interval
kind: section
title: Eviction monitoring interval
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: Eviction monitoring interval
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#eviction-signals-and-thresholds
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#node-conditions-node-conditions
word_count: 14
---

The kubelet evaluates eviction thresholds based on its configured `housekeeping-interval`,
which defaults to `10s`.
