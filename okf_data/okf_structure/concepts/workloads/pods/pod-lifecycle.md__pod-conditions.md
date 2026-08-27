---
id: okf-structure/concepts/workloads/pods/pod-lifecycle.md#pod-conditions
kind: section
title: Pod conditions
source: concepts/workloads/pods/pod-lifecycle.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/
heading: Pod conditions
parent: okf-structure/concepts/workloads/pods/pod-lifecycle
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#how-pods-handle-problems-with-containers-container-restarts
next_sibling: okf-structure/concepts/workloads/pods/pod-lifecycle.md#resizing-pods-pod-resize
word_count: 783
---

A Pod has a PodStatus, which has an array of
PodConditions
through which the Pod has or has not passed. The kubelet manages the following
PodConditions:

* `PodScheduled`: the Pod has been scheduled to a node.
* `PodReadyToStartContainers`: (beta feature; enabled by default) the
  Pod sandbox has been successfully created, networking configured, storage volumes mounted,
  and any dynamic resources (if requested) allocated.
* `ContainersReady`: all containers in the Pod are ready.
* `Initialized`: all init containers
  have completed successfully.
* `Ready`: the Pod is able to serve requests and should be added to the load
  balancing pools of all matching Services.
* `DisruptionTarget`: the pod is about to be terminated due to a disruption (such as preemption, eviction or garbage-collection).
* `PodResizePending`: a pod resize was requested but cannot be applied. See Pod resize status.
* `PodResizeInProgress`: the pod is in the process of resizing. See
  Pod resize status.

Field name           | Description
:--------------------|:-----------
`type`               | Name of this Pod condition.
`status`             | Indicates whether that condition is applicable, with possible values "`True`", "`False`", or "`Unknown`".
`lastProbeTime`      | Timestamp of when the Pod condition was last probed.
`lastTransitionTime` | Timestamp for when the Pod last transitioned from one status to another.
`reason`             | Machine-readable, UpperCamelCase text indicating the reason for the condition's last transition.
`message`            | Human-readable message indicating details about the last status transition.

### Pod readiness {#pod-readiness-gate}

Your application can inject extra feedback or signals into PodStatus:
_Pod readiness_. To use this, set `readinessGates` in the Pod's `spec` to
specify a list of additional conditions that the kubelet evaluates for Pod readiness.

Readiness gates are determined by the current state of `status.condition`
fields for the Pod. If Kubernetes cannot find such a condition in the
`status.conditions` field of a Pod, the status of the condition
is defaulted to "`False`".

Here is an example:

```yaml
kind: Pod
...
spec:
  readinessGates:
    - conditionType: "www.example.com/feature-1"
status:
  conditions:
    - type: Ready                              # a built-in PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
    - type: "www.example.com/feature-1"        # an extra PodCondition
      status: "False"
      lastProbeTime: null
      lastTransitionTime: 2018-01-01T00:00:00Z
  containerStatuses:
    - containerID: docker://abcd...
      ready: true
...
```

The Pod conditions you add must have names that meet the Kubernetes
label key format.

### Status for Pod readiness {#pod-readiness-status}

The `kubectl patch` command does not support patching object status.
To set these `status.conditions` for the Pod, applications and
operators should use
the `PATCH` action.
You can use a Kubernetes client library to
write code that sets custom Pod conditions for Pod readiness.

For a Pod that uses custom conditions, that Pod is evaluated to be ready **only**
when both the following statements apply:

* All containers in the Pod are ready.
* All conditions specified in `readinessGates` are `True`.

When a Pod's containers are Ready but at least one custom condition is missing or
`False`, the kubelet sets the Pod's condition to `ContainersReady`.

### Pod readiness to start containers {#pod-ready-to-start-containers}

During its early development, this condition was named `PodHasNetwork`.

After a Pod gets scheduled on a node, it needs to be admitted by the kubelet and
to have any required storage volumes mounted. Once these phases are complete,
the kubelet works with
a container runtime (using cri) to set up a
runtime sandbox and configure networking for the Pod. If the Pod uses
Dynamic Resource Allocation,
those resources are also allocated during this phase.
If the `PodReadyToStartContainersCondition`
feature gate is enabled
(it is enabled by default for Kubernetes ), the
`PodReadyToStartContainers` condition will be added to the `status.conditions` field of a Pod.

The `PodReadyToStartContainers` condition is set to `False` by the kubelet when it detects a
Pod does not have a runtime sandbox with networking configured. This occurs in
the following scenarios:

- Early in the lifecycle of the Pod, when the kubelet has not yet begun to set up a sandbox for
  the Pod using the container runtime.
- Later in the lifecycle of the Pod, when the Pod sandbox has been destroyed due to either:
  - the node rebooting, without the Pod getting evicted
  - for container runtimes that use virtual machines for isolation, the Pod
    sandbox virtual machine rebooting, which then requires creating a new sandbox and
    fresh container network configuration.

After sandbox creation, network configuration, volume mounting, and (if requested) dynamic resource
allocation are complete, the kubelet sets the `PodReadyToStartContainers` condition to `True`.
Image pulling and container creation occur after this point.

For a Pod with init containers, the kubelet sets the `Initialized` condition to
`True` after the init containers have successfully completed (which happens
after successful sandbox creation and network configuration by the runtime
plugin). For a Pod without init containers, the kubelet sets the `Initialized`
condition to `True` before sandbox creation and network configuration starts.
