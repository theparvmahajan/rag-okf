---
id: okf-structure/setup/best-practices/certificates.md#where-certificates-are-stored
kind: section
title: Where certificates are stored
source: setup/best-practices/certificates.md
url: https://kubernetes.io/docs/setup/best-practices/certificates/
heading: Where certificates are stored
parent: okf-structure/setup/best-practices/certificates
children: []
prev_sibling: okf-structure/setup/best-practices/certificates.md#how-certificates-are-used-by-your-cluster
next_sibling: okf-structure/setup/best-practices/certificates.md#configure-certificates-manually
word_count: 34
---

If you install Kubernetes with kubeadm, most certificates are stored in `/etc/kubernetes/pki`.
All paths in this documentation are relative to that directory, with the exception of user account
certificates which kubeadm places in `/etc/kubernetes`.
