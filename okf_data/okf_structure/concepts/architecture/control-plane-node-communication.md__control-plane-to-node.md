---
id: okf-structure/concepts/architecture/control-plane-node-communication.md#control-plane-to-node
kind: section
title: Control plane to node
source: concepts/architecture/control-plane-node-communication.md
url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
heading: Control plane to node
parent: okf-structure/concepts/architecture/control-plane-node-communication
children: []
prev_sibling: okf-structure/concepts/architecture/control-plane-node-communication.md#node-to-control-plane
next_sibling: okf-structure/concepts/architecture/control-plane-node-communication.md#whatsnext
word_count: 484
---

There are two primary communication paths from the control plane (the API server) to the nodes.
The first is from the API server to the kubelet process which runs on each node in the cluster.
The second is from the API server to any node, pod, or service through the API server's _proxy_
functionality.

### API server to kubelet

The connections from the API server to the kubelet are used for:

* Fetching logs for pods.
* Attaching (usually through `kubectl`) to running pods.
* Providing the kubelet's port-forwarding functionality.

These connections terminate at the kubelet's HTTPS endpoint. By default, the API server does not
verify the kubelet's serving certificate, which makes the connection subject to man-in-the-middle
attacks and **unsafe** to run over untrusted and/or public networks.

To verify this connection, use the `--kubelet-certificate-authority` flag to provide the API
server with a root certificate bundle to use to verify the kubelet's serving certificate.

If that is not possible, use SSH tunneling between the API server and kubelet if
required to avoid connecting over an
untrusted or public network.

Finally, Kubelet authentication and/or authorization
should be enabled to secure the kubelet API.

### API server to nodes, pods, and services

The connections from the API server to a node, pod, or service default to plain HTTP connections
and are therefore neither authenticated nor encrypted. They can be run over a secure HTTPS
connection by prefixing `https:` to the node, pod, or service name in the API URL, but they will
not validate the certificate provided by the HTTPS endpoint nor provide client credentials. So
while the connection will be encrypted, it will not provide any guarantees of integrity. These
connections **are not currently safe** to run over untrusted or public networks.

### SSH tunnels

Kubernetes supports SSH tunnels to protect the control plane to nodes communication paths. In this
configuration, the API server initiates an SSH tunnel to each node in the cluster (connecting to
the SSH server listening on port 22) and passes all traffic destined for a kubelet, node, pod, or
service through the tunnel.
This tunnel ensures that the traffic is not exposed outside of the network in which the nodes are
running.

SSH tunnels are currently deprecated, so you shouldn't opt to use them unless you know what you
are doing. The Konnectivity service is a replacement for this
communication channel.

### Konnectivity service

As a replacement to the SSH tunnels, the Konnectivity service provides TCP level proxy for the
control plane to cluster communication. The Konnectivity service consists of two parts: the
Konnectivity server in the control plane network and the Konnectivity agents in the nodes network.
The Konnectivity agents initiate connections to the Konnectivity server and maintain the network
connections.
After enabling the Konnectivity service, all control plane to nodes traffic goes through these
connections.

Follow the Konnectivity service task to set
up the Konnectivity service in your cluster.
