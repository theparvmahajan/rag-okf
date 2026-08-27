---
id: okf-structure/concepts/overview/working-with-objects/finalizers.md#owner-references-labels-and-finalizers-owners-labels-finalizers
kind: section
title: Owner references, labels, and finalizers {#owners-labels-finalizers}
source: concepts/overview/working-with-objects/finalizers.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/
heading: Owner references, labels, and finalizers {#owners-labels-finalizers}
parent: okf-structure/concepts/overview/working-with-objects/finalizers
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/finalizers.md#how-finalizers-work
next_sibling: okf-structure/concepts/overview/working-with-objects/finalizers.md#whatsnext
word_count: 241
---

Like labels,
owner references
describe the relationships between objects in Kubernetes, but are used for a
different purpose. When a
controller manages objects
like Pods, it uses labels to track changes to groups of related objects. For
example, when a Job creates one or
more Pods, the Job controller applies labels to those pods and tracks changes to
any Pods in the cluster with the same label.

The Job controller also adds *owner references* to those Pods, pointing at the
Job that created the Pods. If you delete the Job while these Pods are running,
Kubernetes uses the owner references (not labels) to determine which Pods in the
cluster need cleanup.

Kubernetes also processes finalizers when it identifies owner references on a
resource targeted for deletion. 

In some situations, finalizers can block the deletion of dependent objects,
which can cause the targeted owner object to remain for
longer than expected without being fully deleted. In these situations, you
should check finalizers and owner references on the target owner and dependent
objects to troubleshoot the cause. 

In cases where objects are stuck in a deleting state, avoid manually
removing finalizers to allow deletion to continue. Finalizers are usually added
to resources for a reason, so forcefully removing them can lead to issues in
your cluster. This should only be done when the purpose of the finalizer is
understood and is accomplished in another way (for example, manually cleaning
up some dependent object).
