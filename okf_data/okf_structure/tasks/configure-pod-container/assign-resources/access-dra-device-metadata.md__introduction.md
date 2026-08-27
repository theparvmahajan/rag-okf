---
id: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#introduction
kind: section
title: Access DRA Device Metadata
source: tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/access-dra-device-metadata/
heading: null
parent: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/access-dra-device-metadata.md#prerequisites
word_count: 63
---

This page shows you how to access
device metadata
from containers that use _dynamic resource allocation (DRA)_. Device metadata
lets workloads discover information about allocated devices such as device
attributes or network interface details — by reading JSON files at
well-known paths inside the container.

Before reading this page, familiarize yourself with
Dynamic Resource Allocation (DRA)
and how to
allocate devices to workloads.
