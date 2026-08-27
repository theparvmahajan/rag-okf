---
id: okf-structure/tasks/configure-pod-container/security-context.md#configure-volume-permission-and-ownership-change-policy-for-pods
kind: section
title: Configure volume permission and ownership change policy for Pods
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Configure volume permission and ownership change policy for Pods
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#configure-fine-grained-supplementalgroups-control-for-a-pod-supplementalgroupspolicy
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#delegating-volume-permission-and-ownership-change-to-csi-driver
word_count: 192
---

By default, Kubernetes recursively changes ownership and permissions for the contents of each
volume to match the `fsGroup` specified in a Pod's `securityContext` when that volume is
mounted.
For large volumes, checking and changing ownership and permissions can take a lot of time,
slowing Pod startup. You can use the `fsGroupChangePolicy` field inside a `securityContext`
to control the way that Kubernetes checks and manages ownership and permissions
for a volume.

**fsGroupChangePolicy** - `fsGroupChangePolicy` defines behavior for changing ownership
  and permission of the volume before being exposed inside a Pod.
  This field only applies to volume types that support `fsGroup` controlled ownership and permissions.
  This field has two possible values:

* _OnRootMismatch_: Only change permissions and ownership if the permission and the ownership of
  root directory does not match with expected permissions of the volume.
  This could help shorten the time it takes to change ownership and permission of a volume.
* _Always_: Always change permission and ownership of the volume when volume is mounted.

For example:

```yaml
securityContext:
  runAsUser: 1000
  runAsGroup: 3000
  fsGroup: 2000
  fsGroupChangePolicy: "OnRootMismatch"
```

This field has no effect on ephemeral volume types such as
`secret`,
`configMap`,
and `emptyDir`.
