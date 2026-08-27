---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#tokenrequest-api-tokens-tokenrequest-api-tokens
kind: section
title: TokenRequest API tokens {#tokenrequest-api-tokens}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: TokenRequest API tokens {#tokenrequest-api-tokens}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#serviceaccount-secret-tokens-serviceaccount-secret-tokens
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#openid-connect-token-authentication-openid-connect-token-authentication
word_count: 71
---

The TokenRequest API is a useful tool for generating short-lived credentials for service
authentication to the API server or third-party systems. However, it is not generally recommended
for user authentication as there is no revocation method available, and distributing credentials
to users in a secure manner can be challenging.

When using TokenRequest tokens for service authentication, it is recommended to implement a short
lifespan to reduce the impact of compromised tokens.
