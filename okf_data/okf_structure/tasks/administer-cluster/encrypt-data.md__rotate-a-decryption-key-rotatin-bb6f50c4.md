---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#rotate-a-decryption-key-rotating-a-decryption-key
kind: section
title: Rotate a decryption key {#rotating-a-decryption-key}
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Rotate a decryption key {#rotating-a-decryption-key}
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#prevent-plain-text-retrieval-cleanup-all-secrets-encrypted
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#decrypt-all-data-decrypting-all-data
word_count: 212
---

Changing an encryption key for Kubernetes without incurring downtime requires a multi-step operation,
especially in the presence of a highly-available deployment where multiple `kube-apiserver` processes
are running.

1. Generate a new key and add it as the second key entry for the current provider on all
   control plane nodes.
1. Restart **all** `kube-apiserver` processes, to ensure each server can decrypt
   any data that are encrypted with the new key.
1. Make a secure backup of the new encryption key. If you lose all copies of this key you would
   need to delete all the resources were encrypted under the lost key, and workloads may not
   operate as expected during the time that at-rest encryption is broken.
1. Make the new key the first entry in the `keys` array so that it is used for encryption-at-rest
   for new writes
1. Restart all `kube-apiserver` processes to ensure each control plane host now encrypts using the new key
1. As a privileged user, run `kubectl get secrets --all-namespaces -o json | kubectl replace -f -`
   to encrypt all existing Secrets with the new key
1. After you have updated all existing Secrets to use the new key and have made a secure backup of the
   new key, remove the old decryption key from the configuration.
