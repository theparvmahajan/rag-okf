---
id: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-the-capabilities-of-a-workload-or-user-at-runtime
kind: section
title: Controlling the capabilities of a workload or user at runtime
source: tasks/administer-cluster/securing-a-cluster.md
url: https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/
heading: Controlling the capabilities of a workload or user at runtime
parent: okf-structure/tasks/administer-cluster/securing-a-cluster
children: []
prev_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#controlling-access-to-the-kubelet
next_sibling: okf-structure/tasks/administer-cluster/securing-a-cluster.md#protecting-cluster-components-from-compromise
word_count: 816
---

Authorization in Kubernetes is intentionally high level, focused on coarse actions on resources.
More powerful controls exist as **policies** to limit by use case how those objects act on the
cluster, themselves, and other resources.

### Limiting resource usage on a cluster

Resource quota limits the number or capacity of
resources granted to a namespace. This is most often used to limit the amount of CPU, memory,
or persistent disk a namespace can allocate, but can also control how many pods, services, or
volumes exist in each namespace.

Limit ranges restrict the maximum or minimum size of some of the
resources above, to prevent users from requesting unreasonably high or low values for commonly
reserved resources like memory, or to provide default limits when none are specified.

### Controlling what privileges containers run with

A pod definition contains a security context
that allows it to request access to run as a specific Linux user on a node (like root),
access to run privileged or access the host network, and other controls that would otherwise
allow it to run unfettered on a hosting node.

You can configure Pod security admission
to enforce use of a particular Pod Security Standard
in a namespace, or to detect breaches.

Generally, most application workloads need limited access to host resources so they can
successfully run as a root process (uid 0) without access to host information. However,
considering the privileges associated with the root user, you should write application
containers to run as a non-root user. Similarly, administrators who wish to prevent
client applications from escaping their containers should apply the **Baseline**
or **Restricted** Pod Security Standard.

### Preventing containers from loading unwanted kernel modules

The Linux kernel automatically loads kernel modules from disk if needed in certain
circumstances, such as when a piece of hardware is attached or a filesystem is mounted. Of
particular relevance to Kubernetes, even unprivileged processes can cause certain
network-protocol-related kernel modules to be loaded, just by creating a socket of the
appropriate type. This may allow an attacker to exploit a security hole in a kernel module
that the administrator assumed was not in use.

To prevent specific modules from being automatically loaded, you can uninstall them from
the node, or add rules to block them. On most Linux distributions, you can do that by
creating a file such as `/etc/modprobe.d/kubernetes-blacklist.conf` with contents like:

```
# DCCP is unlikely to be needed, has had multiple serious
# vulnerabilities, and is not well-maintained.
blacklist dccp

# SCTP is not used in most Kubernetes clusters, and has also had
# vulnerabilities in the past.
blacklist sctp
```

To block module loading more generically, you can use a Linux Security Module (such as
SELinux) to completely deny the `module_request` permission to containers, preventing the
kernel from loading modules for containers under any circumstances. (Pods would still be
able to use modules that had been loaded manually, or modules that were loaded by the
kernel on behalf of some more-privileged process.)

### Restricting network access

The network policies for a namespace
allows application authors to restrict which pods in other namespaces may access pods and ports
within their namespaces. Many of the supported Kubernetes networking providers
now respect network policy.

Quota and limit ranges can also be used to control whether users may request node ports or
load-balanced services, which on many clusters can control whether those users applications
are visible outside of the cluster.

Additional protections may be available that control network rules on a per-plugin or per-
environment basis, such as per-node firewalls, physically separating cluster nodes to
prevent cross talk, or advanced networking policy.

### Restricting cloud metadata API access

Cloud platforms (AWS, Azure, GCE, etc.) often expose metadata services locally to instances.
By default these APIs are accessible by pods running on an instance and can contain cloud
credentials for that node, or provisioning data such as kubelet credentials. These credentials
can be used to escalate within the cluster or to other cloud services under the same account.

When running Kubernetes on a cloud platform, limit permissions given to instance credentials, use
network policies to restrict pod access
to the metadata API, and avoid using provisioning data to deliver secrets.

### Controlling which nodes pods may access

By default, there are no restrictions on which nodes may run a pod.  Kubernetes offers a
rich set of policies for controlling placement of pods onto nodes
and the taint-based pod placement and eviction
that are available to end users. For many clusters use of these policies to separate workloads
can be a convention that authors adopt or enforce via tooling.

As an administrator, a beta admission plugin `PodNodeSelector` can be used to force pods
within a namespace to default or require a specific node selector, and if end users cannot
alter namespaces, this can strongly limit the placement of all of the pods in a specific workload.
