---
id: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#introduction
kind: section
title: Configure Multiple Schedulers
source: tasks/extend-kubernetes/configure-multiple-schedulers.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/
heading: null
parent: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#prerequisites
word_count: 94
---

Kubernetes ships with a default scheduler that is described
here.
If the default scheduler does not suit your needs you can implement your own scheduler.
Moreover, you can even run multiple schedulers simultaneously alongside the default
scheduler and instruct Kubernetes what scheduler to use for each of your pods. Let's
learn how to run multiple schedulers in Kubernetes with an example.

A detailed description of how to implement a scheduler is outside the scope of this
document. Please refer to the kube-scheduler implementation in
pkg/scheduler
in the Kubernetes source directory for a canonical example.
