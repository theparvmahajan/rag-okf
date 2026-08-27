---
id: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#identify-devices-to-claim-identify-devices
kind: section
title: Identify devices to claim {#identify-devices}
source: tasks/configure-pod-container/assign-resources/allocate-devices-dra.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/
heading: Identify devices to claim {#identify-devices}
parent: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#prerequisites
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#claim-resources-claim-resources
word_count: 81
---

Your cluster administrator or the device drivers create
_DeviceClasses_ that
define categories of devices. You can claim devices by using
cel to filter for specific device properties.

Get a list of DeviceClasses in the cluster:

```shell
kubectl get deviceclasses
```
The output is similar to the following:

```
NAME                 AGE
driver.example.com   16m
```
If you get a permission error, you might not have access to get DeviceClasses.
Check with your cluster administrator or with the driver provider for available
device properties.
