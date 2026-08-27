---
id: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#introduction
kind: section
title: Creating a cluster with kubeadm
source: setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md
url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
heading: null
parent: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm
children: []
prev_sibling: null
next_sibling: okf-structure/setup/production-environment/tools/kubeadm/create-cluster-kubeadm.md#prerequisites
word_count: 141
---

Using `kubeadm`, you can create a minimum viable Kubernetes cluster that conforms to best practices.
In fact, you can use `kubeadm` to set up a cluster that will pass the
Kubernetes Conformance tests.
`kubeadm` also supports other cluster lifecycle functions, such as
bootstrap tokens and cluster upgrades.

The `kubeadm` tool is good if you need:

- A simple way for you to try out Kubernetes, possibly for the first time.
- A way for existing users to automate setting up a cluster and test their application.
- A building block in other ecosystem and/or installer tools with a larger
  scope.

You can install and use `kubeadm` on various machines: your laptop, a set
of cloud servers, a Raspberry Pi, and more. Whether you're deploying into the
cloud or on-premises, you can integrate `kubeadm` into provisioning systems such
as Ansible or Terraform.
