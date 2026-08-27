---
id: okf-structure/concepts/storage/projected-volumes.md#securitycontext-interactions
kind: section
title: SecurityContext interactions
source: concepts/storage/projected-volumes.md
url: https://kubernetes.io/docs/concepts/storage/projected-volumes/
heading: SecurityContext interactions
parent: okf-structure/concepts/storage/projected-volumes
children: []
prev_sibling: okf-structure/concepts/storage/projected-volumes.md#podcertificate-projected-volumes-podcertificate
next_sibling: null
word_count: 438
---

The proposal
for file permission handling in projected service account volume enhancement
introduced the projected files having the correct owner permissions set.

### Linux

In Linux pods that have a projected volume and `RunAsUser` set in the Pod
`SecurityContext`,
the projected files have the correct ownership set including container user
ownership.

When all containers in a pod have the same `runAsUser` set in their
`PodSecurityContext`
or container
`SecurityContext`,
then the kubelet ensures that the contents of the `serviceAccountToken` volume are owned by that user,
and the token file has its permission mode set to `0600`.

Ephemeral containers
added to a Pod after it is created do *not* change volume permissions that were
set when the pod was created.

If a Pod's `serviceAccountToken` volume permissions were set to `0600` because
all other containers in the Pod have the same `runAsUser`, ephemeral
containers must use the same `runAsUser` to be able to read the token.

### Windows

In Windows pods that have a projected volume and `RunAsUsername` set in the
Pod `SecurityContext`, the ownership is not enforced due to the way user
accounts are managed in Windows. Windows stores and manages local user and group
accounts in a database file called Security Account Manager (SAM). Each
container maintains its own instance of the SAM database, to which the host has
no visibility into while the container is running. Windows containers are
designed to run the user mode portion of the OS in isolation from the host,
hence the maintenance of a virtual SAM database. As a result, the kubelet running
on the host does not have the ability to dynamically configure host file
ownership for virtualized container accounts. It is recommended that if files on
the host machine are to be shared with the container then they should be placed
into their own volume mount outside of `C:\`.

By default, the projected files will have the following ownership as shown for
an example projected volume file:

```powershell
PS C:\> Get-Acl C:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crt | Format-List

Path   : Microsoft.PowerShell.Core\FileSystem::C:\var\run\secrets\kubernetes.io\serviceaccount\..2021_08_31_22_22_18.318230061\ca.crt
Owner  : BUILTIN\Administrators
Group  : NT AUTHORITY\SYSTEM
Access : NT AUTHORITY\SYSTEM Allow  FullControl
         BUILTIN\Administrators Allow  FullControl
         BUILTIN\Users Allow  ReadAndExecute, Synchronize
Audit  :
Sddl   : O:BAG:SYD:AI(A;ID;FA;;;SY)(A;ID;FA;;;BA)(A;ID;0x1200a9;;;BU)
```

This implies all administrator users like `ContainerAdministrator` will have
read, write and execute access while, non-administrator users will have read and
execute access.

In general, granting the container access to the host is discouraged as it can
open the door for potential security exploits.

Creating a Windows Pod with `RunAsUser` in it's `SecurityContext` will result in
the Pod being stuck at `ContainerCreating` forever. So it is advised to not use
the Linux only `RunAsUser` option with Windows Pods.
