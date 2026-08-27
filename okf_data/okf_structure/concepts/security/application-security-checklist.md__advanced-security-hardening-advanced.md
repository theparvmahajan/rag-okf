---
id: okf-structure/concepts/security/application-security-checklist.md#advanced-security-hardening-advanced
kind: section
title: Advanced security hardening {#advanced}
source: concepts/security/application-security-checklist.md
url: https://kubernetes.io/docs/concepts/security/application-security-checklist/
heading: Advanced security hardening {#advanced}
parent: okf-structure/concepts/security/application-security-checklist
children: []
prev_sibling: okf-structure/concepts/security/application-security-checklist.md#base-security-hardening
next_sibling: null
word_count: 139
---

This section of this guide covers some advanced security hardening points
which might be valuable based on different Kubernetes environment setup.

### Linux container security

Configure Security Context
for the pod-container.

- [ ] Set the Seccomp Profile for a Container.
- [ ] Restrict a Container's Access to Resources with AppArmor.
- [ ] Assign SELinux Labels to a Container.

### Runtime classes

- [ ] Configure appropriate runtime classes for containers.

Some containers may require a different isolation level from what is provided by
the default runtime of the cluster. `runtimeClassName` can be used in a podspec
to define a different runtime class.

For sensitive workloads consider using kernel emulation tools like
gVisor, or virtualized isolation using a mechanism
such as kata-containers.

In high trust environments, consider using
confidential virtual machines
to improve cluster security even further.
