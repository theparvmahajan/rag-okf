---
id: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-access-to-the-kubernetes-api
kind: section
title: Controlling access to the Kubernetes API
source: tasks/administer-cluster/securing-a-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/
heading: Controlling access to the Kubernetes API
parent: okf-structure/tasks/administer-cluster/securing-a-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-access-to-the-kubelet
word_count: 522
---

As Kubernetes is entirely API-driven, controlling and limiting who can access the cluster and what actions
they are allowed to perform is the first line of defense.

### Use Transport Layer Security (TLS) for all API traffic

Kubernetes expects that all API communication in the cluster is encrypted by default with TLS, and the
majority of installation methods will allow the necessary certificates to be created and distributed to
the cluster components. Note that some components and installation methods may enable local ports over
HTTP and administrators should familiarize themselves with the settings of each component to identify
potentially unsecured traffic.

### API Authentication

Choose an authentication mechanism for the API servers to use that matches the common access patterns
when you install a cluster. For instance, small, single-user clusters may wish to use a simple certificate
or static Bearer token approach. Larger clusters may wish to integrate an existing OIDC or LDAP server that
allow users to be subdivided into groups.

All API clients must be authenticated, even those that are part of the infrastructure like nodes,
proxies, the scheduler, and volume plugins. These clients are typically service accounts or use x509 client certificates, and they are created automatically at cluster startup or are setup as part of the cluster installation.

Consult the authentication reference document for more information.

### API Authorization

Once authenticated, every API call is also expected to pass an authorization check. Kubernetes ships
an integrated Role-Based Access Control (RBAC) component that matches an incoming user or group to a
set of permissions bundled into roles. These permissions combine verbs (get, create, delete) with
resources (pods, services, nodes) and can be namespace-scoped or cluster-scoped. A set of out-of-the-box
roles are provided that offer reasonable default separation of responsibility depending on what
actions a client might want to perform. It is recommended that you use the
Node and
RBAC authorizers together, in combination with the
NodeRestriction admission plugin.

As with authentication, simple and broad roles may be appropriate for smaller clusters, but as
more users interact with the cluster, it may become necessary to separate teams into separate
namespaces with more limited roles.

With authorization, it is important to understand how updates on one object may cause actions in
other places. For instance, a user may not be able to create pods directly, but allowing them to
create a deployment, which creates pods on their behalf, will let them create those pods
indirectly. Likewise, deleting a node from the API will result in the pods scheduled to that node
being terminated and recreated on other nodes. The out-of-the box roles represent a balance
between flexibility and common use cases, but more limited roles should be carefully reviewed
to prevent accidental escalation. You can make roles specific to your use case if the out-of-box ones don't meet your needs.

Consult the authorization reference section for more information.

If your cluster uses Dynamic Resource Allocation (DRA),
review DRA synthetic subresource authorization (`resourceclaims/binding` and
`resourceclaims/driver`) and grant only the minimum required verbs to each
component. For details, see
Hardening Guide - Dynamic Resource Allocation
and
Harden Dynamic Resource Allocation in Your Cluster.
