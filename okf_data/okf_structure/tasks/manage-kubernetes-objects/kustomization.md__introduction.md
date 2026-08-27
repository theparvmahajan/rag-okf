---
id: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#introduction
kind: section
title: Declarative Management of Kubernetes Objects Using Kustomize
source: tasks/manage-kubernetes-objects/kustomization.md
url: https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/
heading: null
parent: okf-structure/tasks/manage-kubernetes-objects/kustomization
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/manage-kubernetes-objects/kustomization.md#prerequisites
word_count: 65
---

Kustomize is a standalone tool
to customize Kubernetes objects
through a kustomization file.

Since 1.14, kubectl also
supports the management of Kubernetes objects using a kustomization file.
To view resources found in a directory containing a kustomization file, run the following command:

```shell
kubectl kustomize <kustomization_directory>
```

To apply those resources, run `kubectl apply` with `--kustomize` or `-k` flag:

```shell
kubectl apply -k <kustomization_directory>
```
