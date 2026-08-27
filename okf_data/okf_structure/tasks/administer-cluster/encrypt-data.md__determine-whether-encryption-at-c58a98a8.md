---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#determine-whether-encryption-at-rest-is-already-enabled-determining-whether-encryption-at-rest-is-already-enabled
kind: section
title: Determine whether encryption at rest is already enabled {#determining-whether-encryption-at-rest-is-already-enabled}
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: Determine whether encryption at rest is already enabled {#determining-whether-encryption-at-rest-is-already-enabled}
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#understanding-the-encryption-at-rest-configuration
word_count: 184
---

By default, the API server stores plain-text representations of resources into etcd, with
no at-rest encryption.

The `kube-apiserver` process accepts an argument `--encryption-provider-config`
that specifies a path to a configuration file. The contents of that file, if you specify one,
control how Kubernetes API data is encrypted in etcd.
If you are running the kube-apiserver without the `--encryption-provider-config` command line
argument, you do not have encryption at rest enabled. If you are running the kube-apiserver
with the `--encryption-provider-config` command line argument, and the file that it references
specifies the `identity` provider as the first encryption provider in the list, then you
do not have at-rest encryption enabled
(**the default `identity` provider does not provide any confidentiality protection.**)

If you are running the kube-apiserver
with the `--encryption-provider-config` command line argument, and the file that it references
specifies a provider other than `identity` as the first encryption provider in the list, then
you already have at-rest encryption enabled. However, that check does not tell you whether
a previous migration to encrypted storage has succeeded. If you are not sure, see
ensure all relevant data are encrypted.
