---
id: okf-structure/concepts/configuration/windows-resource-management.md#introduction
kind: section
title: Resource Management for Windows nodes
source: concepts/configuration/windows-resource-management.md
url: https://kubernetes.io/docs/concepts/configuration/windows-resource-management/
heading: null
parent: okf-structure/concepts/configuration/windows-resource-management
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/configuration/windows-resource-management.md#memory-management-resource-management-memory
word_count: 156
---

This page outlines the differences in how resources are managed between Linux and Windows.

On Linux nodes, cgroups are used
as a pod boundary for resource control. Containers are created within that boundary
for network, process and file system isolation. The Linux cgroup APIs can be used to
gather CPU, I/O, and memory use statistics.

In contrast, Windows uses a _job object_ per container with a system namespace filter
to contain all processes in a container and provide logical isolation from the
host.
(Job objects are a Windows process isolation mechanism and are different from
what Kubernetes refers to as a Job).

There is no way to run a Windows container without the namespace filtering in
place. This means that system privileges cannot be asserted in the context of the
host, and thus privileged containers are not available on Windows.
Containers cannot assume an identity from the host because the Security Account Manager
(SAM) is separate.
