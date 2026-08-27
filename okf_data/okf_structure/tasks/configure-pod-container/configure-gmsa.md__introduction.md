---
id: okf-structure/tasks/configure-pod-container/configure-gmsa.md#introduction
kind: section
title: Configure GMSA for Windows Pods and containers
source: tasks/configure-pod-container/configure-gmsa.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-gmsa/
heading: null
parent: okf-structure/tasks/configure-pod-container/configure-gmsa
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/configure-gmsa.md#prerequisites
word_count: 102
---

This page shows how to configure
Group Managed Service Accounts (GMSA)
for Pods and containers that will run on Windows nodes. Group Managed Service Accounts
are a specific type of Active Directory account that provides automatic password management,
simplified service principal name (SPN) management, and the ability to delegate the management
to other administrators across multiple servers.

In Kubernetes, GMSA credential specs are configured at a Kubernetes cluster-wide scope
as Custom Resources. Windows Pods, as well as individual containers within a Pod,
can be configured to use a GMSA for domain based functions (e.g. Kerberos authentication)
when interacting with other Windows services.
