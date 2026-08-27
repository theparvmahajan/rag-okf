---
id: okf-structure/concepts/storage/volumes.md#introduction
kind: section
title: Volumes
source: concepts/storage/volumes.md
url: https://kubernetes.io/docs/concepts/storage/volumes/
heading: null
parent: okf-structure/concepts/storage/volumes
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/storage/volumes.md#why-volumes-are-important
word_count: 162
---

Kubernetes _volumes_ provide a way for containers in a Pod
to access and share data via the filesystem. There are different kinds of volume that you can use for different purposes,
such as:

- populating a configuration file based on a ConfigMap
  or a Secret
- providing some temporary scratch space for a Pod
- sharing a filesystem between two different containers in the same Pod
- sharing a filesystem between two different Pods (even if those Pods run on different nodes)
- durably storing data so that it stays available even if the Pod restarts or is replaced
- passing configuration information to an app running in a container, based on details of the Pod
  the container is in
  (for example: telling a sidecar container
  what namespace the Pod is running in)
- providing read-only access to data in a different container image

Data sharing can be between different local processes within a container, or between different containers,
or between Pods.
