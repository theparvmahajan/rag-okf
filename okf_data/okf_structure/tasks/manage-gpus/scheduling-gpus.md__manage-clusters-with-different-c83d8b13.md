---
id: okf-structure/tasks/manage-gpus/scheduling-gpus.md#manage-clusters-with-different-types-of-gpus
kind: section
title: Manage clusters with different types of GPUs
source: tasks/manage-gpus/scheduling-gpus.md
url: https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/
heading: Manage clusters with different types of GPUs
parent: okf-structure/tasks/manage-gpus/scheduling-gpus
children: []
prev_sibling: okf-structure/tasks/manage-gpus/scheduling-gpus.md#using-device-plugins
next_sibling: okf-structure/tasks/manage-gpus/scheduling-gpus.md#automatic-node-labelling-node-labeller
word_count: 68
---

If different nodes in your cluster have different types of GPUs, then you
can use Node Labels and Node Selectors
to schedule pods to appropriate nodes.

For example:

```shell
# Label your nodes with the accelerator type they have.
kubectl label nodes node1 accelerator=example-gpu-x100
kubectl label nodes node2 accelerator=other-gpu-k915
```

That label key `accelerator` is just an example; you can use
a different label key if you prefer.
