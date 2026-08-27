---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#bootstrap-tokens-bootstrap-tokens
kind: section
title: Bootstrap tokens {#bootstrap-tokens}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: Bootstrap tokens {#bootstrap-tokens}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#static-token-file-static-token-file
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#serviceaccount-secret-tokens-serviceaccount-secret-tokens
word_count: 84
---

Bootstrap tokens are used for joining
nodes to clusters and are not recommended for user authentication due to several reasons:

- They have hard-coded group memberships that are not suitable for general use, making them
  unsuitable for authentication purposes.
- Manually generating bootstrap tokens can lead to weak tokens that can be guessed by an attacker,
  which can be a security risk.
- There is no lockout mechanism available to prevent brute-force attacks, making it easier for
  attackers to guess or crack the token.
