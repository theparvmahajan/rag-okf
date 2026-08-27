---
id: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#securing-etcd-clusters
kind: section
title: Securing etcd clusters
source: tasks/administer-cluster/configure-upgrade-etcd.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/
heading: Securing etcd clusters
parent: okf-structure/tasks/administer-cluster/configure-upgrade-etcd
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#starting-etcd-clusters
next_sibling: okf-structure/tasks/administer-cluster/configure-upgrade-etcd.md#replacing-a-failed-etcd-member
word_count: 316
---

Access to etcd is equivalent to root permission in the cluster so ideally only
the API server should have access to it. Considering the sensitivity of the
data, it is recommended to grant permission to only those nodes that require
access to etcd clusters.

To secure etcd, either set up firewall rules or use the security features
provided by etcd. etcd security features depend on x509 Public Key
Infrastructure (PKI). To begin, establish secure communication channels by
generating a key and certificate pair. For example, use key pairs `peer.key`
and `peer.cert` for securing communication between etcd members, and
`client.key` and `client.cert` for securing communication between etcd and its
clients. See the example scripts
provided by the etcd project to generate key pairs and CA files for client
authentication.

### Securing communication

To configure etcd with secure peer communication, specify flags
`--peer-key-file=peer.key` and `--peer-cert-file=peer.cert`, and use HTTPS as
the URL schema.

Similarly, to configure etcd with secure client communication, specify flags
`--key=k8sclient.key` and `--cert=k8sclient.cert`, and use HTTPS as
the URL schema. Here is an example on a client command that uses secure
communication:

```
ETCDCTL_API=3 etcdctl --endpoints 10.2.0.9:2379 \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  member list
```

### Limiting access of etcd clusters

After configuring secure communication, restrict the access of the etcd cluster to
only the Kubernetes API servers using TLS authentication.

For example, consider key pairs `k8sclient.key` and `k8sclient.cert` that are
trusted by the CA `etcd.ca`. When etcd is configured with `--client-cert-auth`
along with TLS, it verifies the certificates from clients by using system CAs
or the CA passed in by `--trusted-ca-file` flag. Specifying flags
`--client-cert-auth=true` and `--trusted-ca-file=etcd.ca` will restrict the
access to clients with the certificate `k8sclient.cert`.

Once etcd is configured correctly, only clients with valid certificates can
access it. To give Kubernetes API servers the access, configure them with the
flags `--etcd-certfile=k8sclient.cert`, `--etcd-keyfile=k8sclient.key` and
`--etcd-cafile=ca.cert`.

etcd authentication is not planned for Kubernetes.
