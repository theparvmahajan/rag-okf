---
id: okf-structure/tasks/configure-pod-container/assign-pods-nodes.md#create-a-pod-that-gets-scheduled-to-your-chosen-node
kind: section
title: Create a pod that gets scheduled to your chosen node
source: tasks/configure-pod-container/assign-pods-nodes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/
heading: Create a pod that gets scheduled to your chosen node
parent: okf-structure/tasks/configure-pod-container/assign-pods-nodes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pods-nodes.md#add-a-label-to-a-node
next_sibling: okf-structure/tasks/configure-pod-container/assign-pods-nodes.md#create-a-pod-that-gets-scheduled-to-specific-node
word_count: 92
---

This pod configuration file describes a pod that has a node selector,
`disktype: ssd`. This means that the pod will get scheduled on a node that has
a `disktype=ssd` label.

1. Use the configuration file to create a pod that will get scheduled on your
   chosen node:
    
    ```shell
    kubectl apply -f https://k8s.io/examples/pods/pod-nginx.yaml
    ```

1. Verify that the pod is running on your chosen node:

    ```shell
    kubectl get pods --output=wide
    ```

    The output is similar to this:
    
    ```shell
    NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
    nginx    1/1       Running   0          13s    10.200.0.4   worker0
    ```
