---
id: okf-structure/concepts/security/linux-kernel-security-constraints.md#kernel-level-security-features-and-privileged-containers-kernel-security-features-privileged-containers
kind: section
title: Kernel-level security features and privileged containers {#kernel-security-features-privileged-containers}
source: concepts/security/linux-kernel-security-constraints.md
url: https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/
heading: Kernel-level security features and privileged containers {#kernel-security-features-privileged-containers}
parent: okf-structure/concepts/security/linux-kernel-security-constraints
children: []
prev_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#security-features-in-the-linux-kernel-linux-security-features
next_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#recommendations-and-best-practices-recommendations-best-practices
word_count: 295
---

Kubernetes lets you specify that some trusted containers can run in
*privileged* mode. Any container in a Pod can run in privileged mode to use
operating system administrative capabilities that would otherwise be
inaccessible. This is available for both Windows and Linux.

Privileged containers explicitly override some of the Linux kernel constraints
that you might use in your workloads, as follows:

* **seccomp**: Privileged containers run as the `Unconfined` seccomp profile,
  overriding any seccomp profile that you specified in your manifest.
* **AppArmor**: Privileged containers ignore any applied AppArmor profiles.
* **SELinux**: Privileged containers run as the `unconfined_t` domain.

### Privileged containers {#privileged-containers}

Any container in a Pod can enable *Privileged mode* if you set the
`privileged: true` field in the
`securityContext`
field for the container. Privileged containers override or undo many other hardening settings such as the applied seccomp profile, AppArmor profile, or
SELinux constraints. Privileged containers are given all Linux capabilities,
including capabilities that they don't require. For example, a root user in a
privileged container might be able to use the `CAP_SYS_ADMIN` and
`CAP_NET_ADMIN` capabilities on the node, bypassing the runtime seccomp
configuration and other restrictions.

In most cases, you should avoid using privileged containers, and instead grant
the specific capabilities required by your container using the `capabilities`
field in the `securityContext` field. Only use privileged mode if you have a
capability that you can't grant with the securityContext. This is useful for
containers that want to use operating system administrative capabilities such
as manipulating the network stack or accessing hardware devices.

In Kubernetes version 1.26 and later, you can also run Windows containers in a
similarly privileged mode by setting the `windowsOptions.hostProcess` flag on
the security context of the Pod spec. For details and instructions, see
Create a Windows HostProcess Pod.
