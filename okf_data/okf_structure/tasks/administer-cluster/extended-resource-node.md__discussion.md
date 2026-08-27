---
id: okf-structure/tasks/administer-cluster/extended-resource-node.md#discussion
kind: section
title: Discussion
source: tasks/administer-cluster/extended-resource-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/
heading: Discussion
parent: okf-structure/tasks/administer-cluster/extended-resource-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/extended-resource-node.md#advertise-a-new-extended-resource-on-one-of-your-nodes
next_sibling: okf-structure/tasks/administer-cluster/extended-resource-node.md#clean-up
word_count: 241
---

Extended resources are similar to memory and CPU resources. For example,
just as a Node has a certain amount of memory and CPU to be shared by all components
running on the Node, it can have a certain number of dongles to be shared
by all components running on the Node. And just as application developers
can create Pods that request a certain amount of memory and CPU, they can
create Pods that request a certain number of dongles.

Extended resources are opaque to Kubernetes; Kubernetes does not
know anything about what they are. Kubernetes knows only that a Node
has a certain number of them. Extended resources must be advertised in integer
amounts. For example, a Node can advertise four dongles, but not 4.5 dongles.

### Storage example

Suppose a Node has 800 GiB of a special kind of disk storage. You could
create a name for the special storage, say example.com/special-storage.
Then you could advertise it in chunks of a certain size, say 100 GiB. In that case,
your Node would advertise that it has eight resources of type
example.com/special-storage.

```yaml
Capacity:
 ...
 example.com/special-storage: 8
```

If you want to allow arbitrary requests for special storage, you
could advertise special storage in chunks of size 1 byte. In that case, you would advertise
800Gi resources of type example.com/special-storage.

```yaml
Capacity:
 ...
 example.com/special-storage:  800Gi
```

Then a Container could request any number of bytes of special storage, up to 800Gi.
