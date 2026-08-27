---
id: okf-structure/tasks/administer-cluster/configure-feature-gates.md#introduction
kind: section
title: Enable Or Disable Feature Gates
source: tasks/administer-cluster/configure-feature-gates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/
heading: null
parent: okf-structure/tasks/administer-cluster/configure-feature-gates
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#prerequisites
word_count: 66
---

This page shows how to enable or disable feature gates to control specific Kubernetes 
features in your cluster. Enabling feature gates allows you to test and use Alpha or 
Beta features before they become generally available.

For some stable (GA) gates, you can also disable them, usually for one minor release 
after GA; however if you do that, your cluster may not be conformant as Kubernetes.
