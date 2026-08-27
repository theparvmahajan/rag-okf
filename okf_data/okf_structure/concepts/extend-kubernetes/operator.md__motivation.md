---
id: okf-structure/concepts/extend-kubernetes/operator.md#motivation
kind: section
title: Motivation
source: concepts/extend-kubernetes/operator.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
heading: Motivation
parent: okf-structure/concepts/extend-kubernetes/operator
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/operator.md#introduction
next_sibling: okf-structure/concepts/extend-kubernetes/operator.md#operators-in-kubernetes
word_count: 88
---

The _operator pattern_ aims to capture the key aim of a human operator who
is managing a service or set of services. Human operators who look after
specific applications and services have deep knowledge of how the system
ought to behave, how to deploy it, and how to react if there are problems.

People who run workloads on Kubernetes often like to use automation to take
care of repeatable tasks. The operator pattern captures how you can write
code to automate a task beyond what Kubernetes itself provides.
