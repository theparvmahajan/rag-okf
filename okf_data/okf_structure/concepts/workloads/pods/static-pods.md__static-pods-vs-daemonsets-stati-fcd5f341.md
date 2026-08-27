---
id: okf-structure/concepts/workloads/pods/static-pods.md#static-pods-vs-daemonsets-static-pods-vs-daemonsets
kind: section
title: Static Pods vs DaemonSets {#static-pods-vs-daemonsets}
source: concepts/workloads/pods/static-pods.md
url: https://kubernetes.io/docs/concepts/workloads/pods/static-pods/
heading: Static Pods vs DaemonSets {#static-pods-vs-daemonsets}
parent: okf-structure/concepts/workloads/pods/static-pods
children: []
prev_sibling: okf-structure/concepts/workloads/pods/static-pods.md#limitations-limitations
next_sibling: okf-structure/concepts/workloads/pods/static-pods.md#whatsnext
word_count: 90
---

If you are running clustered Kubernetes and are using static Pods to run a Pod
on every node, you should probably be using a
DaemonSet instead.

Static Pods are not managed by the control plane, so they cannot be rolled out,
rolled back, or scaled using standard Kubernetes mechanisms. DaemonSets provide
these capabilities and are the recommended approach for running node-level workloads.

Static Pods are started by the kubelet before the API server is available, which
makes them suitable for bootstrapping control plane components. DaemonSets require
a running control plane.
