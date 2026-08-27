---
id: okf-structure/tasks/tls/certificate-rotation.md#overview
kind: section
title: Overview
source: tasks/tls/certificate-rotation.md
url: https://kubernetes.io/docs/tasks/tls/certificate-rotation/
heading: Overview
parent: okf-structure/tasks/tls/certificate-rotation
children: []
prev_sibling: okf-structure/tasks/tls/certificate-rotation.md#prerequisites
next_sibling: okf-structure/tasks/tls/certificate-rotation.md#enabling-client-certificate-rotation
word_count: 76
---

The kubelet uses certificates to authenticate with the Kubernetes API.  By
default, these certificates are issued with a one-year expiration so that they do
not need to be renewed too frequently.

Kubernetes contains the kubelet certificate
rotation,
that will automatically generate a new key and request a new certificate from
the Kubernetes API as the current certificate approaches expiration. Once the
new certificate is available, it will be used for authenticating connections to
the Kubernetes API.
