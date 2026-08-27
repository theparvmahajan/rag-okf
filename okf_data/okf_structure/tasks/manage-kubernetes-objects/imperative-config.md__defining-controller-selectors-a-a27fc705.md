---
id: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#defining-controller-selectors-and-podtemplate-labels
kind: section
title: Defining controller selectors and PodTemplate labels
source: tasks/manage-kubernetes-objects/imperative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/imperative-config/
heading: Defining controller selectors and PodTemplate labels
parent: okf-structure/tasks/manage-kubernetes-objects/imperative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#migrating-from-imperative-commands-to-imperative-object-configuration
next_sibling: okf-structure/tasks/manage-kubernetes-objects/imperative-config.md#whatsnext
word_count: 42
---

Updating selectors on controllers is strongly discouraged.

The recommended approach is to define a single, immutable PodTemplate label
used only by the controller selector with no other semantic meaning.

Example label:

```yaml
selector:
  matchLabels:
      controller-selector: "apps/v1/deployment/nginx"
template:
  metadata:
    labels:
      controller-selector: "apps/v1/deployment/nginx"
```
