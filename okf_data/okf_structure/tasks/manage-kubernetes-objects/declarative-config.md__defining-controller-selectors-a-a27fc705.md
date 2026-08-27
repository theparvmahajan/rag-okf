---
id: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#defining-controller-selectors-and-podtemplate-labels
kind: section
title: Defining controller selectors and PodTemplate labels
source: tasks/manage-kubernetes-objects/declarative-config.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/
heading: Defining controller selectors and PodTemplate labels
parent: okf-structure/tasks/manage-kubernetes-objects/declarative-config
children: []
prev_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#changing-management-methods
next_sibling: okf-structure/tasks/manage-kubernetes-objects/declarative-config.md#whatsnext
word_count: 41
---

Updating selectors on controllers is strongly discouraged.

The recommended approach is to define a single, immutable PodTemplate label
used only by the controller selector with no other semantic meaning.

**Example:**

```yaml
selector:
  matchLabels:
      controller-selector: "apps/v1/deployment/nginx"
template:
  metadata:
    labels:
      controller-selector: "apps/v1/deployment/nginx"
```
