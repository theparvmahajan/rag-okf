---
id: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#about-device-allocation-with-dra-about-device-allocation-dra
kind: section
title: About device allocation with DRA {#about-device-allocation-dra}
source: tasks/configure-pod-container/assign-resources/allocate-devices-dra.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/
heading: About device allocation with DRA {#about-device-allocation-dra}
parent: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#introduction
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#prerequisites
word_count: 45
---

As a workload operator, you can _claim_ devices for your workloads by creating
ResourceClaims or ResourceClaimTemplates. When you deploy your workload,
Kubernetes and the device drivers find available devices, allocate them to your
Pods, and place the Pods on nodes that can access those devices.
