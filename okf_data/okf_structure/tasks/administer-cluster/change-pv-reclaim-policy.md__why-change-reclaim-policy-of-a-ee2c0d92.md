---
id: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy.md#why-change-reclaim-policy-of-a-persistentvolume
kind: section
title: Why change reclaim policy of a PersistentVolume
source: tasks/administer-cluster/change-pv-reclaim-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-pv-reclaim-policy/
heading: Why change reclaim policy of a PersistentVolume
parent: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/change-pv-reclaim-policy.md#changing-the-reclaim-policy-of-a-persistentvolume
word_count: 96
---

PersistentVolumes can have various reclaim policies, including "Retain",
"Recycle", and "Delete". For dynamically provisioned PersistentVolumes,
the default reclaim policy is "Delete". This means that a dynamically provisioned
volume is automatically deleted when a user deletes the corresponding
PersistentVolumeClaim. This automatic behavior might be inappropriate if the volume
contains precious data. In that case, it is more appropriate to use the "Retain"
policy. With the "Retain" policy, if a user deletes a PersistentVolumeClaim,
the corresponding PersistentVolume will not be deleted. Instead, it is moved to the
Released phase, where all of its data can be manually recovered.
