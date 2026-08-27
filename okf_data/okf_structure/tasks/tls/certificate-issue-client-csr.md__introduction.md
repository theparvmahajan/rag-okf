---
id: okf-structure/tasks/tls/certificate-issue-client-csr.md#introduction
kind: section
title: Issue a Certificate for a Kubernetes API Client Using a CertificateSigningRequest
source: tasks/tls/certificate-issue-client-csr.md
url: https://kubernetes.io/docs/tasks/tls/certificate-issue-client-csr/
heading: null
parent: okf-structure/tasks/tls/certificate-issue-client-csr
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/tls/certificate-issue-client-csr.md#prerequisites
word_count: 106
---

Kubernetes lets you use a public key infrastructure (PKI) to authenticate to your cluster
as a client.

A few steps are required in order to get a normal user to be able to
authenticate and invoke an API. First, this user must have an X.509 certificate
issued by an authority that your Kubernetes cluster trusts. The client must then present that certificate to the Kubernetes API.

You use a CertificateSigningRequest
as part of this process, either you or some other principal must approve the request.

You will create a private key, and then get a certificate issued, and finally configure
that private key for a client.
