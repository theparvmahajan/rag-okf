---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#topology-spread-constraint-examples
kind: section
title: Topology spread constraint examples
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: Topology spread constraint examples
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#consistency
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#implicit-conventions
word_count: 878
---

### Example: one topology spread constraint {#example-one-topologyspreadconstraint}

Suppose you have a 4-node cluster where 3 Pods labeled `foo: bar` are located in
node1, node2 and node3 respectively:

graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class zoneA,zoneB cluster;

If you want an incoming Pod to be evenly spread with existing Pods across zones, you
can use a manifest similar to:

From that manifest, `topologyKey: zone` implies the even distribution will only be applied
to nodes that are labeled `zone: <any value>` (nodes that don't have a `zone` label
are skipped). The field `whenUnsatisfiable: DoNotSchedule` tells the scheduler to let the
incoming Pod stay pending if the scheduler can't find a way to satisfy the constraint.

If the scheduler placed this incoming Pod into zone `A`, the distribution of Pods would
become `[3, 1]`. That means the actual skew is then 2 (calculated as `3 - 1`), which
violates `maxSkew: 1`. To satisfy the constraints and context for this example, the
incoming Pod can only be placed onto a node in zone `B`:

graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        p4(mypod) --> n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;

OR

graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        p4(mypod) --> n3
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;

You can tweak the Pod spec to meet various kinds of requirements:

- Change `maxSkew` to a bigger value - such as `2` -  so that the incoming Pod can
  be placed into zone `A` as well.
- Change `topologyKey` to `node` so as to distribute the Pods evenly across nodes
  instead of zones. In the above example, if `maxSkew` remains `1`, the incoming
  Pod can only be placed onto the node `node4`.
- Change `whenUnsatisfiable: DoNotSchedule` to `whenUnsatisfiable: ScheduleAnyway`
  to ensure the incoming Pod to be always schedulable (suppose other scheduling APIs
  are satisfied). However, it's preferred to be placed into the topology domain which
  has fewer matching Pods. (Be aware that this preference is jointly normalized
  with other internal scheduling priorities such as resource usage ratio).

### Example: multiple topology spread constraints {#example-multiple-topologyspreadconstraints}

This builds upon the previous example. Suppose you have a 4-node cluster where 3
existing Pods labeled `foo: bar` are located on node1, node2 and node3 respectively:

graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3 k8s;
    class p4 plain;
    class zoneA,zoneB cluster;

You can combine two topology spread constraints to control the spread of Pods both
by node and by zone:

In this case, to match the first constraint, the incoming Pod can only be placed onto
nodes in zone `B`; while in terms of the second constraint, the incoming Pod can only be
scheduled to the node `node4`. The scheduler only considers options that satisfy all
defined constraints, so the only valid placement is onto node `node4`.

### Example: conflicting topology spread constraints {#example-conflicting-topologyspreadconstraints}

Multiple constraints can lead to conflicts. Suppose you have a 3-node cluster across 2 zones:

graph BT
    subgraph "zoneB"
        p4(Pod) --> n3(Node3)
        p5(Pod) --> n3
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n1
        p3(Pod) --> n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4,p1,p2,p3,p4,p5 k8s;
    class zoneA,zoneB cluster;

If you were to apply
`two-constraints.yaml`
(the manifest from the previous example)
to **this** cluster, you would see that the Pod `mypod` stays in the `Pending` state.
This happens because: to satisfy the first constraint, the Pod `mypod` can only
be placed into zone `B`; while in terms of the second constraint, the Pod `mypod`
can only schedule to node `node2`. The intersection of the two constraints returns
an empty set, and the scheduler cannot place the Pod.

To overcome this situation, you can either increase the value of `maxSkew` or modify
one of the constraints to use `whenUnsatisfiable: ScheduleAnyway`. Depending on
circumstances, you might also decide to delete an existing Pod manually - for example,
if you are troubleshooting why a bug-fix rollout is not making progress.

#### Interaction with node affinity and node selectors

The scheduler will skip the non-matching nodes from the skew calculations if the
incoming Pod has `spec.nodeSelector` or `spec.affinity.nodeAffinity` defined.

### Example: topology spread constraints with node affinity {#example-topologyspreadconstraints-with-nodeaffinity}

Suppose you have a 5-node cluster ranging across zones A to C:

graph BT
    subgraph "zoneB"
        p3(Pod) --> n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        p1(Pod) --> n1(Node1)
        p2(Pod) --> n2(Node2)
    end

classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
class n1,n2,n3,n4,p1,p2,p3 k8s;
class p4 plain;
class zoneA,zoneB cluster;

graph BT
    subgraph "zoneC"
        n5(Node5)
    end

classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
class n5 k8s;
class zoneC cluster;

and you know that zone `C` must be excluded. In this case, you can compose a manifest
as below, so that Pod `mypod` will be placed into zone `B` instead of zone `C`.
Similarly, Kubernetes also respects `spec.nodeSelector`.
