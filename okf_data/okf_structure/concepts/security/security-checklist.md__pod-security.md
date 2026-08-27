---
id: okf-structure/concepts/security/security-checklist.md#pod-security
kind: section
title: Pod security
source: concepts/security/security-checklist.md
url: https://kubernetes.io/docs/concepts/security/security-checklist/
heading: Pod security
parent: okf-structure/concepts/security/security-checklist
children: []
prev_sibling: okf-structure/concepts/security/security-checklist.md#network-security
next_sibling: okf-structure/concepts/security/security-checklist.md#logs-and-auditing
word_count: 712
---

- [ ] RBAC rights to `create`, `update`, `patch`, `delete` workloads is only granted if necessary.
- [ ] Appropriate Pod Security Standards policy is applied for all namespaces and enforced.
- [ ] Memory limit is set for the workloads with a limit equal or inferior to the request.
- [ ] CPU limit might be set on sensitive workloads.
- [ ] For nodes that support it, Seccomp is enabled with appropriate syscalls
  profile for programs.
- [ ] For nodes that support it, AppArmor or SELinux is enabled with appropriate
  profile for programs.

RBAC authorization is crucial but
cannot be granular enough to have authorization on the Pods' resources
(or on any resource that manages Pods). The only granularity is the API verbs
on the resource itself, for example, `create` on Pods. Without
additional admission, the authorization to create these resources allows direct
unrestricted access to the schedulable nodes of a cluster.

The Pod Security Standards
define three different policies, privileged, baseline and restricted that limit
how fields can be set in the `PodSpec` regarding security.
These standards can be enforced at the namespace level with the new
Pod Security admission,
enabled by default, or by third-party admission webhook. Please note that,
contrary to the removed PodSecurityPolicy admission it replaces,
Pod Security
admission can be easily combined with admission webhooks and external services.

Pod Security admission `restricted` policy, the most restrictive policy of the
Pod Security Standards set,
can operate in several modes,
`warn`, `audit` or `enforce` to gradually apply the most appropriate
security context
according to security best practices. Nevertheless, pods'
security context
should be separately investigated to limit the privileges and access pods may
have on top of the predefined security standards, for specific use cases.

For a hands-on tutorial on Pod Security,
see the blog post
Kubernetes 1.23: Pod Security Graduates to Beta.

Memory and CPU limits
should be set in order to restrict the memory and CPU resources a pod can
consume on a node, and therefore prevent potential DoS attacks from malicious or
breached workloads. Such policy can be enforced by an admission controller.
Please note that CPU limits will throttle usage and thus can have unintended
effects on auto-scaling features or efficiency i.e. running the process in best
effort with the CPU resource available.

Memory limit superior to request can expose the whole node to OOM issues.

### Enabling Seccomp

Seccomp stands for secure computing mode and has been a feature of the Linux kernel since version 2.6.12.
It can be used to sandbox the privileges of a process, restricting the calls it is able to make
from userspace into the kernel. Kubernetes lets you automatically apply seccomp profiles loaded onto
a node to your Pods and containers.

Seccomp can improve the security of your workloads by reducing the Linux kernel syscall attack
surface available inside containers. The seccomp filter mode leverages BPF to create an allow or
deny list of specific syscalls, named profiles.

Since Kubernetes 1.27, you can enable the use of `RuntimeDefault` as the default seccomp profile
for all workloads. A security tutorial is available on this
topic. In addition, the
Kubernetes Security Profiles Operator
is a project that facilitates the management and use of seccomp in clusters.

Seccomp is only available on Linux nodes.

### Enabling AppArmor or SELinux

#### AppArmor

AppArmor is a Linux kernel security module that can
provide an easy way to implement Mandatory Access Control (MAC) and better
auditing through system logs. A default AppArmor profile is enforced on nodes that support it, or a custom profile can be configured.
Like seccomp, AppArmor is also configured
through profiles, where each profile is either running in enforcing mode, which
blocks access to disallowed resources or complain mode, which only reports
violations. AppArmor profiles are enforced on a per-container basis, with an
annotation, allowing for processes to gain just the right privileges.

AppArmor is only available on Linux nodes, and enabled in
some Linux distributions.

#### SELinux

SELinux is also a
Linux kernel security module that can provide a mechanism for supporting access
control security policies, including Mandatory Access Controls (MAC). SELinux
labels can be assigned to containers or pods
via their `securityContext` section.

SELinux is only available on Linux nodes, and enabled in
some Linux distributions.
