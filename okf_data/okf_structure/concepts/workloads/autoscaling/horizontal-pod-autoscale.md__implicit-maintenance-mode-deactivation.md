---
id: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#implicit-maintenance-mode-deactivation
kind: section
title: Implicit maintenance-mode deactivation
source: concepts/workloads/autoscaling/horizontal-pod-autoscale.md
url: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/
heading: Implicit maintenance-mode deactivation
parent: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale
children: []
prev_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#support-for-horizontalpodautoscaler-in-kubectl
next_sibling: okf-structure/concepts/workloads/autoscaling/horizontal-pod-autoscale.md#whatsnext
word_count: 335
---

You can implicitly deactivate the HPA for a target without the
need to change the HPA configuration itself. If the target's desired replica count
is set to 0, and the HPA's minimum replica count is greater than 0, the HPA
stops adjusting the target (and sets the `ScalingActive` Condition on itself
to `false`) until you reactivate it by manually adjusting the target's desired
replica count or HPA's minimum replica count.

### Migrating Deployments and StatefulSets to horizontal autoscaling

When an HPA is enabled, it is recommended that the value of `spec.replicas` of
the Deployment and / or StatefulSet be removed from their
manifest(s). If this isn't done, any time
a change to that object is applied, for example via `kubectl apply -f
deployment.yaml`, this will instruct Kubernetes to scale the current number of Pods
to the value of the `spec.replicas` key. This may not be
desired and could be troublesome when an HPA is active, resulting in thrashing or flapping behavior.

Keep in mind that the removal of `spec.replicas` may incur a one-time
degradation of Pod counts as the default value of this key is 1 (reference
Deployment Replicas).
Upon the update, all Pods except 1 will begin their termination procedures. Any
deployment application afterwards will behave as normal and respect a rolling
update configuration as desired. You can avoid this degradation by choosing one of the following two
methods based on how you are modifying your deployments:

1. `kubectl apply edit-last-applied deployment/<deployment_name>`
2. In the editor, remove `spec.replicas`. When you save and exit the editor, `kubectl`
   applies the update. No changes to Pod counts happen at this step.
3. You can now remove `spec.replicas` from the manifest. If you use source code management,
   also commit your changes or take whatever other steps for revising the source code
   are appropriate for how you track updates.
4. From here on out you can run `kubectl apply -f deployment.yaml`

When using the Server-Side Apply
you can follow the transferring ownership
guidelines, which cover this exact use case.
