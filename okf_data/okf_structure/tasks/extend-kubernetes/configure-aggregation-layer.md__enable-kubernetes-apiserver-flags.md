---
id: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#enable-kubernetes-apiserver-flags
kind: section
title: Enable Kubernetes Apiserver flags
source: tasks/extend-kubernetes/configure-aggregation-layer.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-aggregation-layer/
heading: Enable Kubernetes Apiserver flags
parent: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#authentication-flow
next_sibling: okf-structure/tasks/extend-kubernetes/configure-aggregation-layer.md#whatsnext
word_count: 653
---

Enable the aggregation layer via the following `kube-apiserver` flags.
They may have already been taken care of by your provider.

    --requestheader-client-ca-file=<path to aggregator CA cert>
    --requestheader-allowed-names=front-proxy-client
    --requestheader-extra-headers-prefix=X-Remote-Extra-
    --requestheader-group-headers=X-Remote-Group
    --requestheader-username-headers=X-Remote-User
    --proxy-client-cert-file=<path to aggregator proxy cert>
    --proxy-client-key-file=<path to aggregator proxy key>

### CA Reusage and Conflicts

The Kubernetes apiserver has two client CA options:

* `--client-ca-file`
* `--requestheader-client-ca-file`

Each of these functions independently and can conflict with each other,
if not used correctly.

* `--client-ca-file`: When a request arrives to the Kubernetes apiserver,
  if this option is enabled, the Kubernetes apiserver checks the certificate
  of the request. If it is signed by one of the CA certificates in the file referenced by
  `--client-ca-file`, then the request is treated as a legitimate request,
  and the user is the value of the common name `CN=`, while the group is the organization `O=`.
  See the documentation on TLS authentication.
* `--requestheader-client-ca-file`: When a request arrives to the Kubernetes apiserver,
  if this option is enabled, the Kubernetes apiserver checks the certificate of the request.
  If it is signed by one of the CA certificates in the file reference by `--requestheader-client-ca-file`,
  then the request is treated as a potentially legitimate request. The Kubernetes apiserver then
  checks if the common name `CN=` is one of the names in the list provided by `--requestheader-allowed-names`.
  If the name is allowed, the request is approved; if it is not, the request is not.

If _both_ `--client-ca-file` and `--requestheader-client-ca-file` are provided,
then the request first checks the `--requestheader-client-ca-file` CA and then the
`--client-ca-file`. Normally, different CAs, either root CAs or intermediate CAs,
are used for each of these options; regular client requests match against `--client-ca-file`,
while aggregation requests match against `--requestheader-client-ca-file`. However,
if both use the _same_ CA, then client requests that normally would pass via `--client-ca-file`
will fail, because the CA will match the CA in `--requestheader-client-ca-file`,
but the common name `CN=` will **not** match one of the acceptable common names in
`--requestheader-allowed-names`. This can cause your kubelets and other control plane components,
as well as end-users, to be unable to authenticate to the Kubernetes apiserver.

For this reason, use different CA certs for the `--client-ca-file`
option - to authorize control plane components and end-users - and the `--requestheader-client-ca-file` option - to authorize aggregation apiserver requests.

Do **not** reuse a CA that is used in a different context unless you understand
the risks and the mechanisms to protect the CA's usage.

If you are not running kube-proxy on a host running the API server,
then you must make sure that the system is enabled with the following
`kube-apiserver` flag:

    --enable-aggregator-routing=true

### Register APIService objects

You can dynamically configure what client requests are proxied to extension
apiserver. The following is an example registration:

```yaml

apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  name: <name of the registration object>
spec:
  group: <API group name this extension apiserver hosts>
  version: <API version this extension apiserver hosts>
  groupPriorityMinimum: <priority this APIService for this group, see API documentation>
  versionPriority: <prioritizes ordering of this version within a group, see API documentation>
  service:
    namespace: <namespace of the extension apiserver service>
    name: <name of the extension apiserver service>
  caBundle: <pem encoded ca cert that signs the server cert used by the webhook>
```

The name of an APIService object must be a valid
path segment name.

#### Contacting the extension apiserver

Once the Kubernetes apiserver has determined a request should be sent to an extension apiserver,
it needs to know how to contact it.

The `service` stanza is a reference to the service for an extension apiserver.
The service namespace and name are required. The port is optional and defaults to 443.

Here is an example of an extension apiserver that is configured to be called on port "1234",
and to verify the TLS connection against the ServerName
`my-service-name.my-service-namespace.svc` using a custom CA bundle.

```yaml
apiVersion: apiregistration.k8s.io/v1
kind: APIService
...
spec:
  ...
  service:
    namespace: my-service-namespace
    name: my-service-name
    port: 1234
  caBundle: "Ci0tLS0tQk...<base64-encoded PEM bundle>...tLS0K"
...
```
