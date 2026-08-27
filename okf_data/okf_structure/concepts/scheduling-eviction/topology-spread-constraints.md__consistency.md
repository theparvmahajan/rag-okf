---
id: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#consistency
kind: section
title: Consistency
source: concepts/scheduling-eviction/topology-spread-constraints.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/
heading: Consistency
parent: okf-structure/concepts/scheduling-eviction/topology-spread-constraints
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#topologyspreadconstraints-field
next_sibling: okf-structure/concepts/scheduling-eviction/topology-spread-constraints.md#topology-spread-constraint-examples
word_count: 111
---

You should set the same Pod topology spread constraints on all pods in a group.

Usually, if you are using a workload controller such as a Deployment, the pod template
takes care of this for you. If you mix different spread constraints then Kubernetes
follows the API definition of the field; however, the behavior is more likely to become
confusing and troubleshooting is less straightforward.

You need a mechanism to ensure that all the nodes in a topology domain (such as a
cloud provider region) are labeled consistently.
To avoid you needing to manually label nodes, most clusters automatically
populate well-known labels such as `kubernetes.io/hostname`. Check whether
your cluster supports this.
