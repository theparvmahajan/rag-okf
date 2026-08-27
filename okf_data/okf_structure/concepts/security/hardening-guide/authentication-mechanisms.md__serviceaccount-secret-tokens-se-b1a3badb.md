---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#serviceaccount-secret-tokens-serviceaccount-secret-tokens
kind: section
title: ServiceAccount secret tokens {#serviceaccount-secret-tokens}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: ServiceAccount secret tokens {#serviceaccount-secret-tokens}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#bootstrap-tokens-bootstrap-tokens
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#tokenrequest-api-tokens-tokenrequest-api-tokens
word_count: 114
---

Service account secrets
are available as an option to allow workloads running in the cluster to authenticate to the
API server. In Kubernetes < 1.23, these were the default option, however, they are being replaced
with TokenRequest API tokens. While these secrets could be used for user authentication, they are
generally unsuitable for a number of reasons:

- They cannot be set with an expiry and will remain valid until the associated service account is deleted.
- The authentication tokens are visible to any cluster user who can read secrets in the namespace
  that they are defined in.
- Service accounts cannot be added to arbitrary groups complicating RBAC management where they are used.
