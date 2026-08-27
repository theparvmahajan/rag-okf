---
id: okf-structure/concepts/extend-kubernetes/operator.md#operators-in-kubernetes
kind: section
title: Operators in Kubernetes
source: concepts/extend-kubernetes/operator.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
heading: Operators in Kubernetes
parent: okf-structure/concepts/extend-kubernetes/operator
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/operator.md#motivation
next_sibling: okf-structure/concepts/extend-kubernetes/operator.md#an-example-operator-example
word_count: 79
---

Kubernetes is designed for automation. Out of the box, you get lots of
built-in automation from the core of Kubernetes. You can use Kubernetes
to automate deploying and running workloads, *and* you can automate how
Kubernetes does that.

Kubernetes' operator pattern
concept lets you extend the cluster's behaviour without modifying the code of Kubernetes
itself by linking controllers to
one or more custom resources. Operators are clients of the Kubernetes API that act as
controllers for a Custom Resource.
