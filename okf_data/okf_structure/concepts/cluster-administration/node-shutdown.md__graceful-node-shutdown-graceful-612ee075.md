---
id: okf-structure/concepts/cluster-administration/node-shutdown.md#graceful-node-shutdown-graceful-node-shutdown
kind: section
title: Graceful node shutdown {#graceful-node-shutdown}
source: concepts/cluster-administration/node-shutdown.md
url: https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/
heading: Graceful node shutdown {#graceful-node-shutdown}
parent: okf-structure/concepts/cluster-administration/node-shutdown
children: []
prev_sibling: okf-structure/concepts/cluster-administration/node-shutdown.md#introduction
next_sibling: okf-structure/concepts/cluster-administration/node-shutdown.md#non-graceful-node-shutdown-handling-non-graceful-node-shutdown
word_count: 1193
---

The kubelet attempts to detect node system shutdown and terminates pods running on the node.

Kubelet ensures that pods follow the normal
pod termination process
during the node shutdown. During node shutdown, the kubelet does not accept new
Pods (even if those Pods are already bound to the node).

### Enabling graceful node shutdown

On Linux, the graceful node shutdown feature is controlled with the `GracefulNodeShutdown`
feature gate which is
enabled by default in 1.21.

The graceful node shutdown feature depends on systemd since it takes advantage of
systemd inhibitor locks to
delay the node shutdown with a given duration.

On Windows, the graceful node shutdown feature is controlled with the `WindowsGracefulNodeShutdown`
feature gate
which is introduced in 1.32 as an alpha feature. In Kubernetes 1.34 the feature is Beta
and is enabled by default.

The Windows graceful node shutdown feature depends on kubelet running as a Windows service,
it will then have a registered service control handler
to delay the preshutdown event with a given duration.

Windows graceful node shutdown can not be cancelled.

If kubelet is not running as a Windows service, it will not be able to set and monitor
the Preshutdown event,
the node will have to go through the Non-Graceful Node Shutdown procedure mentioned above.

In the case where the Windows graceful node shutdown feature is enabled, but the kubelet is not
running as a Windows service, the kubelet will continue running instead of failing. However,
it will log an error indicating that it needs to be run as a Windows service.

### Configuring graceful node shutdown

Note that by default, both configuration options described below,
`shutdownGracePeriod` and `shutdownGracePeriodCriticalPods`, are set to zero,
thus not activating the graceful node shutdown functionality.
To activate the feature, both options should be configured appropriately and
set to non-zero values.

Once the kubelet is notified of a node shutdown, it sets a `NotReady` condition on
the Node, with the `reason` set to `"node is shutting down"`. The kube-scheduler honors this condition
and does not schedule any Pods onto the affected node; other third-party schedulers are
expected to follow the same logic. This means that new Pods won't be scheduled onto that node
and therefore none will start.

The kubelet **also** rejects Pods during the `PodAdmission` phase if an ongoing
node shutdown has been detected, so that even Pods with a
toleration for
`node.kubernetes.io/not-ready:NoSchedule` do not start there.

When kubelet is setting that condition on its Node via the API,
the kubelet also begins terminating any Pods that are running locally.

During a graceful shutdown, kubelet terminates pods in two phases:

1. Terminate regular pods running on the node.
1. Terminate critical pods
   running on the node.

The graceful node shutdown feature is configured with two
`KubeletConfiguration` options:

- `shutdownGracePeriod`:

  Specifies the total duration that the node should delay the shutdown by. This is the total
  grace period for pod termination for both regular and
  critical pods.

- `shutdownGracePeriodCriticalPods`:

  Specifies the duration used to terminate
  critical pods
  during a node shutdown. This value should be less than `shutdownGracePeriod`.

There are cases when Node termination was cancelled by the system (or perhaps manually
by an administrator). In either of those situations the Node will return to the `Ready` state.
However, Pods which already started the process of termination will not be restored by kubelet
and will need to be re-scheduled.

For example, if `shutdownGracePeriod=30s`, and
`shutdownGracePeriodCriticalPods=10s`, kubelet will delay the node shutdown by
30 seconds. During the shutdown, the first 20 (30-10) seconds would be reserved
for gracefully terminating normal pods, and the last 10 seconds would be
reserved for terminating critical pods.

When pods were evicted during the graceful node shutdown, they are marked as shutdown.
Running `kubectl get pods` shows the status of the evicted pods as `Terminated`.
And `kubectl describe pod` indicates that the pod was evicted because of node shutdown:

```
Reason:         Terminated
Message:        Pod was terminated in response to imminent node shutdown.
```

### Pod Priority based graceful node shutdown {#pod-priority-graceful-node-shutdown}

To provide more flexibility during graceful node shutdown around the ordering
of pods during shutdown, graceful node shutdown honors the PriorityClass for
Pods, provided that you enabled this feature in your cluster. The feature
allows cluster administrators to explicitly define the ordering of pods
during graceful node shutdown based on
priority classes.

The Graceful Node Shutdown feature, as described
above, shuts down pods in two phases, non-critical pods, followed by critical
pods. If additional flexibility is needed to explicitly define the ordering of
pods during shutdown in a more granular way, pod priority based graceful
shutdown can be used.

When graceful node shutdown honors pod priorities, this makes it possible to do
graceful node shutdown in multiple phases, each phase shutting down a
particular priority class of pods. The kubelet can be configured with the exact
phases and shutdown time per phase.

Assuming the following custom pod
priority classes
in a cluster,

| Pod priority class name | Pod priority class value |
| ----------------------- | ------------------------ |
| `custom-class-a`        | 100000                   |
| `custom-class-b`        | 10000                    |
| `custom-class-c`        | 1000                     |
| `regular/unset`         | 0                        |

Within the kubelet configuration
the settings for `shutdownGracePeriodByPodPriority` could look like:

| Pod priority class value | Shutdown period |
| ------------------------ | --------------- |
| 100000                   | 10 seconds      |
| 10000                    | 180 seconds     |
| 1000                     | 120 seconds     |
| 0                        | 60 seconds      |

The corresponding kubelet config YAML configuration would be:

```yaml
shutdownGracePeriodByPodPriority:
  - priority: 100000
    shutdownGracePeriodSeconds: 10
  - priority: 10000
    shutdownGracePeriodSeconds: 180
  - priority: 1000
    shutdownGracePeriodSeconds: 120
  - priority: 0
    shutdownGracePeriodSeconds: 60
```

The above table implies that any pod with `priority` value >= 100000 will get
just 10 seconds to shut down, any pod with value >= 10000 and < 100000 will get 180
seconds to shut down, any pod with value >= 1000 and < 10000 will get 120 seconds to shut down.
Finally, all other pods will get 60 seconds to shut down.

One doesn't have to specify values corresponding to all of the classes. For
example, you could instead use these settings:

| Pod priority class value | Shutdown period |
| ------------------------ | --------------- |
| 100000                   | 300 seconds     |
| 1000                     | 120 seconds     |
| 0                        | 60 seconds      |

In the above case, the pods with `custom-class-b` will go into the same bucket
as `custom-class-c` for shutdown.

If there are no pods in a particular range, then the kubelet does not wait
for pods in that priority range. Instead, the kubelet immediately skips to the
next priority class value range.

If this feature is enabled and no configuration is provided, then no ordering
action will be taken.

Using this feature requires enabling the `GracefulNodeShutdownBasedOnPodPriority`
feature gate,
and setting `ShutdownGracePeriodByPodPriority` in the
kubelet config
to the desired configuration containing the pod priority class values and
their respective shutdown periods.

The ability to take Pod priority into account during graceful node shutdown was introduced
as an Alpha feature in Kubernetes v1.23. In Kubernetes 
the feature is Beta and is enabled by default.

Metrics `graceful_shutdown_start_time_seconds` and `graceful_shutdown_end_time_seconds`
are emitted under the kubelet subsystem to monitor node shutdowns.
