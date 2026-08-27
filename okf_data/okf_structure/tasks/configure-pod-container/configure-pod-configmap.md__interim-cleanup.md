---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#interim-cleanup
kind: section
title: Interim cleanup
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Interim cleanup
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#create-a-configmap
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#define-container-environment-variables-using-configmap-data
word_count: 53
---

Before proceeding, clean up some of the ConfigMaps you made:

```bash
kubectl delete configmap special-config
kubectl delete configmap env-config
kubectl delete configmap -l 'game-config in (config-4,config-5)'
```

Now that you have learned to define ConfigMaps, you can move on to the next
section, and learn how to use these objects with Pods.

---
