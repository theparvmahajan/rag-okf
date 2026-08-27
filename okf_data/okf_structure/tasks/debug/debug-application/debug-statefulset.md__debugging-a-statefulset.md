---
id: okf-structure/tasks/debug/debug-application/debug-statefulset.md#debugging-a-statefulset
kind: section
title: Debugging a StatefulSet
source: tasks/debug/debug-application/debug-statefulset.md
url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-statefulset/
heading: Debugging a StatefulSet
parent: okf-structure/tasks/debug/debug-application/debug-statefulset
children: []
prev_sibling: okf-structure/tasks/debug/debug-application/debug-statefulset.md#prerequisites
next_sibling: okf-structure/tasks/debug/debug-application/debug-statefulset.md#whatsnext
word_count: 79
---

In order to list all the pods which belong to a StatefulSet, which have a label `app.kubernetes.io/name=MyApp` set on them,
you can use the following:

```shell
kubectl get pods -l app.kubernetes.io/name=MyApp
```

If you find that any Pods listed are in `Unknown` or `Terminating` state for an extended period of time,
refer to the Deleting StatefulSet Pods task for
instructions on how to deal with them.
You can debug individual Pods in a StatefulSet using the
Debugging Pods guide.
