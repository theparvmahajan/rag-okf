---
id: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#webhook-token-authentication-webhook-token-authentication
kind: section
title: Webhook token authentication {#webhook-token-authentication}
source: concepts/security/hardening-guide/authentication-mechanisms.md
url: https://kubernetes.io/docs/concepts/security/hardening-guide/authentication-mechanisms/
heading: Webhook token authentication {#webhook-token-authentication}
parent: okf-structure/concepts/security/hardening-guide/authentication-mechanisms
children: []
prev_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#openid-connect-token-authentication-openid-connect-token-authentication
next_sibling: okf-structure/concepts/security/hardening-guide/authentication-mechanisms.md#authenticating-proxy-authenticating-proxy
word_count: 123
---

Webhook token authentication
is another option for integrating external authentication providers into Kubernetes. This mechanism
allows for an authentication service, either running inside the cluster or externally, to be
contacted for an authentication decision over a webhook. It is important to note that the suitability
of this mechanism will likely depend on the software used for the authentication service, and there
are some Kubernetes-specific considerations to take into account.

To configure Webhook authentication, access to control plane server filesystems is required. This
means that it will not be possible with Managed Kubernetes unless the provider specifically makes it
available. Additionally, any software installed in the cluster to support this access should be
isolated from general workloads, as it will run with high privileges.
