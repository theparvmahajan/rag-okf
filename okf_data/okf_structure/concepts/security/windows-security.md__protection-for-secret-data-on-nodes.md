---
id: okf-structure/concepts/security/windows-security.md#protection-for-secret-data-on-nodes
kind: section
title: Protection for Secret data on nodes
source: concepts/security/windows-security.md
url: https://kubernetes.io/docs/concepts/security/windows-security/
heading: Protection for Secret data on nodes
parent: okf-structure/concepts/security/windows-security
children: []
prev_sibling: okf-structure/concepts/security/windows-security.md#introduction
next_sibling: okf-structure/concepts/security/windows-security.md#container-users
word_count: 55
---

On Windows, data from Secrets are written out in clear text onto the node's local
storage (as compared to using tmpfs / in-memory filesystems on Linux). As a cluster
operator, you should take both of the following additional measures:

1. Use file ACLs to secure the Secrets' file location.
1. Apply volume-level encryption using
   BitLocker.
