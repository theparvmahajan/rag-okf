---
id: okf-structure/tutorials/security/apparmor.md#specifying-apparmor-confinement
kind: section
title: Specifying AppArmor confinement
source: tutorials/security/apparmor.md
url: https://kubernetes.io/docs/tutorials/security/apparmor/
heading: Specifying AppArmor confinement
parent: okf-structure/tutorials/security/apparmor
children: []
prev_sibling: okf-structure/tutorials/security/apparmor.md#authoring-profiles
next_sibling: okf-structure/tutorials/security/apparmor.md#whatsnext
word_count: 171
---

Prior to Kubernetes v1.30, AppArmor was specified through annotations. Use the documentation version
selector to view the documentation with this deprecated API.

### AppArmor profile within security context {#appArmorProfile}

You can specify the `appArmorProfile` on either a container's `securityContext` or on a Pod's
`securityContext`. If the profile is set at the pod level, it will be used as the default profile
for all containers in the pod (including init, sidecar, and ephemeral containers). If both a pod & container
AppArmor profile are set, the container's profile will be used.

An AppArmor profile has 2 fields:

`type` _(required)_ - indicates which kind of AppArmor profile will be applied. Valid options are:

`Localhost`
: a profile pre-loaded on the node (specified by `localhostProfile`).

`RuntimeDefault`
: the container runtime's default profile.

`Unconfined`
: no AppArmor enforcement.

`localhostProfile` - The name of a profile loaded on the node that should be used.
The profile must be preconfigured on the node to work.
This option must be provided if and only if the `type` is `Localhost`.
