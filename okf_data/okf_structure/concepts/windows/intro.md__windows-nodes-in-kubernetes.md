---
id: okf-structure/concepts/windows/intro.md#windows-nodes-in-kubernetes
kind: section
title: Windows nodes in Kubernetes
source: concepts/windows/intro.md
url: https://kubernetes.io/docs/concepts/windows/intro/
heading: Windows nodes in Kubernetes
parent: okf-structure/concepts/windows/intro
children: []
prev_sibling: okf-structure/concepts/windows/intro.md#introduction
next_sibling: okf-structure/concepts/windows/intro.md#compatibility-and-limitations-limitations
word_count: 105
---

To enable the orchestration of Windows containers in Kubernetes, include Windows nodes
in your existing Linux cluster. Scheduling Windows containers in
Pods on Kubernetes is similar to
scheduling Linux-based containers.

In order to run Windows containers, your Kubernetes cluster must include
multiple operating systems.
While you can only run the control plane on Linux,
you can deploy worker nodes running either Windows or Linux.

Windows nodes are
supported provided that the operating system is
Windows Server 2022 or Windows Server 2025.

This document uses the term *Windows containers* to mean Windows containers with
process isolation. Kubernetes does not support running Windows containers with
Hyper-V isolation.
