---
id: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#introduction
kind: section
title: Find Out What Container Runtime is Used on a Node
source: tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md
url: https://kubernetes.io/docs/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use/
heading: null
parent: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/migrating-from-dockershim/find-out-runtime-you-use.md#prerequisites
word_count: 77
---

This page outlines steps to find out what container runtime
the nodes in your cluster use.

Depending on the way you run your cluster, the container runtime for the nodes may
have been pre-configured or you need to configure it. If you're using a managed
Kubernetes service, there might be vendor-specific ways to check what container runtime is
configured for the nodes. The method described on this page should work whenever
the execution of `kubectl` is allowed.
