---
id: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-image-signatures-with-admission-controller
kind: section
title: Verifying Image Signatures with Admission Controller
source: tasks/administer-cluster/verify-signed-artifacts.md
url: https://kubernetes.io/docs/tasks/administer-cluster/verify-signed-artifacts/
heading: Verifying Image Signatures with Admission Controller
parent: okf-structure/tasks/administer-cluster/verify-signed-artifacts
children: []
prev_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verifying-image-signatures
next_sibling: okf-structure/tasks/administer-cluster/verify-signed-artifacts.md#verify-the-software-bill-of-materials
word_count: 36
---

For non-control plane images (for example
conformance image),
signatures can also be verified at deploy time using
sigstore policy-controller
admission controller.

Here are some helpful resources to get started with `policy-controller`:

- Installation
- Configuration Options
