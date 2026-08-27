---
id: okf-structure/tutorials/configuration/pod-sidecar-containers.md#adopting-built-in-sidecar-containers
kind: section
title: Adopting built-in sidecar containers
source: tutorials/configuration/pod-sidecar-containers.md
url: https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/
heading: Adopting built-in sidecar containers
parent: okf-structure/tutorials/configuration/pod-sidecar-containers
children: []
prev_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#benefits-of-a-built-in-sidecar-container
next_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#whatsnext
word_count: 936
---

The `SidecarContainers` feature gate
is in beta state starting from Kubernetes version 1.29 and is enabled by default.
Some clusters may have this feature disabled or have software installed that is incompatible with the feature.

When this happens, the Pod may be rejected or the sidecar containers may block Pod startup,
rendering the Pod useless. This condition is easy to detect as the Pod simply gets stuck on
initialization. However, it is often unclear what caused the problem.

Here are the considerations and troubleshooting steps that one can take while adopting sidecar containers for their workload.

### Ensure the feature gate is enabled

As a very first step, make sure that both API server and Nodes are at Kubernetes version v1.29 or
later. The feature will break on clusters where Nodes are running earlier versions where it is not enabled.

The feature can be enabled on nodes with the version 1.28. The behavior of built-in sidecar
container termination was different in version 1.28, and it is not recommended to adjust
the behavior of a sidecar to that behavior. However, if the only concern is the startup order, the
above statement can be changed to Nodes running version 1.28 with the feature gate enabled.

You should ensure that the feature gate is enabled for the API server(s) within the control plane
**and** for all nodes.

One of the ways to check the feature gate enablement is to run a command like this:

- For API Server:

  ```shell
  kubectl get --raw /metrics | grep kubernetes_feature_enabled | grep SidecarContainers
  ```

- For the individual node:

  ```shell
  kubectl get --raw /api/v1/nodes/<node-name>/proxy/metrics | grep kubernetes_feature_enabled | grep SidecarContainers
  ```

If you see something like this:

```
kubernetes_feature_enabled{name="SidecarContainers",stage="BETA"} 1
```

it means that the feature is enabled.

### Check for 3rd party tooling and mutating webhooks

If you experience issues when validating the feature, it may be an indication that one of the
3rd party tools or mutating webhooks are broken.

When the `SidecarContainers` feature gate is enabled, Pods gain a new field in their API.
Some tools or mutating webhooks might have been built with an earlier version of Kubernetes API.

If tools pass unknown fields as-is using various patching strategies to mutate a Pod object,
this will not be a problem. However, there are tools that will strip out unknown fields;
if you have those, they must be recompiled with the v1.28+ version of Kubernetes API client code.

The way to check this is to use the `kubectl describe pod` command with your Pod that has passed through
mutating admission. If any tools stripped out the new field (`restartPolicy:Always`),
you will not see it in the command output.

If you hit an issue like this, please advise the author of the tools or the webhooks
use one of the patching strategies for modifying objects instead of a full object update.

Mutating webhook may update Pods based on some conditions.
Thus, sidecar containers may work for some Pods and fail for others.

### Automatic injection of sidecars

If you are using software that injects sidecars automatically,
there are a few possible strategies you may follow to
ensure that native sidecar containers can be used.
All strategies are generally options you may choose to decide whether
the Pod the sidecar will be injected to will land on a Node supporting the feature or not.

As an example, you can follow this conversation in Istio community.
The discussion explores the options listed below.

1. Mark Pods that land to nodes supporting sidecars. You can use node labels
   and node affinity to mark nodes supporting sidecar containers and Pods landing on those nodes.
1. Check Nodes compatibility on injection. During sidecar injection, you may use
   the following strategies to check node compatibility:
   - query node version and assume the feature gate is enabled on the version 1.29+
   - query node prometheus metrics and check feature enablement status
   - assume the nodes are running with a supported version skew
     from the API server
   - there may be other custom ways to detect nodes compatibility.
1. Develop a universal sidecar injector. The idea of a universal sidecar injector is to
   inject a sidecar container as a regular container as well as a native sidecar container.
   And have a runtime logic to decide which one will work. The universal sidecar injector
   is wasteful, as it will account for requests twice, but may be considered as a workable
   solution for special cases.
   - One way would be on start of a native sidecar container
     detect the node version and exit immediately if the version does not support the sidecar feature.
   - Consider a runtime feature detection design:
     - Define an empty dir so containers can communicate with each other
     - Inject an init container, let's call it `NativeSidecar` with `restartPolicy=Always`.
     - `NativeSidecar` must write a file to an empty directory indicating the first run and exit
       immediately with exit code `0`.
     - `NativeSidecar` on restart (when native sidecars are supported) checks that file already
       exists in the empty dir and changes it - indicating that the built-in sidecar containers
       are supported and running.
     - Inject regular container, let's call it `OldWaySidecar`.
     - `OldWaySidecar` on start checks the presence of a file in an empty dir.
     - If the file indicates that the `NativeSidecar` is NOT running, it assumes that the sidecar
       feature is not supported and works assuming it is the sidecar.
     - If the file indicates that the `NativeSidecar` is running, it either does nothing and sleeps
       forever (in the case when Pod’s `restartPolicy=Always`) or exits immediately with exit code `0`
       (in the case when Pod’s `restartPolicy!=Always`).
