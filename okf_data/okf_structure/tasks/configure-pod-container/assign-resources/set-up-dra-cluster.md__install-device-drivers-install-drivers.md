---
id: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#install-device-drivers-install-drivers
kind: section
title: Install device drivers {#install-drivers}
source: tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/
heading: Install device drivers {#install-drivers}
parent: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#verify-that-dra-is-enabled-verify
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#create-deviceclasses-create-deviceclasses
word_count: 125
---

After you enable DRA for your cluster, you can install the drivers for your
attached devices. For instructions, check the documentation of your device
owner or the project that maintains the device drivers. The drivers that you
install must be compatible with DRA.

To verify that your installed drivers are working as expected, list
ResourceSlices in your cluster:

```shell
kubectl get resourceslices
```
The output is similar to the following:

```
NAME                                                  NODE                DRIVER               POOL                             AGE
00000-driver.example.com-cluster-1-node-1-abcde      cluster-1-node-1    driver.example.com   cluster-1-device-pool-1-r1gc     7s
00000-driver.example.com-cluster-1-node-2-fghij      cluster-1-node-2    driver.example.com   cluster-1-device-pool-2-446z     8s
```

Try the following troubleshooting steps:

1. Check the health of the DRA driver and look for error messages about
   publishing ResourceSlices in its log output. The vendor of the driver
   may have further instructions about installation and troubleshooting.
