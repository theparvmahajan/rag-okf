---
id: okf-structure/tasks/administer-cluster/kms-provider.md#verifying-that-the-data-is-encrypted
kind: section
title: Verifying that the data is encrypted
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Verifying that the data is encrypted
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#encrypting-your-data-with-the-kms-provider
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#ensuring-all-secrets-are-encrypted
word_count: 164
---

When encryption at rest is correctly configured, resources are encrypted on write.
After restarting your `kube-apiserver`, any newly created or updated Secret or other resource types
configured in `EncryptionConfiguration` should be encrypted when stored. To verify,
you can use the `etcdctl` command line program to retrieve the contents of your secret data.

1. Create a new secret called `secret1` in the `default` namespace:

   ```shell
   kubectl create secret generic secret1 -n default --from-literal=mykey=mydata
   ```

1. Using the `etcdctl` command line, read that secret out of etcd:

   ```shell
   ETCDCTL_API=3 etcdctl get /kubernetes.io/secrets/default/secret1 [...] | hexdump -C
   ```

   where `[...]` contains the additional arguments for connecting to the etcd server.

1. Verify the stored secret is prefixed with `k8s:enc:kms:v1:` for KMS v1 or prefixed with `k8s:enc:kms:v2:` for KMS v2, which indicates that the `kms` provider has encrypted the resulting data.

1. Verify that the secret is correctly decrypted when retrieved via the API:

   ```shell
   kubectl describe secret secret1 -n default
   ```

   The Secret should contain `mykey: mydata`
