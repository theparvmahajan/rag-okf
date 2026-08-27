---
id: okf-structure/concepts/overview/working-with-objects/namespaces.md#not-all-objects-are-in-a-namespace
kind: section
title: Not all objects are in a namespace
source: concepts/overview/working-with-objects/namespaces.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
heading: Not all objects are in a namespace
parent: okf-structure/concepts/overview/working-with-objects/namespaces
children: []
prev_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#namespaces-and-dns
next_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#automatic-labelling
word_count: 63
---

Most Kubernetes resources (e.g. Pods, Services, Deployments, and others) are in some namespaces. However namespace resources are not themselves in a namespace. And low-level resources, such as
Nodes and
PersistentVolumes, are not in any namespace.

To see which Kubernetes resources are and aren't in a namespace:

```shell
# In a namespace
kubectl api-resources --namespaced=true

# Not in a namespace
kubectl api-resources --namespaced=false
```
