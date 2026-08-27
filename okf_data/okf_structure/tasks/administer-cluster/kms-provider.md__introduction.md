---
id: okf-structure/tasks/administer-cluster/kms-provider.md#introduction
kind: section
title: Using a KMS provider for data encryption
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: null
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#prerequisites
word_count: 123
---

This page shows how to configure a Key Management Service (KMS) provider and plugin to enable secret data encryption.
In Kubernetes  there are two versions of KMS at-rest encryption.
You should use KMS v2 if feasible because KMS v1 is deprecated (since Kubernetes v1.28) and disabled by default (since Kubernetes v1.29).
KMS v2 offers significantly better performance characteristics than KMS v1.

This documentation is for the generally available implementation of KMS v2 (and for the
deprecated version 1 implementation).
If you are using any control plane components older than Kubernetes v1.29, please check
the equivalent page in the documentation for the version of Kubernetes that your cluster
is running. Earlier releases of Kubernetes had different behavior that may be relevant
for information security.
