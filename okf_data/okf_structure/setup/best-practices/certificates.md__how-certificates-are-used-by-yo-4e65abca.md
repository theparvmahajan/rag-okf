---
id: okf-structure/setup/best-practices/certificates.md#how-certificates-are-used-by-your-cluster
kind: section
title: How certificates are used by your cluster
source: setup/best-practices/certificates.md
url: https://kubernetes.io/docs/setup/best-practices/certificates/
heading: How certificates are used by your cluster
parent: okf-structure/setup/best-practices/certificates
children: []
prev_sibling: okf-structure/setup/best-practices/certificates.md#introduction
next_sibling: okf-structure/setup/best-practices/certificates.md#where-certificates-are-stored
word_count: 285
---

Kubernetes requires PKI for the following operations:

### Server certificates

* Server certificate for the API server endpoint
* Server certificate for the etcd server
* Server certificates
  for each kubelet (every node runs a kubelet)
* Optional server certificate for the front-proxy

### Client certificates

* Client certificates for each kubelet, used to authenticate to the API server as a client of
  the Kubernetes API
* Client certificate for each API server, used to authenticate to etcd
* Client certificate for the controller manager to securely communicate with the API server
* Client certificate for the scheduler to securely communicate with the API server
* Client certificates, one for each node, for kube-proxy to authenticate to the API server
* Optional client certificates for administrators of the cluster to authenticate to the API server
* Optional client certificate for the front-proxy

### Kubelet's server and client certificates

To establish a secure connection and authenticate itself to the kubelet, the API Server
requires a client certificate and key pair.

In this scenario, there are two approaches for certificate usage:

* Shared Certificates: The kube-apiserver can utilize the same certificate and key pair it uses
  to authenticate its clients. This means that the existing certificates, such as `apiserver.crt`
  and `apiserver.key`, can be used for communicating with the kubelet servers.

* Separate Certificates: Alternatively, the kube-apiserver can generate a new client certificate
  and key pair to authenticate its communication with the kubelet servers. In this case,
  a distinct certificate named `kubelet-client.crt` and its corresponding private key,
  `kubelet-client.key` are created.

`front-proxy` certificates are required only when using the API server aggregation layer
to support an extension API server.

etcd also implements mutual TLS to authenticate clients and peers.
