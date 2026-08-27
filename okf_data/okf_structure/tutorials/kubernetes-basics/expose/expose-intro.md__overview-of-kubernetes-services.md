---
id: okf-structure/tutorials/kubernetes-basics/expose/expose-intro.md#overview-of-kubernetes-services
kind: section
title: Overview of Kubernetes Services
source: tutorials/kubernetes-basics/expose/expose-intro.md
url: https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/
heading: Overview of Kubernetes Services
parent: okf-structure/tutorials/kubernetes-basics/expose/expose-intro
children: []
prev_sibling: okf-structure/tutorials/kubernetes-basics/expose/expose-intro.md#prerequisites
next_sibling: okf-structure/tutorials/kubernetes-basics/expose/expose-intro.md#services-and-labels
word_count: 470
---

Kubernetes Pods are mortal. Pods have a
lifecycle. When a worker node dies,
the Pods running on the Node are also lost. A Replicaset
might then dynamically drive the cluster back to the desired state via the creation
of new Pods to keep your application running. As another example, consider an image-processing
backend with 3 replicas. Those replicas are exchangeable; the front-end system should
not care about backend replicas or even if a Pod is lost and recreated. That said,
each Pod in a Kubernetes cluster has a unique IP address, even Pods on the same Node,
so there needs to be a way of automatically reconciling changes among Pods so that your
applications continue to function.

_A Kubernetes Service is an abstraction layer which defines a logical set of Pods and
enables external traffic exposure, load balancing and service discovery for those Pods._

A Service in Kubernetes is an abstraction
which defines a logical set of Pods and a policy by which to access them. Services
enable a loose coupling between dependent Pods. A Service is defined using YAML or JSON,
like all Kubernetes object manifests. The set of Pods targeted by a Service is usually
determined by a _label selector_ (see below for why you might want a Service without
including a `selector` in the spec).

Although each Pod has a unique IP address, those IPs are not exposed outside the
cluster without a Service. Services allow your applications to receive traffic.
Services can be exposed in different ways by specifying a `type` in the `spec` of the Service:

* _ClusterIP_ (default) - Exposes the Service on an internal IP in the cluster. This
type makes the Service only reachable from within the cluster.

* _NodePort_ - Exposes the Service on the same port of each selected Node in the cluster using NAT.
Makes a Service accessible from outside the cluster using `NodeIP:NodePort`. Superset of ClusterIP.

* _LoadBalancer_ - Creates an external load balancer in the current cloud (if supported)
and assigns a fixed, external IP to the Service. Superset of NodePort.

* _ExternalName_ - Maps the Service to the contents of the `externalName` field
(e.g. `foo.bar.example.com`), by returning a `CNAME` record with its value.
No proxying of any kind is set up. This type requires v1.7 or higher of `kube-dns`,
or CoreDNS version 0.0.8 or higher.

More information about the different types of Services can be found in the
Using Source IP tutorial. Also see
Connecting Applications with Services.

Additionally, note that there are some use cases with Services that involve not defining
a `selector` in the spec. A Service created without `selector` will also not create
the corresponding Endpoints object. This allows users to manually map a Service to
specific endpoints. Another possibility why there may be no selector is you are strictly
using `type: ExternalName`.
