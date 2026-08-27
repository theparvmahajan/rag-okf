---
id: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#prerequisites
kind: section
title: Prerequisites
source: tasks/manage-kubernetes-objects/storage-version-migration.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/
heading: Prerequisites
parent: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#introduction
next_sibling: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#re-encrypt-kubernetes-secrets-using-storage-version-migration
word_count: 55
---

Install `kubectl`.

 

Ensure that your cluster has the `StorageVersionMigrator`
feature gate
enabled. You will need control plane administrator access to make that change.

Enable storage version migration REST API by setting runtime config
`storagemigration.k8s.io/v1beta1` to `true` for the API server. For more information on
how to do that,
read enable or disable a Kubernetes API.
