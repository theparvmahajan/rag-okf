---
id: okf-structure/concepts/security/multi-tenancy.md#implementations
kind: section
title: Implementations
source: concepts/security/multi-tenancy.md
url: https://kubernetes.io/docs/concepts/security/multi-tenancy/
heading: Implementations
parent: okf-structure/concepts/security/multi-tenancy
children: []
prev_sibling: okf-structure/concepts/security/multi-tenancy.md#additional-considerations
next_sibling: null
word_count: 731
---

There are two primary ways to share a Kubernetes cluster for multi-tenancy: using Namespaces
(that is, a Namespace per tenant) or by virtualizing the control plane (that is, virtual control
plane per tenant).

In both cases, data plane isolation, and management of additional considerations such as API
Priority and Fairness, is also recommended.

Namespace isolation is well-supported by Kubernetes, has a negligible resource cost, and provides
mechanisms to allow tenants to interact appropriately, such as by allowing service-to-service
communication. However, it can be difficult to configure, and doesn't apply to Kubernetes
resources that can't be namespaced, such as Custom Resource Definitions, Storage Classes, and Webhooks.

Control plane virtualization allows for isolation of non-namespaced resources at the cost of
somewhat higher resource usage and more difficult cross-tenant sharing. It is a good option when
namespace isolation is insufficient but dedicated clusters are undesirable, due to the high cost
of maintaining them (especially on-prem) or due to their higher overhead and lack of resource
sharing. However, even within a virtualized control plane, you will likely see benefits by using
namespaces as well.

The two options are discussed in more detail in the following sections.

### Namespace per tenant

As previously mentioned, you should consider isolating each workload in its own namespace, even if
you are using dedicated clusters or virtualized control planes. This ensures that each workload
only has access to its own resources, such as ConfigMaps and Secrets, and allows you to tailor
dedicated security policies for each workload. In addition, it is a best practice to give each
namespace names that are unique across your entire fleet (that is, even if they are in separate
clusters), as this gives you the flexibility to switch between dedicated and shared clusters in
the future, or to use multi-cluster tooling such as service meshes.

Conversely, there are also advantages to assigning namespaces at the tenant level, not just the
workload level, since there are often policies that apply to all workloads owned by a single
tenant. However, this raises its own problems. Firstly, this makes it difficult or impossible to
customize policies to individual workloads, and secondly, it may be challenging to come up with a
single level of "tenancy" that should be given a namespace. For example, an organization may have
divisions, teams, and subteams - which should be assigned a namespace?

One possible approach is to organize your namespaces into hierarchies, and share certain policies and
resources between them. This could include managing namespace labels, namespace lifecycles,
delegated access, and shared resource quotas across related namespaces. These capabilities can
be useful in both multi-team and multi-customer scenarios.

### Virtual control plane per tenant

Another form of control-plane isolation is to use Kubernetes extensions to provide each tenant a
virtual control-plane that enables segmentation of cluster-wide API resources.
Data plane isolation techniques can be used with this model to securely
manage worker nodes across tenants.

The virtual control plane based multi-tenancy model extends namespace-based multi-tenancy by
providing each tenant with dedicated control plane components, and hence complete control over
cluster-wide resources and add-on services. Worker nodes are shared across all tenants, and are
managed by a Kubernetes cluster that is normally inaccessible to tenants.
This cluster is often referred to as a _super-cluster_ (or sometimes as a _host-cluster_).
Since a tenant’s control-plane is not directly associated with underlying compute resources it is
referred to as a _virtual control plane_.

A virtual control plane typically consists of the Kubernetes API server, the controller manager,
and the etcd data store. It interacts with the super cluster via a metadata synchronization
controller which coordinates changes across tenant control planes and the control plane of the
super-cluster.

By using per-tenant dedicated control planes, most of the isolation problems due to sharing one
API server among all tenants are solved. Examples include noisy neighbors in the control plane,
uncontrollable blast radius of policy misconfigurations, and conflicts between cluster scope
objects such as webhooks and CRDs.  Hence, the virtual control plane model is particularly
suitable for cases where each tenant requires access to a Kubernetes API server and expects the
full cluster manageability.

The improved isolation comes at the  cost of running and maintaining an individual virtual control
plane per tenant. In addition, per-tenant control planes do not solve isolation problems in the
data plane, such as node-level noisy neighbors or security threats. These must still be addressed
separately.
