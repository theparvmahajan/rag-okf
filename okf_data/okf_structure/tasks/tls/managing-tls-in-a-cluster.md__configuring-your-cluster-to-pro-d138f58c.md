---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#configuring-your-cluster-to-provide-signing
kind: section
title: Configuring your cluster to provide signing
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Configuring your cluster to provide signing
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#approving-certificatesigningrequests-approving-certificate-signing-requests
next_sibling: null
word_count: 45
---

This page assumes that a signer is set up to serve the certificates API. The
Kubernetes controller manager provides a default implementation of a signer. To
enable it, pass the `--cluster-signing-cert-file` and
`--cluster-signing-key-file` parameters to the controller manager with paths to
your Certificate Authority's keypair.
