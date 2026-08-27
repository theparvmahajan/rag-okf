You can link a `Pod` to a PodGroup to indicate
that the `Pod` belongs to a group of `Pods` scheduled together. This enables the scheduler
to apply group-level policies such as gang scheduling rather than treating each `Pod` independently.

## Specifying a scheduling group

When the `GenericWorkload`
feature gate is enabled,
you can set the `spec.schedulingGroup` field in your `Pod` manifest. This field establishes a link to a specific `PodGroup` object in the same namespace by name.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-0
  namespace: some-ns
spec:
  schedulingGroup:
    podGroupName: training-worker-0
  containers:
  - name: ml-worker
    image: training:v1
```

The `schedulingGroup` field is immutable. Once set, a `Pod` cannot be moved to a
different `PodGroup`.

## Behavior

When you set `spec.schedulingGroup`, the scheduler looks up the referenced
PodGroup and applies the
scheduling policy defined in it:

* If the `PodGroup` uses the `basic` policy, each `Pod` is scheduled independently using
  standard Kubernetes behavior. The grouping is used as group-level label.
* If the `PodGroup` uses the `gang` policy, the `Pod` enters an "all-or-nothing" scheduling
  lifecycle. The scheduler tries to place at least `minCount` `Pods` in the group
  simultaneously; none of them bind to nodes unless the minimum is met.

## Missing PodGroup reference

If a `Pod` references a `PodGroup` that does not yet exist, the `Pod` remains pending.
The scheduler automatically reconsiders the `Pod` once the `PodGroup` is created.

This applies regardless of whether the eventual policy is `basic` or `gang`,
because the scheduler requires the `PodGroup` to determine the policy.

## Whatsnext

* Learn about the PodGroup API and its lifecycle.
* Read about PodGroup scheduling policies.
* Understand the gang scheduling algorithm.