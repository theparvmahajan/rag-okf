---
id: okf-structure/tasks/administer-cluster/decrypt-data.md#introduction
kind: section
title: Decrypt Confidential Data that is Already Encrypted at Rest
source: tasks/administer-cluster/decrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/decrypt-data/
heading: null
parent: okf-structure/tasks/administer-cluster/decrypt-data
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/decrypt-data.md#prerequisites
word_count: 163
---

All of the APIs in Kubernetes that let you write persistent API resource data support
at-rest encryption. For example, you can enable at-rest encryption for
Secrets.
This at-rest encryption is additional to any system-level encryption for the
etcd cluster or for the filesystem(s) on hosts where you are running the
kube-apiserver.

This page shows how to switch from encryption of API data at rest, so that API data
are stored unencrypted. You might want to do this to improve performance; usually,
though, if it was a good idea to encrypt some data, it's also a good idea to leave them
encrypted.

This task covers encryption for resource data stored using the
Kubernetes API. For example, you can
encrypt Secret objects, including the key-value data they contain.

If you wanted to manage encryption for data in filesystems that are mounted into containers, you instead
need to either:

- use a storage integration that provides encrypted
  volumes
- encrypt the data within your own application
