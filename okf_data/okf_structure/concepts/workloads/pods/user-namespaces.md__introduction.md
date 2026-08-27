---
id: okf-structure/concepts/workloads/pods/user-namespaces.md#introduction
kind: section
title: User Namespaces
source: concepts/workloads/pods/user-namespaces.md
url: https://kubernetes.io/docs/concepts/workloads/pods/user-namespaces/
heading: null
parent: okf-structure/concepts/workloads/pods/user-namespaces
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/user-namespaces.md#prerequisites
word_count: 123
---

This page explains how user namespaces are used in Kubernetes pods. A user
namespace isolates the user running inside the container from the one
in the host.

A process running as root in a container can run as a different (non-root) user
in the host; in other words, the process has full privileges for operations
inside the user namespace, but is unprivileged for operations outside the
namespace.

You can use this feature to reduce the damage a compromised container can do to
the host or other pods in the same node. There are [several security
vulnerabilities][KEP-vulns] rated either **HIGH** or **CRITICAL** that were not
exploitable when user namespaces is active. It is expected user namespace will
mitigate some future vulnerabilities too.

[KEP-vulns]: https://github.com/kubernetes/enhancements/tree/217d790720c5aef09b8bd4d6ca96284a0affe6c2/keps/sig-node/127-user-namespaces#motivation
