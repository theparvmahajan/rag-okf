---
id: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#introduction
kind: section
title: Configure Default Memory Requests and Limits for a Namespace
source: tasks/administer-cluster/manage-resources/memory-default-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/memory-default-namespace/
heading: null
parent: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/memory-default-namespace.md#prerequisites
word_count: 80
---

This page shows how to configure default memory requests and limits for a
namespace.

A Kubernetes cluster can be divided into namespaces. Once you have a namespace that
has a default memory
limit,
and you then try to create a Pod with a container that does not specify its own memory
limit, then the
control plane assigns the default
memory limit to that container.

Kubernetes assigns a default memory request under certain conditions that are explained later in this topic.
