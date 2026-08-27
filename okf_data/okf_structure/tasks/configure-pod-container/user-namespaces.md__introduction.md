---
id: okf-structure/tasks/configure-pod-container/user-namespaces.md#introduction
kind: section
title: Use a User Namespace With a Pod
source: tasks/configure-pod-container/user-namespaces.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/
heading: null
parent: okf-structure/tasks/configure-pod-container/user-namespaces
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/user-namespaces.md#prerequisites
word_count: 174
---

This page shows how to configure a user namespace for pods. This allows you to
isolate the user running inside the container from the one in the host.

A process running as root in a container can run as a different (non-root) user
in the host; in other words, the process has full privileges for operations
inside the user namespace, but is unprivileged for operations outside the
namespace.

You can use this feature to reduce the damage a compromised container can do to
the host or other pods in the same node. There are [several security
vulnerabilities][KEP-vulns] rated either **HIGH** or **CRITICAL** that were not
exploitable when user namespaces is active. It is expected user namespace will
mitigate some future vulnerabilities too.

Without using a user namespace a container running as root, in the case of a
container breakout, has root privileges on the node. And if some capability were
granted to the container, the capabilities are valid on the host too. None of
this is true when user namespaces are used.

[KEP-vulns]: https://github.com/kubernetes/enhancements/tree/217d790720c5aef09b8bd4d6ca96284a0affe6c2/keps/sig-node/127-user-namespaces#motivation
