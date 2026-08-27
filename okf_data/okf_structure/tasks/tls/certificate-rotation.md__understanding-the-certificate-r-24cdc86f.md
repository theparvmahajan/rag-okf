---
id: okf-structure/tasks/tls/certificate-rotation.md#understanding-the-certificate-rotation-configuration
kind: section
title: Understanding the certificate rotation configuration
source: tasks/tls/certificate-rotation.md
url: https://kubernetes.io/docs/tasks/tls/certificate-rotation/
heading: Understanding the certificate rotation configuration
parent: okf-structure/tasks/tls/certificate-rotation
children: []
prev_sibling: okf-structure/tasks/tls/certificate-rotation.md#enabling-client-certificate-rotation
next_sibling: null
word_count: 249
---

When a kubelet starts up, if it is configured to bootstrap (using the
`--bootstrap-kubeconfig` flag), it will use its initial certificate to connect
to the Kubernetes API and issue a certificate signing request. You can view the
status of certificate signing requests using:

```sh
kubectl get csr
```

Initially, a certificate signing request from the kubelet on a node will have a
status of `Pending`. If the certificate signing request meets specific
criteria, it will be auto-approved by the controller manager, and then it will have
a status of `Approved`. Next, the controller manager will sign a certificate,
issued for the duration specified by the 
`--cluster-signing-duration` parameter, and the signed certificate
will be attached to the certificate signing request.

The kubelet will retrieve the signed certificate from the Kubernetes API and
write that to disk, in the location specified by `--cert-dir`. Then the kubelet
will use the new certificate to connect to the Kubernetes API.

As the expiration of the signed certificate approaches, the kubelet will
automatically issue a new certificate signing request, using the Kubernetes API. 
This can happen at any point between 30% and 10% of the time remaining on the 
certificate. Again, the controller manager will automatically approve the certificate
request and attach a signed certificate to the certificate signing request. The
kubelet will retrieve the new signed certificate from the Kubernetes API and
write that to disk. Then it will update the connections it has to the
Kubernetes API to reconnect using the new certificate.
