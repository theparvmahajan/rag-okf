---
id: okf-structure/concepts/configuration/manage-resources-containers.md#resource-types
kind: section
title: Resource types
source: concepts/configuration/manage-resources-containers.md
url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
heading: Resource types
parent: okf-structure/concepts/configuration/manage-resources-containers
children: []
prev_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#requests-and-limits
next_sibling: okf-structure/concepts/configuration/manage-resources-containers.md#resource-requests-and-limits-of-pod-and-container
word_count: 218
---

A *resource type* has a base unit and can be requested, limited, or both.
Kubernetes has the following built-in resource types:

| Resource type | Description | Base unit |
|---|---|---|
| `cpu` | Compute processing | cpu (core) |
| `memory` | RAM | Bytes |
| `ephemeral-storage` | Local ephemeral storage | Bytes |
| `hugepages-<size>` | Huge pages (Linux only) | Bytes |

Clusters can also provide
extended resources
(resources with a custom name, typically exposed by device plugins).

### Huge pages

For Linux workloads, you can specify _huge page_ resources.
Huge pages are a Linux-specific feature where the node kernel allocates blocks of memory
that are much larger than the default page size.

For example, on a system where the default page size is 4KiB, you could specify a limit,
`hugepages-2Mi: 80Mi`. If the container tries allocating over 40 2MiB huge pages (a
total of 80 MiB), that allocation fails.

You cannot overcommit `hugepages-*` resources.
This is different from the `memory` and `cpu` resources.

CPU and memory are collectively referred to as *compute resources*, or *resources*. Compute
resources are measurable quantities that can be requested, allocated, and
consumed. They are distinct from
API resources. API resources, such as Pods and
Services are objects that can be read and modified
through the Kubernetes API server.
