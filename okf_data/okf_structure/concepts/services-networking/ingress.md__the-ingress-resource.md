---
id: okf-structure/concepts/services-networking/ingress.md#the-ingress-resource
kind: section
title: The Ingress resource
source: concepts/services-networking/ingress.md
url: https://kubernetes.io/docs/concepts/services-networking/ingress/
heading: The Ingress resource
parent: okf-structure/concepts/services-networking/ingress
children: []
prev_sibling: okf-structure/concepts/services-networking/ingress.md#prerequisites
next_sibling: okf-structure/concepts/services-networking/ingress.md#hostname-wildcards
word_count: 985
---

A minimal Ingress resource example:

An Ingress needs `apiVersion`, `kind`, `metadata` and `spec` fields.
The name of an Ingress object must be a valid
DNS subdomain name.
For general information about working with config files, see
deploying applications,
configuring containers,
managing resources.
Ingress controllers frequently use annotations to configure behavior.
Review the documentation for your choice of ingress controller to learn which annotations are expected and / or supported.

The Ingress spec
has all the information needed to configure a load balancer or proxy server. Most importantly, it
contains a list of rules matched against all incoming requests. Ingress resource only supports rules
for directing HTTP(S) traffic.

If the `ingressClassName` is omitted, a default Ingress class
should be defined.

Some ingress controllers work even without the definition of a
default IngressClass. Even if you use an ingress controller that is able
to operate without any IngressClass, the Kubernetes project still recommends
that you define a default IngressClass.

### Ingress rules

Each HTTP rule contains the following information:

* An optional host. In this example, no host is specified, so the rule applies to all inbound
  HTTP traffic through the IP address specified. If a host is provided (for example,
  foo.bar.com), the rules apply to that host.
* A list of paths (for example, `/testpath`), each of which has an associated
  backend defined with a `service.name` and a `service.port.name` or
  `service.port.number`. Both the host and path must match the content of an
  incoming request before the load balancer directs traffic to the referenced
  Service.
* A backend is a combination of Service and port names as described in the
  Service doc or a custom resource backend
  by way of a CRD. HTTP (and HTTPS) requests to the
  Ingress that match the host and path of the rule are sent to the listed backend.

A `defaultBackend` is often configured in an Ingress controller to service any requests that do not
match a path in the spec.

### DefaultBackend {#default-backend}

An Ingress with no rules sends all traffic to a single default backend and `.spec.defaultBackend`
is the backend that should handle requests in that case.
The `defaultBackend` is conventionally a configuration option of the
Ingress controller and
is not specified in your Ingress resources.
If no `.spec.rules` are specified, `.spec.defaultBackend` must be specified.
If `defaultBackend` is not set, the handling of requests that do not match any of the rules will be up to the
ingress controller (consult the documentation for your ingress controller to find out how it handles this case).

If none of the hosts or paths match the HTTP request in the Ingress objects, the traffic is
routed to your default backend.

### Resource backends {#resource-backend}

A `Resource` backend is an ObjectRef to another Kubernetes resource within the
same namespace as the Ingress object. A `Resource` is a mutually exclusive
setting with Service, and will fail validation if both are specified. A common
usage for a `Resource` backend is to ingress data to an object storage backend
with static assets.

After creating the Ingress above, you can view it with the following command:

```bash
kubectl describe ingress ingress-resource-backend
```

```
Name:             ingress-resource-backend
Namespace:        default
Address:
Default backend:  APIGroup: k8s.example.com, Kind: StorageBucket, Name: static-assets
Rules:
  Host        Path  Backends
  ----        ----  --------
  *
              /icons   APIGroup: k8s.example.com, Kind: StorageBucket, Name: icon-assets
Annotations:  <none>
Events:       <none>
```

### Path types

Each path in an Ingress is required to have a corresponding path type. Paths
that do not include an explicit `pathType` will fail validation. There are three
supported path types:

* `ImplementationSpecific`: With this path type, matching is up to the
  IngressClass. Implementations can treat this as a separate `pathType` or treat
  it identically to `Prefix` or `Exact` path types.

* `Exact`: Matches the URL path exactly and with case sensitivity.

* `Prefix`: Matches based on a URL path prefix split by `/`. Matching is case
  sensitive and done on a path element by element basis. A path element refers
  to the list of labels in the path split by the `/` separator. A request is a
  match for path _p_ if every _p_ is an element-wise prefix of _p_ of the
  request path.

  
  If the last element of the path is a substring of the last
  element in request path, it is not a match (for example: `/foo/bar`
  matches `/foo/bar/baz`, but does not match `/foo/barbaz`).
  

### Examples

| Kind   | Path(s)                         | Request path(s)               | Matches?                           |
|--------|---------------------------------|-------------------------------|------------------------------------|
| Prefix | `/`                             | (all paths)                   | Yes                                |
| Exact  | `/foo`                          | `/foo`                        | Yes                                |
| Exact  | `/foo`                          | `/bar`                        | No                                 |
| Exact  | `/foo`                          | `/foo/`                       | No                                 |
| Exact  | `/foo/`                         | `/foo`                        | No                                 |
| Prefix | `/foo`                          | `/foo`, `/foo/`               | Yes                                |
| Prefix | `/foo/`                         | `/foo`, `/foo/`               | Yes                                |
| Prefix | `/aaa/bb`                       | `/aaa/bbb`                    | No                                 |
| Prefix | `/aaa/bbb`                      | `/aaa/bbb`                    | Yes                                |
| Prefix | `/aaa/bbb/`                     | `/aaa/bbb`                    | Yes, ignores trailing slash        |
| Prefix | `/aaa/bbb`                      | `/aaa/bbb/`                   | Yes,  matches trailing slash       |
| Prefix | `/aaa/bbb`                      | `/aaa/bbb/ccc`                | Yes, matches subpath               |
| Prefix | `/aaa/bbb`                      | `/aaa/bbbxyz`                 | No, does not match string prefix   |
| Prefix | `/`, `/aaa`                     | `/aaa/ccc`                    | Yes, matches `/aaa` prefix         |
| Prefix | `/`, `/aaa`, `/aaa/bbb`         | `/aaa/bbb`                    | Yes, matches `/aaa/bbb` prefix     |
| Prefix | `/`, `/aaa`, `/aaa/bbb`         | `/ccc`                        | Yes, matches `/` prefix            |
| Prefix | `/aaa`                          | `/ccc`                        | No, uses default backend           |
| Mixed  | `/foo` (Prefix), `/foo` (Exact) | `/foo`                        | Yes, prefers Exact                 |

#### Multiple matches

In some cases, multiple paths within an Ingress will match a request. In those
cases precedence will be given first to the longest matching path. If two paths
are still equally matched, precedence will be given to paths with an exact path
type over prefix path type.
