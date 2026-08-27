---
id: okf-structure/concepts/security/service-accounts.md#what-are-service-accounts-what-are-service-accounts
kind: section
title: What are service accounts? {#what-are-service-accounts}
source: concepts/security/service-accounts.md
url: https://kubernetes.io/docs/concepts/security/service-accounts/
heading: What are service accounts? {#what-are-service-accounts}
parent: okf-structure/concepts/security/service-accounts
children: []
prev_sibling: okf-structure/concepts/security/service-accounts.md#introduction
next_sibling: okf-structure/concepts/security/service-accounts.md#use-cases-for-kubernetes-service-accounts-use-cases
word_count: 376
---

A service account is a type of non-human account that, in Kubernetes, provides
a distinct identity in a Kubernetes cluster. Application Pods, system
components, and entities inside and outside the cluster can use a specific
ServiceAccount's credentials to identify as that ServiceAccount. This identity
is useful in various situations, including authenticating to the API server or
implementing identity-based security policies.

Service accounts exist as ServiceAccount objects in the API server. Service
accounts have the following properties:

* **Namespaced:** Each service account is bound to a Kubernetes
  namespace. Every namespace
  gets a `default` ServiceAccount upon creation.

* **Lightweight:** Service accounts exist in the cluster and are
  defined in the Kubernetes API. You can quickly create service accounts to
  enable specific tasks.

* **Portable:** A configuration bundle for a complex containerized workload
  might include service account definitions for the system's components. The
  lightweight nature of service accounts and the namespaced identities make
  the configurations portable.

Service accounts are different from user accounts, which are authenticated
human users in the cluster. By default, user accounts don't exist in the Kubernetes
API server; instead, the API server treats user identities as opaque
data. You can authenticate as a user account using multiple methods. Some
Kubernetes distributions might add custom extension APIs to represent user
accounts in the API server.

| Description | ServiceAccount | User or group |
| --- | --- | --- |
| Location | Kubernetes API (ServiceAccount object) | External |
| Access control | Kubernetes RBAC or other authorization mechanisms | Kubernetes RBAC or other identity and access management mechanisms |
| Intended use | Workloads, automation | People |

### Default service accounts {#default-service-accounts}

When you create a cluster, Kubernetes automatically creates a ServiceAccount
object named `default` for every namespace in your cluster. The `default`
service accounts in each namespace get no permissions by default other than the
default API discovery permissions
that Kubernetes grants to all authenticated principals if role-based access control (RBAC) is enabled.
If you delete the `default` ServiceAccount object in a namespace, the
control plane
replaces it with a new one.

If you deploy a Pod in a namespace, and you don't
manually assign a ServiceAccount to the Pod, Kubernetes
assigns the `default` ServiceAccount for that namespace to the Pod.
