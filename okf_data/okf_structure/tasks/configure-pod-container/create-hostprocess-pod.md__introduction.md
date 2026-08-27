---
id: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#introduction
kind: section
title: Create a Windows HostProcess Pod
source: tasks/configure-pod-container/create-hostprocess-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/create-hostprocess-pod/
heading: null
parent: okf-structure/tasks/configure-pod-container/create-hostprocess-pod
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/configure-pod-container/create-hostprocess-pod.md#prerequisites
word_count: 318
---

Windows HostProcess containers enable you to run containerized
workloads on a Windows host. These containers operate as
normal processes but have access to the host network namespace,
storage, and devices when given the appropriate user privileges.
HostProcess containers can be used to deploy network plugins,
storage configurations, device plugins, kube-proxy, and other
components to Windows nodes without the need for dedicated proxies or
the direct installation of host services.

Administrative tasks such as installation of security patches, event
log collection, and more can be performed without requiring cluster operators to
log onto each Windows node. HostProcess containers can run as any user that is
available on the host or is in the domain of the host machine, allowing administrators
to restrict resource access through user permissions. While neither filesystem or process
isolation are supported, a new volume is created on the host upon starting the container
to give it a clean and consolidated workspace. HostProcess containers can also be built on
top of existing Windows base images and do not inherit the same
compatibility requirements
as Windows server containers, meaning that the version of the base images does not need
to match that of the host. It is, however, recommended that you use the same base image
version as your Windows Server container workloads to ensure you do not have any unused
images taking up space on the node. HostProcess containers also support
volume mounts within the container volume.

### When should I use a Windows HostProcess container?

- When you need to perform tasks which require the networking namespace of the host.
HostProcess containers have access to the host's network interfaces and IP addresses.
- You need access to resources on the host such as the filesystem, event logs, etc.
- Installation of specific device drivers or Windows services.
- Consolidation of administrative tasks and security policies. This reduces the degree of
privileges needed by Windows nodes.
