---
id: okf-structure/tasks/administer-cluster/quota-api-object.md#create-a-persistentvolumeclaim
kind: section
title: Create a PersistentVolumeClaim
source: tasks/administer-cluster/quota-api-object.md
url: https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/
heading: Create a PersistentVolumeClaim
parent: okf-structure/tasks/administer-cluster/quota-api-object
children: []
prev_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#create-a-resourcequota
next_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#attempt-to-create-a-second-persistentvolumeclaim
word_count: 48
---

Here is the configuration file for a PersistentVolumeClaim object:

Create the PersistentVolumeClaim:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects-pvc.yaml --namespace=quota-object-example
```

Verify that the PersistentVolumeClaim was created:

```shell
kubectl get persistentvolumeclaims --namespace=quota-object-example
```

The output shows that the PersistentVolumeClaim exists and has status Pending:

```
NAME             STATUS
pvc-quota-demo   Pending
```
