---
id: okf-structure/tutorials/cluster-management/install-use-dra.md#introduction
kind: section
title: Install Drivers and Allocate Devices with DRA
source: tutorials/cluster-management/install-use-dra.md
url: https://kubernetes.io/docs/tutorials/cluster-management/install-use-dra/
heading: null
parent: okf-structure/tutorials/cluster-management/install-use-dra
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/cluster-management/install-use-dra.md#prerequisites
word_count: 160
---

This tutorial shows you how to install Dynamic Resource Allocation (DRA) drivers in your cluster and how to
use them in conjunction with the DRA APIs to allocate devices to Pods. This page is intended for cluster administrators.

Dynamic Resource Allocation (DRA)
lets a cluster manage availability and allocation of hardware resources to
satisfy Pod-based claims for hardware requirements and preferences. To support
this, a mixture of Kubernetes built-in components (like the Kubernetes
scheduler, kubelet, and kube-controller-manager) and third-party drivers from
device owners (called DRA drivers) share the responsibility to advertise,
allocate, prepare, mount, healthcheck, unprepare, and cleanup resources
throughout the Pod lifecycle. These components share information via a series of
DRA specific APIs in the `resource.k8s.io` API group including DeviceClasses, ResourceSlices, ResourceClaims, as well as
new fields in the Pod spec itself.

### Objectives
* Deploy an example DRA driver
* Deploy a Pod requesting a hardware claim using DRA APIs
* Delete a Pod that has a claim
