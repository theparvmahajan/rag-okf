---
id: okf-structure/concepts/security/api-server-bypass-risks.md#the-etcd-api
kind: section
title: The etcd API
source: concepts/security/api-server-bypass-risks.md
url: https://kubernetes.io/docs/concepts/security/api-server-bypass-risks/
heading: The etcd API
parent: okf-structure/concepts/security/api-server-bypass-risks
children: []
prev_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#the-kubelet-api-kubelet-api
next_sibling: okf-structure/concepts/security/api-server-bypass-risks.md#container-runtime-socket-runtime-socket
word_count: 304
---

Kubernetes clusters use etcd as a datastore. The `etcd` service listens on TCP port 2379.
The only clients that need access are the Kubernetes API server and any backup tooling
that you use. Direct access to this API allows for disclosure or modification of any
data held in the cluster.

Access to the etcd API is typically managed by client certificate authentication.
Any certificate issued by a certificate authority that etcd trusts allows full access
to the data stored inside etcd.

Direct access to etcd is not subject to Kubernetes admission control and is not logged
by Kubernetes audit logging. An attacker who has read access to the API server's
etcd client certificate private key (or can create a new trusted client certificate) can gain
cluster admin rights by accessing cluster secrets or modifying access rules. Even without
elevating their Kubernetes RBAC privileges, an attacker who can modify etcd can retrieve any API object
or create new workloads inside the cluster.

Many Kubernetes providers configure
etcd to use mutual TLS (both client and server verify each other's certificate for authentication).
There is no widely accepted implementation of authorization for the etcd API, although
the feature exists. Since there is no authorization model, any certificate
with client access to etcd can be used to gain full access to etcd. Typically, etcd client certificates
that are only used for health checking can also grant full read and write access.

### Mitigations {#etcd-api-mitigations}

- Ensure that the certificate authority trusted by etcd is used only for the purposes of
  authentication to that service.
- Control access to the private key for the etcd server certificate, and to the API server's
  client certificate and key.
- Consider restricting access to the etcd port at a network level, to only allow access
  from specified and trusted IP address ranges.
