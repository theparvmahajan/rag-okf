---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#cleanup
kind: section
title: Cleanup
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Cleanup
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#restrictions
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#whatsnext
word_count: 89
---

Delete the ConfigMaps and Pods that you made:

```bash
kubectl delete configmaps/game-config configmaps/game-config-2 configmaps/game-config-3 \
               configmaps/game-config-env-file
kubectl delete pod dapi-test-pod --now

# You might already have removed the next set
kubectl delete configmaps/special-config configmaps/env-config
kubectl delete configmap -l 'game-config in (config-4,config-5)'
```

Remove the `kustomization.yaml` file that you used to generate the ConfigMap:

```bash
rm kustomization.yaml
```

If you created a directory `configure-pod-container` and no longer need it, you should remove that too,
or move it into the trash can / deleted files location.

```bash
rm -r configure-pod-container
```
