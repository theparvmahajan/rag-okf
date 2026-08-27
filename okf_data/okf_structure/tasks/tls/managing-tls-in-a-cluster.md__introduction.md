---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#introduction
kind: section
title: Manage TLS Certificates in a Cluster
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: null
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#prerequisites
word_count: 94
---

Kubernetes provides a `certificates.k8s.io` API, which lets you provision TLS
certificates signed by a Certificate Authority (CA) that you control. These CAs
and certificates can be used by your workloads to establish trust.

The `certificates.k8s.io` API uses a protocol that is similar to the ACME
draft.

Certificates created using the `certificates.k8s.io` API are signed by a
dedicated CA. It is possible to configure your cluster to use the cluster root
CA for this purpose, but you should never rely on this. Do not assume that
these certificates will validate against the cluster root CA.
