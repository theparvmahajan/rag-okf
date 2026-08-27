---
id: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels.md#requiring-the-baseline-pod-security-standard-with-namespace-labels
kind: section
title: Requiring the `baseline` Pod Security Standard with namespace labels
source: tasks/configure-pod-container/enforce-standards-namespace-labels.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/
heading: Requiring the `baseline` Pod Security Standard with namespace labels
parent: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels.md#add-labels-to-existing-namespaces-with-kubectl-label
word_count: 84
---

This manifest defines a Namespace `my-baseline-namespace` that:

- _Blocks_ any pods that don't satisfy the `baseline` policy requirements.
- Generates a user-facing warning and adds an audit annotation to any created pod that does not
  meet the `restricted` policy requirements.
- Pins the versions of the `baseline` and `restricted` policies to v.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-baseline-namespace
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/enforce-version: v

    # We are setting these to our _desired_ `enforce` level.
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/audit-version: v
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/warn-version: v
```
