---
id: okf-structure/concepts/storage/volumes.md#how-volumes-work
kind: section
title: How volumes work
source: concepts/storage/volumes.md
url: https://kubernetes.io/docs/concepts/storage/volumes/
heading: How volumes work
parent: okf-structure/concepts/storage/volumes
children: []
prev_sibling: okf-structure/concepts/storage/volumes.md#why-volumes-are-important
next_sibling: okf-structure/concepts/storage/volumes.md#types-of-volumes-volume-types
word_count: 267
---

Kubernetes supports many types of volumes. A Pod
can use any number of volume types simultaneously.
Ephemeral volume types have a lifetime linked to a specific Pod,
but persistent volumes exist beyond
the lifetime of any individual Pod. When a Pod ceases to exist, Kubernetes destroys ephemeral volumes;
however, Kubernetes does not destroy persistent volumes.
For any kind of volume in a given Pod, data is preserved across container restarts.

At its core, a volume is a directory, possibly with some data in it, which
is accessible to the containers in a pod. How that directory comes to be, the
medium that backs it, and the contents of it are determined by the particular
volume type used.

To use a volume, specify the volumes to provide for the Pod in `.spec.volumes`
and declare where to mount those volumes into containers in `.spec.containers[*].volumeMounts`.

When a Pod is launched, a process in the container sees a filesystem view composed from the initial contents of
the container image, plus volumes
(if defined) mounted inside the container.
The process sees a root filesystem that initially matches the contents of the container image.
Any writes to within that filesystem hierarchy, if allowed, affect what that process views
when it performs a subsequent filesystem access.
Volumes are mounted at specified paths within the container filesystem.
For each container defined within a Pod, you must independently specify where
to mount each volume that the container uses.

Volumes cannot mount within other volumes (but see Using subPath
for a related mechanism). Also, a volume cannot contain a hard link to anything in
a different volume.
