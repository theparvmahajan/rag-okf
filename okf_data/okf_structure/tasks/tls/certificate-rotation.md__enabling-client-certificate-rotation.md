---
id: okf-structure/tasks/tls/certificate-rotation.md#enabling-client-certificate-rotation
kind: section
title: Enabling client certificate rotation
source: tasks/tls/certificate-rotation.md
url: https://kubernetes.io/docs/tasks/tls/certificate-rotation/
heading: Enabling client certificate rotation
parent: okf-structure/tasks/tls/certificate-rotation
children: []
prev_sibling: okf-structure/tasks/tls/certificate-rotation.md#overview
next_sibling: okf-structure/tasks/tls/certificate-rotation.md#understanding-the-certificate-rotation-configuration
word_count: 48
---

The `kubelet` process accepts an argument `--rotate-certificates` that controls
if the kubelet will automatically request a new certificate as the expiration of
the certificate currently in use approaches.

The `kube-controller-manager` process accepts an argument
`--cluster-signing-duration`  (`--experimental-cluster-signing-duration` prior to 1.19)
that controls how long certificates will be issued for.
