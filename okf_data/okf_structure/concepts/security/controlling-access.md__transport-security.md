---
id: okf-structure/concepts/security/controlling-access.md#transport-security
kind: section
title: Transport security
source: concepts/security/controlling-access.md
url: https://kubernetes.io/docs/concepts/security/controlling-access/
heading: Transport security
parent: okf-structure/concepts/security/controlling-access
children: []
prev_sibling: okf-structure/concepts/security/controlling-access.md#introduction
next_sibling: okf-structure/concepts/security/controlling-access.md#authentication
word_count: 142
---

By default, the Kubernetes API server listens on port 6443 on the first non-localhost
network interface, protected by TLS. In a typical production Kubernetes cluster, the
API serves on port 443. The port can be changed with the `--secure-port`, and the
listening IP address with the `--bind-address` flag.

The API server presents a certificate. This certificate may be signed using
a private certificate authority (CA), or based on a public key infrastructure linked
to a generally recognized CA. The certificate and corresponding private key can be set
by using the `--tls-cert-file` and `--tls-private-key-file` flags.

If your cluster uses a private certificate authority, you need a copy of that CA
certificate configured into your `~/.kube/config` on the client, so that you can
trust the connection and be confident it was not intercepted.

Your client can present a TLS client certificate at this stage.
