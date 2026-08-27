---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#get-the-certificate
kind: section
title: Get the certificate
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: Get the certificate
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#approve-the-certificatesigningrequest-approve-certificate-signing-request
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#configure-the-certificate-into-kubeconfig
word_count: 47
---

Retrieve the certificate from the CSR to check that it looks OK.

```shell
kubectl get csr/myuser -o yaml
```

The certificate value is in Base64-encoded format under `.status.certificate`.

Export the issued certificate from the CertificateSigningRequest.

```shell
kubectl get csr myuser -o jsonpath='{.status.certificate}'| base64 -d > myuser.crt
```
