---
id: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#claim-resources-claim-resources
kind: section
title: Claim resources {#claim-resources}
source: tasks/configure-pod-container/assign-resources/allocate-devices-dra.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/allocate-devices-dra/
heading: Claim resources {#claim-resources}
parent: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#identify-devices-to-claim-identify-devices
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/allocate-devices-dra.md#request-devices-in-workloads-using-dra-request-devices-workloads
word_count: 288
---

You can request resources from a DeviceClass by using 
ResourceClaims. To
create a ResourceClaim, do one of the following:

* Manually create a ResourceClaim if you want multiple Pods to share access to
  the same devices, or if you want a claim to exist beyond the lifetime of a
  Pod.
* Use a
  ResourceClaimTemplate
  to let Kubernetes generate and manage per-Pod ResourceClaims. Create a
  ResourceClaimTemplate if you want every Pod to have access to separate devices
  that have similar configurations. For example, you might want simultaneous
  access to devices for Pods in a Job that uses
  parallel execution.

If you directly reference a specific ResourceClaim in a Pod, that ResourceClaim
must already exist in the cluster. If a referenced ResourceClaim doesn't exist,
the Pod remains in a pending state until the ResourceClaim is created. You can
reference an auto-generated ResourceClaim in a Pod, but this isn't recommended
because auto-generated ResourceClaims are bound to the lifetime of the Pod that
triggered the generation.

To create a workload that claims resources, select one of the following options:

Review the following example manifest: 

This manifest creates a ResourceClaimTemplate that requests devices in the
`example-device-class` DeviceClass that match both of the following parameters:

  * Devices that have a `driver.example.com/type` attribute with a value of
    `gpu`.
  * Devices that have `64Gi` of capacity.

To create the ResourceClaimTemplate, run the following command:

```shell
kubectl apply -f https://k8s.io/examples/dra/resourceclaimtemplate.yaml
```

Review the following example manifest:

This manifest creates ResourceClaim that requests devices in the
`example-device-class` DeviceClass that match both of the following parameters:

  * Devices that have a `driver.example.com/type` attribute with a value of
    `gpu`.
  * Devices that have `64Gi` of capacity.

To create the ResourceClaim, run the following command:

```shell
kubectl apply -f https://k8s.io/examples/dra/resourceclaim.yaml
```
