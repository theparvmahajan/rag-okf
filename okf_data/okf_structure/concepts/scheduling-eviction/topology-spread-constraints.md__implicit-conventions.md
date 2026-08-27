---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#implicit-conventions
kind: section
title: Implicit conventions
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: Implicit conventions
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#topology-spread-constraint-examples
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#cluster-level-default-constraints
word_count: 246
---

There are some implicit conventions worth noting here:

- Only the Pods holding the same namespace as the incoming Pod can be matching candidates.

- The scheduler only considers nodes that have all `topologySpreadConstraints[*].topologyKey` present at the same time.
  Nodes missing any of these `topologyKeys` are bypassed. This implies that:

  1. any Pods located on those bypassed nodes do not impact `maxSkew` calculation - in the
     above example, suppose the node `node1`
     does not have a label "zone", then the 2 Pods will
     be disregarded, hence the incoming Pod will be scheduled into zone `A`.
  2. the incoming Pod has no chances to be scheduled onto this kind of nodes -
     in the above example, suppose a node `node5` has the **mistyped** label `zone-typo: zoneC`
     (and no `zone` label set). After node `node5` joins the cluster, it will be bypassed and
     Pods for this workload aren't scheduled there.

- Be aware of what will happen if the incoming Pod's
  `topologySpreadConstraints[*].labelSelector` doesn't match its own labels. In the
  above example, if you remove the incoming Pod's labels, it can still be placed onto
  nodes in zone `B`, since the constraints are still satisfied. However, after that
  placement, the degree of imbalance of the cluster remains unchanged - it's still zone `A`
  having 2 Pods labeled as `foo: bar`, and zone `B` having 1 Pod labeled as
  `foo: bar`. If this is not what you expect, update the workload's
  `topologySpreadConstraints[*].labelSelector` to match the labels in the pod template.
