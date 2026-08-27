---
id: okf-structure/tasks/debug/debug-cluster/topology.md#check-the-device-plugin-resource-api-device-plugin-resource-api
kind: section
title: Check the device plugin resource API {#device-plugin-resource-api}
source: tasks/debug/debug-cluster/topology.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/
heading: Check the device plugin resource API {#device-plugin-resource-api}
parent: okf-structure/tasks/debug/debug-cluster/topology
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#examples
next_sibling: null
word_count: 50
---

The kubelet provides a `PodResourceLister` gRPC service to enable discovery of resources and associated metadata.
By using its List gRPC endpoint,
information about reserved memory for each container can be retrieved, which is contained
in protobuf `ContainerMemory` message.

This information can be retrieved solely for pods in Guaranteed QoS class.
