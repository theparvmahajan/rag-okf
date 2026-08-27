---
id: okf-structure/tasks/administer-cluster/kms-provider.md#configuring-the-kms-provider
kind: section
title: Configuring the KMS provider
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Configuring the KMS provider
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#kms-encryption-and-per-object-encryption-keys
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#implementing-a-kms-plugin
word_count: 257
---

To configure a KMS provider on the API server, include a provider of type `kms` in the
`providers` array in the encryption configuration file and set the following properties:

### KMS v1 {#configuring-the-kms-provider-kms-v1}

* `apiVersion`: API Version for KMS provider. Leave this value empty or set it to `v1`.
* `name`: Display name of the KMS plugin. Cannot be changed once set.
* `endpoint`: Listen address of the gRPC server (KMS plugin). The endpoint is a UNIX domain socket.
* `cachesize`: Number of data encryption keys (DEKs) to be cached in the clear.
  When cached, DEKs can be used without another call to the KMS;
  whereas DEKs that are not cached require a call to the KMS to unwrap.
* `timeout`: How long should `kube-apiserver` wait for kms-plugin to respond before
  returning an error (default is 3 seconds).

### KMS v2 {#configuring-the-kms-provider-kms-v2}

* `apiVersion`: API Version for KMS provider. Set this to `v2`.
* `name`: Display name of the KMS plugin. Cannot be changed once set.
* `endpoint`: Listen address of the gRPC server (KMS plugin). The endpoint is a UNIX domain socket.
* `timeout`: How long should `kube-apiserver` wait for kms-plugin to respond before
  returning an error (default is 3 seconds).

KMS v2 does not support the `cachesize` property. All data encryption keys (DEKs) will be cached in
the clear once the server has unwrapped them via a call to the KMS. Once cached, DEKs can be used
to perform decryption indefinitely without making a call to the KMS.

See Understanding the encryption at rest configuration.
