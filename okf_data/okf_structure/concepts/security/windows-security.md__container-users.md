---
id: okf-structure/concepts/security/windows-security.md#container-users
kind: section
title: Container users
source: concepts/security/windows-security.md
url: https://kubernetes.io/docs/concepts/security/windows-security/
heading: Container users
parent: okf-structure/concepts/security/windows-security
children: []
prev_sibling: okf-structure/concepts/security/windows-security.md#protection-for-secret-data-on-nodes
next_sibling: okf-structure/concepts/security/windows-security.md#pod-level-security-isolation
word_count: 105
---

RunAsUsername
can be specified for Windows Pods or containers to execute the container
processes as specific user. This is roughly equivalent to
RunAsUser.

Windows containers offer two default user accounts, ContainerUser and ContainerAdministrator.
The differences between these two user accounts are covered in
When to use ContainerAdmin and ContainerUser user accounts
within Microsoft's _Secure Windows containers_ documentation.

Local users can be added to container images during the container build process.

* Nano Server based images run as
  `ContainerUser` by default
* Server Core based images run as
  `ContainerAdministrator` by default

Windows containers can also run as Active Directory identities by utilizing
Group Managed Service Accounts
