---
id: okf-structure/tasks/administer-cluster/safely-drain-node.md#the-eviction-api-eviction-api
kind: section
title: The Eviction API {#eviction-api}
source: tasks/administer-cluster/safely-drain-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
heading: The Eviction API {#eviction-api}
parent: okf-structure/tasks/administer-cluster/safely-drain-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#draining-multiple-nodes-in-parallel
next_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#whatsnext
word_count: 43
---

If you prefer not to use kubectl drain (such as
to avoid calling to an external command, or to get finer control over the pod
eviction process), you can also programmatically cause evictions using the
eviction API.

For more information, see API-initiated eviction.
