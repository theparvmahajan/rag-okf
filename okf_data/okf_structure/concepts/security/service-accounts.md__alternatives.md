---
id: okf-structure/concepts/security/service-accounts.md#alternatives
kind: section
title: Alternatives
source: concepts/security/service-accounts.md
url: https://kubernetes.io/docs/concepts/security/service-accounts/
heading: Alternatives
parent: okf-structure/concepts/security/service-accounts
children: []
prev_sibling: okf-structure/concepts/security/service-accounts.md#authenticating-service-account-credentials-authenticating-credentials
next_sibling: okf-structure/concepts/security/service-accounts.md#whatsnext
word_count: 158
---

* Issue your own tokens using another mechanism, and then use
  Webhook Token Authentication
  to validate bearer tokens using your own validation service.
* Provide your own identities to Pods.
  * Use the SPIFFE CSI driver plugin to provide SPIFFE SVIDs as X.509 certificate pairs to Pods.
    
  * Use a service mesh such as Istio to provide certificates to Pods.
* Authenticate from outside the cluster to the API server without using service account tokens:
  * Configure the API server to accept OpenID Connect (OIDC) tokens from your identity provider.
  * Use service accounts or user accounts created using an external Identity
    and Access Management (IAM) service, such as from a cloud provider, to
    authenticate to your cluster.
  * Use the CertificateSigningRequest API with client certificates.
* Configure the kubelet to retrieve credentials from an image registry.
* Use a Device Plugin to access a virtual Trusted Platform Module (TPM), which
  then allows authentication using a private key.
