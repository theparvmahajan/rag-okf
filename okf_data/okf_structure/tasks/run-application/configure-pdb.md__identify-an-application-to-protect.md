---
id: okf-structure/tasks/run-application/configure-pdb.md#identify-an-application-to-protect
kind: section
title: Identify an Application to Protect
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Identify an Application to Protect
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#protecting-an-application-with-a-poddisruptionbudget
next_sibling: okf-structure/tasks/run-application/configure-pdb.md#think-about-how-your-application-reacts-to-disruptions
word_count: 93
---

The most common use case when you want to protect an application
specified by one of the built-in Kubernetes controllers:

- Deployment
- ReplicationController
- ReplicaSet
- StatefulSet

In this case, make a note of the controller's `.spec.selector`; the same
selector goes into the PDBs `.spec.selector`.

From version 1.15 PDBs support custom controllers where the
scale subresource
is enabled.

You can also use PDBs with pods which are not controlled by one of the above
controllers, or arbitrary groups of pods, but there are some restrictions,
described in Arbitrary workloads and arbitrary selectors.
