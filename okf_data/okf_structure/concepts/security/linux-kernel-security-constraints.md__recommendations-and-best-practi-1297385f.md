---
id: okf-structure/concepts/security/linux-kernel-security-constraints.md#recommendations-and-best-practices-recommendations-best-practices
kind: section
title: Recommendations and best practices {#recommendations-best-practices}
source: concepts/security/linux-kernel-security-constraints.md
url: https://kubernetes.io/docs/concepts/security/linux-kernel-security-constraints/
heading: Recommendations and best practices {#recommendations-best-practices}
parent: okf-structure/concepts/security/linux-kernel-security-constraints
children: []
prev_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#kernel-level-security-features-and-privileged-containers-kernel-security-features-privileged-containers
next_sibling: okf-structure/concepts/security/linux-kernel-security-constraints.md#whatsnext
word_count: 112
---

* Before configuring kernel-level security capabilities, you should consider
  implementing network-level isolation. For more information, read the
  Security Checklist.
* Unless necessary, run Linux workloads as non-root by setting specific user and
  group IDs in your Pod manifest and by specifying `runAsNonRoot: true`.

Additionally, you can run workloads in user namespaces by setting
`hostUsers: false` in your Pod manifest. This lets you run containers as root
users in the user namespace, but as non-root users in the host namespace on the
node. This is still in early stages of development and might not have the level
of support that you need. For instructions, refer to
Use a User Namespace With a Pod.
