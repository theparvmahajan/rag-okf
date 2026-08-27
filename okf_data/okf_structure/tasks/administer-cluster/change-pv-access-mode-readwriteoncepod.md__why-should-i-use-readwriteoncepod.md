---
id: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#why-should-i-use-readwriteoncepod
kind: section
title: Why should I use `ReadWriteOncePod`?
source: tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod/
heading: Why should I use `ReadWriteOncePod`?
parent: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/change-pv-access-mode-readwriteoncepod.md#migrating-existing-persistentvolumes
word_count: 85
---

Prior to Kubernetes v1.22, the `ReadWriteOnce` access mode was commonly used to
restrict PersistentVolume access for workloads that required single-writer
access to storage. However, this access mode had a limitation: it restricted
volume access to a single *node*, allowing multiple pods on the same node to
read from and write to the same volume simultaneously. This could pose a risk
for applications that demand strict single-writer access for data safety.

If ensuring single-writer access is critical for your workloads, consider
migrating your volumes to `ReadWriteOncePod`.
