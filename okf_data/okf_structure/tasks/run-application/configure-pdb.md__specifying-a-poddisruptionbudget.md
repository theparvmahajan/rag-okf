---
id: okf-structure/tasks/run-application/configure-pdb.md#specifying-a-poddisruptionbudget
kind: section
title: Specifying a PodDisruptionBudget
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Specifying a PodDisruptionBudget
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#think-about-how-your-application-reacts-to-disruptions
next_sibling: okf-structure/tasks/run-application/configure-pdb.md#create-the-pdb-object
word_count: 570
---

A `PodDisruptionBudget` has three fields:

- A label selector `.spec.selector` to specify the set of
  pods to which it applies. This field is required.
- `.spec.minAvailable` which is a description of the number of pods from that
  set that must still be available after the eviction, even in the absence
  of the evicted pod. `minAvailable` can be either an absolute number or a percentage.
- `.spec.maxUnavailable` (available in Kubernetes 1.7 and higher) which is a description
  of the number of pods from that set that can be unavailable after the eviction.
  It can be either an absolute number or a percentage.

The behavior for an empty selector differs between the policy/v1beta1 and policy/v1 APIs for
PodDisruptionBudgets. For policy/v1beta1 an empty selector matches zero pods, while
for policy/v1 an empty selector matches every pod in the namespace.

You can specify only one of `maxUnavailable` and `minAvailable` in a single `PodDisruptionBudget`.
`maxUnavailable` can only be used to control the eviction of pods
that all have the same associated controller managing them. In the examples below, "desired replicas"
is the `scale` of the controller managing the pods being selected by the
`PodDisruptionBudget`.

Example 1: With a `minAvailable` of 5, evictions are allowed as long as they leave behind
5 or more healthy pods among those selected by the PodDisruptionBudget's `selector`.

Example 2: With a `minAvailable` of 30%, evictions are allowed as long as at least 30%
of the number of desired replicas are healthy.

Example 3: With a `maxUnavailable` of 5, evictions are allowed as long as there are at most 5
unhealthy replicas among the total number of desired replicas.

Example 4: With a `maxUnavailable` of 30%, evictions are allowed as long as the number of 
unhealthy replicas does not exceed 30% of the total number of desired replica rounded up to 
the nearest integer. If the total number of desired replicas is just one, that single replica
is still allowed for disruption, leading to an effective unavailability of 100%.

In typical usage, a single budget would be used for a collection of pods managed by
a controller—for example, the pods in a single ReplicaSet or StatefulSet.

A disruption budget does not truly guarantee that the specified
number/percentage of pods will always be up. For example, a node that hosts a
pod from the collection may fail when the collection is at the minimum size
specified in the budget, thus bringing the number of available pods from the
collection below the specified size. The budget can only protect against
voluntary evictions, not all causes of unavailability.

If you set `maxUnavailable` to 0% or 0, or you set `minAvailable` to 100% or the number of replicas,
you are requiring zero voluntary evictions. When you set zero voluntary evictions for a workload
object such as ReplicaSet, then you cannot successfully drain a Node running one of those Pods.
If you try to drain a Node where an unevictable Pod is running, the drain never completes.
This is permitted as per the semantics of `PodDisruptionBudget`.

You can find examples of pod disruption budgets defined below. They match pods with the label
`app: zookeeper`.

Example PDB Using minAvailable:

Example PDB Using maxUnavailable:

For example, if the above `zk-pdb` object selects the pods of a StatefulSet of size 3, both
specifications have the exact same meaning. The use of `maxUnavailable` is recommended as it
automatically responds to changes in the number of replicas of the corresponding controller.
