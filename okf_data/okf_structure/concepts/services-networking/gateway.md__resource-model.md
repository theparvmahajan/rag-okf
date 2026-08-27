---
id: okf-structure/concepts/services-networking/gateway.md#resource-model
kind: section
title: Resource model
source: concepts/services-networking/gateway.md
url: https://kubernetes.io/docs/concepts/services-networking/gateway/
heading: Resource model
parent: okf-structure/concepts/services-networking/gateway
children: []
prev_sibling: okf-structure/concepts/services-networking/gateway.md#design-principles
next_sibling: okf-structure/concepts/services-networking/gateway.md#request-flow
word_count: 877
---

Gateway API has four stable API kinds:

* __GatewayClass:__ Defines a set of gateways with common configuration and managed by a controller
  that implements the class.

* __Gateway:__ Defines an instance of traffic handling infrastructure, such as cloud load balancer.

* __HTTPRoute:__ Defines HTTP-specific rules for mapping traffic from a Gateway listener to a
  representation of backend network endpoints. These endpoints are often represented as a
  Service.

* __GRPCRoute:__ Defines gRPC-specific rules for mapping traffic from a Gateway listener to a
representation of backend network endpoints. These endpoints are often represented as a
  Service.

Gateway API is organized into different API kinds that have interdependent relationships to support
the role-oriented nature of organizations. A Gateway object is associated with exactly one GatewayClass;
the GatewayClass describes the gateway controller responsible for managing Gateways of this class.
One or more route kinds such as HTTPRoute, are then associated to Gateways. A Gateway can filter the routes
that may be attached to its `listeners`, forming a bidirectional trust model with routes.

The following figure illustrates the relationships of the three stable Gateway API kinds:

### GatewayClass {#api-kind-gateway-class}

Gateways can be implemented by different controllers, often with different configurations. A Gateway
must reference a GatewayClass that contains the name of the controller that implements the
class.

A minimal GatewayClass example:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: example-class
spec:
  controllerName: example.com/gateway-controller
```

In this example, a controller that has implemented Gateway API is configured to manage GatewayClasses
with the controller name `example.com/gateway-controller`. Gateways of this class will be managed by
the implementation's controller.

See the GatewayClass
reference for a full definition of this API kind.

### Gateway {#api-kind-gateway}

A Gateway describes an instance of traffic handling infrastructure. It defines a network endpoint
that can be used for processing traffic, i.e. filtering, balancing, splitting, etc. for backends
such as a Service. For example, a Gateway may represent a cloud load balancer or an in-cluster proxy
server that is configured to accept HTTP traffic.

A typical Gateway resource example:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: example-gateway
  namespace: example-namespace
spec:
  gatewayClassName: example-class
  listeners:
  - name: http
    protocol: HTTP
    port: 80
    hostname: "www.example.com"
    allowedRoutes:
      namespaces:
        from: Same
```

In this example, an instance of traffic handling infrastructure is programmed to listen for HTTP
traffic on port 80. Since the `addresses` field is unspecified, an address or hostname is assigned
to the Gateway by the implementation's controller. This address is used as a network endpoint for
processing traffic of backend network endpoints defined in routes.

See the Gateway
reference for a full definition of this API kind. For guidance on configuring HTTPS/TLS listeners, see the
Gateway API TLS Guide.

By default, a Gateway only accepts Routes from the same namespace. Cross-namespace Routes require configuring `allowedRoutes`.

### HTTPRoute {#api-kind-httproute}

The HTTPRoute kind specifies routing behavior of HTTP requests from a Gateway listener to backend network
endpoints. For a Service backend, an implementation may represent the backend network endpoint as a Service
IP or the backing EndpointSlices of the Service. An HTTPRoute represents configuration that is applied to the
underlying Gateway implementation. For example, defining a new HTTPRoute may result in configuring additional
traffic routes in a cloud load balancer or in-cluster proxy server.

A typical HTTPRoute example:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: example-httproute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "www.example.com"
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /login
    backendRefs:
    - name: example-svc
      port: 8080
```

In this example, HTTP traffic from Gateway `example-gateway` with the Host: header set to `www.example.com`
and the request path specified as `/login` will be routed to Service `example-svc` on port `8080`.

See the HTTPRoute
reference for a full definition of this API kind.

### GRPCRoute {#api-kind-grpcroute}

The GRPCRoute kind specifies routing behavior of gRPC requests from a Gateway listener to backend network
endpoints. For a Service backend, an implementation may represent the backend network endpoint as a Service
IP or the backing EndpointSlices of the Service. A GRPCRoute represents configuration that is applied to the
underlying Gateway implementation. For example, defining a new GRPCRoute may result in configuring additional
traffic routes in a cloud load balancer or in-cluster proxy server.

Gateways supporting GRPCRoute are required to support HTTP/2 without an initial upgrade from HTTP/1,
so gRPC traffic is guaranteed to flow properly.

A typical GRPCRoute example:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: example-grpcroute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "svc.example.com"
  rules:
  - backendRefs:
    - name: example-svc
      port: 50051
```

In this example, gRPC traffic from Gateway `example-gateway` with the host set to `svc.example.com`
will be directed to the service `example-svc` on port `50051` from the same namespace.

GRPCRoute allows matching specific gRPC services, as per the following example:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GRPCRoute
metadata:
  name: example-grpcroute
spec:
  parentRefs:
  - name: example-gateway
  hostnames:
  - "svc.example.com"
  rules:
  - matches:
    - method:
        service: com.example
        method: Login
    backendRefs:
    - name: foo-svc
      port: 50051
```

In this case, the GRPCRoute will match any traffic for svc.example.com and apply its routing rules
to forward the traffic to the correct backend. Since there is only one match specified,only requests
for the com.example.User.Login method to svc.example.com will be forwarded.
RPCs of any other method` will not be matched by this Route.

See the GRPCRoute
reference for a full definition of this API kind.
