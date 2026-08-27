---
id: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#introduction
kind: section
title: Migrate Kubernetes Objects Using Storage Version Migration
source: tasks/manage-kubernetes-objects/storage-version-migration.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/
heading: null
parent: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/manage-kubernetes-objects/storage-version-migration.md#prerequisites
word_count: 129
---

Kubernetes relies on API data being actively re-written, to support some
maintenance activities related to at rest storage. Two prominent examples are
the versioned schema of stored resources (that is, the preferred storage schema
changing from v1 to v2 for a given resource) and encryption at rest
(that is, rewriting stale data based on a change in how the data should be encrypted).

Running storage version migrations allows for the assurance that all objects for
a Resource have been migrated off of a stale storage version. The requirements
to running a storage migration is ensuring that the Resource has an integer
resource version. All Kubernetes Resources and CRDs are ensured to have this
property, but migration will fail if this is not the case, for instance with
aggregated APIs.
