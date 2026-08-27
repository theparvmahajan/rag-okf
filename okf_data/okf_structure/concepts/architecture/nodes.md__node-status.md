---
id: okf-structure/concepts/architecture/nodes.md#node-status
kind: section
title: Node status
source: concepts/architecture/nodes.md
url: https://kubernetes.io/docs/concepts/architecture/nodes/
heading: Node status
parent: okf-structure/concepts/architecture/nodes
children: []
prev_sibling: okf-structure/concepts/architecture/nodes.md#management
next_sibling: okf-structure/concepts/architecture/nodes.md#node-heartbeats
word_count: 41
---

A Node's status contains the following information:

* Addresses
* Conditions
* Capacity and Allocatable
* Info

You can use `kubectl` to view a Node's status and other details:

```shell
kubectl describe node <insert-node-name-here>
```

See Node Status for more details.
