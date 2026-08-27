---
id: okf-structure/tasks/administer-cluster/developing-cloud-controller-manager.md#background
kind: section
title: Background
source: tasks/administer-cluster/developing-cloud-controller-manager.md
url: https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/
heading: Background
parent: okf-structure/tasks/administer-cluster/developing-cloud-controller-manager
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/developing-cloud-controller-manager.md#developing
word_count: 92
---

Since cloud providers develop and release at a different pace compared to the Kubernetes project, abstracting the provider-specific code to the `cloud-controller-manager` binary allows cloud vendors to evolve independently from the core Kubernetes code.

The Kubernetes project provides skeleton cloud-controller-manager code with Go interfaces to allow you (or your cloud provider) to plug in your own implementations. This means that a cloud provider can implement a cloud-controller-manager by importing packages from Kubernetes core; each cloudprovider will register their own code by calling `cloudprovider.RegisterCloudProvider` to update a global variable of available cloud providers.
