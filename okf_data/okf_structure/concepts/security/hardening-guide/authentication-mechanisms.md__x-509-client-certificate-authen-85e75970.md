---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#x-509-client-certificate-authentication-x509-client-certificate-authentication
kind: section
title: X.509 client certificate authentication {#x509-client-certificate-authentication}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: X.509 client certificate authentication {#x509-client-certificate-authentication}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#introduction
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#static-token-file-static-token-file
word_count: 213
---

Kubernetes leverages X.509 client certificate
authentication for system components, such as when the kubelet authenticates to the API Server.
While this mechanism can also be used for user authentication, it might not be suitable for
production use due to several restrictions:

- Client certificates cannot be individually revoked. Once compromised, a certificate can be used
  by an attacker until it expires. To mitigate this risk, it is recommended to configure short
  lifetimes for user authentication credentials created using client certificates.
- If a certificate needs to be invalidated, the certificate authority must be re-keyed, which
  can introduce availability risks to the cluster.
- There is no permanent record of client certificates created in the cluster. Therefore, all
  issued certificates must be recorded if you need to keep track of them.
- Private keys used for client certificate authentication cannot be password-protected. Anyone
  who can read the file containing the key will be able to make use of it.
- Using client certificate authentication requires a direct connection from the client to the
  API server without any intervening TLS termination points, which can complicate network architectures.
- Group data is embedded in the `O` value of the client certificate, which means the user's group
  memberships cannot be changed for the lifetime of the certificate.
