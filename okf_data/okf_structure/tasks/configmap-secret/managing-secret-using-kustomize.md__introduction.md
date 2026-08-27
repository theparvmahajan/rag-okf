---
id: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#introduction
kind: section
title: Managing Secrets using Kustomize
source: tasks/configmap-secret/managing-secret-using-kustomize.md
url: https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kustomize/
heading: null
parent: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configmap-secret/managing-secret-using-kustomize.md#prerequisites
word_count: 34
---

`kubectl` supports using the Kustomize object management tool to manage Secrets
and ConfigMaps. You create a *resource generator* using Kustomize, which
generates a Secret that you can apply to the API server using `kubectl`.
