---
id: okf-structure/tasks/run-application/configure-pdb.md#arbitrary-workloads-and-arbitrary-selectors-arbitrary-controllers-and-selectors
kind: section
title: Arbitrary workloads and arbitrary selectors {#arbitrary-controllers-and-selectors}
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Arbitrary workloads and arbitrary selectors {#arbitrary-controllers-and-selectors}
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#unhealthy-pod-eviction-policy
next_sibling: null
word_count: 166
---

You can skip this section if you only use PDBs with the built-in
workload resources (Deployment, ReplicaSet, StatefulSet and ReplicationController)
or with custom resources
that implement a `scale` subresource,
and where the PDB selector exactly matches the selector of the Pod's owning resource.

You can use a PDB with pods controlled by another resource, by an
"operator", or bare pods, but with these restrictions:

- only `.spec.minAvailable` can be used, not `.spec.maxUnavailable`.
- only an integer value can be used with `.spec.minAvailable`, not a percentage.

It is not possible to use other availability configurations,
because Kubernetes cannot derive a total number of pods without a supported owning resource.

You can use a selector which selects a subset or superset of the pods belonging to a
workload resource. The eviction API will disallow eviction of any pod covered by multiple PDBs,
so most users will want to avoid overlapping selectors. One reasonable use of overlapping
PDBs is when pods are being transitioned from one PDB to another.
