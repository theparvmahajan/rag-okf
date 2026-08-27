---
id: okf-structure/tasks/administer-cluster/kms-provider.md#kms-encryption-and-per-object-encryption-keys
kind: section
title: KMS encryption and per-object encryption keys
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: KMS encryption and per-object encryption keys
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#configuring-the-kms-provider
word_count: 162
---

The KMS encryption provider uses an envelope encryption scheme to encrypt data in etcd.
The data is encrypted using a data encryption key (DEK).
The DEKs are encrypted with a key encryption key (KEK) that is stored and managed in a remote KMS.

If you use the (deprecated) v1 implementation of KMS, a new DEK is generated for each encryption.

With KMS v2, a new DEK is generated **per encryption**: the API server uses a
_key derivation function_ to generate single use data encryption keys from a secret seed
combined with some random data.
The seed is rotated whenever the KEK is rotated
(see the _Understanding key_id and Key Rotation_ section below for more details).

The KMS provider uses gRPC to communicate with a specific KMS plugin over a UNIX domain socket.
The KMS plugin, which is implemented as a gRPC server and deployed on the same host(s)
as the Kubernetes control plane, is responsible for all communication with the remote KMS.
