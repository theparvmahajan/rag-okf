---
id: okf-structure/tasks/configure-pod-container/security-context.md#delegating-volume-permission-and-ownership-change-to-csi-driver
kind: section
title: Delegating volume permission and ownership change to CSI driver
source: tasks/configure-pod-container/security-context.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/security-context/
heading: Delegating volume permission and ownership change to CSI driver
parent: okf-structure/tasks/configure-pod-container/security-context
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/security-context.md#configure-volume-permission-and-ownership-change-policy-for-pods
next_sibling: okf-structure/tasks/configure-pod-container/security-context.md#set-the-security-context-for-a-container
word_count: 84
---

If you deploy a Container Storage Interface (CSI)
driver which supports the `VOLUME_MOUNT_GROUP` `NodeServiceCapability`, the
process of setting file ownership and permissions based on the
`fsGroup` specified in the `securityContext` will be performed by the CSI driver
instead of Kubernetes. In this case, since Kubernetes doesn't perform any
ownership and permission change, `fsGroupChangePolicy` does not take effect, and
as specified by CSI, the driver is expected to mount the volume with the
provided `fsGroup`, resulting in a volume that is readable/writable by the
`fsGroup`.
