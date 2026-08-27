---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#objectives
kind: section
title: Objectives
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Objectives
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#prerequisites
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#creating-a-statefulset
word_count: 100
---

StatefulSets are intended to be used with stateful applications and distributed
systems. However, the administration of stateful applications and
distributed systems on Kubernetes is a broad, complex topic. In order to
demonstrate the basic features of a StatefulSet, and not to conflate the former
topic with the latter, you will deploy a simple web application using a StatefulSet.

After this tutorial, you will be familiar with the following.

* How to create a StatefulSet
* How a StatefulSet manages its Pods
* How to delete a StatefulSet
* How to scale a StatefulSet
* How to update a StatefulSet's Pods
