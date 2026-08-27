---
id: okf-structure/concepts/cluster-administration/node-shutdown.md#non-graceful-node-shutdown-handling-non-graceful-node-shutdown
kind: section
title: Non-graceful node shutdown handling {#non-graceful-node-shutdown}
source: concepts/cluster-administration/node-shutdown.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
heading: Non-graceful node shutdown handling {#non-graceful-node-shutdown}
parent: okf-structure/concepts/cluster-administration/node-shutdown
children: []
prev_sibling: okf-structure/concepts/cluster-administration/node-shutdown.md#graceful-node-shutdown-graceful-node-shutdown
next_sibling: okf-structure/concepts/cluster-administration/node-shutdown.md#whatsnext
word_count: 594
---

A node shutdown action may not be detected by kubelet's Node Shutdown Manager,
either because the command does not trigger the inhibitor locks mechanism used by
kubelet or because of a user error, i.e., the ShutdownGracePeriod and
ShutdownGracePeriodCriticalPods are not configured properly. Please refer to above
section Graceful Node Shutdown for more details.

When a node is shutdown but not detected by kubelet's Node Shutdown Manager, the pods
that are part of a StatefulSet
will be stuck in terminating status on the shutdown node and cannot move to a new running node.
This is because kubelet on the shutdown node is not available to delete the pods so
the StatefulSet cannot create a new pod with the same name. If there are volumes used by the pods,
the VolumeAttachments will not be deleted from the original shutdown node so the volumes
used by these pods cannot be attached to a new running node. As a result, the
application running on the StatefulSet cannot function properly. If the original
shutdown node comes up, the pods will be deleted by kubelet and new pods will be
created on a different running node. If the original shutdown node does not come up,
these pods will be stuck in terminating status on the shutdown node forever.

To mitigate the above situation, a user can manually add the taint `node.kubernetes.io/out-of-service`
with either `NoExecute` or `NoSchedule` effect to a Node marking it out-of-service.
If a Node is marked out-of-service with this taint, the pods on the node will be forcefully deleted
if there are no matching tolerations on it and volume detach operations for the pods terminating on
the node will happen immediately. This allows the Pods on the out-of-service node to recover quickly
on a different node.

During a non-graceful shutdown, Pods are terminated in the two phases:

1. Force delete the Pods that do not have matching `out-of-service` tolerations.
1. Immediately perform detach volume operation for such pods.

- Before adding the taint `node.kubernetes.io/out-of-service`, it should be verified
  that the node is already in shutdown or power off state (not in the middle of restarting).
- The user is required to manually remove the out-of-service taint after the pods are
  moved to a new node and the user has checked that the shutdown node has been
  recovered since the user was the one who originally added the taint.

### Forced storage detach on timeout {#storage-force-detach-on-timeout}

In any situation where a pod deletion has not succeeded for 6 minutes, kubernetes will
force detach volumes being unmounted if the node is unhealthy at that instant. Any
workload still running on the node that uses a force-detached volume will cause a
violation of the
CSI specification,
which states that `ControllerUnpublishVolume` "**must** be called after all
`NodeUnstageVolume` and `NodeUnpublishVolume` on the volume are called and succeed".
In such circumstances, volumes on the node in question might encounter data corruption.

The forced storage detach behaviour is optional; users might opt to use the "Non-graceful
node shutdown" feature instead.

Force storage detach on timeout can be disabled by setting the `disable-force-detach-on-timeout`
config field in `kube-controller-manager`. Disabling the force detach on timeout feature means
that a volume that is hosted on a node that is unhealthy for more than 6 minutes will not have
its associated
VolumeAttachment
deleted.

After this setting has been applied, unhealthy pods still attached to volumes must be recovered
via the Non-Graceful Node Shutdown procedure mentioned above.

- Caution must be taken while using the Non-Graceful Node Shutdown procedure.
- Deviation from the steps documented above can result in data corruption.
