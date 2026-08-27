---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#authenticating-proxy-authenticating-proxy
kind: section
title: Authenticating proxy {#authenticating-proxy}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: Authenticating proxy {#authenticating-proxy}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#webhook-token-authentication-webhook-token-authentication
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#whatsnext
word_count: 146
---

Another option for integrating external authentication systems into Kubernetes is to use an
authenticating proxy.
With this mechanism, Kubernetes expects to receive requests from the proxy with specific header
values set, indicating the username and group memberships to assign for authorization purposes.
It is important to note that there are specific considerations to take into account when using
this mechanism.

Firstly, securely configured TLS must be used between the proxy and Kubernetes API server to
mitigate the risk of traffic interception or sniffing attacks. This ensures that the communication
between the proxy and Kubernetes API server is secure.

Secondly, it is important to be aware that an attacker who is able to modify the headers of the
request may be able to gain unauthorized access to Kubernetes resources. As such, it is important
to ensure that the headers are properly secured and cannot be tampered with.
