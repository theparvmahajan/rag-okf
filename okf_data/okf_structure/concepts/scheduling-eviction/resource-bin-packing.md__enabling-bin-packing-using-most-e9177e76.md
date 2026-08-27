---
id: okf-structure/concepts/scheduling-eviction/resource-bin-packing.md#enabling-bin-packing-using-mostallocated-strategy
kind: section
title: Enabling bin packing using MostAllocated strategy
source: concepts/scheduling-eviction/resource-bin-packing.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/
heading: Enabling bin packing using MostAllocated strategy
parent: okf-structure/concepts/scheduling-eviction/resource-bin-packing
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/resource-bin-packing.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/resource-bin-packing.md#enabling-bin-packing-using-requestedtocapacityratio
word_count: 177
---

The `MostAllocated` strategy scores the nodes based on the utilization of resources, favoring the ones with higher allocation.
For each resource type, you can set a weight to modify its influence in the node score.

To set the `MostAllocated` strategy for the `NodeResourcesFit` plugin, use a
scheduler configuration similar to the following:

```yaml
apiVersion: kubescheduler.config.k8s.io/v1
kind: KubeSchedulerConfiguration
profiles:
- pluginConfig:
  - args:
      scoringStrategy:
        resources:
        - name: cpu
          weight: 1
        - name: memory
          weight: 1
        - name: intel.com/foo
          weight: 3
        - name: intel.com/bar
          weight: 3
        type: MostAllocated
    name: NodeResourcesFit
```

With this configuration, nodes are scored using a weighted average of utilization across all four
resources. Because `intel.com/foo` and `intel.com/bar` each carry a weight of `3` versus `1` for
CPU and memory, the utilization of those extended resources has three times more influence on the
final node score. The scheduler selects the highest-scoring node, aiming to schedule pods on
highly utilized nodes. This helps prepare for scale-down of the least utilized nodes.

To learn more about other parameters and their default configuration, see the API documentation for
`NodeResourcesFitArgs`.
