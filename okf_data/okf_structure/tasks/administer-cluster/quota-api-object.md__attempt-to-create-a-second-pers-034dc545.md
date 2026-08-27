---
id: okf-structure/tasks/administer-cluster/quota-api-object.md#attempt-to-create-a-second-persistentvolumeclaim
kind: section
title: Attempt to create a second PersistentVolumeClaim
source: tasks/administer-cluster/quota-api-object.md
url: https://kubernetes.io/docs/tasks/administer-cluster/quota-api-object/
heading: Attempt to create a second PersistentVolumeClaim
parent: okf-structure/tasks/administer-cluster/quota-api-object
children: []
prev_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#create-a-persistentvolumeclaim
next_sibling: okf-structure/tasks/administer-cluster/quota-api-object.md#notes
word_count: 57
---

Here is the configuration file for a second PersistentVolumeClaim:

Attempt to create the second PersistentVolumeClaim:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-objects-pvc-2.yaml --namespace=quota-object-example
```

The output shows that the second PersistentVolumeClaim was not created,
because it would have exceeded the quota for the namespace.

```
persistentvolumeclaims "pvc-quota-demo-2" is forbidden:
exceeded quota: object-quota-demo, requested: persistentvolumeclaims=1,
used: persistentvolumeclaims=1, limited: persistentvolumeclaims=1
```
