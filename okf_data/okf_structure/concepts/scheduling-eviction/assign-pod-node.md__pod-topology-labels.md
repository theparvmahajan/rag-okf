---
id: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#pod-topology-labels
kind: section
title: Pod topology labels
source: concepts/scheduling-eviction/assign-pod-node.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
heading: Pod topology labels
parent: okf-structure/concepts/scheduling-eviction/assign-pod-node
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#pod-topology-spread-constraints
next_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#operators
word_count: 85
---

Pods inherit the topology labels (`topology.kubernetes.io/zone` and `topology.kubernetes.io/region`) from their assigned Node if those labels are present. These labels can then be utilized via the Downward API to provide the workload with node topology awareness.

Here is an example of a Pod using downward API for it's zone and region:
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-topology-labels
spec:
  containers:
    - name: app
      image: alpine
      command: ["sh", "-c", "env"]
      env:
        - name: MY_ZONE
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['topology.kubernetes.io/zone']
        - name: MY_REGION
          valueFrom:
            fieldRef:
              fieldPath: metadata.labels['topology.kubernetes.io/region']
```
