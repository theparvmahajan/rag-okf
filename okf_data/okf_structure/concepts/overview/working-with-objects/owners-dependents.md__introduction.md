---
id: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#introduction
kind: section
title: Owners and Dependents
source: concepts/overview/working-with-objects/owners-dependents.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/owners-dependents/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/owners-dependents
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/owners-dependents.md#owner-references-in-object-specifications
word_count: 104
---

In Kubernetes, some objects are
*owners* of other objects. For example, a
ReplicaSet is the owner
of a set of Pods. These owned objects are *dependents* of their owner.

Ownership is different from the labels and selectors
mechanism that some resources also use. For example, consider a Service that
creates `EndpointSlice` objects. The Service uses labels to allow the control plane to
determine which `EndpointSlice` objects are used for that Service. In addition
to the labels, each `EndpointSlice` that is managed on behalf of a Service has
an owner reference. Owner references help different parts of Kubernetes avoid
interfering with objects they don’t control.
