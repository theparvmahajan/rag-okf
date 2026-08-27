---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#configurable-scaling-behavior
kind: section
title: Configurable scaling behavior
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Configurable scaling behavior
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-metrics-apis
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-horizontalpodautoscaler-in-kubectl
word_count: 1048
---

(the `autoscaling/v2beta2` API version previously provided this ability as a beta feature)

If you use the `v2` HorizontalPodAutoscaler API, you can use the `behavior` field
(see the API reference)
to configure separate scale-up and scale-down behaviors.
You specify these behaviors by setting `scaleUp` and / or `scaleDown`
under the `behavior` field.

Scaling policies let you control the rate of change of replicas while scaling.
Also two settings can be used to prevent flapping: you can specify a
_stabilization window_ for smoothing replica counts, and a tolerance to ignore
minor metric fluctuations below a specified threshold.

### Scaling policies

One or more scaling policies can be specified in the `behavior` section of the spec.
When multiple policies are specified the policy which allows the highest amount of
change is the policy which is selected by default. The following example shows this behavior
while scaling down:

```yaml
behavior:
  scaleDown:
    policies:
    - type: Pods
      value: 4
      periodSeconds: 60
    - type: Percent
      value: 10
      periodSeconds: 60
```

`periodSeconds` indicates the length of time in the past for which the policy must hold true.
The maximum value that you can set for `periodSeconds` is 1800 (half an hour).
The first policy _(Pods)_ allows at most 4 replicas to be scaled down in one minute. The second policy
_(Percent)_ allows at most 10% of the current replicas to be scaled down in one minute.

Since by default the policy which allows the highest amount of change is selected, the second policy will
only be used when the number of pod replicas is more than 40. With 40 or less replicas, the first policy will be applied.
For instance if there are 80 replicas and the target has to be scaled down to 10 replicas
then during the first step 8 replicas will be reduced. In the next iteration when the number
of replicas is 72, 10% of the pods is 7.2 but the number is rounded up to 8. On each loop of
the autoscaler controller the number of pods to be change is re-calculated based on the number
of current replicas. When the number of replicas falls below 40 the first policy _(Pods)_ is applied
and 4 replicas will be reduced at a time.

The policy selection can be changed by specifying the `selectPolicy` field for a scaling
direction. By setting the value to `Min` which would select the policy which allows the
smallest change in the replica count. Setting the value to `Disabled` completely disables
scaling in that direction.

### Stabilization window

The stabilization window is used to restrict the flapping of
replica count when the metrics used for scaling keep fluctuating. The autoscaling algorithm
uses this window to infer a previous desired state and avoid unwanted changes to workload
scale.

For example, in the following example snippet, a stabilization window is specified for `scaleDown`.

```yaml
behavior:
  scaleDown:
    stabilizationWindowSeconds: 300
```

When the metrics indicate that the target should be scaled down the algorithm looks
into previously computed desired states, and uses the highest value from the specified
interval. In the above example, all desired states from the past 5 minutes will be considered.

This approximates a rolling maximum, and avoids having the scaling algorithm frequently
remove Pods only to trigger recreating an equivalent Pod just moments later.

### Tolerance {#tolerance}

The `tolerance` field configures a threshold for metric variations, preventing the
autoscaler from scaling for changes below that value.

This tolerance is defined as the amount of variation around the desired metric value under
which no scaling will occur. For example, consider a HorizontalPodAutoscaler configured
with a target memory consumption of 100MiB and a scale-up tolerance of 5%:

```yaml
behavior:
  scaleUp:
    tolerance: 0.05 # 5% tolerance for scale up
```

With this configuration, the HPA algorithm will only consider scaling up if the memory
consumption is higher than 105MiB (that is: 5% above the target).

If you don't set this field, the HPA applies the default cluster-wide tolerance of 10%. This
default can be updated for both scale-up and scale-down using the
kube-controller-manager
`--horizontal-pod-autoscaler-tolerance` command line argument. (You can't use the Kubernetes API
to configure this default value.)

### Default behavior

To use the custom scaling not all fields have to be specified. Only values which need to be
customized can be specified. These custom values are merged with default values. The default values
match the existing behavior in the HPA algorithm.

```yaml
behavior:
  scaleDown:
    stabilizationWindowSeconds: 300
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
  scaleUp:
    stabilizationWindowSeconds: 0
    policies:
    - type: Percent
      value: 100
      periodSeconds: 15
    - type: Pods
      value: 4
      periodSeconds: 15
    selectPolicy: Max
```
For scaling down the stabilization window is _300_ seconds (or the value of the
`--horizontal-pod-autoscaler-downscale-stabilization` command line option, if provided). There is only a single policy
for scaling down which allows a 100% of the currently running replicas to be removed which
means the scaling target can be scaled down to the minimum allowed replicas.
For scaling up there is no stabilization window. When the metrics indicate that the target should be
scaled up the target is scaled up immediately. There are 2 policies where 4 pods or a 100% of the currently
running replicas may at most be added every 15 seconds till the HPA reaches its steady state.

### Example: change downscale stabilization window

To provide a custom downscale stabilization window of 1 minute, the following
behavior would be added to the HPA:

```yaml
behavior:
  scaleDown:
    stabilizationWindowSeconds: 60
```

### Example: limit scale down rate

To limit the rate at which pods are removed by the HPA to 10% per minute, the
following behavior would be added to the HPA:

```yaml
behavior:
  scaleDown:
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
```

To ensure that no more than 5 Pods are removed per minute, you can add a second scale-down
policy with a fixed size of 5, and set `selectPolicy` to minimum. Setting `selectPolicy` to `Min` means
that the autoscaler chooses the policy that affects the smallest number of Pods:

```yaml
behavior:
  scaleDown:
    policies:
    - type: Percent
      value: 10
      periodSeconds: 60
    - type: Pods
      value: 5
      periodSeconds: 60
    selectPolicy: Min
```

### Example: disable scale down

The `selectPolicy` value of `Disabled` turns off scaling the given direction.
So to prevent downscaling the following policy would be used:

```yaml
behavior:
  scaleDown:
    selectPolicy: Disabled
```
