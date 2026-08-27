---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#changing-management-methods
kind: section
title: Changing management methods
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: Changing management methods
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#how-to-change-ownership-of-a-field-between-the-configuration-file-and-direct-imperative-writers
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#defining-controller-selectors-and-podtemplate-labels
word_count: 229
---

Kubernetes objects should be managed using only one method at a time.
Switching from one method to another is possible, but is a manual process.

It is OK to use imperative deletion with declarative management.

TODO(pwittrock): We need to make using imperative commands with
declarative object configuration work so that it doesn't write the
fields to the annotation, and instead.  Then add this bullet point.

- using imperative commands with declarative configuration to manage where each manages different fields.

### Migrating from imperative command management to declarative object configuration

Migrating from imperative command management to declarative object
configuration involves several manual steps:

1. Export the live object to a local configuration file:

   ```shell
   kubectl get <kind>/<name> -o yaml > <kind>_<name>.yaml
   ```

1. Manually remove the `status` field from the configuration file.

   
   This step is optional, as `kubectl apply` does not update the status field
   even if it is present in the configuration file.
   

1. Set the `kubectl.kubernetes.io/last-applied-configuration` annotation on the object:

   ```shell
   kubectl replace --save-config -f <kind>_<name>.yaml
   ```

1. Change processes to use `kubectl apply` for managing the object exclusively.

TODO(pwittrock): Why doesn't export remove the status field?  Seems like it should.

### Migrating from imperative object configuration to declarative object configuration

1. Set the `kubectl.kubernetes.io/last-applied-configuration` annotation on the object:

   ```shell
   kubectl replace --save-config -f <kind>_<name>.yaml
   ```

1. Change processes to use `kubectl apply` for managing the object exclusively.
