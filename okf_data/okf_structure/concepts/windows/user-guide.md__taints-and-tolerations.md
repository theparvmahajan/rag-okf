---
id: okf-structure/concepts/windows/user-guide.md#taints-and-tolerations
kind: section
title: Taints and tolerations
source: concepts/windows/user-guide.md
url: https://kubernetes.io/docs/concepts/windows/user-guide/
heading: Taints and tolerations
parent: okf-structure/concepts/windows/user-guide
children: []
prev_sibling: okf-structure/concepts/windows/user-guide.md#configuring-container-user
next_sibling: null
word_count: 734
---

Users need to use some combination of taint
and node selectors in order to schedule Linux and Windows workloads to their respective OS-specific nodes.
The recommended approach is outlined below,
with one of its main goals being that this approach should not break compatibility for existing Linux workloads.

You can (and should) set `.spec.os.name` for each Pod, to indicate the operating system
that the containers in that Pod are designed for. For Pods that run Linux containers, set
`.spec.os.name` to `linux`. For Pods that run Windows containers, set `.spec.os.name`
to `windows`.

If you are running a version of Kubernetes older than 1.24, you may need to enable
the `IdentifyPodOS` feature gate
to be able to set a value for `.spec.pod.os`.

The scheduler does not use the value of `.spec.os.name` when assigning Pods to nodes. You should
use normal Kubernetes mechanisms for
assigning pods to nodes
to ensure that the control plane for your cluster places pods onto nodes that are running the
appropriate operating system.

The `.spec.os.name` value has no effect on the scheduling of the Windows pods,
so taints and tolerations (or node selectors) are still required
 to ensure that the Windows pods land onto appropriate Windows nodes.

### Ensuring OS-specific workloads land on the appropriate container host

Users can ensure Windows containers can be scheduled on the appropriate host using taints and tolerations.
All Kubernetes nodes running Kubernetes  have the following default labels:

* kubernetes.io/os = [windows|linux]
* kubernetes.io/arch = [amd64|arm64|...]

If a Pod specification does not specify a `nodeSelector` such as `"kubernetes.io/os": windows`,
it is possible the Pod can be scheduled on any host, Windows or Linux.
This can be problematic since a Windows container can only run on Windows and a Linux container can only run on Linux.
The best practice for Kubernetes  is to use a `nodeSelector`.

However, in many cases users have a pre-existing large number of deployments for Linux containers,
as well as an ecosystem of off-the-shelf configurations, such as community Helm charts, and programmatic Pod generation cases, such as with operators.
In those situations, you may be hesitant to make the configuration change to add `nodeSelector` fields to all Pods and Pod templates.
The alternative is to use taints. Because the kubelet can set taints during registration,
it could easily be modified to automatically add a taint when running on Windows only.

For example:  `--register-with-taints='os=windows:NoSchedule'`

By adding a taint to all Windows nodes, nothing will be scheduled on them (that includes existing Linux Pods).
In order for a Windows Pod to be scheduled on a Windows node,
it would need both the `nodeSelector` and the appropriate matching toleration to choose Windows.

```yaml
nodeSelector:
    kubernetes.io/os: windows
    node.kubernetes.io/windows-build: '10.0.20348'
tolerations:
    - key: "os"
      operator: "Equal"
      value: "windows"
      effect: "NoSchedule"
```

### Handling multiple Windows versions in the same cluster

The Windows Server version used by each pod must match that of the node. If you want to use multiple Windows
Server versions in the same cluster, then you should set additional node labels and `nodeSelector` fields.

Kubernetes automatically adds a label,
`node.kubernetes.io/windows-build`
to simplify this.

This label reflects the Windows major, minor, and build number that need to match for compatibility.
Here are values used for each Windows Server version:

| Product Name                         | Version                |
|--------------------------------------|------------------------|
| Windows Server 2022                  | 10.0.20348             |
| Windows Server 2025                  | 10.0.26100             |

### Simplifying with RuntimeClass

[RuntimeClass] can be used to simplify the process of using taints and tolerations.
A cluster administrator can create a `RuntimeClass` object which is used to encapsulate these taints and tolerations.

1. Save this file to `runtimeClasses.yml`. It includes the appropriate `nodeSelector`
   for the Windows OS, architecture, and version.

   ```yaml
   ---
   apiVersion: node.k8s.io/v1
   kind: RuntimeClass
   metadata:
     name: windows-2019
   handler: example-container-runtime-handler
   scheduling:
     nodeSelector:
       kubernetes.io/os: 'windows'
       kubernetes.io/arch: 'amd64'
       node.kubernetes.io/windows-build: '10.0.20348'
     tolerations:
     - effect: NoSchedule
       key: os
       operator: Equal
       value: "windows"
   ```

1. Run `kubectl create -f runtimeClasses.yml` using as a cluster administrator
1. Add `runtimeClassName: windows-2019` as appropriate to Pod specs

   For example:

   ```yaml
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: iis-2019
     labels:
       app: iis-2019
   spec:
     replicas: 1
     template:
       metadata:
         name: iis-2019
         labels:
           app: iis-2019
       spec:
         runtimeClassName: windows-2019
         containers:
         - name: iis
           image: mcr.microsoft.com/windows/servercore/iis:windowsservercore-ltsc2019
           resources:
             limits:
               cpu: 1
               memory: 800Mi
             requests:
               cpu: .1
               memory: 300Mi
           ports:
             - containerPort: 80
    selector:
       matchLabels:
         app: iis-2019
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: iis
   spec:
     type: LoadBalancer
     ports:
     - protocol: TCP
       port: 80
     selector:
       app: iis-2019
   ```

[RuntimeClass]: /docs/concepts/containers/runtime-class/
