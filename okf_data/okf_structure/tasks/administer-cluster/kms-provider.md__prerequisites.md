---
id: okf-structure/tasks/administer-cluster/kms-provider.md#prerequisites
kind: section
title: Prerequisites
source: tasks/administer-cluster/kms-provider.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/
heading: Prerequisites
parent: okf-structure/tasks/administer-cluster/kms-provider
children: []
prev_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/kms-provider.md#kms-encryption-and-per-object-encryption-keys
word_count: 130
---

The version of Kubernetes that you need depends on which KMS API version
you have selected.  Kubernetes recommends using KMS v2.

- If you selected KMS API v1 to support clusters prior to version v1.27
  or if you have a legacy KMS plugin that only supports KMS v1,
  any supported Kubernetes version will work.  This API is deprecated as of Kubernetes v1.28.
  Kubernetes does not recommend the use of this API.

### KMS v1

* Kubernetes version 1.10.0 or later is required

* For version 1.29 and later, the v1 implementation of KMS is disabled by default.
  To enable the feature, set `--feature-gates=KMSv1=true` to configure a KMS v1 provider.

* Your cluster must use etcd v3 or later

### KMS v2

* Your cluster must use etcd v3 or later
