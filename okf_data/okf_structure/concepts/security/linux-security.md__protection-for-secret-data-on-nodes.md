---
id: okf-structure/concepts/security/linux-security.md#protection-for-secret-data-on-nodes
kind: section
title: Protection for Secret data on nodes
source: concepts/security/linux-security.md
url: https://kubernetes.io/docs/concepts/security/linux-security/
heading: Protection for Secret data on nodes
parent: okf-structure/concepts/security/linux-security
children: []
prev_sibling: okf-structure/concepts/security/linux-security.md#introduction
next_sibling: null
word_count: 97
---

On Linux nodes, memory-backed volumes (such as `secret`
volume mounts, or `emptyDir` with `medium: Memory`)
are implemented with a `tmpfs` filesystem.

If you have swap configured and use an older Linux kernel (or a current kernel and an unsupported configuration of Kubernetes),
**memory** backed volumes can have data written to persistent storage.

The Linux kernel officially supports the `noswap` option from version 6.3,
therefore it is recommended the used kernel version is 6.3 or later,
or supports the `noswap` option via a backport, if swap is enabled on the node.

Read swap memory management
for more info.
