---
id: okf-structure/concepts/security/pod-security-standards.md#pod-os-field
kind: section
title: Pod OS field
source: concepts/security/pod-security-standards.md
url: https://kubernetes.io/docs/concepts/security/pod-security-standards/
heading: Pod OS field
parent: okf-structure/concepts/security/pod-security-standards
children: []
prev_sibling: okf-structure/concepts/security/pod-security-standards.md#policy-instantiation
next_sibling: okf-structure/concepts/security/pod-security-standards.md#user-namespaces
word_count: 149
---

Kubernetes lets you use nodes that run either Linux or Windows. You can mix both kinds of
node in one cluster.
Windows in Kubernetes has some limitations and differentiators from Linux-based
workloads. Specifically, many of the Pod `securityContext` fields
have no effect on Windows.

Kubelets prior to v1.24 don't enforce the pod OS field, and if a cluster has nodes on versions earlier than v1.24 the Restricted policies should be pinned to a version prior to v1.25.

### Restricted Pod Security Standard changes
Another important change, made in Kubernetes v1.25 is that the  _Restricted_ policy
has been updated to use the `pod.spec.os.name` field. Based on the OS name, certain policies that are specific
to a particular OS can be relaxed for the other OS.

#### OS-specific policy controls
Restrictions on the following controls are only required if `.spec.os.name` is not `windows`:
- Privilege Escalation
- Seccomp
- Linux Capabilities
