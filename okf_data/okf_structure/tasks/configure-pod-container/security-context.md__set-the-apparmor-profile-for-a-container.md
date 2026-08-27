---
id: okf-structure/tasks/configure-pod-container/security-context.md#set-the-apparmor-profile-for-a-container
kind: section
title: Set the AppArmor Profile for a Container
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Set the AppArmor Profile for a Container
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#set-the-seccomp-profile-for-a-container
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#assign-selinux-labels-to-a-container
word_count: 233
---

To set the AppArmor profile for a Container, include the `appArmorProfile` field
in the `securityContext` section of your Container. The `appArmorProfile` field
is a
AppArmorProfile object consisting of `type` and `localhostProfile`.
Valid options for `type` include `RuntimeDefault`(default), `Unconfined`, and
`Localhost`. `localhostProfile` must only be set if `type` is `Localhost`. It
indicates the name of the pre-configured profile on the node. The profile needs
to be loaded onto all nodes suitable for the Pod, since you don't know where the
pod will be scheduled. 
Approaches for setting up custom profiles are discussed in
Setting up nodes with profiles.

Note: If `containers[*].securityContext.appArmorProfile.type` is explicitly set 
to `RuntimeDefault`, then the Pod will not be admitted if AppArmor is not
enabled on the Node. However if `containers[*].securityContext.appArmorProfile.type`
is not specified, then the default (which is also `RuntimeDefault`) will only
be applied if the node has AppArmor enabled. If the node has AppArmor disabled
the Pod will be admitted but the Container will not be restricted by the 
`RuntimeDefault` profile.

Here is an example that sets the AppArmor profile to the node's container runtime
default profile:

```yaml
...
containers:
- name: container-1
  securityContext:
    appArmorProfile:
      type: RuntimeDefault
```

Here is an example that sets the AppArmor profile to a pre-configured profile
named `k8s-apparmor-example-deny-write`:

```yaml
...
containers:
- name: container-1
  securityContext:
    appArmorProfile:
      type: Localhost
      localhostProfile: k8s-apparmor-example-deny-write
```

For more details please see, Restrict a Container's Access to Resources with AppArmor.
