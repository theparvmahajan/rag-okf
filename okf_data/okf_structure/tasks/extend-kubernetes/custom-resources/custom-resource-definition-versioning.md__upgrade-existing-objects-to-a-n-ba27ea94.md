---
id: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#upgrade-existing-objects-to-a-new-stored-version
kind: section
title: Upgrade existing objects to a new stored version
source: tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/
heading: Upgrade existing objects to a new stored version
parent: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#writing-reading-and-updating-versioned-customresourcedefinition-objects
next_sibling: null
word_count: 146
---

When deprecating versions and dropping support, select a storage upgrade
procedure. 

*Option 1:* Use the Storage Version Migrator

1. Run the storage Version migrator
2. Remove the old version from the CustomResourceDefinition `status.storedVersions` field.

*Option 2:* Manually upgrade the existing objects to a new stored version

The following is an example procedure to upgrade from `v1beta1` to `v1`.

1. Set `v1` as the storage in the CustomResourceDefinition file and apply it
   using kubectl. The `storedVersions` is now `v1beta1, v1`.
2. Write an upgrade procedure to list all existing objects and write them with
   the same content. This forces the backend to write objects in the current
   storage version, which is `v1`.
3. Remove `v1beta1` from the CustomResourceDefinition `status.storedVersions` field.

Here is an example of how to patch the `status` subresource for a CRD object using `kubectl`:
```bash
kubectl patch customresourcedefinitions <CRD_Name> --subresource='status' --type='merge' -p '{"status":{"storedVersions":["v1"]}}'
```
