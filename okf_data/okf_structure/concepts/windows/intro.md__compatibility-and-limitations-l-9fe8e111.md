---
id: okf-structure/concepts/windows/intro.md#compatibility-and-limitations-limitations
kind: section
title: Compatibility and limitations {#limitations}
source: concepts/windows/intro.md
url: https://kubernetes.io/docs/concepts/windows/intro/
heading: Compatibility and limitations {#limitations}
parent: okf-structure/concepts/windows/intro
children: []
prev_sibling: okf-structure/concepts/windows/intro.md#windows-nodes-in-kubernetes
next_sibling: okf-structure/concepts/windows/intro.md#node-problem-detector
word_count: 1400
---

Some node features are only available if you use a specific
container runtime; others are not available on Windows nodes,
including:

* HugePages: not supported for Windows containers
* Privileged containers: not supported for Windows containers.
  HostProcess Containers offer similar functionality.
* TerminationGracePeriod: requires containerD

Not all features of shared namespaces are supported. See API compatibility
for more details.

See Windows OS version compatibility for details on
the Windows versions that Kubernetes is tested against.

From an API and kubectl perspective, Windows containers behave in much the same
way as Linux-based containers. However, there are some notable differences in key
functionality which are outlined in this section.

### Comparison with Linux {#compatibility-linux-similarities}

Key Kubernetes elements work the same way in Windows as they do in Linux. This
section refers to several key workload abstractions and how they map to Windows.

* Pods

  A Pod is the basic building block of Kubernetes–the smallest and simplest unit in
  the Kubernetes object model that you create or deploy. You may not deploy Windows and
  Linux containers in the same Pod. All containers in a Pod are scheduled onto a single
  Node where each Node represents a specific platform and architecture. The following
  Pod capabilities, properties and events are supported with Windows containers:

  * Single or multiple containers per Pod with process isolation and volume sharing
  * Pod `status` fields
  * Readiness, liveness, and startup probes
  * postStart & preStop container lifecycle hooks
  * ConfigMap, Secrets: as environment variables or volumes
  * `emptyDir` volumes
  * Named pipe host mounts
  * Resource limits
  * OS field: 

    The `.spec.os.name` field should be set to `windows` to indicate that the current Pod uses Windows containers.

    If you set the `.spec.os.name` field to `windows`,
    you must not set the following fields in the `.spec` of that Pod:

    * `spec.hostPID`
    * `spec.hostIPC`
    * `spec.securityContext.seLinuxOptions`
    * `spec.securityContext.seccompProfile`
    * `spec.securityContext.fsGroup`
    * `spec.securityContext.fsGroupChangePolicy`
    * `spec.securityContext.sysctls`
    * `spec.shareProcessNamespace`
    * `spec.securityContext.runAsUser`
    * `spec.securityContext.runAsGroup`
    * `spec.securityContext.supplementalGroups`
    * `spec.containers[*].securityContext.seLinuxOptions`
    * `spec.containers[*].securityContext.seccompProfile`
    * `spec.containers[*].securityContext.capabilities`
    * `spec.containers[*].securityContext.readOnlyRootFilesystem`
    * `spec.containers[*].securityContext.privileged`
    * `spec.containers[*].securityContext.allowPrivilegeEscalation`
    * `spec.containers[*].securityContext.procMount`
    * `spec.containers[*].securityContext.runAsUser`
    * `spec.containers[*].securityContext.runAsGroup`

    In the above list, wildcards (`*`) indicate all elements in a list.
    For example, `spec.containers[*].securityContext` refers to the SecurityContext object
    for all containers. If any of these fields is specified, the Pod will
    not be admitted by the API server.

* Workload resources including:
  * ReplicaSet
  * Deployment
  * StatefulSet
  * DaemonSet
  * Job
  * CronJob
  * ReplicationController
* Services
  See Load balancing and Services for more details.

Pods, workload resources, and Services are critical elements to managing Windows
workloads on Kubernetes. However, on their own they are not enough to enable
the proper lifecycle management of Windows workloads in a dynamic cloud native
environment.

* `kubectl exec`
* Pod and container metrics
* Horizontal pod autoscaling
* Resource quotas
* Scheduler preemption

### Command line options for the kubelet {#kubelet-compatibility}

Some kubelet command line options behave differently on Windows, as described below:

* The `--windows-priorityclass` lets you set the scheduling priority of the kubelet process
  (see CPU resource management)
* The `--kube-reserved`, `--system-reserved` , and `--eviction-hard` flags update
  NodeAllocatable
* Eviction by using `--enforce-node-allocable` is not implemented
* When running on a Windows node the kubelet does not have memory or CPU
  restrictions. `--kube-reserved` and `--system-reserved` only subtract from `NodeAllocatable`
  and do not guarantee resource provided for workloads.
  See Resource Management for Windows nodes
  for more information.
* The `PIDPressure` Condition is not implemented
* The kubelet does not take OOM eviction actions

### API compatibility {#api}

There are subtle differences in the way the Kubernetes APIs work for Windows due to the OS
and container runtime. Some workload properties were designed for Linux, and fail to run on Windows.

At a high level, these OS concepts are different:

* Identity - Linux uses userID (UID) and groupID (GID) which
  are represented as integer types. User and group names
  are not canonical - they are just an alias in `/etc/groups`
  or `/etc/passwd` back to UID+GID. Windows uses a larger binary
  security identifier (SID)
  which is stored in the Windows Security Access Manager (SAM) database. This
  database is not shared between the host and containers, or between containers.
* File permissions - Windows uses an access control list based on (SIDs), whereas
  POSIX systems such as Linux use a bitmask based on object permissions and UID+GID,
  plus _optional_ access control lists.
* File paths - the convention on Windows is to use `\` instead of `/`. The Go IO
  libraries typically accept both and just make it work, but when you're setting a
  path or command line that's interpreted inside a container, `\` may be needed.
* Signals - Windows interactive apps handle termination differently, and can
  implement one or more of these:
  * A UI thread handles well-defined messages including `WM_CLOSE`.
  * Console apps handle Ctrl-C or Ctrl-break using a Control Handler.
  * Services register a Service Control Handler function that can accept
    `SERVICE_CONTROL_STOP` control codes.

Container exit codes follow the same convention where 0 is success, and nonzero is failure.
The specific error codes may differ across Windows and Linux. However, exit codes
passed from the Kubernetes components (kubelet, kube-proxy) are unchanged.

#### Field compatibility for container specifications {#compatibility-v1-pod-spec-containers}

The following list documents differences between how Pod container specifications
work between Windows and Linux:

* Huge pages are not implemented in the Windows container
  runtime, and are not available. They require asserting a user
  privilege
  that's not configurable for containers.
* `requests.cpu` and `requests.memory` - requests are subtracted
  from node available resources, so they can be used to avoid overprovisioning a
  node. However, they cannot be used to guarantee resources in an overprovisioned
  node. They should be applied to all containers as a best practice if the operator
  wants to avoid overprovisioning entirely.
* `securityContext.allowPrivilegeEscalation` -
   not possible on Windows; none of the capabilities are hooked up
* `securityContext.capabilities` -
   POSIX capabilities are not implemented on Windows
* `securityContext.privileged` -
   Windows doesn't support privileged containers, use HostProcess Containers instead
* `securityContext.procMount` -
   Windows doesn't have a `/proc` filesystem
* `securityContext.readOnlyRootFilesystem` -
   not possible on Windows; write access is required for registry & system
   processes to run inside the container
* `securityContext.runAsGroup` -
   not possible on Windows as there is no GID support
* `securityContext.runAsNonRoot` -
   this setting will prevent containers from running as `ContainerAdministrator`
   which is the closest equivalent to a root user on Windows.
* `securityContext.runAsUser` -
   use `runAsUserName`
   instead
* `securityContext.seLinuxOptions` -
   not possible on Windows as SELinux is Linux-specific
* `terminationMessagePath` -
   this has some limitations in that Windows doesn't support mapping single files. The
   default value is `/dev/termination-log`, which does work because it does not
   exist on Windows by default.

#### Field compatibility for Pod specifications {#compatibility-v1-pod}

The following list documents differences between how Pod specifications work between Windows and Linux:

* `hostIPC` and `hostpid` - host namespace sharing is not possible on Windows
* `hostNetwork` - host networking is not possible on Windows
* `dnsPolicy` - setting the Pod `dnsPolicy` to `ClusterFirstWithHostNet` is
   not supported on Windows because host networking is not provided. Pods always
   run with a container network.
* `podSecurityContext` see below
* `shareProcessNamespace` - this is a beta feature, and depends on Linux namespaces
  which are not implemented on Windows. Windows cannot share process namespaces or
  the container's root filesystem. Only the network can be shared.
* `terminationGracePeriodSeconds` - this is not fully implemented in Docker on Windows,
  see the GitHub issue.
  The behavior today is that the ENTRYPOINT process is sent CTRL_SHUTDOWN_EVENT,
  then Windows waits 5 seconds by default, and finally shuts down
  all processes using the normal Windows shutdown behavior. The 5
  second default is actually in the Windows registry
  inside the container,
  so it can be overridden when the container is built.
* `volumeDevices` - this is a beta feature, and is not implemented on Windows.
  Windows cannot attach raw block devices to pods.
* `volumes`
  * If you define an `emptyDir` volume, you cannot set its volume source to `memory`.
* You cannot enable `mountPropagation` for volume mounts as this is not
  supported on Windows.

#### Host network access {#compatibility-v1-pod-sec-containers-hostnetwork}

Kubernetes v1.26 to v1.32  included alpha support for running Windows Pods in the host's network namespace.

Kubernetes v does **not** include the `WindowsHostNetwork` feature gate
or support for running Windows Pods in the host's network namespace.

#### Field compatibility for Pod security context {#compatibility-v1-pod-spec-containers-securitycontext}

Only the `securityContext.runAsNonRoot` and `securityContext.windowsOptions` from the Pod
`securityContext` fields work on Windows.
