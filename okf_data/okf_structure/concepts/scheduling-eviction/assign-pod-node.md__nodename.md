---
id: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#nodename
kind: section
title: nodeName
source: concepts/scheduling-eviction/assign-pod-node.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/
heading: nodeName
parent: okf-structure/concepts/scheduling-eviction/assign-pod-node
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#affinity-and-anti-affinity
next_sibling: okf-structure/concepts/scheduling-eviction/assign-pod-node.md#nominatednodename
word_count: 226
---

`nodeName` is a more direct form of node selection than affinity or
`nodeSelector`. `nodeName` is a field in the Pod spec. If the `nodeName` field
is not empty, the scheduler ignores the Pod and the kubelet on the named node
tries to place the Pod on that node. Using `nodeName` overrules using
`nodeSelector` or affinity and anti-affinity rules.

Some of the limitations of using `nodeName` to select nodes are:

- If the named node does not exist, the Pod will not run, and in
  some cases may be automatically deleted.
- If the named node does not have the resources to accommodate the
  Pod, the Pod will fail and its reason will indicate why,
  for example OutOfmemory or OutOfcpu.
- Node names in cloud environments are not always predictable or stable.

`nodeName` is intended for use by custom schedulers or advanced use cases where
you need to bypass any configured schedulers. Bypassing the schedulers might lead to
failed Pods if the assigned Nodes get oversubscribed. You can use node affinity
or the `nodeSelector` field to assign a Pod to a specific Node without bypassing the schedulers.

Here is an example of a Pod spec using the `nodeName` field:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeName: kube-01
```

The above Pod will only run on the node `kube-01`.
