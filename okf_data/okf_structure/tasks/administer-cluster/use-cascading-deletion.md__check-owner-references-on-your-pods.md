---
id: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#check-owner-references-on-your-pods
kind: section
title: Check owner references on your pods
source: tasks/administer-cluster/use-cascading-deletion.md
url: https://kubernetes.io/docs/tasks/administer-cluster/use-cascading-deletion/
heading: Check owner references on your pods
parent: okf-structure/tasks/administer-cluster/use-cascading-deletion
children: []
prev_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/use-cascading-deletion.md#use-foreground-cascading-deletion-use-foreground-cascading-deletion
word_count: 47
---

Check that the `ownerReferences` field is present on your pods:

```shell 
kubectl get pods -l app=nginx --output=yaml
```

The output has an `ownerReferences` field similar to this:

```yaml
apiVersion: v1
    ...
    ownerReferences:
    - apiVersion: apps/v1
      blockOwnerDeletion: true
      controller: true
      kind: ReplicaSet
      name: nginx-deployment-6b474476c4
      uid: 4fdcd81c-bd5d-41f7-97af-3a3b759af9a7
    ...
```
