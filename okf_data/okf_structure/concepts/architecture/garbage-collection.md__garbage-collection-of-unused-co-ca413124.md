---
id: okf-structure/concepts/architecture/garbage-collection.md#garbage-collection-of-unused-containers-and-images-containers-images
kind: section
title: Garbage collection of unused containers and images {#containers-images}
source: concepts/architecture/garbage-collection.md
url: https://kubernetes.io/docs/concepts/architecture/garbage-collection/
heading: Garbage collection of unused containers and images {#containers-images}
parent: okf-structure/concepts/architecture/garbage-collection
children: []
prev_sibling: okf-structure/concepts/architecture/garbage-collection.md#cascading-deletion-cascading-deletion
next_sibling: okf-structure/concepts/architecture/garbage-collection.md#configuring-garbage-collection-configuring-gc
word_count: 458
---

The kubelet performs garbage
collection on unused images every five minutes and on unused containers every
minute. You should avoid using external garbage collection tools, as these can
break the kubelet behavior and remove containers that should exist.

To configure options for unused container and image garbage collection, tune the
kubelet using a configuration file
and change the parameters related to garbage collection using the
`KubeletConfiguration`
resource type.

### Container image lifecycle

Kubernetes manages the lifecycle of all images through its *image manager*,
which is part of the kubelet, with the cooperation of
cadvisor. The kubelet
considers the following disk usage limits when making garbage collection
decisions:

* `HighThresholdPercent`
* `LowThresholdPercent`

Disk usage above the configured `HighThresholdPercent` value triggers garbage
collection, which deletes images in order based on the last time they were used,
starting with the oldest first. The kubelet deletes images
until disk usage reaches the `LowThresholdPercent` value.

#### Garbage collection for unused container images {#image-maximum-age-gc}

You can specify the maximum time a local image can be unused for,
regardless of disk usage. This is a kubelet setting that you configure for each node.

To configure the setting, you need to set a value for the `imageMaximumGCAge`
field in the kubelet configuration file.

The value is specified as a Kubernetes duration.
See duration in the glossary
for more details.

For example, you can set the configuration field to `12h45m`,
which means 12 hours and 45 minutes.

This feature does not track image usage across kubelet restarts. If the kubelet
is restarted, the tracked image age is reset, causing the kubelet to wait the full
`imageMaximumGCAge` duration before qualifying images for garbage collection
based on image age.

### Container garbage collection {#container-image-garbage-collection}

The kubelet garbage collects unused containers based on the following variables,
which you can define:

* `MinAge`: the minimum age at which the kubelet can garbage collect a
  container. Disable by setting to `0`.
* `MaxPerPodContainer`: the maximum number of dead containers each Pod 
  can have. Disable by setting to less than `0`.
* `MaxContainers`: the maximum number of dead containers the cluster can have.
  Disable by setting to less than `0`.

In addition to these variables, the kubelet garbage collects unidentified and
deleted containers, typically starting with the oldest first.

`MaxPerPodContainer` and `MaxContainers` may potentially conflict with each other
in situations where retaining the maximum number of containers per Pod
(`MaxPerPodContainer`) would go outside the allowable total of global dead
containers (`MaxContainers`). In this situation, the kubelet adjusts
`MaxPerPodContainer` to address the conflict. A worst-case scenario would be to
downgrade `MaxPerPodContainer` to `1` and evict the oldest containers.
Additionally, containers owned by pods that have been deleted are removed once
they are older than `MinAge`.

The kubelet only garbage collects the containers it manages.
