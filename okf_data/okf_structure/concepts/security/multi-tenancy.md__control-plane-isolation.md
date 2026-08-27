---
id: okf-structure/concepts/security/multi-tenancy.md#control-plane-isolation
kind: section
title: Control plane isolation
source: concepts/security/multi-tenancy.md
url: https://kubernetes.io/docs/concepts/security/multi-tenancy/
heading: Control plane isolation
parent: okf-structure/concepts/security/multi-tenancy
children: []
prev_sibling: okf-structure/concepts/security/multi-tenancy.md#terminology
next_sibling: okf-structure/concepts/security/multi-tenancy.md#data-plane-isolation
word_count: 725
---

Control plane isolation ensures that different tenants cannot access or affect each others'
Kubernetes API resources.

### Namespaces

In Kubernetes, a Namespace provides a
mechanism for isolating groups of API resources within a single cluster. This isolation has two
key dimensions:

1. Object names within a namespace can overlap with names in other namespaces, similar to files in
   folders. This allows tenants to name their resources without having to consider what other
   tenants are doing.

2. Many Kubernetes security policies are scoped to namespaces. For example, RBAC Roles and Network
   Policies are namespace-scoped resources. Using RBAC, Users and Service Accounts can be
   restricted to a namespace.

In a multi-tenant environment, a Namespace helps segment a tenant's workload into a logical and
distinct management unit. In fact, a common practice is to isolate every workload in its own
namespace, even if multiple workloads are operated by the same tenant. This ensures that each
workload has its own identity and can be configured with an appropriate security policy.

The namespace isolation model requires configuration of several other Kubernetes resources,
networking plugins, and adherence to security best practices to properly isolate tenant workloads.
These considerations are discussed below.

### Access controls

The most important type of isolation for the control plane is authorization. If teams or their
workloads can access or modify each others' API resources, they can change or disable all other
types of policies thereby negating any protection those policies may offer. As a result, it is
critical to ensure that each tenant has the appropriate access to only the namespaces they need,
and no more. This is known as the "Principle of Least Privilege."

Role-based access control (RBAC) is commonly used to enforce authorization in the Kubernetes
control plane, for both users and workloads (service accounts).
Roles and
RoleBindings are
Kubernetes objects that are used at a namespace level to enforce access control in your
application; similar objects exist for authorizing access to cluster-level objects, though these
are less useful for multi-tenant clusters.

In a multi-team environment, RBAC must be used to restrict tenants' access to the appropriate
namespaces, and ensure that cluster-wide resources can only be accessed or modified by privileged
users such as cluster administrators.

If a policy ends up granting a user more permissions than they need, this is likely a signal that
the namespace containing the affected resources should be refactored into finer-grained
namespaces. Namespace management tools may simplify the management of these finer-grained
namespaces by applying common RBAC policies to different namespaces, while still allowing
fine-grained policies where necessary.

### Quotas

Kubernetes workloads consume node resources, like CPU and memory.  In a multi-tenant environment,
you can use Resource Quotas to manage resource usage of
tenant workloads.  For the multiple teams use case, where tenants have access to the Kubernetes
API, you can use resource quotas to limit the number of API resources (for example: the number of
Pods, or the number of ConfigMaps) that a tenant can create. Limits on object count ensure
fairness and aim to avoid _noisy neighbor_ issues from affecting other tenants that share a
control plane.

Resource quotas are namespaced objects. By mapping tenants to namespaces, cluster admins can use
quotas to ensure that a tenant cannot monopolize a cluster's resources or overwhelm its control
plane. Namespace management tools simplify the administration of quotas. In addition, while
Kubernetes quotas only apply within a single namespace, some namespace management tools allow
groups of namespaces to share quotas, giving administrators far more flexibility with less effort
than built-in quotas.

Quotas prevent a single tenant from consuming greater than their allocated share of resources
hence minimizing the “noisy neighbor” issue, where one tenant negatively impacts the performance
of other tenants' workloads.

When you apply a quota to namespace, Kubernetes requires you to also specify resource requests and
limits for each container. Limits are the upper bound for the amount of resources that a container
can consume. Containers that attempt to consume resources that exceed the configured limits will
either be throttled or killed, based on the resource type. When resource requests are set lower
than limits, each container is guaranteed the requested amount but there may still be some
potential for impact across workloads.

Quotas cannot protect against all kinds of resource sharing, such as network traffic.
Node isolation (described below) may be a better solution for this problem.
