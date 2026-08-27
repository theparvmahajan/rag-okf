---
id: okf-structure/concepts/security/windows-security.md#pod-level-security-isolation
kind: section
title: Pod-level security isolation
source: concepts/security/windows-security.md
url: https://kubernetes.io/docs/concepts/security/windows-security/
heading: Pod-level security isolation
parent: okf-structure/concepts/security/windows-security
children: []
prev_sibling: okf-structure/concepts/security/windows-security.md#container-users
next_sibling: null
word_count: 47
---

Linux-specific pod security context mechanisms (such as SELinux, AppArmor, Seccomp, or custom
POSIX capabilities) are not supported on Windows nodes.

Privileged containers are not supported
on Windows.
Instead HostProcess containers
can be used on Windows to perform many of the tasks performed by privileged containers on Linux.
