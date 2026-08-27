---
id: okf-structure/concepts/workloads/controllers/replicaset.md#how-a-replicaset-works
kind: section
title: How a ReplicaSet works
source: concepts/workloads/controllers/replicaset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
heading: How a ReplicaSet works
parent: okf-structure/concepts/workloads/controllers/replicaset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#introduction
next_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#when-to-use-a-replicaset
word_count: 180
---

A ReplicaSet is defined with fields, including a selector that specifies how to identify Pods it can acquire, a number
of replicas indicating how many Pods it should be maintaining, and a pod template specifying the data of new Pods
it should create to meet the number of replicas criteria. A ReplicaSet then fulfills its purpose by creating
and deleting Pods as needed to reach the desired number. When a ReplicaSet needs to create new Pods, it uses its Pod
template.

A ReplicaSet is linked to its Pods via the Pods' metadata.ownerReferences
field, which specifies what resource the current object is owned by. All Pods acquired by a ReplicaSet have their owning
ReplicaSet's identifying information within their ownerReferences field. It's through this link that the ReplicaSet
knows of the state of the Pods it is maintaining and plans accordingly.

A ReplicaSet identifies new Pods to acquire by using its selector. If there is a Pod that has no
OwnerReference or the OwnerReference is not a controller and it
matches a ReplicaSet's selector, it will be immediately acquired by said ReplicaSet.
