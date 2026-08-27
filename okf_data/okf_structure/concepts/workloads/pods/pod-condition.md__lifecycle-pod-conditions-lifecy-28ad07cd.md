---
id: okf-structure/concepts/workloads/pods/pod-condition.md#lifecycle-pod-conditions-lifecycle-pod-conditions
kind: section
title: Lifecycle Pod conditions {#lifecycle-pod-conditions}
source: concepts/workloads/pods/pod-condition.md
url: https://kubernetes.io/docs/concepts/workloads/pods/pod-condition/
heading: Lifecycle Pod conditions {#lifecycle-pod-conditions}
parent: okf-structure/concepts/workloads/pods/pod-condition
children: []
prev_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#built-in-pod-conditions-built-in-pod-conditions
next_sibling: okf-structure/concepts/workloads/pods/pod-condition.md#other-pod-conditions-other-pod-conditions
word_count: 552
---

As a Pod progresses through its lifecycle, the kubelet sets the following conditions roughly in this order:

1. `PodScheduled`: the Pod has been scheduled to a node.
1. `PodReadyToStartContainers`: the Pod sandbox has been successfully created and networking configured. The sandbox and network are set up by the container runtime and CNI plugin.
1. `Initialized`: all init containers have completed successfully. For a Pod without init containers, this is set to `True` before sandbox creation.
1. `ContainersReady`: all containers in the Pod are ready. A container's readiness is determined by its readiness probe, if configured.
1. `Ready`: the Pod is able to serve requests and should be added to the load balancing pools of all matching Services. Pods that are not `Ready` are removed from Service endpoints.

The `Ready` condition depends on more than just `ContainersReady`. If the Pod specifies `readinessGates`, all of those custom conditions must also be `True` for the Pod to be `Ready`. See Pod readiness for details.

You can inspect a Pod's conditions using kubectl:

```shell
kubectl get pod <pod-name> -o yaml
```

The following shows what `status.conditions` looks like for a running Pod:

```yaml
status:
  conditions:
    - type: PodScheduled
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-03-29T08:52:21Z"
      observedGeneration: 1
    - type: PodReadyToStartContainers
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:16Z"
      observedGeneration: 1
    - type: Initialized
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-03-29T08:52:21Z"
      observedGeneration: 1
    - type: ContainersReady
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:45Z"
      observedGeneration: 1
    - type: Ready
      status: "True"
      lastProbeTime: null
      lastTransitionTime: "2026-04-11T06:02:45Z"
      observedGeneration: 1
```

### PodReadyToStartContainers {#pod-ready-to-start-containers}

During its early development, this condition was named `PodHasNetwork`.

After a Pod gets scheduled on a node, it needs to be admitted by the kubelet
and to have any required storage volumes mounted. Once these phases are complete,
the kubelet works with a container runtime
(using Container Runtime Interface (CRI))
to set up a runtime sandbox and configure networking for the Pod.
If the `PodReadyToStartContainersCondition` feature gate is enabled
(it is enabled by default for Kubernetes ),
the `PodReadyToStartContainers` condition will be added to the `status.conditions` field of a Pod.

The `PodReadyToStartContainers` condition is set to `False` by the kubelet
when it detects a Pod does not have a runtime sandbox with networking configured. This occurs in the following scenarios:

- Early in the lifecycle of the Pod, when the kubelet has not yet begun to set up a sandbox for the Pod using the container runtime.
- Later in the lifecycle of the Pod, when the Pod sandbox has been destroyed due to either:
  - the node rebooting, without the Pod getting evicted
  - for container runtimes that use virtual machines for isolation, the Pod sandbox virtual machine rebooting, which then requires creating a new sandbox and fresh container network configuration.

The `PodReadyToStartContainers` condition is set to `True` by the kubelet after the successful completion of sandbox creation and network configuration for the Pod by the runtime plugin. The kubelet can start pulling container images and create containers after `PodReadyToStartContainers` condition has been set to `True`.

For a Pod with init containers, the kubelet sets the `Initialized` condition to `True` after the init containers have successfully completed (which happens after successful sandbox creation and network configuration by the runtime plugin). For a Pod without init containers, the kubelet sets the `Initialized` condition to `True` before sandbox creation and network configuration starts.
