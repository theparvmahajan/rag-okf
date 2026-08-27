---
id: okf-structure/concepts/workloads/pods/disruptions.md#pod-disruption-conditions-pod-disruption-conditions
kind: section
title: Pod disruption conditions {#pod-disruption-conditions}
source: concepts/workloads/pods/disruptions.md
url: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
heading: Pod disruption conditions {#pod-disruption-conditions}
parent: okf-structure/concepts/workloads/pods/disruptions
children: []
prev_sibling: okf-structure/concepts/workloads/pods/disruptions.md#poddisruptionbudget-example-pdb-example
next_sibling: okf-structure/concepts/workloads/pods/disruptions.md#separating-cluster-owner-and-application-owner-roles
word_count: 305
---

A dedicated Pod `DisruptionTarget` condition
is added to indicate
that the Pod is about to be deleted due to a disruption.
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
