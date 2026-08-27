---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-integration-with-the-topology-manager
kind: section
title: Device plugin integration with the Topology Manager
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: Device plugin integration with the Topology Manager
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#monitoring-device-plugin-resources
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-examples-examples
word_count: 186
---

The Topology Manager is a Kubelet component that allows resources to be co-ordinated in a Topology
aligned manner. In order to do this, the Device Plugin API was extended to include a
`TopologyInfo` struct.

```gRPC
message TopologyInfo {
    repeated NUMANode nodes = 1;
}

message NUMANode {
    int64 ID = 1;
}
```

Device Plugins that wish to leverage the Topology Manager can send back a populated TopologyInfo
struct as part of the device registration, along with the device IDs and the health of the device.
The device manager will then use this information to consult with the Topology Manager and make
resource assignment decisions.

`TopologyInfo` supports setting a `nodes` field to either `nil` or a list of NUMA nodes. This
allows the Device Plugin to advertise a device that spans multiple NUMA nodes.

Setting `TopologyInfo` to `nil` or providing an empty list of NUMA nodes for a given device
indicates that the Device Plugin does not have a NUMA affinity preference for that device.

An example `TopologyInfo` struct populated for a device by a Device Plugin:

```
pluginapi.Device{ID: "25102017", Health: pluginapi.Healthy, Topology:&pluginapi.TopologyInfo{Nodes: []*pluginapi.NUMANode{&pluginapi.NUMANode{ID: 0,},}}}
```
