---
id: okf-structure/tasks/run-application/configure-pdb.md#unhealthy-pod-eviction-policy
kind: section
title: Unhealthy Pod Eviction Policy
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Unhealthy Pod Eviction Policy
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#check-the-status-of-the-pdb
next_sibling: okf-structure/tasks/run-application/configure-pdb.md#arbitrary-workloads-and-arbitrary-selectors-arbitrary-controllers-and-selectors
word_count: 245
---

PodDisruptionBudget guarding an application ensures that `.status.currentHealthy` number of pods
does not fall below the number specified in `.status.desiredHealthy` by disallowing eviction of healthy pods.
By using `.spec.unhealthyPodEvictionPolicy`, you can also define the criteria when unhealthy pods
should be considered for eviction. The default behavior when no policy is specified corresponds
to the `IfHealthyBudget` policy.

Policies:

`IfHealthyBudget`
: Running pods (`.status.phase="Running"`), but not yet healthy can be evicted only
  if the guarded application is not disrupted (`.status.currentHealthy` is at least
  equal to `.status.desiredHealthy`).

: This policy ensures that running pods of an already disrupted application have
  the best chance to become healthy. This has negative implications for draining
  nodes, which can be blocked by misbehaving applications that are guarded by a PDB.
  More specifically applications with pods in `CrashLoopBackOff` state
  (due to a bug or misconfiguration), or pods that are just failing to report the
  `Ready` condition.

`AlwaysAllow`
: Running pods (`.status.phase="Running"`), but not yet healthy are considered
  disrupted and can be evicted regardless of whether the criteria in a PDB is met.

: This means prospective running pods of a disrupted application might not get a
  chance to become healthy. By using this policy, cluster managers can easily evict
  misbehaving applications that are guarded by a PDB. More specifically applications
  with pods in `CrashLoopBackOff` state (due to a bug or misconfiguration), or pods
  that are just failing to report the `Ready` condition.

Pods in `Pending`, `Succeeded` or `Failed` phase are always considered for eviction.
