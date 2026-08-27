---
id: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels.md#add-labels-to-existing-namespaces-with-kubectl-label
kind: section
title: Add labels to existing namespaces with `kubectl label`
source: tasks/configure-pod-container/enforce-standards-namespace-labels.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/enforce-standards-namespace-labels/
heading: Add labels to existing namespaces with `kubectl label`
parent: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/enforce-standards-namespace-labels.md#requiring-the-baseline-pod-security-standard-with-namespace-labels
next_sibling: null
word_count: 214
---

When an `enforce` policy (or version) label is added or changed, the admission plugin will test
each pod in the namespace against the new policy. Violations are returned to the user as warnings.

It is helpful to apply the `--dry-run` flag when initially evaluating security profile changes for
namespaces. The Pod Security Standard checks will still be run in _dry run_ mode, giving you
information about how the new policy would treat existing pods, without actually updating a policy.

```shell
kubectl label --dry-run=server --overwrite ns --all \
    pod-security.kubernetes.io/enforce=baseline
```

### Applying to all namespaces

If you're just getting started with the Pod Security Standards, a suitable first step would be to
configure all namespaces with audit annotations for a stricter level such as `baseline`:

```shell
kubectl label --overwrite ns --all \
  pod-security.kubernetes.io/audit=baseline \
  pod-security.kubernetes.io/warn=baseline
```

Note that this is not setting an enforce level, so that namespaces that haven't been explicitly
evaluated can be distinguished. You can list namespaces without an explicitly set enforce level
using this command:

```shell
kubectl get namespaces --selector='!pod-security.kubernetes.io/enforce'
```

### Applying to a single namespace

You can update a specific namespace as well. This command adds the `enforce=restricted`
policy to `my-existing-namespace`, pinning the restricted policy version to v.

```shell
kubectl label --overwrite ns my-existing-namespace \
  pod-security.kubernetes.io/enforce=restricted \
  pod-security.kubernetes.io/enforce-version=v
```
