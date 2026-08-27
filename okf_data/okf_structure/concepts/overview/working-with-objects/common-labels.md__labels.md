---
id: okf-structure/concepts/overview/working-with-objects/common-labels.md#labels
kind: section
title: Labels
source: concepts/overview/working-with-objects/common-labels.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/common-labels/
heading: Labels
parent: okf-structure/concepts/overview/working-with-objects/common-labels
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/common-labels.md#introduction
next_sibling: okf-structure/concepts/overview/working-with-objects/common-labels.md#applications-and-instances-of-applications
word_count: 175
---

In order to take full advantage of using these labels, they should be applied
on every resource object.

| Key                                 | Description           | Example  | Type |
| ----------------------------------- | --------------------- | -------- | ---- |
| `app.kubernetes.io/name`            | The name of the application | `mysql` | string |
| `app.kubernetes.io/instance`        | A unique name identifying the instance of an application | `mysql-abcxyz` | string |
| `app.kubernetes.io/version`         | The current version of the application (e.g., a SemVer 1.0, revision hash, etc.) | `5.7.21` | string |
| `app.kubernetes.io/component`       | The component within the architecture | `database` | string |
| `app.kubernetes.io/part-of`         | The name of a higher level application this one is part of | `wordpress` | string |
| `app.kubernetes.io/managed-by`      | The tool being used to manage the operation of an application | `Helm` | string |

To illustrate these labels in action, consider the following StatefulSet object:

```yaml
# This is an excerpt
apiVersion: apps/v1
kind: StatefulSet
metadata:
  labels:
    app.kubernetes.io/name: mysql
    app.kubernetes.io/instance: mysql-abcxyz
    app.kubernetes.io/version: "5.7.21"
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: wordpress
    app.kubernetes.io/managed-by: Helm
```
