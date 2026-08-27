---
id: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md#schedule-a-pod-using-required-node-affinity
kind: section
title: Schedule a Pod using required node affinity
source: tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/
heading: Schedule a Pod using required node affinity
parent: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md#add-a-label-to-a-node
next_sibling: okf-structure/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity.md#schedule-a-pod-using-preferred-node-affinity
word_count: 89
---

This manifest describes a Pod that has a `requiredDuringSchedulingIgnoredDuringExecution` node affinity,`disktype: ssd`. 
This means that the pod will get scheduled only on a node that has a `disktype=ssd` label. 

1. Apply the manifest to create a Pod that is scheduled onto your
   chosen node:
    
    ```shell
    kubectl apply -f https://k8s.io/examples/pods/pod-nginx-required-affinity.yaml
    ```

1. Verify that the pod is running on your chosen node:

    ```shell
    kubectl get pods --output=wide
    ```

    The output is similar to this:
    
    ```
    NAME     READY     STATUS    RESTARTS   AGE    IP           NODE
    nginx    1/1       Running   0          13s    10.200.0.4   worker0
    ```
