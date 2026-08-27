---
id: okf-structure/tasks/administer-cluster/change-default-storage-class.md#why-change-the-default-storage-class
kind: section
title: Why change the default storage class?
source: tasks/administer-cluster/change-default-storage-class.md
url: https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/
heading: Why change the default storage class?
parent: okf-structure/tasks/administer-cluster/change-default-storage-class
children: []
prev_sibling: okf-structure/tasks/administer-cluster/change-default-storage-class.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/change-default-storage-class.md#changing-the-default-storageclass
word_count: 128
---

Depending on the installation method, your Kubernetes cluster may be deployed with
an existing StorageClass that is marked as default. This default StorageClass
is then used to dynamically provision storage for PersistentVolumeClaims
that do not require any specific storage class. See
PersistentVolumeClaim documentation
for details.

The pre-installed default StorageClass may not fit well with your expected workload;
for example, it might provision storage that is too expensive. If this is the case,
you can either change the default StorageClass or disable it completely to avoid
dynamic provisioning of storage.

Deleting the default StorageClass may not work, as it may be re-created
automatically by the addon manager running in your cluster. Please consult the docs for your installation
for details about addon manager and how to disable individual addons.
