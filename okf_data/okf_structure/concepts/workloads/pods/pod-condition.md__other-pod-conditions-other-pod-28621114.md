---
id: okf-structure/concepts/workloads/pods/pod-condition.md#other-pod-conditions-other-pod-conditions
kind: section
title: Other Pod conditions {#other-pod-conditions}
source: concepts/workloads/pods/pod-condition.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
heading: Other Pod conditions {#other-pod-conditions}
parent: okf-structure/concepts/workloads/pods/pod-condition
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#lifecycle-pod-conditions-lifecycle-pod-conditions
next_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#enhanced-pod-readiness
word_count: 509
---

The following conditions are not part of the normal Pod lifecycle progression.
They are set in response to specific operations or events.

### DisruptionTarget {#disruption-target}

A dedicated Pod `DisruptionTarget` condition is added to indicate that
the Pod is about to be deleted due to a disruption.
The `reason` field of the condition additionally
indicates one of the following reasons for the Pod termination:

`PreemptionByScheduler`
: Pod is due to be preempted by a scheduler in order to accommodate a new Pod with a higher priority. For more information, see Pod priority preemption.

`DeletionByTaintManager`
: Pod is due to be deleted by Taint Manager (which is part of the node lifecycle controller within `kube-controller-manager`) due to a `NoExecute` taint that the Pod does not tolerate; see taint-based evictions.

`EvictionByEvictionAPI`
: Pod has been marked for eviction using the Kubernetes API .

`DeletionByPodGC`
: Pod, that is bound to a no longer existing Node, is due to be deleted by Pod garbage collection.

`TerminationByKubelet`
: Pod has been terminated by the kubelet, because of either node pressure eviction,
  the graceful node shutdown,
  or preemption for system critical pods.

In all other disruption scenarios, like eviction due to exceeding
Pod container limits,
Pods don't receive the `DisruptionTarget` condition because the disruptions were
probably caused by the Pod and would reoccur on retry.

A Pod disruption might be interrupted. The control plane might re-attempt to
continue the disruption of the same Pod, but it is not guaranteed. As a result,
the `DisruptionTarget` condition might be added to a Pod, but that Pod might then not actually be
deleted. In such a situation, after some time, the
Pod disruption condition will be cleared.

Along with cleaning up the pods, the Pod garbage collector (PodGC) will also mark them as failed if they are in a non-terminal
phase (see also Pod garbage collection).

When using a Job (or CronJob), you may want to use these Pod disruption conditions as part of your Job's
Pod failure policy.

For more details, see Disruptions.

### PodResizePending and PodResizeInProgress {#pod-resize-conditions}

The kubelet updates the Pod's status conditions to indicate the state of a resize request:

- `type: PodResizePending`: The kubelet cannot immediately grant the request. The `message` field provides an explanation of why.
  - `reason: Infeasible`: The requested resize is impossible on the current node (for example, requesting more resources than the node has).
  - `reason: Deferred`: The requested resize is currently not possible, but might become feasible later (for example if another pod is removed). The kubelet will retry the resize.
- `type: PodResizeInProgress`: The kubelet has accepted the resize and allocated resources, but the changes are still being applied. This is usually brief but might take longer depending on the resource type and runtime behavior. Any errors during actuation are reported in the `message` field (along with `reason: Error`).

If the requested resize is _Deferred_, the kubelet will periodically re-attempt the resize, for example when another pod is removed or scaled down.

For more details on Pod resize, see Resize CPU and Memory Resources assigned to Containers.
