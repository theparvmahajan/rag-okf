---
id: okf-structure/concepts/services-networking/ingress.md#types-of-ingress
kind: section
title: Types of Ingress
source: concepts/services-networking/ingress.md
url: https://kubernetes.io/docs/concepts/services-networking/ingress/
heading: Types of Ingress
parent: okf-structure/concepts/services-networking/ingress
children: []
prev_sibling: okf-structure/concepts/services-networking/ingress.md#ingress-class
next_sibling: okf-structure/concepts/services-networking/ingress.md#updating-an-ingress
word_count: 750
---

### Ingress backed by a single Service {#single-service-ingress}

There are existing Kubernetes concepts that allow you to expose a single Service
(see alternatives). You can also do this with an Ingress by specifying a
*default backend* with no rules.

If you create it using `kubectl apply -f` you should be able to view the state
of the Ingress you added:

```bash
kubectl get ingress test-ingress
```

```
NAME           CLASS         HOSTS   ADDRESS         PORTS   AGE
test-ingress   external-lb   *       203.0.113.123   80      59s
```

Where `203.0.113.123` is the IP allocated by the Ingress controller to satisfy
this Ingress.

Ingress controllers and load balancers may take a minute or two to allocate an IP address.
Until that time, you often see the address listed as `<pending>`.

### Simple fanout

A fanout configuration routes traffic from a single IP address to more than one Service,
based on the HTTP URI being requested. An Ingress allows you to keep the number of load balancers
down to a minimum. For example, a setup like:

It would require an Ingress such as:

When you create the Ingress with `kubectl apply -f`:

```shell
kubectl describe ingress simple-fanout-example
```

```
Name:             simple-fanout-example
Namespace:        default
Address:          178.91.123.132
Default backend:  default-http-backend:80 (10.8.2.3:8080)
Rules:
  Host         Path  Backends
  ----         ----  --------
  foo.bar.com
               /foo   service1:4200 (10.8.0.90:4200)
               /bar   service2:8080 (10.8.0.91:8080)
Events:
  Type     Reason  Age                From                     Message
  ----     ------  ----               ----                     -------
  Normal   ADD     22s                loadbalancer-controller  default/test
```

The Ingress controller provisions an implementation-specific load balancer
that satisfies the Ingress, as long as the Services (`service1`, `service2`) exist.
When it has done so, you can see the address of the load balancer at the
Address field.

Depending on the Ingress controller
you are using, you may need to create a default-http-backend
Service.

### Name based virtual hosting

Name-based virtual hosts support routing HTTP traffic to multiple host names at the same IP address.

The following Ingress tells the backing load balancer to route requests based on
the Host header.

If you create an Ingress resource without any hosts defined in the rules, then any
web traffic to the IP address of your Ingress controller can be matched without a name based
virtual host being required.

For example, the following Ingress routes traffic
requested for `first.bar.com` to `service1`, `second.bar.com` to `service2`,
and any traffic whose request host header doesn't match `first.bar.com`
and `second.bar.com` to `service3`.

### TLS

You can secure an Ingress by specifying a secret
that contains a TLS private key and certificate. The Ingress resource only
supports a single TLS port, 443, and assumes TLS termination at the ingress point
(traffic to the Service and its Pods is in plaintext).
If the TLS configuration section in an Ingress specifies different hosts, they are
multiplexed on the same port according to the hostname specified through the
SNI TLS extension (provided the Ingress controller supports SNI). The TLS secret
must contain keys named `tls.crt` and `tls.key` that contain the certificate
and private key to use for TLS. For example:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: testsecret-tls
  namespace: default
data:
  tls.crt: base64 encoded cert
  tls.key: base64 encoded key
type: kubernetes.io/tls
```

Referencing this secret in an Ingress tells the Ingress controller to
secure the channel from the client to the load balancer using TLS. You need to make
sure the TLS secret you created came from a certificate that contains a Common
Name (CN), also known as a Fully Qualified Domain Name (FQDN) for `https-example.foo.com`.

Keep in mind that TLS will not work on the default rule because the
certificates would have to be issued for all the possible sub-domains. Therefore,
`hosts` in the `tls` section need to explicitly match the `host` in the `rules`
section.

There is a gap between TLS features supported by various ingress controllers.
You should refer to the documentation for the ingress controller(s) you've chosen to
understand how TLS works in your environment.

### Load balancing {#load-balancing}

An Ingress controller is bootstrapped with some load balancing policy settings
that it applies to all Ingress, such as the load balancing algorithm, backend
weight scheme, and others. More advanced load balancing concepts
(e.g. persistent sessions, dynamic weights) are not yet exposed through the
Ingress. You can instead get these features through the load balancer used for
a Service.

It's also worth noting that even though health checks are not exposed directly
through the Ingress, there exist parallel concepts in Kubernetes such as
readiness probes
that allow you to achieve the same end result. Please review the controller
specific documentation to see how they handle health checks.
