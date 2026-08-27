---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#approve-the-certificatesigningrequest-approve-certificate-signing-request
kind: section
title: Approve the CertificateSigningRequest {#approve-certificate-signing-request}
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: Approve the CertificateSigningRequest {#approve-certificate-signing-request}
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-a-kubernetes-certificatesigningrequest-create-k8s-certificatessigningrequest
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#get-the-certificate
word_count: 31
---

Use kubectl to find the CSR you made, and manually approve it.

Get the list of CSRs:

```shell
kubectl get csr
```

Approve the CSR:

```shell
kubectl certificate approve myuser
```
