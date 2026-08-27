---
id: okf-structure/concepts/security/secrets-good-practices.md#cluster-administrators
kind: section
title: Cluster administrators
source: concepts/security/secrets-good-practices.md
url: https://kubernetes.io/docs/concepts/security/secrets-good-practices/
heading: Cluster administrators
parent: okf-structure/concepts/security/secrets-good-practices
children: []
prev_sibling: okf-structure/concepts/security/secrets-good-practices.md#introduction
next_sibling: okf-structure/concepts/security/secrets-good-practices.md#good-practices-for-using-swap-memory
word_count: 408
---

This section provides good practices that cluster administrators can use to
improve the security of confidential information in the cluster.

### Configure encryption at rest

By default, Secret objects are stored unencrypted in etcd. You should configure encryption of your Secret
data in `etcd`. For instructions, refer to
Encrypt Secret Data at Rest.

### Configure least-privilege access to Secrets {#least-privilege-secrets}

When planning your access control mechanism, such as Kubernetes
Role-based Access Control (RBAC),
consider the following guidelines for access to `Secret` objects. You should
also follow the other guidelines in
RBAC good practices.

- **Components**: Restrict `watch` or `list` access to only the most
  privileged, system-level components. Only grant `get` access for Secrets if
  the component's normal behavior requires it.
- **Humans**: Restrict `get`, `watch`, or `list` access to Secrets. Only allow
  cluster administrators to access `etcd`. This includes read-only access. For
  more complex access control, such as restricting access to Secrets with
  specific annotations, consider using third-party authorization mechanisms.

Granting `list` access to Secrets implicitly lets the subject fetch the
contents of the Secrets.

A user who can create a Pod that uses a Secret can also see the value of that
Secret. Even if cluster policies do not allow a user to read the Secret
directly, the same user could have access to run a Pod that then exposes the
Secret. You can detect or limit the impact caused by Secret data being exposed,
either intentionally or unintentionally, by a user with this access. Some
recommendations include:

*  Use short-lived Secrets
*  Implement audit rules that alert on specific events, such as concurrent
   reading of multiple Secrets by a single user

#### Restrict Access for Secrets
Use separate namespaces to isolate access to mounted secrets.

### Improve etcd management policies

Consider wiping or shredding the durable storage used by `etcd` once it is
no longer in use.

If there are multiple `etcd` instances, configure encrypted SSL/TLS
communication between the instances to protect the Secret data in transit.

### Configure access to external Secrets

You can use third-party Secrets store providers to keep your confidential data
outside your cluster and then configure Pods to access that information.
The Kubernetes Secrets Store CSI Driver
is a DaemonSet that lets the kubelet retrieve Secrets from external stores, and
mount the Secrets as a volume into specific Pods that you authorize to access
the data.

For a list of supported providers, refer to
Providers for the Secret Store CSI Driver.
