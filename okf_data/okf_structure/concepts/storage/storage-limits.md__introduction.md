---
id: okf-structure/concepts/storage/storage-limits.md#introduction
kind: section
title: Node-specific Volume Limits
source: concepts/storage/storage-limits.md
url: https://kubernetes.io/docs/concepts/storage/storage-limits/
heading: null
parent: okf-structure/concepts/storage/storage-limits
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/storage-limits.md#kubernetes-default-limits
word_count: 63
---

This page describes the maximum number of volumes that can be attached
to a Node for various cloud providers.

Cloud providers like Google, Amazon, and Microsoft typically have a limit on
how many volumes can be attached to a Node. It is important for Kubernetes to
respect those limits. Otherwise, Pods scheduled on a Node could get stuck
waiting for volumes to attach.
