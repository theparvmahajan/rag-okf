---
id: okf-structure/concepts/services-networking/service.md#services-in-kubernetes
kind: section
title: Services in Kubernetes
source: concepts/services-networking/service.md
url: https://kubernetes.io/docs/concepts/services-networking/service/
heading: Services in Kubernetes
parent: okf-structure/concepts/services-networking/service
children: []
prev_sibling: okf-structure/concepts/services-networking/service.md#introduction
next_sibling: okf-structure/concepts/services-networking/service.md#defining-a-service
word_count: 336
---

The Service API, part of Kubernetes, is an abstraction to help you expose groups of
Pods over a network. Each Service object defines a logical set of endpoints (usually
these endpoints are Pods) along with a policy about how to make those pods accessible.

For example, consider a stateless image-processing backend which is running with
3 replicas.  Those replicas are fungible—frontends do not care which backend
they use.  While the actual Pods that compose the backend set may change, the
frontend clients should not need to be aware of that, nor should they need to keep
track of the set of backends themselves.

The Service abstraction enables this decoupling.

The set of Pods targeted by a Service is usually determined
by a selector that you
define.
To learn about other ways to define Service endpoints,
see Services _without_ selectors.

If your workload speaks HTTP, you might choose to use an
Ingress to control how web traffic
reaches that workload.
Ingress is not a Service type, but it acts as the entry point for your
cluster. An Ingress lets you consolidate your routing rules into a single resource, so
that you can expose multiple components of your workload, running separately in your
cluster, behind a single listener.

The Gateway API for Kubernetes
provides extra capabilities beyond Ingress and Service. You can add Gateway to your cluster -
it is a family of extension APIs, implemented using
CustomResourceDefinitions -
and then use these to configure access to network services that are running in your cluster.

### Cloud-native service discovery

If you're able to use Kubernetes APIs for service discovery in your application,
you can query the API server
for matching EndpointSlices. Kubernetes updates the EndpointSlices for a Service
whenever the set of Pods in a Service changes.

For non-native applications, Kubernetes offers ways to place a network port or load
balancer in between your application and the backend Pods.

Either way, your workload can use these service discovery
mechanisms to find the target it wants to connect to.
