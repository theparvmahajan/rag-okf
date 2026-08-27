---
id: okf-structure/tasks/configure-pod-container/configure-service-account.md#serviceaccount-token-volume-projection
kind: section
title: ServiceAccount token volume projection
source: tasks/configure-pod-container/configure-service-account.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/
heading: ServiceAccount token volume projection
parent: okf-structure/tasks/configure-pod-container/configure-service-account
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#add-imagepullsecrets-to-a-service-account
next_sibling: okf-structure/tasks/configure-pod-container/configure-service-account.md#whatsnext
word_count: 962
---

To enable and use token request projection, you must specify each of the following
command line arguments to `kube-apiserver`:

`--service-account-issuer`
: defines the Identifier of the service account token issuer. You can specify the
  `--service-account-issuer` argument multiple times, this can be useful to enable
  a non-disruptive change of the issuer. When this flag is specified multiple times,
  the first is used to generate tokens and all are used to determine which issuers
  are accepted. You must be running Kubernetes v1.22 or later to be able to specify
  `--service-account-issuer` multiple times.

`--service-account-key-file`
: specifies the path to a file containing PEM-encoded X.509 private or public keys
  (RSA or ECDSA), used to verify ServiceAccount tokens. The specified file can contain
  multiple keys, and the flag can be specified multiple times with different files.
  If specified multiple times, tokens signed by any of the specified keys are considered
  valid by the Kubernetes API server.

`--service-account-signing-key-file`
: specifies the path to a file that contains the current private key of the service
  account token issuer. The issuer signs issued ID tokens with this private key.

`--api-audiences` (can be omitted)
: defines audiences for ServiceAccount tokens. The service account token authenticator
  validates that tokens used against the API are bound to at least one of these audiences.
  If `api-audiences` is specified multiple times, tokens for any of the specified audiences
  are considered valid by the Kubernetes API server. If you specify the `--service-account-issuer`
  command line argument but you don't set `--api-audiences`, the control plane defaults to
  a single element audience list that contains only the issuer URL.

The kubelet can also project a ServiceAccount token into a Pod. You can
specify desired properties of the token, such as the audience and the validity
duration. These properties are _not_ configurable on the default ServiceAccount
token. The token will also become invalid against the API when either the Pod
or the ServiceAccount is deleted.

You can configure this behavior for the `spec` of a Pod using a
projected volume type called
`ServiceAccountToken`.

The token from this projected volume is a JSON Web Token  (JWT).
The JSON payload of this token follows a well defined schema - an example payload for a pod bound token:

```yaml
{
  "aud": [  # matches the requested audiences, or the API server's default audiences when none are explicitly requested
    "https://kubernetes.default.svc"
  ],
  "exp": 1731613413,
  "iat": 1700077413,
  "iss": "https://kubernetes.default.svc",  # matches the first value passed to the --service-account-issuer flag
  "jti": "ea28ed49-2e11-4280-9ec5-bc3d1d84661a", 
  "kubernetes.io": {
    "namespace": "kube-system",
    "node": {
      "name": "127.0.0.1",
      "uid": "58456cb0-dd00-45ed-b797-5578fdceaced"
    },
    "pod": {
      "name": "coredns-69cbfb9798-jv9gn",
      "uid": "778a530c-b3f4-47c0-9cd5-ab018fb64f33"
    },
    "serviceaccount": {
      "name": "coredns",
      "uid": "a087d5a0-e1dd-43ec-93ac-f13d89cd13af"
    },
    "warnafter": 1700081020
  },
  "nbf": 1700077413,
  "sub": "system:serviceaccount:kube-system:coredns"
}
```

### Launch a Pod using service account token projection

To provide a Pod with a token with an audience of `vault` and a validity duration
of two hours, you could define a Pod manifest that is similar to:

Create the Pod:

```shell
kubectl create -f https://k8s.io/examples/pods/pod-projected-svc-token.yaml
```

The kubelet will: request and store the token on behalf of the Pod; make
the token available to the Pod at a configurable file path; and refresh
the token as it approaches expiration. The kubelet proactively requests rotation
for the token if it is older than 80% of its total time-to-live (TTL),
or if the token is older than 24 hours.

The application is responsible for reloading the token when it rotates. It's
often good enough for the application to load the token on a schedule
(for example: once every 5 minutes), without tracking the actual expiry time.

### Service account issuer discovery

If you have enabled token projection
for ServiceAccounts in your cluster, then you can also make use of the discovery
feature. Kubernetes provides a way for clients to federate as an _identity provider_,
so that one or more external systems can act as a _relying party_.

The issuer URL must comply with the
OIDC Discovery Spec. In
practice, this means it must use the `https` scheme, and should serve an OpenID
provider configuration at `{service-account-issuer}/.well-known/openid-configuration`.

If the URL does not comply, ServiceAccount issuer discovery endpoints are not
registered or accessible.

When enabled, the Kubernetes API server publishes an OpenID Provider
Configuration document via HTTP. The configuration document is published at
`/.well-known/openid-configuration`.
The OpenID Provider Configuration is sometimes referred to as the _discovery document_.
The Kubernetes API server publishes the related
JSON Web Key Set (JWKS), also via HTTP, at `/openid/v1/jwks`.

The responses served at `/.well-known/openid-configuration` and
`/openid/v1/jwks` are designed to be OIDC compatible, but not strictly OIDC
compliant. Those documents contain only the parameters necessary to perform
validation of Kubernetes service account tokens.

Clusters that use RBAC include a
default ClusterRole called `system:service-account-issuer-discovery`.
A default ClusterRoleBinding assigns this role to the `system:serviceaccounts` group,
which all ServiceAccounts implicitly belong to.
This allows pods running on the cluster to access the service account discovery document
via their mounted service account token. Administrators may, additionally, choose to
bind the role to `system:authenticated` or `system:unauthenticated` depending on their
security requirements and which external systems they intend to federate with.

The JWKS response contains public keys that a relying party can use to validate
the Kubernetes service account tokens. Relying parties first query for the
OpenID Provider Configuration, and use the `jwks_uri` field in the response to
find the JWKS.

In many cases, Kubernetes API servers are not available on the public internet,
but public endpoints that serve cached responses from the API server can be made
available by users or by service providers. In these cases, it is possible to
override the `jwks_uri` in the OpenID Provider Configuration so that it points
to the public endpoint, rather than the API server's address, by passing the
`--service-account-jwks-uri` flag to the API server. Like the issuer URL, the
JWKS URI is required to use the `https` scheme.
