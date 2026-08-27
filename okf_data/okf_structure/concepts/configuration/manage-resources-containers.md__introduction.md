---
id: okf-structure/concepts/configuration/manage-resources-containers.md#introduction
kind: section
title: Resource Management for Pods and Containers
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: null
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#requests-and-limits
word_count: 108
---

When you specify a pod, you can optionally specify how much of each resource a 
container needs. The most common resources to specify are CPU and memory 
(RAM); there are others.

When you specify the resource _request_ for containers in a Pod, the
kube-scheduler uses this information to decide which node to place the Pod on. 
When you specify a resource _limit_ for a container, the kubelet enforces those 
limits so that the running container is not allowed to use more of that resource 
than the limit you set. The kubelet also reserves at least the _request_ amount of 
that system resource specifically for that container to use.
