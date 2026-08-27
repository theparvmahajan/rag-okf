---
id: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#node-out-of-memory-behavior
kind: section
title: Node out of memory behavior
source: concepts/scheduling-eviction/node-pressure-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/
heading: Node out of memory behavior
parent: okf-structure/concepts/scheduling-eviction/node-pressure-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#node-conditions-node-conditions
next_sibling: okf-structure/concepts/scheduling-eviction/node-pressure-eviction.md#good-practices-node-pressure-eviction-good-practices
word_count: 182
---

If the node experiences an _out of memory_ (OOM) event prior to the kubelet
being able to reclaim memory, the node depends on the oom_killer
to respond.

The kubelet sets an `oom_score_adj` value for each container based on the QoS for the pod.

| Quality of Service | `oom_score_adj`                                                                   |
|--------------------|-----------------------------------------------------------------------------------|
| `Guaranteed`       | -997                                                                              |
| `BestEffort`       | 1000                                                                              |
| `Burstable`        | _min(max(2, 1000 - (1000 × memoryRequestBytes) / machineMemoryCapacityBytes), 999)_ |

The kubelet also sets an `oom_score_adj` value of `-997` for any containers in Pods that have
`system-node-critical` Priority.

If the kubelet can't reclaim memory before a node experiences OOM, the
`oom_killer` calculates an `oom_score` based on the percentage of memory it's
using on the node, and then adds the `oom_score_adj` to get an effective `oom_score`
for each container. It then kills the container with the highest score.

This means that containers in low QoS pods that consume a large amount of memory
relative to their scheduling requests are killed first.

Unlike pod eviction, if a container is OOM killed, the kubelet can restart it
based on its `restartPolicy`.
