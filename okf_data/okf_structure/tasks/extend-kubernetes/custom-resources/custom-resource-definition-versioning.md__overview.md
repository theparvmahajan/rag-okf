---
id: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#overview
kind: section
title: Overview
source: tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning/
heading: Overview
parent: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#prerequisites
next_sibling: okf-structure/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning.md#specify-multiple-versions
word_count: 491
---

The CustomResourceDefinition API provides a workflow for introducing and upgrading
to new versions of a CustomResourceDefinition.

When a CustomResourceDefinition is created, the first version is set in the
CustomResourceDefinition `spec.versions` list to an appropriate stability level
and a version number. For example `v1beta1` would indicate that the first
version is not yet stable. All custom resource objects will initially be stored
at this version.

Once the CustomResourceDefinition is created, clients may begin using the
`v1beta1` API.

Later it might be necessary to add new version such as `v1`.

Adding a new version:

1. Pick a conversion strategy. Since custom resource objects need the ability to
   be served at both versions, that means they will sometimes be served in a
   different version than the one stored. To make this possible, the custom resource objects must sometimes be converted between the
   version they are stored at and the version they are served at. If the
   conversion involves schema changes and requires custom logic, a conversion
   webhook should be used. If there are no schema changes, the default `None`
   conversion strategy may be used and only the `apiVersion` field will be
   modified when serving different versions.
1. If using conversion webhooks, create and deploy the conversion webhook. See
   the Webhook conversion for more details.
1. Update the CustomResourceDefinition to include the new version in the
   `spec.versions` list with `served:true`.  Also, set `spec.conversion` field
   to the selected conversion strategy. If using a conversion webhook, configure
   `spec.conversion.webhookClientConfig` field to call the webhook.

Once the new version is added, clients may incrementally migrate to the new
version. It is perfectly safe for some clients to use the old version while
others use the new version.

Migrate stored objects to the new version:

1. See the upgrade existing objects to a new stored version section.

It is safe for clients to use both the old and new version before, during and
after upgrading the objects to a new stored version.

Removing an old version:

1. Ensure all clients are fully migrated to the new version. The kube-apiserver
   logs can be reviewed to help identify any clients that are still accessing via
   the old version.
1. Set `served` to `false` for the old version in the `spec.versions` list. If
   any clients are still unexpectedly using the old version they may begin reporting
   errors attempting to access the custom resource objects at the old version.
   If this occurs, switch back to using `served:true` on the old version, migrate the 
   remaining clients to the new version and repeat this step.
1. Ensure the upgrade of existing objects to the new stored version step has been completed.
   1. Verify that the `storage` is set to `true` for the new version in the `spec.versions` list in the CustomResourceDefinition.
   1. Verify that the old version is no longer listed in the CustomResourceDefinition `status.storedVersions`.
1. Remove the old version from the CustomResourceDefinition `spec.versions` list.
1. Drop conversion support for the old version in conversion webhooks.
