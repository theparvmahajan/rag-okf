---
id: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#use-configmap-defined-environment-variables-in-pod-commands
kind: section
title: Use ConfigMap-defined environment variables in Pod commands
source: tasks/configure-pod-container/configure-pod-configmap.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/
heading: Use ConfigMap-defined environment variables in Pod commands
parent: okf-structure/tasks/configure-pod-container/configure-pod-configmap
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables
next_sibling: okf-structure/tasks/configure-pod-container/configure-pod-configmap.md#add-configmap-data-to-a-volume
word_count: 72
---

You can use ConfigMap-defined environment variables in the `command` and `args` of a container
using the `$(VAR_NAME)` Kubernetes substitution syntax.

For example, the following Pod manifest:

Create that Pod, by running:

```shell
kubectl create -f https://kubernetes.io/examples/pods/pod-configmap-env-var-valueFrom.yaml
```

That pod produces the following output from the `test-container` container:
```shell
kubectl logs dapi-test-pod
```

```
very charm
```

Once you're happy to move on, delete that Pod:
```shell
kubectl delete pod dapi-test-pod --now
```
