---
id: okf-structure/concepts/security/controlling-access.md#introduction
kind: section
title: Controlling Access to the Kubernetes API
source: concepts/security/controlling-access.md
url: https://kubernetes.io/docs/concepts/security/controlling-access/
heading: null
parent: okf-structure/concepts/security/controlling-access
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/security/controlling-access.md#transport-security
word_count: 64
---

This page provides an overview of controlling access to the Kubernetes API.

Users access the Kubernetes API using `kubectl`,
client libraries, or by making REST requests.  Both human users and
Kubernetes service accounts can be
authorized for API access.
When a request reaches the API, it goes through several stages, illustrated in the
following diagram:

Diagram of request handling steps for Kubernetes API request
