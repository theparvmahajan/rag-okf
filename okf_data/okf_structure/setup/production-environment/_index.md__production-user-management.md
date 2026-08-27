---
id: okf-structure/setup/production-environment/_index.md#production-user-management
kind: section
title: Production user management
source: setup/production-environment/_index.md
url: https://kubernetes.io/docs/setup/production-environment/
heading: Production user management
parent: okf-structure/setup/production-environment/_index
children: []
prev_sibling: okf-structure/setup/production-environment/_index.md#production-cluster-setup
next_sibling: okf-structure/setup/production-environment/_index.md#set-limits-on-workload-resources
word_count: 523
---

In production, you may be moving from a model where you or a small group of
people are accessing the cluster to where there may potentially be dozens or
hundreds of people. In a learning environment or platform prototype, you might have a single
administrative account for everything you do. In production, you will want
more accounts with different levels of access to different namespaces.

Taking on a production-quality cluster means deciding how you
want to selectively allow access by other users. In particular, you need to
select strategies for validating the identities of those who try to access your
cluster (authentication) and deciding if they have permissions to do what they
are asking (authorization):

- *Authentication*: The apiserver can authenticate users using client
  certificates, bearer tokens, an authenticating proxy, or HTTP basic auth.
  You can choose which authentication methods you want to use.
  Using plugins, the apiserver can leverage your organization’s existing
  authentication methods, such as LDAP or Kerberos. See
  Authentication
  for a description of these different methods of authenticating Kubernetes users.
- *Authorization*: When you set out to authorize your regular users, you will probably choose
  between RBAC and ABAC authorization. See Authorization Overview
  to review different modes for authorizing user accounts (as well as service account access to
  your cluster):
  - *Role-based access control* (RBAC): Lets you
    assign access to your cluster by allowing specific sets of permissions to authenticated users.
    Permissions can be assigned for a specific namespace (Role) or across the entire cluster
    (ClusterRole). Then using RoleBindings and ClusterRoleBindings, those permissions can be attached
    to particular users.
  - *Attribute-based access control* (ABAC): Lets you
    create policies based on resource attributes in the cluster and will allow or deny access
    based on those attributes. Each line of a policy file identifies versioning properties (apiVersion
    and kind) and a map of spec properties to match the subject (user or group), resource property,
    non-resource property (/version or /apis), and readonly. See
    Examples for details.

As someone setting up authentication and authorization on your production Kubernetes cluster, here are some things to consider:

- *Set the authorization mode*: When the Kubernetes API server
  (kube-apiserver)
  starts, supported authorization modes must be set using an *--authorization-config* file or the *--authorization-mode*
  flag. For example, that flag in the *kube-adminserver.yaml* file (in */etc/kubernetes/manifests*)
  could be set to Node,RBAC. This would allow Node and RBAC authorization for authenticated requests.
- *Create user certificates and role bindings (RBAC)*: If you are using RBAC
  authorization, users can create a CertificateSigningRequest (CSR) that can be
  signed by the cluster CA. Then you can bind Roles and ClusterRoles to each user.
  See Certificate Signing Requests
  for details.
- *Create policies that combine attributes (ABAC)*: If you are using ABAC
  authorization, you can assign combinations of attributes to form policies to
  authorize selected users or groups to access particular resources (such as a
  pod), namespace, or apiGroup. For more information, see
  Examples.
- *Consider Admission Controllers*: Additional forms of authorization for
  requests that can come in through the API server include
  Webhook Token Authentication.
  Webhooks and other special authorization types need to be enabled by adding
  Admission Controllers
  to the API server.
