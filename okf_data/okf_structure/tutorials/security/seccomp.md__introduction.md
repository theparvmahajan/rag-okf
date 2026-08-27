---
id: okf-structure/tutorials/security/seccomp.md#introduction
kind: section
title: Restrict a Container's Syscalls with seccomp
source: tutorials/security/seccomp.md
url: https://kubernetes.io/docs/tutorials/security/seccomp/
heading: null
parent: okf-structure/tutorials/security/seccomp
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/security/seccomp.md#objectives
word_count: 110
---

Seccomp stands for secure computing mode and has been a feature of the Linux
kernel since version 2.6.12. It can be used to sandbox the privileges of a
process, restricting the calls it is able to make from userspace into the
kernel. Kubernetes lets you automatically apply seccomp profiles loaded onto a
node to your Pods and containers.

Identifying the privileges required for your workloads can be difficult. In this
tutorial, you will go through how to load seccomp profiles into a local
Kubernetes cluster, how to apply them to a Pod, and how you can begin to craft
profiles that give only the necessary privileges to your container processes.
