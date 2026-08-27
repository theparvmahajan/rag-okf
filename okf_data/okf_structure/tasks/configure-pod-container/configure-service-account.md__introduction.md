---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#introduction
kind: section
title: Configure Service Accounts for Pods
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: null
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#prerequisites
word_count: 102
---

Kubernetes offers two distinct ways for clients that run within your
cluster, or that otherwise have a relationship to your cluster's
control plane
to authenticate to the
API server.

A _service account_ provides an identity for processes that run in a Pod,
and maps to a ServiceAccount object. When you authenticate to the API
server, you identify yourself as a particular _user_. Kubernetes recognises
the concept of a user, however, Kubernetes itself does **not** have a User
API.

This task guide is about ServiceAccounts, which do exist in the Kubernetes
API. The guide shows you some ways to configure ServiceAccounts for Pods.
