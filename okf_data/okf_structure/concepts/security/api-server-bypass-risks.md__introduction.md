---
id: okf-structure/concepts/security/api-server-bypass-risks.md#introduction
kind: section
title: Kubernetes API Server Bypass Risks
source: concepts/security/api-server-bypass-risks.md
url: https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/
heading: null
parent: okf-structure/concepts/security/api-server-bypass-risks
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#static-pods-static-pods
word_count: 94
---

The Kubernetes API server is the main point of entry to a cluster for external parties
(users and services) interacting with it.

As part of this role, the API server has several key built-in security controls, such as
audit logging and admission controllers.
However, there are ways to modify the configuration
or content of the cluster that bypass these controls.

This page describes the ways in which the security controls built into the
Kubernetes API server can be bypassed, so that cluster operators
and security architects can ensure that these bypasses are appropriately restricted.
