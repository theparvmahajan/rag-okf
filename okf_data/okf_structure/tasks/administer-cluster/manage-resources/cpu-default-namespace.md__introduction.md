---
id: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#introduction
kind: section
title: Configure Default CPU Requests and Limits for a Namespace
source: tasks/administer-cluster/manage-resources/cpu-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/cpu-default-namespace/
heading: null
parent: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/cpu-default-namespace.md#prerequisites
word_count: 79
---

This page shows how to configure default CPU requests and limits for a
namespace.

A Kubernetes cluster can be divided into namespaces. If you create a Pod within a
namespace that has a default CPU
limit, and any container in that Pod does not specify
its own CPU limit, then the
control plane assigns the default
CPU limit to that container.

Kubernetes assigns a default CPU
request,
but only under certain conditions that are explained later in this page.
