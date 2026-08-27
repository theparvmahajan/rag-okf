---
id: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-registration
kind: section
title: Device plugin registration
source: concepts/extend-kubernetes/compute-storage-net/device-plugins.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
heading: Device plugin registration
parent: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#introduction
next_sibling: okf-structure/concepts/extend-kubernetes/compute-storage-net/device-plugins.md#device-plugin-implementation
word_count: 317
---

The kubelet exports a `Registration` gRPC service:

```gRPC
service Registration {
	rpc Register(RegisterRequest) returns (Empty) {}
}
```

A device plugin can register itself with the kubelet through this gRPC service.
During the registration, the device plugin needs to send:

* The name of its Unix socket.
* The Device Plugin API version against which it was built.
* The `ResourceName` it wants to advertise. Here `ResourceName` needs to follow the
  extended resource naming scheme
  as `vendor-domain/resourcetype`.
  (For example, an NVIDIA GPU is advertised as `nvidia.com/gpu`.)

Following a successful registration, the device plugin sends the kubelet the
list of devices it manages, and the kubelet is then in charge of advertising those
resources to the API server as part of the kubelet node status update.
For example, after a device plugin registers `hardware-vendor.example/foo` with the kubelet
and reports two healthy devices on a node, the node status is updated
to advertise that the node has 2 "Foo" devices installed and available.

Then, users can request devices as part of a Pod specification
(see `container`).
Requesting extended resources is similar to how you manage requests and limits for
other resources, with the following differences:
* Extended resources are only supported as integer resources and cannot be overcommitted.
* Devices cannot be shared between containers.

### Example {#example-pod}

Suppose a Kubernetes cluster is running a device plugin that advertises resource `hardware-vendor.example/foo`
on certain nodes. Here is an example of a pod requesting this resource to run a demo workload:

```yaml
---
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
spec:
  containers:
    - name: demo-container-1
      image: registry.k8s.io/pause:3.8
      resources:
        limits:
          hardware-vendor.example/foo: 2
#
# This Pod needs 2 of the hardware-vendor.example/foo devices
# and can only schedule onto a Node that's able to satisfy
# that need.
#
# If the Node has more than 2 of those devices available, the
# remainder would be available for other Pods to use.
```
