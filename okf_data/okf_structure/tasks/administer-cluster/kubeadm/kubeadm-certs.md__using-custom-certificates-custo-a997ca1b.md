---
id: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#using-custom-certificates-custom-certificates
kind: section
title: Using custom certificates {#custom-certificates}
source: tasks/administer-cluster/kubeadm/kubeadm-certs.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
heading: Using custom certificates {#custom-certificates}
parent: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kubeadm/kubeadm-certs.md#choosing-an-encryption-algorithm-choosing-encryption-algorithm
word_count: 96
---

By default, kubeadm generates all the certificates needed for a cluster to run.
You can override this behavior by providing your own certificates.

To do so, you must place them in whatever directory is specified by the
`--cert-dir` flag or the `certificatesDir` field of kubeadm's `ClusterConfiguration`.
By default this is `/etc/kubernetes/pki`.

If a given certificate and private key pair exists before running `kubeadm init`,
kubeadm does not overwrite them. This means you can, for example, copy an existing
CA into `/etc/kubernetes/pki/ca.crt` and `/etc/kubernetes/pki/ca.key`,
and kubeadm will use this CA for signing the rest of the certificates.
