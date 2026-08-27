---
id: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#introduction
kind: section
title: Running Kubernetes Node Components as a Non-root User
source: tasks/administer-cluster/kubelet-in-userns.md
url: https://kubernetes.io/docs/tasks/administer-cluster/kubelet-in-userns/
heading: null
parent: okf-structure/tasks/administer-cluster/kubelet-in-userns
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/administer-cluster/kubelet-in-userns.md#prerequisites
word_count: 65
---

This document describes how to run Kubernetes Node components such as kubelet, CRI, OCI, and CNI
without root privileges, by using a user namespace.

This technique is also known as _rootless mode_.

This document describes how to run Kubernetes Node components (and hence pods) as a non-root user.

If you are just looking for how to run a pod as a non-root user, see SecurityContext.
