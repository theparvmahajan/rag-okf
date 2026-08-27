---
id: okf-structure/tasks/administer-cluster/kms-provider.md#ensuring-all-secrets-are-encrypted
kind: section
title: Ensuring all secrets are encrypted
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Ensuring all secrets are encrypted
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#verifying-that-the-data-is-encrypted
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#switching-from-a-local-encryption-provider-to-the-kms-provider
word_count: 82
---

When encryption at rest is correctly configured, resources are encrypted on write.
Thus we can perform an in-place no-op update to ensure that data is encrypted.

The following command reads all secrets and then updates them to apply server side encryption.
If an error occurs due to a conflicting write, retry the command.
For larger clusters, you may wish to subdivide the secrets by namespace or script an update.

```shell
kubectl get secrets --all-namespaces -o json | kubectl replace -f -
```
