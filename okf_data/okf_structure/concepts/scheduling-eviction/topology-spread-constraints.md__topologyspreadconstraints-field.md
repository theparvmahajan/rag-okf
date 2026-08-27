---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#topologyspreadconstraints-field
kind: section
title: '`topologySpreadConstraints` field'
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: '`topologySpreadConstraints` field'
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#motivation
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#consistency
word_count: 1285
---

The Pod API includes a field, `spec.topologySpreadConstraints`. The usage of this field looks like
the following:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: example-pod
spec:
  # Configure a topology spread constraint
  topologySpreadConstraints:
    - maxSkew: <integer>
      minDomains: <integer> # optional
      topologyKey: <string>
      whenUnsatisfiable: <string>
      labelSelector: <object>
      matchLabelKeys: <list> # optional; beta since v1.27
      nodeAffinityPolicy: [Honor|Ignore] # optional; beta since v1.26
      nodeTaintsPolicy: [Honor|Ignore] # optional; beta since v1.26
  ### other Pod fields go here
```

There can only be one `topologySpreadConstraint` for a given `topologyKey` and `whenUnsatisfiable` value. For example, if you have defined a `topologySpreadConstraint` that uses the `topologyKey` "kubernetes.io/hostname" and `whenUnsatisfiable` value "DoNotSchedule", you can only add another `topologySpreadConstraint` for the `topologyKey` "kubernetes.io/hostname" if you use a different `whenUnsatisfiable` value.

You can read more about this field by running `kubectl explain Pod.spec.topologySpreadConstraints` or
refer to the scheduling section of the API reference for Pod.

### Spread constraint definition

You can define one or multiple `topologySpreadConstraints` entries to instruct the
kube-scheduler how to place each incoming Pod in relation to the existing Pods across
your cluster. Those fields are:

- **maxSkew** describes the degree to which Pods may be unevenly distributed. You must
  specify this field and the number must be greater than zero. Its semantics differ
  according to the value of `whenUnsatisfiable`:

  - if you select `whenUnsatisfiable: DoNotSchedule`, then `maxSkew` defines the
    maximum permitted difference between the number of matching pods in the target
    topology and the _global minimum_
    (the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains).
    For example, if you have 3 zones with 2, 2 and 1 matching pods respectively,
    `MaxSkew` is set to 1 then the global minimum is 1.
  - if you select `whenUnsatisfiable: ScheduleAnyway`, the scheduler gives higher
    precedence to topologies that would help reduce the skew.

- **minDomains** indicates a minimum number of eligible domains. This field is optional.
  A domain is a particular instance of a topology. An eligible domain is a domain whose
  nodes match the node selector.

  
  
  Before Kubernetes v1.30, the `minDomains` field was only available if the
  `MinDomainsInPodTopologySpread` feature gate
  was enabled (default since v1.28). In older Kubernetes clusters it might be explicitly
  disabled or the field might not be available.
  

  - The value of `minDomains` must be greater than 0, when specified.
    You can only specify `minDomains` in conjunction with `whenUnsatisfiable: DoNotSchedule`.
  - When the number of eligible domains with match topology keys is less than `minDomains`,
    Pod topology spread treats global minimum as 0, and then the calculation of `skew` is performed.
    The global minimum is the minimum number of matching Pods in an eligible domain,
    or zero if the number of eligible domains is less than `minDomains`.
  - When the number of eligible domains with matching topology keys equals or is greater than
    `minDomains`, this value has no effect on scheduling.
  - If you do not specify `minDomains`, the constraint behaves as if `minDomains` is 1.

- **topologyKey** is the key of node labels. Nodes that have a label with this key
	and identical values are considered to be in the same topology.
  We call each instance of a topology (in other words, a <key, value> pair) a domain. The scheduler
  will try to put a balanced number of pods into each domain.
	Also, we define an eligible domain as a domain whose nodes meet the requirements of
	nodeAffinityPolicy and nodeTaintsPolicy.

- **whenUnsatisfiable** indicates how to deal with a Pod if it doesn't satisfy the spread constraint:
  - `DoNotSchedule` (default) tells the scheduler not to schedule it.
  - `ScheduleAnyway` tells the scheduler to still schedule it while prioritizing nodes that minimize the skew.

- **labelSelector** is used to find matching Pods. Pods
  that match this label selector are counted to determine the
  number of Pods in their corresponding topology domain.
  See Label Selectors
  for more details.

- **matchLabelKeys** is a list of pod label keys to select the group of pods over which 
  the spreading skew will be calculated. At a pod creation, 
  the kube-apiserver uses those keys to lookup values from the incoming pod labels,
  and those key-value labels will be merged with any existing `labelSelector`.
  The same key is forbidden to exist in both `matchLabelKeys` and `labelSelector`. 
  `matchLabelKeys` cannot be set when `labelSelector` isn't set. 
  Keys that don't exist in the pod labels will be ignored. 
  A null or empty list means only match against the `labelSelector`.

  
  It's not recommended to use `matchLabelKeys` with labels that might be updated directly on pods.
  Even if you edit the pod's label that is specified at `matchLabelKeys` **directly**,
  (that is, you edit the Pod and not a Deployment),
  kube-apiserver doesn't reflect the label update onto the merged `labelSelector`.
  

  With `matchLabelKeys`, you don't need to update the `pod.spec` between different revisions.
  The controller/operator just needs to set different values to the same label key for different
  revisions. For example, if you are configuring a Deployment, you can use the label keyed with
  pod-template-hash, which
  is added automatically by the Deployment controller, to distinguish between different revisions
  in a single Deployment.

  ```yaml
      topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: DoNotSchedule
            labelSelector:
              matchLabels:
                app: foo
            matchLabelKeys:
              - pod-template-hash
  ```

  
  The `matchLabelKeys` field is a beta-level field and enabled by default in 1.27. You can disable it by disabling the
  `MatchLabelKeysInPodTopologySpread` feature gate.

  Before v1.34, `matchLabelKeys` was handled implicitly.
  Since v1.34, key-value labels corresponding to `matchLabelKeys` are explicitly merged into `labelSelector`.
  You can disable it and revert to the previous behavior by disabling the `MatchLabelKeysInPodTopologySpreadSelectorMerge` 
  feature gate of kube-apiserver.  
  

- **nodeAffinityPolicy** indicates how we will treat Pod's nodeAffinity/nodeSelector
  when calculating pod topology spread skew. Options are:
  - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations.
  - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.

  If this value is null, the behavior is equivalent to the Honor policy.

  
  The `nodeAffinityPolicy` became beta in 1.26 and graduated to GA in 1.33.
  It's enabled by default in beta, you can disable it by disabling the
  `NodeInclusionPolicyInPodTopologySpread` feature gate.
  

- **nodeTaintsPolicy** indicates how we will treat node taints when calculating
  pod topology spread skew. Options are:
  - Honor: nodes without taints, along with tainted nodes for which the incoming pod
    has a toleration, are included.
  - Ignore: node taints are ignored. All nodes are included.

  If this value is null, the behavior is equivalent to the Ignore policy.

  
  The `nodeTaintsPolicy` became beta in 1.26 and graduated to GA in 1.33.
  It's enabled by default in beta, you can disable it by disabling the
  `NodeInclusionPolicyInPodTopologySpread` feature gate.
  

When a Pod defines more than one `topologySpreadConstraint`, those constraints are
combined using a logical AND operation: the kube-scheduler looks for a node for the incoming Pod
that satisfies all the configured constraints.

### Node labels

Topology spread constraints rely on node labels to identify the topology
domain(s) that each node is in.
For example, a node might have labels:
```yaml
  region: us-east-1
  zone: us-east-1a
```

For brevity, this example doesn't use the
well-known label keys
`topology.kubernetes.io/zone` and `topology.kubernetes.io/region`. However,
those registered label keys are nonetheless recommended rather than the private
(unqualified) label keys `region` and `zone` that are used here.

You can't make a reliable assumption about the meaning of a private label key
between different contexts.

Suppose you have a 4-node cluster with the following labels:

```
NAME    STATUS   ROLES    AGE     VERSION   LABELS
node1   Ready    <none>   4m26s   v1.16.0   node=node1,zone=zoneA
node2   Ready    <none>   3m58s   v1.16.0   node=node2,zone=zoneA
node3   Ready    <none>   3m17s   v1.16.0   node=node3,zone=zoneB
node4   Ready    <none>   2m43s   v1.16.0   node=node4,zone=zoneB
```

Then the cluster is logically viewed as below:

graph TB
    subgraph "zoneB"
        n3(Node3)
        n4(Node4)
    end
    subgraph "zoneA"
        n1(Node1)
        n2(Node2)
    end

    classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class n1,n2,n3,n4 k8s;
    class zoneA,zoneB cluster;
