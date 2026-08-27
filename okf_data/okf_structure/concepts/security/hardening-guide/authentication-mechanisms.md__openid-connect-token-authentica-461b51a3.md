---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#openid-connect-token-authentication-openid-connect-token-authentication
kind: section
title: OpenID Connect token authentication {#openid-connect-token-authentication}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: OpenID Connect token authentication {#openid-connect-token-authentication}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#tokenrequest-api-tokens-tokenrequest-api-tokens
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#webhook-token-authentication-webhook-token-authentication
word_count: 106
---

Kubernetes supports integrating external authentication services with the Kubernetes API using
OpenID Connect (OIDC).
There is a wide variety of software that can be used to integrate Kubernetes with an identity
provider. However, when using OIDC authentication in Kubernetes, it is important to consider the
following hardening measures:

- The software installed in the cluster to support OIDC authentication should be isolated from
  general workloads as it will run with high privileges.
- Some Kubernetes managed services are limited in the OIDC providers that can be used.
- As with TokenRequest tokens, OIDC tokens should have a short lifespan to reduce the impact of
  compromised tokens.
