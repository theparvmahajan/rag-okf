---
id: okf-structure/tasks/run-application/force-delete-stateful-set-pod.md#statefulset-considerations
kind: section
title: StatefulSet considerations
source: tasks/run-application/force-delete-stateful-set-pod.md
url: https://kubernetes.io/docs/tasks/run-application/force-delete-stateful-set-pod/
heading: StatefulSet considerations
parent: okf-structure/tasks/run-application/force-delete-stateful-set-pod
children: []
prev_sibling: okf-structure/tasks/run-application/force-delete-stateful-set-pod.md#prerequisites
next_sibling: okf-structure/tasks/run-application/force-delete-stateful-set-pod.md#delete-pods
word_count: 170
---

In normal operation of a StatefulSet, there is **never** a need to force delete a StatefulSet Pod.
The StatefulSet controller is responsible for
creating, scaling and deleting members of the StatefulSet. It tries to ensure that the specified
number of Pods from ordinal 0 through N-1 are alive and ready. StatefulSet ensures that, at any time,
there is at most one Pod with a given identity running in a cluster. This is referred to as
*at most one* semantics provided by a StatefulSet.

Manual force deletion should be undertaken with caution, as it has the potential to violate the
at most one semantics inherent to StatefulSet. StatefulSets may be used to run distributed and
clustered applications which have a need for a stable network identity and stable storage.
These applications often have configuration which relies on an ensemble of a fixed number of
members with fixed identities. Having multiple members with the same identity can be disastrous
and may lead to data loss (e.g. split brain scenario in quorum-based systems).
