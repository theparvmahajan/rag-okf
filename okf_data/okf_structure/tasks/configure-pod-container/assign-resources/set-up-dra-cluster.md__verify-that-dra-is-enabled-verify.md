---
id: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#verify-that-dra-is-enabled-verify
kind: section
title: Verify that DRA is enabled {#verify}
source: tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/assign-resources/set-up-dra-cluster/
heading: Verify that DRA is enabled {#verify}
parent: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#optional-enable-additional-dra-api-groups-enable-dra
next_sibling: okf-structure/tasks/configure-pod-container/assign-resources/set-up-dra-cluster.md#install-device-drivers-install-drivers
word_count: 135
---

To verify that the cluster is configured correctly, try to list DeviceClasses:

```shell
kubectl get deviceclasses
```
If the component configuration was correct, the output is similar to the
following:

```
No resources found
```

If DRA isn't correctly configured, the output of the preceding command is
similar to the following:
   
```
error: the server doesn't have a resource type "deviceclasses"
```

For example, this can occur when the resource.k8s.io API group was disabled.
A similar check is applicable to alpha or beta quality top-level types.

Try the following troubleshooting steps:

1. Reconfigure and restart the `kube-apiserver` component.

1. If the complete `.spec.resourceClaims` field gets removed from Pods, or if
   Pods get scheduled without considering the ResourceClaims, then verify
   that the `DynamicResourceAllocation` feature gate is not turned off
   for kube-apiserver, kube-controller-manager, kube-scheduler or the kubelet.
