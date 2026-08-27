---
id: okf-structure/concepts/extend-kubernetes/operator.md#deploying-operators
kind: section
title: Deploying operators
source: concepts/extend-kubernetes/operator.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
heading: Deploying operators
parent: okf-structure/concepts/extend-kubernetes/operator
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/operator.md#an-example-operator-example
next_sibling: okf-structure/concepts/extend-kubernetes/operator.md#using-an-operator-using-operators
word_count: 53
---

The most common way to deploy an operator is to add the
Custom Resource Definition and its associated Controller to your cluster.
The Controller will normally run outside of the
control plane,
much as you would run any containerized application.
For example, you can run the controller in your cluster as a Deployment.
