---
id: okf-structure/concepts/workloads/pods/pod-condition.md#enhanced-pod-readiness
kind: section
title: Enhanced Pod readiness
source: concepts/workloads/pods/pod-condition.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
heading: Enhanced Pod readiness
parent: okf-structure/concepts/workloads/pods/pod-condition
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#other-pod-conditions-other-pod-conditions
next_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#whatsnext
word_count: 281
---

Your application can inject extra feedback or signals into the Pod's `.status`;
this is known as _enhanced Pod readiness_.
To use this, set `readinessGates` in the Pod's `spec` to specify a list of additional
conditions that the kubelet evaluates for Pod readiness.
You then implement, or install, a controller that manages these custom conditions,
and the kubelet uses that as an extra input to decide if the Pod is ready.

Readiness gates are determined by the current state of `status.condition` fields for the Pod.
If Kubernetes cannot find such a condition in the `status.conditions` field of a Pod, the status of the condition is defaulted to "`False`".

```yaml
kind: Pod
...
spec:
  readinessGates:
    - conditionType: "www.example.com/feature-1"
status:
  conditions:
    - type: Ready                              # a built-in PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
    - type: "www.example.com/feature-1"        # an extra PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
  containerStatuses:
    - containerID: docker://abcd...
      ready: true
...
```

The Pod conditions you add must have names that meet the Kubernetes label key format.

### Status for Pod readiness

To set these `status.conditions` for the Pod, applications and
operators should use
the `PATCH` action on the Pod's status subresource. You can use `kubectl patch`
with `--subresource=status`, or a Kubernetes client library to write
code that sets custom Pod conditions for Pod readiness.

For a Pod that uses custom conditions, that Pod is evaluated to be ready **only** when both the following statements apply:

- All containers in the Pod are ready.
- All conditions specified in `readinessGates` are `True`.

When a Pod's containers are Ready but at least one custom condition is missing or `False`,
the kubelet sets the Pod's `Ready` condition to `status: "False"` with `reason: ReadinessGatesNotReady`.
