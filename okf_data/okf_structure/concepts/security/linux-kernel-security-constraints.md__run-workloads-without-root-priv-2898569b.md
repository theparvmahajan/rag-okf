---
id: okf-structure/concepts/security/linux-kernel-security-constraints.md#run-workloads-without-root-privileges-run-without-root
kind: section
title: Run workloads without root privileges {#run-without-root}
source: concepts/security/linux-kernel-security-constraints.md
url: https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/
heading: Run workloads without root privileges {#run-without-root}
parent: okf-structure/concepts/security/linux-kernel-security-constraints
children: []
prev_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#introduction
next_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#security-features-in-the-linux-kernel-linux-security-features
word_count: 183
---

When you deploy a workload in Kubernetes, use the Pod specification to restrict
that workload from running as the root user on the node. You can use the Pod
`securityContext` to define the specific Linux user and group for the processes in
the Pod, and explicitly restrict containers from running as root users. Setting
these values in the Pod manifest takes precedence over similar values in the
container image, which is especially useful if you're running images that you
don't own.

Ensure that the user or group that you assign to the workload has the permissions
required for the application to function correctly. Changing the user or group
to one that doesn't have the correct permissions could lead to file access
issues or failed operations.

Configuring the kernel security features on this page provides fine-grained
control over the actions that processes in your cluster can take, but managing
these configurations can be challenging at scale. Running containers as
non-root, or in user namespaces if you need root privileges, helps to reduce the
chance that you'll need to enforce your configured kernel security capabilities.
