---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#decrypt-all-data-decrypting-all-data
kind: section
title: Decrypt all data {#decrypting-all-data}
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Decrypt all data {#decrypting-all-data}
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#rotate-a-decryption-key-rotating-a-decryption-key
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#configure-automatic-reloading
word_count: 147
---

This example shows how to stop encrypting the Secret API at rest. If you are encrypting
other API kinds, adjust the steps to match.

To disable encryption at rest, place the `identity` provider as the first
entry in your encryption configuration file:

```yaml
---
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
      - secrets
      # list any other resources here that you previously were
      # encrypting at rest
    providers:
      - identity: {} # add this line
      - aescbc:
          keys:
            - name: key1
              secret: <BASE 64 ENCODED SECRET> # keep this in place
                                               # make sure it comes after "identity"
```

Then run the following command to force decryption of all Secrets:

```shell
kubectl get secrets --all-namespaces -o json | kubectl replace -f -
```

Once you have replaced all existing encrypted resources with backing data that
don't use encryption, you can remove the encryption settings from the
`kube-apiserver`.
