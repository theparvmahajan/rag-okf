---
id: okf-structure/concepts/overview/working-with-objects/common-labels.md#applications-and-instances-of-applications
kind: section
title: Applications And Instances Of Applications
source: concepts/overview/working-with-objects/common-labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/
heading: Applications And Instances Of Applications
parent: okf-structure/concepts/overview/working-with-objects/common-labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/common-labels.md#labels
next_sibling: okf-structure/concepts/overview/working-with-objects/common-labels.md#examples
word_count: 93
---

An application can be installed one or more times into a Kubernetes cluster and,
in some cases, the same namespace. For example, WordPress can be installed more
than once where different websites are different installations of WordPress.

The name of an application and the instance name are recorded separately. For
example, WordPress has a `app.kubernetes.io/name` of `wordpress` while it has
an instance name, represented as `app.kubernetes.io/instance` with a value of
`wordpress-abcxyz`. This enables the application and instance of the application
to be identifiable. Every instance of an application must have a unique name.
