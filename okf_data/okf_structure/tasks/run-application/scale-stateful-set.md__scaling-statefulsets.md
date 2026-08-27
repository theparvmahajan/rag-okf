---
id: okf-structure/tasks/run-application/scale-stateful-set.md#scaling-statefulsets
kind: section
title: Scaling StatefulSets
source: tasks/run-application/scale-stateful-set.md
url: https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/
heading: Scaling StatefulSets
parent: okf-structure/tasks/run-application/scale-stateful-set
children: []
prev_sibling: okf-structure/tasks/run-application/scale-stateful-set.md#prerequisites
next_sibling: okf-structure/tasks/run-application/scale-stateful-set.md#troubleshooting
word_count: 103
---

### Use kubectl to scale StatefulSets

First, find the StatefulSet you want to scale.

```shell
kubectl get statefulsets <stateful-set-name>
```

Change the number of replicas of your StatefulSet:

```shell
kubectl scale statefulsets <stateful-set-name> --replicas=<new-replicas>
```

### Make in-place updates on your StatefulSets

Alternatively, you can do
in-place updates
on your StatefulSets.

If your StatefulSet was initially created with `kubectl apply`,
update `.spec.replicas` of the StatefulSet manifests, and then do a `kubectl apply`:

```shell
kubectl apply -f <stateful-set-file-updated>
```

Otherwise, edit that field with `kubectl edit`:

```shell
kubectl edit statefulsets <stateful-set-name>
```

Or use `kubectl patch`:

```shell
kubectl patch statefulsets <stateful-set-name> -p '{"spec":{"replicas":<new-replicas>}}'
```
