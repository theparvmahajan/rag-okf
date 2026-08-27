---
id: okf-structure/concepts/workloads/pods/advanced-pod-config.md#influencing-pod-scheduling-decisions-scheduling
kind: section
title: Influencing Pod scheduling decisions {#scheduling}
source: concepts/workloads/pods/advanced-pod-config.md
url: https://kubernetes.io/docs/concepts/workloads/pods/advanced-pod-config/
heading: Influencing Pod scheduling decisions {#scheduling}
parent: okf-structure/concepts/workloads/pods/advanced-pod-config
children: []
prev_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#pod-and-container-level-security-context-configuration-security-context
next_sibling: okf-structure/concepts/workloads/pods/advanced-pod-config.md#pod-overhead
word_count: 244
---

Kubernetes provides several mechanisms to control which nodes your Pods are scheduled on.

### Node selectors

The simplest form of node selection constraint:

apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    disktype: ssd

### Node affinity

Node affinity allows you to specify rules that constrain which nodes your Pod can be scheduled on. Here's an example of a Pod that prefers running on nodes labelled as being on a particular continent, selecting based on the value of `topology.kubernetes.io/zone` label.

apiVersion: v1
kind: Pod
metadata:
  name: with-node-affinity
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: topology.kubernetes.io/zone
            operator: In
            values:
            - antarctica-east1
            - antarctica-west1
  containers:
  - name: with-node-affinity
    image: registry.k8s.io/pause:3.8

### Pod affinity and anti-affinity

In addition to node affinity, you can also constrain which nodes a Pod can be scheduled on based on the labels of _other Pods_ that are already running on nodes. Pod affinity allows you to specify rules about where a Pod should be placed relative to other Pods.

apiVersion: v1
kind: Pod
metadata:
  name: with-pod-affinity
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchExpressions:
          - key: app
            operator: In
            values:
            - database
        topologyKey: topology.kubernetes.io/zone
  containers:
  - name: with-pod-affinity
    image: registry.k8s.io/pause:3.8

### Tolerations

_Tolerations_ allow Pods to be scheduled on nodes with matching taints:

apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - name: myapp
    image: nginx
  tolerations:
  - key: "key"
    operator: "Equal"
    value: "value"
    effect: "NoSchedule"

For more information, see Assign Pods to Nodes.
