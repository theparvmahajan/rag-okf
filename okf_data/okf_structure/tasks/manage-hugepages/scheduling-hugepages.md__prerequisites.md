---
id: okf-structure/tasks/manage-hugepages/scheduling-hugepages.md#prerequisites
kind: section
title: Prerequisites
source: tasks/manage-hugepages/scheduling-hugepages.md
url: https://kubernetes.io/docs/tasks/manage-hugepages/scheduling-hugepages/
heading: Prerequisites
parent: okf-structure/tasks/manage-hugepages/scheduling-hugepages
children: []
prev_sibling: okf-structure/tasks/manage-hugepages/scheduling-hugepages.md#introduction
next_sibling: okf-structure/tasks/manage-hugepages/scheduling-hugepages.md#api
word_count: 134
---

Kubernetes nodes must
pre-allocate huge pages
in order for the node to report its huge page capacity.

A node can pre-allocate huge pages for multiple sizes, for instance,
the following line in `/etc/default/grub` allocates `2*1GiB` of 1 GiB
and `512*2 MiB` of 2 MiB pages:

```
GRUB_CMDLINE_LINUX="hugepagesz=1G hugepages=2 hugepagesz=2M hugepages=512"
```

The nodes will automatically discover and report all huge page resources as
schedulable resources.

When you describe the Node, you should see something similar to the following
in the following in the `Capacity` and `Allocatable` sections:

```
Capacity:
  cpu:                ...
  ephemeral-storage:  ...
  hugepages-1Gi:      2Gi
  hugepages-2Mi:      1Gi
  memory:             ...
  pods:               ...
Allocatable:
  cpu:                ...
  ephemeral-storage:  ...
  hugepages-1Gi:      2Gi
  hugepages-2Mi:      1Gi
  memory:             ...
  pods:               ...
```

For dynamically allocated pages (after boot), the Kubelet needs to be restarted
for the new allocations to be refrelected.
