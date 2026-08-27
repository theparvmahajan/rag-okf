---
id: okf-structure/tasks/run-application/scale-deployment.md#other-ways-to-change-the-replica-count
kind: section
title: Other ways to change the replica count
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: Other ways to change the replica count
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/scale-deployment.md#scaling-to-zero
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#when-to-use-manual-versus-automatic-scaling
word_count: 135
---

In addition to `kubectl scale`, you can change `.spec.replicas` with
`kubectl edit` or `kubectl patch`.

### Scale using `kubectl edit`

```shell
kubectl edit deployment nginx-deployment
```

Change the `.spec.replicas` field in the editor, then save and exit.

### Scale using `kubectl patch`

You can update `.spec.replicas` with a strategic merge patch:

```shell
kubectl patch deployment nginx-deployment -p '{"spec":{"replicas":4}}'
```

For scripting, use a JSON patch with a prerequisite test. The following command sets the replica count to 4, but only if the current count is 2:

```shell
kubectl patch deployment nginx-deployment --type=json -p='[
  {"op": "test", "path": "/spec/replicas", "value": 2},
  {"op": "replace", "path": "/spec/replicas", "value": 4}
]'
```

The `test` operation causes the patch to fail if the current value does not match, which prevents unintended changes when multiple people or scripts modify the same Deployment.
