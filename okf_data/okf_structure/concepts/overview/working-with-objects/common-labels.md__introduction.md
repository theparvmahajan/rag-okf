---
id: okf-structure/concepts/overview/working-with-objects/common-labels.md#introduction
kind: section
title: Recommended Labels
source: concepts/overview/working-with-objects/common-labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/common-labels
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/common-labels.md#labels
word_count: 149
---

You can visualize and manage Kubernetes objects with more tools than kubectl and
the dashboard. A common set of labels allows tools to work interoperably, describing
objects in a common manner that all tools can understand.

In addition to supporting tooling, the recommended labels describe applications
in a way that can be queried.

The metadata is organized around the concept of an _application_. Kubernetes is not
a platform as a service (PaaS) and doesn't have or enforce a formal notion of an application.
Instead, applications are informal and described with metadata. The definition of
what an application contains is loose.

These are recommended labels. They make it easier to manage applications
but aren't required for any core tooling.

Shared labels and annotations share a common prefix: `app.kubernetes.io`. Labels
without a prefix are private to users. The shared prefix ensures that shared labels
do not interfere with custom user labels.
