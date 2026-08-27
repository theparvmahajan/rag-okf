---
id: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#get-the-certificatesigningrequest-approved-get-the-certificate-signing-request-approved
kind: section
title: Get the CertificateSigningRequest approved {#get-the-certificate-signing-request-approved}
source: tasks/tls/managing-tls-in-a-cluster.md
url: https://kubernetes.io/docs/tasks/tls/managing-tls-in-a-cluster/
heading: Get the CertificateSigningRequest approved {#get-the-certificate-signing-request-approved}
parent: okf-structure/tasks/tls/managing-tls-in-a-cluster
children: []
prev_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#create-a-certificatesigningrequest-object-to-send-to-the-kubernetes-api
next_sibling: okf-structure/tasks/tls/managing-tls-in-a-cluster.md#sign-the-certificatesigningrequest-sign-the-certificate-signing-request
word_count: 92
---

Approving the certificate signing request
is either done by an automated approval process or on a one-off basis by a cluster
administrator. If you're authorized to approve a certificate request, you can do that
manually using `kubectl`; for example:

```shell
kubectl certificate approve my-svc.my-namespace
```

```none
certificatesigningrequest.certificates.k8s.io/my-svc.my-namespace approved
```

You should now see the following:

```shell
kubectl get csr
```

```none
NAME                  AGE   SIGNERNAME            REQUESTOR              REQUESTEDDURATION   CONDITION
my-svc.my-namespace   10m   example.com/serving   yourname@example.com   <none>              Approved
```

This means the certificate request has been approved and is waiting for the
requested signer to sign it.
