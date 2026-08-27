---
id: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#clean-up-clean-up
kind: section
title: Clean up {#clean-up}
source: tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/
heading: Clean up {#clean-up}
parent: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#create-deviceclasses-create-deviceclasses
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#whatsnext
word_count: 20
---

To delete the DeviceClass that you created in this task, run the following
command:

```shell
kubectl delete -f https://k8s.io/examples/dra/deviceclass.yaml
```
