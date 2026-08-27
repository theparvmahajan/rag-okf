---
id: okf-structure/tasks/administer-cluster/encrypt-data.md#introduction
kind: section
title: Encrypting Confidential Data at Rest
source: tasks/administer-cluster/encrypt-data.md
url: https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
heading: null
parent: okf-structure/tasks/administer-cluster/encrypt-data
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/encrypt-data.md#prerequisites
word_count: 125
---

All of the APIs in Kubernetes that let you write persistent API resource data support
at-rest encryption. For example, you can enable at-rest encryption for
Secrets.
This at-rest encryption is additional to any system-level encryption for the
etcd cluster or for the filesystem(s) on hosts where you are running the
kube-apiserver.

This page shows how to enable and configure encryption of API data at rest.

This task covers encryption for resource data stored using the
Kubernetes API. For example, you can
encrypt Secret objects, including the key-value data they contain.

If you want to encrypt data in filesystems that are mounted into containers, you instead need
to either:

- use a storage integration that provides encrypted
  volumes
- encrypt the data within your own application
