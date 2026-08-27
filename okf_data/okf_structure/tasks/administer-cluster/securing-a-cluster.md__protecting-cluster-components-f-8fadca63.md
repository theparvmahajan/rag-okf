---
id: okf-structure/tasks/administer-cluster/securing-a-cluster.md#protecting-cluster-components-from-compromise
kind: section
title: Protecting cluster components from compromise
source: tasks/administer-cluster/securing-a-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/
heading: Protecting cluster components from compromise
parent: okf-structure/tasks/administer-cluster/securing-a-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-the-capabilities-of-a-workload-or-user-at-runtime
next_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#what-s-next
word_count: 691
---

This section describes some common patterns for protecting clusters from compromise.

### Restrict access to etcd

Write access to the etcd backend for the API is equivalent to gaining root on the entire cluster,
and read access can be used to escalate fairly quickly. Administrators should always use strong
credentials from the API servers to their etcd server, such as mutual auth via TLS client certificates,
and it is often recommended to isolate the etcd servers behind a firewall that only the API servers
may access.

Allowing other components within the cluster to access the master etcd instance with
read or write access to the full keyspace is equivalent to granting cluster-admin access. Using
separate etcd instances for non-master components or using etcd ACLs to restrict read and write
access to a subset of the keyspace is strongly recommended.

### Enable audit logging

The audit logger is a beta feature that records actions taken by the
API for later analysis in the event of a compromise. It is recommended to enable audit logging
and archive the audit file on a secure server.

### Restrict access to alpha or beta features

Alpha and beta Kubernetes features are in active development and may have limitations or bugs
that result in security vulnerabilities. Always assess the value an alpha or beta feature may
provide against the possible risk to your security posture. When in doubt, disable features you
do not use.

### Rotate infrastructure credentials frequently

The shorter the lifetime of a secret or credential the harder it is for an attacker to make
use of that credential. Set short lifetimes on certificates and automate their rotation. Use
an authentication provider that can control how long issued tokens are available and use short
lifetimes where possible. If you use service-account tokens in external integrations, plan to
rotate those tokens frequently. For example, once the bootstrap phase is complete, a bootstrap
token used for setting up nodes should be revoked or its authorization removed.

### Review third party integrations before enabling them

Many third party integrations to Kubernetes may alter the security profile of your cluster. When
enabling an integration, always review the permissions that an extension requests before granting
it access. For example, many security integrations may request access to view all secrets on
your cluster which is effectively making that component a cluster admin. When in doubt,
restrict the integration to functioning in a single namespace if possible.

Components that create pods may also be unexpectedly powerful if they can do so inside namespaces
like the `kube-system` namespace, because those pods can gain access to service account secrets
or run with elevated permissions if those service accounts are granted access to permissive
PodSecurityPolicies.

If you use Pod Security admission and allow
any component to create Pods within a namespace that permits privileged Pods, those Pods may
be able to escape their containers and use this widened access to elevate their privileges.

You should not allow untrusted components to create Pods in any system namespace (those with
names that start with `kube-`) nor in any namespace where that access grant allows the possibility
of privilege escalation.

### Encrypt secrets at rest

In general, the etcd database will contain any information accessible via the Kubernetes API
and may grant an attacker significant visibility into the state of your cluster. Always encrypt
your backups using a well reviewed backup and encryption solution, and consider using full disk
encryption where possible.

Kubernetes supports optional encryption at rest for information in the Kubernetes API.
This lets you ensure that when Kubernetes stores data for objects (for example, `Secret` or
`ConfigMap` objects), the API server writes an encrypted representation of the object.
That encryption means that even someone who has access to etcd backup data is unable
to view the content of those objects.
In Kubernetes  you can also encrypt custom resources;
encryption-at-rest for extension APIs defined in CustomResourceDefinitions was added to
Kubernetes as part of the v1.26 release.

### Receiving alerts for security updates and reporting vulnerabilities

Join the kubernetes-announce
group for emails about security announcements. See the
security reporting
page for more on how to report vulnerabilities.
