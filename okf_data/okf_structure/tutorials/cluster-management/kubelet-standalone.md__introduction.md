---
id: okf-structure/tutorials/cluster-management/kubelet-standalone.md#introduction
kind: section
title: Running Kubelet in Standalone Mode
source: tutorials/cluster-management/kubelet-standalone.md
url: https://kubernetes.io/docs/tutorials/cluster-management/kubelet-standalone/
heading: null
parent: okf-structure/tutorials/cluster-management/kubelet-standalone
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/cluster-management/kubelet-standalone.md#objectives
word_count: 131
---

This tutorial shows you how to run a standalone kubelet instance.

You may have different motivations for running a standalone kubelet.
This tutorial is aimed at introducing you to Kubernetes, even if you don't have
much experience with it. You can follow this tutorial and learn about node setup,
basic (static) Pods, and how Kubernetes manages containers.

Once you have followed this tutorial, you could try using a cluster that has a
control plane to manage pods
and nodes, and other types of objects. For example,
Hello, minikube.

You can also run the kubelet in standalone mode to suit production use cases, such as
to run the control plane for a highly available, resiliently deployed cluster. This
tutorial does not cover the details you need for running a resilient control plane.
