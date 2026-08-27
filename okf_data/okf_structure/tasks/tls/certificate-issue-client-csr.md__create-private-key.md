---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-private-key
kind: section
title: Create private key
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: Create private key
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#prerequisites
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#create-an-x-509-certificate-signing-request-create-x-509-certificatessigningrequest
word_count: 36
---

In this step, you create a private key. You need to keep this private key secret; anyone who has it can impersonate the user.

```shell
# Create a private key
openssl genrsa -out myuser.key 3072
```
