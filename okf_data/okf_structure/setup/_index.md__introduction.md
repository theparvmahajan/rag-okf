---
id: okf-structure/setup/_index.md#introduction
kind: section
title: Getting started
source: setup/_index.md
url: https://kubernetes.io/docs/setup/
heading: null
parent: okf-structure/setup/_index
children: []
prev_sibling: null
next_sibling: okf-structure/setup/_index.md#learning-environment
word_count: 150
---

This section lists the different ways to set up and run Kubernetes.
When you install Kubernetes, choose an installation type based on: ease of maintenance, security,
control, available resources, and expertise required to operate and manage a cluster.

You can download Kubernetes to deploy a Kubernetes cluster
on a local machine, into the cloud, or for your own datacenter.

Several Kubernetes components such as kube-apiserver or kube-proxy can also be
deployed as container images within the cluster.

It is **recommended** to run Kubernetes components as container images wherever
that is possible, and to have Kubernetes manage those components.
Components that run containers - notably, the kubelet - can't be included in this category.

If you don't want to manage a Kubernetes cluster yourself, you could pick a managed service, including
certified platforms.
There are also other standardized and custom solutions across a wide range of cloud and
bare metal environments.
