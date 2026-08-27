---
id: okf-structure/concepts/overview/working-with-objects/namespaces.md#introduction
kind: section
title: Namespaces
source: concepts/overview/working-with-objects/namespaces.md
url: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/
heading: null
parent: okf-structure/concepts/overview/working-with-objects/namespaces
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/overview/working-with-objects/namespaces.md#when-to-use-multiple-namespaces
word_count: 51
---

In Kubernetes, _namespaces_ provide a mechanism for isolating groups of resources within a single cluster. Names of resources need to be unique within a namespace, but not across namespaces. Namespace-based scoping is applicable only for namespaced objects _(e.g. Deployments, Services, etc.)_ and not for cluster-wide objects _(e.g. StorageClass, Nodes, PersistentVolumes, etc.)_.
