---
id: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md#add-a-label-to-a-node
kind: section
title: Add a label to a node
source: tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/
heading: Add a label to a node
parent: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md#schedule-a-pod-using-required-node-affinity
word_count: 140
---

1. List the nodes in your cluster, along with their labels:

    ```shell
    kubectl get nodes --show-labels
    ```
    The output is similar to this:

    ```shell
    NAME      STATUS    ROLES    AGE     VERSION        LABELS
    worker0   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker0
    worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
    worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
    ```
1. Choose one of your nodes, and add a label to it:

    ```shell
    kubectl label nodes <your-node-name> disktype=ssd
    ```
    where `<your-node-name>` is the name of your chosen node.

1. Verify that your chosen node has a `disktype=ssd` label:

    ```shell
    kubectl get nodes --show-labels
    ```

    The output is similar to this:

    ```
    NAME      STATUS    ROLES    AGE     VERSION        LABELS
    worker0   Ready     <none>   1d      v1.13.0        ...,disktype=ssd,kubernetes.io/hostname=worker0
    worker1   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker1
    worker2   Ready     <none>   1d      v1.13.0        ...,kubernetes.io/hostname=worker2
    ```

    In the preceding output, you can see that the `worker0` node has a
    `disktype=ssd` label.
