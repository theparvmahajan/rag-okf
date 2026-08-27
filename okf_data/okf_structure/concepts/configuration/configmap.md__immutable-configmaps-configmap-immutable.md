---
id: okf-structure/concepts/configuration/configmap.md#immutable-configmaps-configmap-immutable
kind: section
title: Immutable ConfigMaps {#configmap-immutable}
source: concepts/configuration/configmap.md
url: https://kubernetes.io/docs/concepts/configuration/configmap/
heading: Immutable ConfigMaps {#configmap-immutable}
parent: okf-structure/concepts/configuration/configmap
children: []
prev_sibling: okf-structure/concepts/configuration/configmap.md#using-configmaps
next_sibling: okf-structure/concepts/configuration/configmap.md#whatsnext
word_count: 157
---

The Kubernetes feature _Immutable Secrets and ConfigMaps_ provides an option to set
individual Secrets and ConfigMaps as immutable. For clusters that extensively use ConfigMaps
(at least tens of thousands of unique ConfigMap to Pod mounts), preventing changes to their
data has the following advantages:

- protects you from accidental (or unwanted) updates that could cause applications outages
- improves performance of your cluster by significantly reducing load on kube-apiserver, by
  closing watches for ConfigMaps marked as immutable.

You can create an immutable ConfigMap by setting the `immutable` field to `true`.
For example:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  ...
data:
  ...
immutable: true
```

Once a ConfigMap is marked as immutable, it is _not_ possible to revert this change
nor to mutate the contents of the `data` or the `binaryData` field. You can
only delete and recreate the ConfigMap. Because existing Pods maintain a mount point
to the deleted ConfigMap, it is recommended to recreate these pods.
