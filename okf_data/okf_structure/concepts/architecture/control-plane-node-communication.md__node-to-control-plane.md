---
id: okf-structure/concepts/architecture/control-plane-node-communication.md#node-to-control-plane
kind: section
title: Node to Control Plane
source: concepts/architecture/control-plane-node-communication.md
url: https://kubernetes.io/docs/concepts/architecture/control-plane-node-communication/
heading: Node to Control Plane
parent: okf-structure/concepts/architecture/control-plane-node-communication
children: []
prev_sibling: okf-structure/concepts/architecture/control-plane-node-communication.md#introduction
next_sibling: okf-structure/concepts/architecture/control-plane-node-communication.md#control-plane-to-node
word_count: 251
---

Kubernetes has a "hub-and-spoke" API pattern. All API usage from nodes (or the pods they run)
terminates at the API server. None of the other control plane components are designed to expose
remote services. The API server is configured to listen for remote connections on a secure HTTPS
port (typically 443) with one or more forms of client
authentication enabled.
One or more forms of authorization should be
enabled, especially if anonymous requests
or service account tokens
are allowed.

Nodes should be provisioned with the public root certificate for the cluster such that they can
connect securely to the API server along with valid client credentials. A good approach is that the
client credentials provided to the kubelet are in the form of a client certificate. See
kubelet TLS bootstrapping
for automated provisioning of kubelet client certificates.

Pods that wish to connect to the API server can do so securely by leveraging a service account so
that Kubernetes will automatically inject the public root certificate and a valid bearer token
into the pod when it is instantiated.
The `kubernetes` service (in `default` namespace) is configured with a virtual IP address that is
redirected (via `kube-proxy`) to the HTTPS endpoint on the API server.

The control plane components also communicate with the API server over the secure port.

As a result, the default operating mode for connections from the nodes and pod running on the
nodes to the control plane is secured by default and can run over untrusted and/or public
networks.
