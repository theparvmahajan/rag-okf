---
id: okf-structure/concepts/configuration/manage-resources-containers.md#local-ephemeral-storage
kind: section
title: Local ephemeral storage
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: Local ephemeral storage
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#how-kubernetes-applies-resource-requests-and-limits-how-pods-with-resource-limits-are-run
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#extended-resources
word_count: 116
---

For general concepts about local ephemeral storage and hints about
configuring the requests and/or limits of ephemeral storage for a container,
please check the local ephemeral storage
page.

### Resource monitoring for local ephemeral storage

The kubelet can measure how much local ephemeral storage is being used. It 
does this as long as you have enabled local ephemeral storage capacity isolation.

Kubernetes tracks the amount of ephemeral storage a Pod uses from the following:
* Writing to the container's writable layer (rootfs), container images, or both.
* Writing to local `emptyDir` volumes.
* The Pod's own logs (usually stored under `/var/log/pods`).
* System files managed by Kubernetes that are mapped into the Pod, such as `/etc/hosts`.
