---
id: okf-structure/concepts/security/service-accounts.md#authenticating-service-account-credentials-authenticating-credentials
kind: section
title: Authenticating service account credentials {#authenticating-credentials}
source: concepts/security/service-accounts.md
url: https://kubernetes.io/docs/concepts/security/service-accounts/
heading: Authenticating service account credentials {#authenticating-credentials}
parent: okf-structure/concepts/security/service-accounts
children: []
prev_sibling: okf-structure/concepts/security/service-accounts.md#how-to-use-service-accounts-how-to-use
next_sibling: okf-structure/concepts/security/service-accounts.md#alternatives
word_count: 414
---

ServiceAccounts use signed
JSON Web Tokens  (JWTs)
to authenticate to the Kubernetes API server, and to any other system where a
trust relationship exists. Depending on how the token was issued
(either time-limited using a `TokenRequest` or using a legacy mechanism with
a Secret), a ServiceAccount token might also have an expiry time, an audience,
and a time after which the token *starts* being valid. When a client that is
acting as a ServiceAccount tries to communicate with the Kubernetes API server,
the client includes an `Authorization: Bearer <token>` header with the HTTP
request. The API server checks the validity of that bearer token as follows:

1. Checks the token signature.
1. Checks whether the token has expired.
1. Checks whether object references in the token claims are currently valid.
1. Checks whether the token is currently valid.
1. Checks the audience claims.

The TokenRequest API produces _bound tokens_ for a ServiceAccount. This
binding is linked to the lifetime of the client, such as a Pod, that is acting
as that ServiceAccount.  See Token Volume Projection
for an example of a bound pod service account token's JWT schema and payload.

For tokens issued using the `TokenRequest` API, the API server also checks that
the specific object reference that is using the ServiceAccount still exists,
matching by the unique ID of that
object. For legacy tokens that are mounted as Secrets in Pods, the API server
checks the token against the Secret.

For more information about the authentication process, refer to
Authentication.

### Authenticating service account credentials in your own code {#authenticating-in-code}

If you have services of your own that need to validate Kubernetes service
account credentials, you can use the following methods:

* TokenReview API
  (recommended)
* OIDC discovery

The Kubernetes project recommends that you use the TokenReview API, because
this method invalidates tokens that are bound to API objects such as Secrets,
ServiceAccounts, Pods or Nodes when those objects are deleted. For example, if you
delete the Pod that contains a projected ServiceAccount token, the cluster
invalidates that token immediately and a TokenReview immediately fails.
If you use OIDC validation instead, your clients continue to treat the token
as valid until the token reaches its expiration timestamp.

Your application should always define the audience that it accepts, and should
check that the token's audiences match the audiences that the application
expects. This helps to minimize the scope of the token so that it can only be
used in your application and nowhere else.
