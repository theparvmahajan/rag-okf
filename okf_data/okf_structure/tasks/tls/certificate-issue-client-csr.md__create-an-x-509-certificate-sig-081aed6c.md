---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-an-x-509-certificate-signing-request-create-x-509-certificatessigningrequest
kind: section
title: Create an X.509 certificate signing request {#create-x.509-certificatessigningrequest}
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: Create an X.509 certificate signing request {#create-x.509-certificatessigningrequest}
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-private-key
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-a-kubernetes-certificatesigningrequest-create-k8s-certificatessigningrequest
word_count: 84
---

This is not the same as the similarly-named CertificateSigningRequest API; the file you generate here goes into the
CertificateSigningRequest.

It is important to set the CN and O attributes of the CSR. CN is the name of the user, and O is the group that this user will belong to.
You can refer to RBAC for standard groups.

```shell
# Change the common name "myuser" to the actual username that you want to use
openssl req -new -key myuser.key -out myuser.csr -subj "/CN=myuser"
```
