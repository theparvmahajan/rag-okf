---
id: okf-structure/concepts/policy/limit-range.md#limitrange-and-admission-checks-for-pods
kind: section
title: LimitRange and admission checks for Pods
source: concepts/policy/limit-range.md
url: https://kubernetes.io/docs/concepts/policy/limit-range/
heading: LimitRange and admission checks for Pods
parent: okf-structure/concepts/policy/limit-range
children: []
prev_sibling: okf-structure/concepts/policy/limit-range.md#constraints-on-resource-limits-and-requests
next_sibling: okf-structure/concepts/policy/limit-range.md#example-resource-constraints
word_count: 199
---

A LimitRange does **not** check the consistency of the default values it applies.
This means that a default value for the _limit_ that is set by LimitRange may be
less than the _request_ value specified for the container in the spec that a client
submits to the API server. If that happens, the final Pod will not be schedulable.

For example, you define a LimitRange with below manifest:

The following examples operate within the default namespace of your cluster, as the namespace
parameter is undefined and the LimitRange scope is limited to the namespace level.
This implies that any references or operations within these examples will interact
with elements within the default namespace of your cluster. You can override the
operating namespace by configuring namespace in the `metadata.namespace` field.

along with a Pod that declares a CPU resource request of `700m`, but not a limit:

then that Pod will not be scheduled, failing with an error similar to:
```
Pod "example-conflict-with-limitrange-cpu" is invalid: spec.containers[0].resources.requests: Invalid value: "700m": must be less than or equal to cpu limit
```

If you set both `request` and `limit`, then that new Pod will be scheduled successfully
even with the same LimitRange in place:
