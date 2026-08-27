---
id: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#summary
kind: section
title: Summary
source: tutorials/configuration/updating-configuration-via-a-configmap.md
url: https://kubernetes.io/docs/tutorials/configuration/updating-configuration-via-a-configmap/
heading: Summary
parent: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap
children: []
prev_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#update-configuration-via-an-immutable-configmap-that-is-mounted-as-a-volume-rollout-configmap-immutable-volume
next_sibling: okf-structure/tutorials/configuration/updating-configuration-via-a-configmap.md#cleanup
word_count: 115
---

Changes to a ConfigMap mounted as a Volume on a Pod are available seamlessly after the subsequent kubelet sync.

Changes to a ConfigMap that configures environment variables for a Pod are available after the subsequent rollout for the Pod.

Once a ConfigMap is marked as immutable, it is not possible to revert this change
(you cannot make an immutable ConfigMap mutable), and you also cannot make any change
to the contents of the `data` or the `binaryData` field. You can delete and recreate
the ConfigMap, or you can make a new different ConfigMap. When you delete a ConfigMap,
running containers and their Pods maintain a mount point to any volume that referenced
that existing ConfigMap.
