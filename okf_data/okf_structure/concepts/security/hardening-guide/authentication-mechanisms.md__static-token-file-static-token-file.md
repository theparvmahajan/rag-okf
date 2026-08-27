---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#static-token-file-static-token-file
kind: section
title: Static token file {#static-token-file}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: Static token file {#static-token-file}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#x-509-client-certificate-authentication-x509-client-certificate-authentication
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#bootstrap-tokens-bootstrap-tokens
word_count: 111
---

Although Kubernetes allows you to load credentials from a
static token file located
on the control plane node disks, this approach is not recommended for production servers due to
several reasons:

- Credentials are stored in clear text on control plane node disks, which can be a security risk.
- Changing any credential requires a restart of the API server process to take effect, which can
  impact availability.
- There is no mechanism available to allow users to rotate their credentials. To rotate a
  credential, a cluster administrator must modify the token on disk and distribute it to the users.
- There is no lockout mechanism available to prevent brute-force attacks.
