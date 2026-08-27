---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#migrating-from-imperative-commands-to-imperative-object-configuration
kind: section
title: Migrating from imperative commands to imperative object configuration
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: Migrating from imperative commands to imperative object configuration
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#creating-and-editing-an-object-from-a-url-without-saving-the-configuration
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#defining-controller-selectors-and-podtemplate-labels
word_count: 57
---

Migrating from imperative commands to imperative object configuration involves
several manual steps.

1. Export the live object to a local object configuration file:

    ```shell
    kubectl get <kind>/<name> -o yaml > <kind>_<name>.yaml
    ```

1. Manually remove the status field from the object configuration file.

1. For subsequent object management, use `replace` exclusively.

    ```shell
    kubectl replace -f <kind>_<name>.yaml
    ```
