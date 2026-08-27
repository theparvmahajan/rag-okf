---
id: okf-structure/concepts/workloads/pods/_index.md#resource-sharing-and-communication
kind: section
title: Resource sharing and communication
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Resource sharing and communication
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#pod-update-and-replacement
next_sibling: okf-structure/concepts/workloads/pods/_index.md#pod-security-settings-pod-security
word_count: 258
---

Pods enable data sharing and communication among their constituent
containers.

### Storage in Pods {#pod-storage}

A Pod can specify a set of shared storage
volumes. All containers
in the Pod can access the shared volumes, allowing those containers to
share data. Volumes also allow persistent data in a Pod to survive
in case one of the containers within needs to be restarted. See
Storage for more information on how
Kubernetes implements shared storage and makes it available to Pods.

### Pod networking

Each Pod is assigned a unique IP address for each address family. Every
container in a Pod shares the network namespace, including the IP address and
network ports. Inside a Pod (and **only** then), the containers that belong to the Pod
can communicate with one another using `localhost`. When containers in a Pod communicate
with entities *outside the Pod*,
they must coordinate how they use the shared network resources (such as ports).
Within a Pod, containers share an IP address and port space, and
can find each other via `localhost`. The containers in a Pod can also communicate
with each other using standard inter-process communications like SystemV semaphores
or POSIX shared memory.  Containers in different Pods have distinct IP addresses
and can not communicate by OS-level IPC without special configuration.
Containers that want to interact with a container running in a different Pod can
use IP networking to communicate.

Containers within the Pod see the system hostname as being the same as the configured
`name` for the Pod. There's more about this in the networking
section.
