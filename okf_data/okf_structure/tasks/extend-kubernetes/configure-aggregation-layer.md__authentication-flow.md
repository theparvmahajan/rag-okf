---
id: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#authentication-flow
kind: section
title: Authentication Flow
source: tasks/extend-kubernetes/configure-aggregation-layer.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/
heading: Authentication Flow
parent: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#prerequisites
next_sibling: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#enable-kubernetes-apiserver-flags
word_count: 1122
---

Unlike Custom Resource Definitions (CRDs), the Aggregation API involves
another server - your Extension apiserver - in addition to the standard Kubernetes apiserver.
The Kubernetes apiserver will need to communicate with your extension apiserver,
and your extension apiserver will need to communicate with the Kubernetes apiserver.
In order for this communication to be secured, the Kubernetes apiserver uses x509
certificates to authenticate itself to the extension apiserver.

This section describes how the authentication and authorization flows work,
and how to configure them.

The high-level flow is as follows:

1. Kubernetes apiserver: authenticate the requesting user and authorize their
   rights to the requested API path.
2. Kubernetes apiserver: proxy the request to the extension apiserver
3. Extension apiserver: authenticate the request from the Kubernetes apiserver
4. Extension apiserver: authorize the request from the original user
5. Extension apiserver: execute

The rest of this section describes these steps in detail.

The flow can be seen in the following diagram.

aggregation auth flows

The source for the above swimlanes can be found in the source of this document.

### Kubernetes Apiserver Authentication and Authorization

A request to an API path that is served by an extension apiserver begins
the same way as all API requests: communication to the Kubernetes apiserver.
This path already has been registered with the Kubernetes apiserver by the extension apiserver.

The user communicates with the Kubernetes apiserver, requesting access to the path.
The Kubernetes apiserver uses standard authentication and authorization configured
with the Kubernetes apiserver to authenticate the user and authorize access to the specific path.

For an overview of authenticating to a Kubernetes cluster, see
"Authenticating to a Cluster".
For an overview of authorization of access to Kubernetes cluster resources, see
"Authorization Overview".

Everything to this point has been standard Kubernetes API requests, authentication and authorization.

The Kubernetes apiserver now is prepared to send the request to the extension apiserver.

### Kubernetes Apiserver Proxies the Request

The Kubernetes apiserver now will send, or proxy, the request to the extension
apiserver that registered to handle the request. In order to do so,
it needs to know several things:

1. How should the Kubernetes apiserver authenticate to the extension apiserver,
   informing the extension apiserver that the request, which comes over the network,
   is coming from a valid Kubernetes apiserver?
2. How should the Kubernetes apiserver inform the extension apiserver of the
   username and group for which the original request was authenticated?

In order to provide for these two, you must configure the Kubernetes apiserver using several flags.

#### Kubernetes Apiserver Client Authentication

The Kubernetes apiserver connects to the extension apiserver over TLS,
authenticating itself using a client certificate. You must provide the
following to the Kubernetes apiserver upon startup, using the provided flags:

* private key file via `--proxy-client-key-file`
* signed client certificate file via `--proxy-client-cert-file`
* certificate of the CA that signed the client certificate file via `--requestheader-client-ca-file`
* valid Common Name values (CNs) in the signed client certificate via `--requestheader-allowed-names`

The Kubernetes apiserver will use the files indicated by `--proxy-client-*-file`
to authenticate to the extension apiserver. In order for the request to be considered
valid by a compliant extension apiserver, the following conditions must be met:

1. The connection must be made using a client certificate that is signed by
   the CA whose certificate is in `--requestheader-client-ca-file`.
2. The connection must be made using a client certificate whose CN is one of
   those listed in `--requestheader-allowed-names`.

You can set this option to blank as `--requestheader-allowed-names=""`.
This will indicate to an extension apiserver that _any_ CN is acceptable.

When started with these options, the Kubernetes apiserver will:

1. Use them to authenticate to the extension apiserver.
2. Create a configmap in the `kube-system` namespace called `extension-apiserver-authentication`,
   in which it will place the CA certificate and the allowed CNs. These in turn can be retrieved
   by extension apiservers to validate requests.

Note that the same client certificate is used by the Kubernetes apiserver to authenticate
against _all_ extension apiservers. It does not create a client certificate per extension
apiserver, but rather a single one to authenticate as the Kubernetes apiserver.
This same one is reused for all extension apiserver requests. 

#### Original Request Username and Group

When the Kubernetes apiserver proxies the request to the extension apiserver,
it informs the extension apiserver of the username and group with which the
original request successfully authenticated. It provides these in http headers
of its proxied request. You must inform the Kubernetes apiserver of the names
of the headers to be used.

* the header in which to store the username via `--requestheader-username-headers`
* the header in which to store the group via `--requestheader-group-headers`
* the prefix to append to all extra headers via `--requestheader-extra-headers-prefix`

These header names are also placed in the `extension-apiserver-authentication` configmap,
so they can be retrieved and used by extension apiservers.

### Extension Apiserver Authenticates the Request

The extension apiserver, upon receiving a proxied request from the Kubernetes apiserver,
must validate that the request actually did come from a valid authenticating proxy,
which role the Kubernetes apiserver is fulfilling. The extension apiserver validates it via:

1. Retrieve the following from the configmap in `kube-system`, as described above:
    * Client CA certificate
    * List of allowed names (CNs)
    * Header names for username, group and extra info
2. Check that the TLS connection was authenticated using a client certificate which:
    * Was signed by the CA whose certificate matches the retrieved CA certificate.
    * Has a CN in the list of allowed CNs, unless the list is blank, in which case all CNs are allowed.
    * Extract the username and group from the appropriate headers

If the above passes, then the request is a valid proxied request from a legitimate
authenticating proxy, in this case the Kubernetes apiserver.

Note that it is the responsibility of the extension apiserver implementation to provide
the above. Many do it by default, leveraging the `k8s.io/apiserver/` package.
Others may provide options to override it using command-line options.

In order to have permission to retrieve the configmap, an extension apiserver
requires the appropriate role. There is a default role named `extension-apiserver-authentication-reader`
in the `kube-system` namespace which can be assigned.

### Extension Apiserver Authorizes the Request

The extension apiserver now can validate that the user/group retrieved from
the headers are authorized to execute the given request. It does so by sending
a standard SubjectAccessReview
request to the Kubernetes apiserver. 

In order for the extension apiserver to be authorized itself to submit the
`SubjectAccessReview` request to the Kubernetes apiserver, it needs the correct permissions.
Kubernetes includes a default `ClusterRole` named `system:auth-delegator` that
has the appropriate permissions. It can be granted to the extension apiserver's service account.

### Extension Apiserver Executes

If the `SubjectAccessReview` passes, the extension apiserver executes the request.
