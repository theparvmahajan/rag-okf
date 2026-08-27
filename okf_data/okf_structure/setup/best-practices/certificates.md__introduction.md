---
id: okf-structure/setup/best-practices/certificates.md#introduction
kind: section
title: PKI certificates and requirements
source: setup/best-practices/certificates.md
url: https://kubernetes.io/docs/setup/best-practices/certificates/
heading: null
parent: okf-structure/setup/best-practices/certificates
children: []
prev_sibling: null
next_sibling: okf-structure/setup/best-practices/certificates.md#how-certificates-are-used-by-your-cluster
word_count: 57
---

Kubernetes requires PKI certificates for authentication over TLS.
If you install Kubernetes with kubeadm, the certificates
that your cluster requires are automatically generated.
You can also generate your own certificates -- for example, to keep your private keys more secure
by not storing them on the API server.
This page explains the certificates that your cluster requires.
