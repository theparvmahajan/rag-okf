---
id: okf-structure/tasks/administer-cluster/namespaces.md#deleting-a-namespace
kind: section
title: Deleting a namespace
source: tasks/administer-cluster/namespaces.md
url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
heading: Deleting a namespace
parent: okf-structure/tasks/administer-cluster/namespaces
children: []
prev_sibling: okf-structure/tasks/administer-cluster/namespaces.md#creating-a-new-namespace
next_sibling: okf-structure/tasks/administer-cluster/namespaces.md#subdividing-your-cluster-using-kubernetes-namespaces
word_count: 33
---

Delete a namespace with

```shell
kubectl delete namespaces <insert-some-namespace-name>
```

This deletes _everything_ under the namespace!

This delete is asynchronous, so for a time you will see the namespace in the `Terminating` state.
