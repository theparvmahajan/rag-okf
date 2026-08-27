---
id: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#update-modes
kind: section
title: Update modes
source: concepts/workloads/autoscaling/vertical-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/
heading: Update modes
parent: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#how-does-a-verticalpodautoscaler-work
next_sibling: okf-structure/concepts/workloads/autoscaling/vertical-pod-autoscale.md#resource-policies
word_count: 522
---

A VerticalPodAutoscaler supports different _update modes_ that control how and when
resource recommendations are applied to your Pods. You configure the update mode using
the `updateMode` field in the VPA spec under `updatePolicy`:

```yaml
---
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "Recreate"  # Off, Initial, Recreate, InPlaceOrRecreate, InPlace
```

### Off {#updateMode-Off}

In the _Off_ update mode, the VPA recommender still analyzes resource usage and generates
recommendations, but these recommendations are not automatically applied to Pods.
The recommendations are only stored in the VPA object's `.status` field.

You can use a tool such as `kubectl` to view the `.status` and the recommendations in it.

### Initial {#updateMode-Initial}

In _Initial_ mode, VPA only sets resource requests when Pods are first created. It does not update resources for already running Pods, even if recommendations change over time. The recommendations apply only during Pod creation.

### Recreate {#updateMode-Recreate}

In _Recreate_ mode, VPA actively manages Pod resources by evicting Pods when their current
resource requests differ significantly from recommendations. When a Pod is evicted, the workload
controller (managing a Deployment, StatefulSet, etc) creates a replacement Pod, and the VPA admission
controller applies the updated resource requests to the new Pod.

### InPlaceOrRecreate {#updateMode-InPlaceOrRecreate}

In `InPlaceOrRecreate` mode, VPA attempts to update Pod resource requests and limits without restarting the Pod when possible. However, if in-place updates cannot be performed for a particular resource change, VPA falls back to evicting the Pod
(similar to `Recreate` mode) and allowing the workload controller to create a replacement Pod with updated resources.

In this mode, the updater applies recommendations in-place using the Resize Container Resources In-Place feature.

### InPlace {#updateMode-InPlace}

This mode is available as an alpha feature in VPA 1.7.0 and requires
Kubernetes 1.33 or later with the `InPlacePodVerticalScaling` cluster feature
gate enabled, and the `InPlace` feature gate enabled on the VPA updater and
admission controller. It uses the
in-place Pod resize
feature to apply updates without disrupting the Pod.

In `InPlace` mode, VPA attempts to update Pod resource requests and limits without
restarting or evicting the Pod. Unlike `InPlaceOrRecreate`, this mode **never falls
back to eviction**. If an in-place update cannot be applied (for example, because the
node does not have enough capacity), VPA defers the update and retries it in a
subsequent reconciliation loop.

To use `InPlace` mode, enable the `InPlace` feature gate on both the VPA updater
and admission controller:

```shell
--feature-gates=InPlace=true
```

Then set `updateMode` to `"InPlace"` in your VPA spec:

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: my-app-vpa
spec:
  targetRef:
    apiVersion: "apps/v1"
    kind: Deployment
    name: my-app
  updatePolicy:
    updateMode: "InPlace"
```

**Key difference from `InPlaceOrRecreate`:** When a resize is deferred, in progress,
or infeasible, `InPlace` mode always waits and retries — it never evicts the Pod,
regardless of how long the update is pending.

### Auto (deprecated) {#updateMode-Auto}

The `Auto` update mode is **deprecated since VPA version 1.4.0**. Use `Recreate` for
eviction-based updates, or `InPlaceOrRecreate` for in-place updates with eviction fallback.

`Auto` mode is currently an alias for `Recreate` mode and behaves identically. It was introduced to allow for future expansion of automatic update strategies.
