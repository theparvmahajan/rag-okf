---
id: okf-structure/tasks/administer-cluster/certificates.md#distributing-self-signed-ca-certificate
kind: section
title: Distributing Self-Signed CA Certificate
source: tasks/administer-cluster/certificates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/certificates/
heading: Distributing Self-Signed CA Certificate
parent: okf-structure/tasks/administer-cluster/certificates
children: []
prev_sibling: okf-structure/tasks/administer-cluster/certificates.md#introduction
next_sibling: okf-structure/tasks/administer-cluster/certificates.md#certificates-api
word_count: 76
---

A client node may refuse to recognize a self-signed CA certificate as valid.
For a non-production deployment, or for a deployment that runs behind a company
firewall, you can distribute a self-signed CA certificate to all clients and
refresh the local list for valid certificates.

On each client, perform the following operations:

```shell
sudo cp ca.crt /usr/local/share/ca-certificates/kubernetes.crt
sudo update-ca-certificates
```

```none
Updating certificates in /etc/ssl/certs...
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d....
done.
```
