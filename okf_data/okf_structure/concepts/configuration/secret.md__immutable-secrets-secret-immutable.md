---
id: okf-structure/concepts/configuration/secret.md#immutable-secrets-secret-immutable
kind: section
title: Immutable Secrets {#secret-immutable}
source: concepts/configuration/secret.md
url: https://kubernetes.io/docs/concepts/configuration/secret/
heading: Immutable Secrets {#secret-immutable}
parent: okf-structure/concepts/configuration/secret
children: []
prev_sibling: okf-structure/concepts/configuration/secret.md#working-with-secrets
next_sibling: okf-structure/concepts/configuration/secret.md#information-security-for-secrets
word_count: 186
---

Kubernetes lets you mark specific Secrets (and ConfigMaps) as _immutable_.
Preventing changes to the data of an existing Secret has the following benefits:

- protects you from accidental (or unwanted) updates that could cause applications outages
- (for clusters that extensively use Secrets - at least tens of thousands of unique Secret
  to Pod mounts), switching to immutable Secrets improves the performance of your cluster
  by significantly reducing load on kube-apiserver. The kubelet does not need to maintain
  a [watch] on any Secrets that are marked as immutable.

### Marking a Secret as immutable {#secret-immutable-create}

You can create an immutable Secret by setting the `immutable` field to `true`. For example,

```yaml
apiVersion: v1
kind: Secret
metadata: ...
data: ...
immutable: true
```

You can also update any existing mutable Secret to make it immutable.

Once a Secret or ConfigMap is marked as immutable, it is _not_ possible to revert this change
nor to mutate the contents of the `data` field. You can only delete and recreate the Secret.
Existing Pods maintain a mount point to the deleted Secret - it is recommended to recreate
these pods.
