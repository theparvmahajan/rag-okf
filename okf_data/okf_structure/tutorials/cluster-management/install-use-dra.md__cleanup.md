---
id: okf-structure/tutorials/cluster-management/install-use-dra.md#cleanup
kind: section
title: Cleanup
source: tutorials/cluster-management/install-use-dra.md
url: https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/
heading: Cleanup
parent: okf-structure/tutorials/cluster-management/install-use-dra
children: []
prev_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#delete-a-pod-that-has-a-claim-delete-pod-claim
next_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#whatsnext
word_count: 36
---

To clean up the resources that you created in this tutorial, follow these steps:

```shell
kubectl delete namespace dra-tutorial
kubectl delete deviceclass gpu.example.com
kubectl delete clusterrole dra-example-driver-role
kubectl delete clusterrolebinding dra-example-driver-role-binding
kubectl delete priorityclass dra-driver-high-priority
```
