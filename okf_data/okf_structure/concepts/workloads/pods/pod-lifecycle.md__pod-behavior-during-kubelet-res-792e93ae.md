---
id: okf-structure/concepts/workloads/pods/pod-lifecycle.md#pod-behavior-during-kubelet-restarts-kubelet-restarts
kind: section
title: Pod behavior during kubelet restarts {#kubelet-restarts}
source: concepts/workloads/pods/pod-lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
heading: Pod behavior during kubelet restarts {#kubelet-restarts}
parent: okf-structure/concepts/workloads/pods/pod-lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#termination-of-pods-pod-termination
next_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#whatsnext
word_count: 345
---

If you restart the kubelet, Pods (and their containers) continue to run
even during the restart.
When there are running Pods on a node, stopping or restarting the kubelet
on that node does **not** cause the kubelet to stop all local Pods
before the kubelet itself stops.
To stop the Pods on a node, you can use `kubectl drain`.

### Detection of kubelet restarts

When the kubelet starts, it checks to see if there is already a Node with bound Pods.
If the Node's `Ready` condition remains unchanged,
in other words the condition has not transitioned from true to false, Kubernetes detects this a _kubelet restart_.
(It's possible to restart the kubelet in other ways, for example to fix a node bug,
but in these cases, Kubernetes picks the safe option and treats this as if you
stopped the kubelet and then later started it).

When the kubelet restarts, the container statuses are managed differently based on the feature gate setting:

* By default, the kubelet does not change container statuses after a restart.
  Containers that were in set to `ready: true` state remain remain ready.

  If you stop the kubelet long enough for it to fail a series of
  node heartbeat checks,
  and then you wait before you start the kubelet again, Kubernetes may begin to evict Pods from that Node.
  However, even though Pod evictions begin to happen, Kubernetes does not mark the
  individual containers in those Pods as `ready: false`. The Pod-level eviction
  happens after the control plane taints the node as `node.kubernetes.io/not-ready` (due to the failed heartbeats).

* In Kubernetes  you can opt in to a legacy behavior where the kubelet always modify
  the containers `ready` value, after a kubelet restart, to be false.

  This legacy behavior was the default for a long time, but caused issue for people using Kubernetes,
  especially in large scale deployments. Although the feature gate allows reverting to this legacy
  behavior temporarily, the Kubernetes project recommends that you file a bug report if you encounter problems.
  The `ChangeContainerStatusOnKubeletRestart`
  feature gate
  will be removed in the future.
