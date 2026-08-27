---
id: okf-structure/concepts/services-networking/service.md#defining-a-service
kind: section
title: Defining a Service
source: concepts/services-networking/service.md
url: https://kubernetes.io/docs/concepts/services-networking/service/
heading: Defining a Service
parent: okf-structure/concepts/services-networking/service
children: []
prev_sibling: okf-structure/concepts/services-networking/service.md#services-in-kubernetes
next_sibling: okf-structure/concepts/services-networking/service.md#service-type-publishing-services-service-types
word_count: 1567
---

A Service is an object
(the same way that a Pod or a ConfigMap is an object). You can create,
view or modify Service definitions using the Kubernetes API. Usually
you use a tool such as `kubectl` to make those API calls for you.

For example, suppose you have a set of Pods that each listen on TCP port 9376
and are labelled as `app.kubernetes.io/name=MyApp`. You can define a Service to
publish that TCP listener:

Applying this manifest creates a new Service named "my-service" with the default
ClusterIP service type. The Service
targets TCP port 9376 on any Pod with the `app.kubernetes.io/name: MyApp` label.

Kubernetes assigns this Service an IP address (the _cluster IP_),
that is used by the virtual IP address mechanism. For more details on that mechanism,
read Virtual IPs and Service Proxies.

The controller for that Service continuously scans for Pods that
match its selector, and then makes any necessary updates to the set of
EndpointSlices for the Service.

The name of a Service object must be a valid
RFC 1123 label name.

A Service can map _any_ incoming `port` to a `targetPort`. By default and
for convenience, the `targetPort` is set to the same value as the `port`
field.

### Port definitions {#field-spec-ports}

Port definitions in Pods have names, and you can reference these names in the
`targetPort` attribute of a Service. For example, we can bind the `targetPort`
of the Service to the Pod port in the following way:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app.kubernetes.io/name: proxy
  ports:
  - name: name-of-service-port
    protocol: TCP
    port: 80
    targetPort: http-web-svc

---
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
      - containerPort: 80
        name: http-web-svc
```

This works even if there is a mixture of Pods in the Service using a single
configured name, with the same network protocol available via different
port numbers. This offers a lot of flexibility for deploying and evolving
your Services. For example, you can change the port numbers that Pods expose
in the next version of your backend software, without breaking clients.

The default protocol for Services is
TCP; you can also
use any other supported protocol.

Because many Services need to expose more than one port, Kubernetes supports
multiple port definitions for a single Service.
Each port definition can have the same `protocol`, or a different one.

### Services without selectors

Services most commonly abstract access to Kubernetes Pods thanks to the selector,
but when used with a corresponding set of
EndpointSlices
objects and without a selector, the Service can abstract other kinds of backends,
including ones that run outside the cluster.

For example:

* You want to have an external database cluster in production, but in your
  test environment you use your own databases.
* You want to point your Service to a Service in a different
  namespace or on another cluster.
* You are migrating a workload to Kubernetes. While evaluating the approach,
  you run only a portion of your backends in Kubernetes.

In any of these scenarios you can define a Service _without_ specifying a
selector to match Pods. For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
```

Because this Service has no selector, the corresponding EndpointSlice
objects are not created automatically. You can map the Service
to the network address and port where it's running, by adding an EndpointSlice
object manually. For example:

```yaml
apiVersion: discovery.k8s.io/v1
kind: EndpointSlice
metadata:
  name: my-service-1 # by convention, use the name of the Service
                     # as a prefix for the name of the EndpointSlice
  labels:
    # You should set the "kubernetes.io/service-name" label.
    # Set its value to match the name of the Service
    kubernetes.io/service-name: my-service
addressType: IPv4
ports:
  - name: http # should match with the name of the service port defined above
    appProtocol: http
    protocol: TCP
    port: 9376
endpoints:
  - addresses:
      - "10.4.5.6"
  - addresses:
      - "10.1.2.3"
```

#### Custom EndpointSlices

When you create an EndpointSlice object for a Service, you can
use any name for the EndpointSlice. Each EndpointSlice in a namespace must have a
unique name. You link an EndpointSlice to a Service by setting the
`kubernetes.io/service-name` label
on that EndpointSlice.

The endpoint IPs _must not_ be: loopback (127.0.0.0/8 for IPv4, ::1/128 for IPv6), or
link-local (169.254.0.0/16 and 224.0.0.0/24 for IPv4, fe80::/64 for IPv6).

The endpoint IP addresses cannot be the cluster IPs of other Kubernetes Services,
because kube proxy doesn't support virtual IPs
as a destination.

For an EndpointSlice that you create yourself, or in your own code,
you should also pick a value to use for the label
`endpointslice.kubernetes.io/managed-by`.
If you create your own controller code to manage EndpointSlices, consider using a
value similar to `"my-domain.example/name-of-controller"`. If you are using a third
party tool, use the name of the tool in all-lowercase and change spaces and other
punctuation to dashes (`-`).
If people are directly using a tool such as `kubectl` to manage EndpointSlices,
use a name that describes this manual management, such as `"staff"` or
`"cluster-admins"`. You should
avoid using the reserved value `"controller"`, which identifies EndpointSlices
managed by Kubernetes' own control plane.

#### Accessing a Service without a selector {#service-no-selector-access}

Accessing a Service without a selector works the same as if it had a selector.
In the example for a Service without a selector,
traffic is routed to one of the two endpoints defined in
the EndpointSlice manifest: a TCP connection to 10.1.2.3 or 10.4.5.6, on port 9376.

The Kubernetes API server does not allow proxying to endpoints that are not mapped to
pods. Actions such as `kubectl port-forward service/<service-name> forwardedPort:servicePort` where the service has no
selector will fail due to this constraint. This prevents the Kubernetes API server
from being used as a proxy to endpoints the caller may not be authorized to access.

An `ExternalName` Service is a special case of Service that does not have
selectors and uses DNS names instead. For more information, see the
ExternalName section.

### EndpointSlices

EndpointSlices are objects that
represent a subset (a _slice_) of the backing network endpoints for a Service.

Your Kubernetes cluster tracks how many endpoints each EndpointSlice represents.
If there are so many endpoints for a Service that a threshold is reached, then
Kubernetes adds another empty EndpointSlice and stores new endpoint information
there.
By default, Kubernetes makes a new EndpointSlice once the existing EndpointSlices
all contain at least 100 endpoints. Kubernetes does not make the new EndpointSlice
until an extra endpoint needs to be added.

See EndpointSlices for more
information about this API.

### Endpoints (deprecated) {#endpoints}

The EndpointSlice API is the evolution of the older
Endpoints
API. The deprecated Endpoints API has several problems relative to
EndpointSlice:

  - It does not support dual-stack clusters.
  - It does not contain information needed to support newer features, such as
    trafficDistribution.
  - It will truncate the list of endpoints if it is too long to fit in a single object.

Because of this, it is recommended that all clients use the
EndpointSlice API rather than Endpoints.

#### Over-capacity endpoints

Kubernetes limits the number of endpoints that can fit in a single Endpoints
object. When there are over 1000 backing endpoints for a Service, Kubernetes
truncates the data in the Endpoints object. Because a Service can be linked
with more than one EndpointSlice, the 1000 backing endpoint limit only
affects the legacy Endpoints API.

In that case, Kubernetes selects at most 1000 possible backend endpoints to store
into the Endpoints object, and sets an
annotation on the Endpoints:
`endpoints.kubernetes.io/over-capacity: truncated`.
The control plane also removes that annotation if the number of backend Pods drops below 1000.

Traffic is still sent to backends, but any load balancing mechanism that relies on the
legacy Endpoints API only sends traffic to at most 1000 of the available backing endpoints.

The same API limit means that you cannot manually update an Endpoints to have more than 1000 endpoints.

### Application protocol

The `appProtocol` field provides a way to specify an application protocol for
each Service port. This is used as a hint for implementations to offer
richer behavior for protocols that they understand.
The value of this field is mirrored by the corresponding
Endpoints and EndpointSlice objects.

This field follows standard Kubernetes label syntax. Valid values are one of:

* IANA standard service names.

* Implementation-defined prefixed names such as `mycompany.com/my-custom-protocol`.

* Kubernetes-defined prefixed names:

| Protocol | Description |
|----------|-------------|
| `kubernetes.io/h2c` | HTTP/2 over cleartext as described in RFC 9113 |
| `kubernetes.io/ws`  | WebSocket over cleartext as described in RFC 6455 |
| `kubernetes.io/wss` | WebSocket over TLS as described in RFC 6455 |

### Multi-port Services

For some Services, you need to expose more than one port.
Kubernetes lets you configure multiple port definitions on a Service object.
When using multiple ports for a Service, you must give all of your ports names
so that these are unambiguous.
For example:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  selector:
    app.kubernetes.io/name: MyApp
  ports:
    - name: http
      protocol: TCP
      port: 80
      targetPort: 9376
    - name: https
      protocol: TCP
      port: 443
      targetPort: 9377
```

As with Kubernetes names in general, names for ports
must only contain lowercase alphanumeric characters and `-`. Port names must
also start and end with an alphanumeric character.

For example, the names `123-abc` and `web` are valid, but `123_abc` and `-web` are not.
