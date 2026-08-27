---
id: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#numeric-comparison-operators-numeric-comparison-operators
kind: section
title: Numeric comparison operators {#numeric-comparison-operators}
source: concepts/scheduling-eviction/taint-and-toleration.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/
heading: Numeric comparison operators {#numeric-comparison-operators}
parent: okf-structure/concepts/scheduling-eviction/taint-and-toleration
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#concepts
next_sibling: okf-structure/concepts/scheduling-eviction/taint-and-toleration.md#example-use-cases
word_count: 390
---

In addition to `Equal` and `Exists`, you can use numeric comparison operators
(`Gt` and `Lt`) to match taints with integer values. This is useful for threshold-based
scheduling, such as matching nodes by reliability level or SLA tier.

* `Gt` matches when the taint value is greater than the toleration value.
* `Lt` matches when the taint value is less than the toleration value.

For numeric operators, both the toleration and taint values must be valid integers.
If either value cannot be parsed as an integer, the toleration does not match.

When you create a Pod that uses `Gt` or `Lt` tolerations operators, the API server validates that
the toleration values are valid integers. Taint values on nodes are not validated at node
registration time. If a node has a non-numeric taint value (for example,
`servicelevel.organization.example/agreed-service-level=high:NoSchedule`),
pods with numeric comparison operators will not match that taint and cannot schedule on that node.

For example, if nodes are tainted with a value representing a service level agreement (SLA):

```shell
kubectl taint nodes node1 servicelevel.organization.example/agreed-service-level=950:NoSchedule
```

A pod can tolerate nodes with SLA greater than 900:

This toleration matches the taint on `node1` because `950 > 900` (the taint value  
is greater than the toleration value for the `Gt` operator).  
Similarly, you can use the `Lt` operator to match taints where the taint value is  
less than the toleration value:

```yaml
tolerations:
- key: "servicelevel.organization.example/agreed-service-level"
  operator: "Lt"
  value: "1000"
  effect: "NoSchedule"
```

When using numeric comparison operators:

* Both the toleration and taint values must be valid signed 64-bit integers
  (zero leading numbers (e.g., "0550") are not allowed).
* If a value cannot be parsed as an integer, the toleration does not match.
* Numeric operators work with all taint effects: `NoSchedule`, `PreferNoSchedule`, and `NoExecute`.
* For `PreferNoSchedule` with numeric operators: if a pod's toleration doesn't satisfy the numeric comparison
  (e.g., taint value < toleration value when using `Gt`), the scheduler gives the node a lower priority
  but may still schedule there if no better options exist.

Before disabling the `TaintTolerationComparisonOperators` feature gate:

* You should identify all workloads using the `Gt` or `Lt` operators to avoid controller hot-loops.
* Update all workload controller templates to use `Equal` or `Exists` operators instead
* Delete any pending pods that use `Gt` or `Lt` operators
* Monitor the `apiserver_request_total` metric for spikes in validation errors
