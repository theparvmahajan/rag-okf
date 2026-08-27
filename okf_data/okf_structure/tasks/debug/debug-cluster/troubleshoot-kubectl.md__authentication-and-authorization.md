---
id: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#authentication-and-authorization
kind: section
title: Authentication and authorization
source: tasks/debug/debug-cluster/troubleshoot-kubectl.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/troubleshoot-kubectl/
heading: Authentication and authorization
parent: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#check-vpn-connectivity
next_sibling: okf-structure/tasks/debug/debug-cluster/troubleshoot-kubectl.md#verify-contexts
word_count: 68
---

If you are using the token based authentication and the kubectl is returning an error
regarding the authentication token or authentication server address, validate the
Kubernetes authentication token and the authentication server address are configured
properly.

If kubectl is returning an error regarding the authorization, make sure that you are
using the valid user credentials. And you have the permission to access the resource
that you have requested.
