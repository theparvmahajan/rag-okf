---
id: okf-structure/tasks/administer-cluster/decrypt-data.md#determine-whether-encryption-at-rest-is-already-enabled
kind: section
title: Determine whether encryption at rest is already enabled
source: tasks/administer-cluster/decrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/
heading: Determine whether encryption at rest is already enabled
parent: okf-structure/tasks/administer-cluster/decrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#decrypt-all-data-decrypting-all-data
word_count: 200
---

By default, the API server uses an `identity` provider that stores plain-text representations
of resources.
**The default `identity` provider does not provide any confidentiality protection.**

The `kube-apiserver` process accepts an argument `--encryption-provider-config`
that specifies a path to a configuration file. The contents of that file, if you specify one,
control how Kubernetes API data is encrypted in etcd.
If it is not specified, you do not have encryption at rest enabled.

The format of that configuration file is YAML, representing a configuration API kind named
`EncryptionConfiguration`.
You can see an example configuration
in Encryption at rest configuration.

If `--encryption-provider-config` is set, check which resources (such as `secrets`) are
configured for encryption, and what provider is used.
Make sure that the preferred provider for that resource type is **not** `identity`; you
only set `identity` (_no encryption_) as default when you want to disable encryption at
rest.
Verify that the first-listed provider for a resource is something **other** than `identity`,
which means that any new information written to resources of that type will be encrypted as
configured. If you do see `identity` as the first-listed provider for any resource, this
means that those resources are being written out to etcd without encryption.
