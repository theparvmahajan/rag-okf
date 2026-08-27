---
id: okf-structure/concepts/security/multi-tenancy.md#additional-considerations
kind: section
title: Additional Considerations
source: concepts/security/multi-tenancy.md
url: https://kubernetes.io/docs/concepts/security/multi-tenancy/
heading: Additional Considerations
parent: okf-structure/concepts/security/multi-tenancy
children: []
prev_sibling: okf-structure/concepts/security/multi-tenancy.md#data-plane-isolation
next_sibling: okf-structure/concepts/security/multi-tenancy.md#implementations
word_count: 710
---

This section discusses other Kubernetes constructs and patterns that are relevant for multi-tenancy.

### API Priority and Fairness

API priority and fairness is a Kubernetes
feature that allows you to assign a priority to certain pods running within the cluster.
When an application calls the Kubernetes API, the API server evaluates the priority assigned to pod.
Calls from pods with higher priority are fulfilled before those with a lower priority.
When contention is high, lower priority calls can be queued until the server is less busy or you
can reject the requests.

Using API priority and fairness will not be very common in SaaS environments unless you are
allowing customers to run applications that interface with the Kubernetes API, for example,
a controller.

### Quality-of-Service (QoS) {#qos}

When you’re running a SaaS application, you may want the ability to offer different
Quality-of-Service (QoS) tiers of service to different tenants. For example, you may have freemium
service that comes with fewer performance guarantees and features and a for-fee service tier with
specific performance guarantees. Fortunately, there are several Kubernetes constructs that can
help you accomplish this within a shared cluster, including network QoS, storage classes, and pod
priority and preemption. The idea with each of these is to provide tenants with the quality of
service that they paid for. Let’s start by looking at networking QoS.

Typically, all pods on a node share a network interface. Without network QoS, some pods may
consume an unfair share of the available bandwidth at the expense of other pods.
The Kubernetes bandwidth plugin creates an
extended resource
for networking that allows you to use Kubernetes resources constructs, i.e. requests/limits, to
apply rate limits to pods by using Linux tc queues.
Be aware that the plugin is considered experimental as per the
Network Plugins
documentation and should be thoroughly tested before use in production environments.

For storage QoS, you will likely want to create different storage classes or profiles with
different performance characteristics. Each storage profile can be associated with a different
tier of service that is optimized for different workloads such IO, redundancy, or throughput.
Additional logic might be necessary to allow the tenant to associate the appropriate storage
profile with their workload.

Finally, there’s pod priority and preemption
where you can assign priority values to pods. When scheduling pods, the scheduler will try
evicting pods with lower priority when there are insufficient resources to schedule pods that are
assigned a higher priority. If you have a use case where tenants have different service tiers in a
shared cluster e.g. free and paid, you may want to give higher priority to certain tiers using
this feature.

### DNS

Kubernetes clusters include a Domain Name System (DNS) service to provide translations from names
to IP addresses, for all Services and Pods. By default, the Kubernetes DNS service allows lookups
across all namespaces in the cluster.

In multi-tenant environments where tenants can access pods and other Kubernetes resources, or where
stronger isolation is required, it may be necessary to prevent pods from looking up services in other
Namespaces.
You can restrict cross-namespace DNS lookups by configuring security rules for the DNS service.
For example, CoreDNS (the default DNS service for Kubernetes) can leverage Kubernetes metadata
to restrict queries to Pods and Services within a namespace. For more information, read an
example of
configuring this within the CoreDNS documentation.

When a Virtual Control Plane per tenant model is used, a DNS
service must be configured per tenant or a multi-tenant DNS service must be used.
Here is an example of a customized version of CoreDNS
that supports multiple tenants.

### Operators

Operators are Kubernetes controllers that manage
applications. Operators can simplify the management of multiple instances of an application, like
a database service, which makes them a common building block in the multi-consumer (SaaS)
multi-tenancy use case.

Operators used in a multi-tenant environment should follow a stricter set of guidelines.
Specifically, the Operator should:

* Support creating resources within different tenant namespaces, rather than just in the namespace
  in which the Operator is deployed.
* Ensure that the Pods are configured with resource requests and limits, to ensure scheduling and fairness.
* Support configuration of Pods for data-plane isolation techniques such as node isolation and
  sandboxed containers.
