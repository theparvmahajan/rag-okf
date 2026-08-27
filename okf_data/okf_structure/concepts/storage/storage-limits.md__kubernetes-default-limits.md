---
id: okf-structure/concepts/storage/storage-limits.md#kubernetes-default-limits
kind: section
title: Kubernetes default limits
source: concepts/storage/storage-limits.md
url: https://kubernetes.io/docs/concepts/storage/storage-limits/
heading: Kubernetes default limits
parent: okf-structure/concepts/storage/storage-limits
children: []
prev_sibling: okf-structure/concepts/storage/storage-limits.md#introduction
next_sibling: okf-structure/concepts/storage/storage-limits.md#dynamic-volume-limits
word_count: 35
---

The Kubernetes scheduler has default limits on the number of volumes
that can be attached to a Node:

  Cloud serviceMaximum volumes per Node
  Amazon Elastic Block Store (EBS)39
  Google Persistent Disk16
  Microsoft Azure Disk Storage16
