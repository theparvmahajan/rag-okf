---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#using-custom-certificates-custom-certificates
word_count: 68
---

You should be familiar with PKI certificates and requirements in Kubernetes.

You should be familiar with how to pass a configuration file to the kubeadm commands.

This guide covers the usage of the `openssl` command (used for manual certificate signing,
if you choose that approach), but you can use your preferred tools.

Some of the steps here use `sudo` for administrator access. You can use any equivalent tool.
