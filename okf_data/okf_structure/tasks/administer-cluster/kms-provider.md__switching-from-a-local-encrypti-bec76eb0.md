---
id: okf-structure/tasks/administer-cluster/kms-provider.md#switching-from-a-local-encryption-provider-to-the-kms-provider
kind: section
title: Switching from a local encryption provider to the KMS provider
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Switching from a local encryption provider to the KMS provider
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#ensuring-all-secrets-are-encrypted
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#whatsnext
word_count: 102
---

To switch from a local encryption provider to the `kms` provider and re-encrypt all of the secrets:

1. Add the `kms` provider as the first entry in the configuration file as shown in the following example.

   ```yaml
   apiVersion: apiserver.config.k8s.io/v1
   kind: EncryptionConfiguration
   resources:
     - resources:
         - secrets
       providers:
         - kms:
             apiVersion: v2
             name : myKmsPlugin
             endpoint: unix:///tmp/socketfile.sock
         - aescbc:
             keys:
               - name: key1
                 secret: <BASE 64 ENCODED SECRET>
   ```

1. Restart all `kube-apiserver` processes.

1. Run the following command to force all secrets to be re-encrypted using the `kms` provider.

   ```shell
   kubectl get secrets --all-namespaces -o json | kubectl replace -f -
   ```
