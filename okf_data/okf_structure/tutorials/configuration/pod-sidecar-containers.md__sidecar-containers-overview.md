---
id: okf-structure/tutorials/configuration/pod-sidecar-containers.md#sidecar-containers-overview
kind: section
title: Sidecar containers overview
source: tutorials/configuration/pod-sidecar-containers.md
url: https://kubernetes.io/docs/tutorials/configuration/pod-sidecar-containers/
heading: Sidecar containers overview
parent: okf-structure/tutorials/configuration/pod-sidecar-containers
children: []
prev_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#prerequisites
next_sibling: okf-structure/tutorials/configuration/pod-sidecar-containers.md#benefits-of-a-built-in-sidecar-container
word_count: 204
---

Sidecar containers are secondary containers that run along with the main
application container within the same Pod.
These containers are used to enhance or to extend the functionality of the primary _app
container_ by providing additional services, or functionalities such as logging, monitoring,
security, or data synchronization, without directly altering the primary application code.
You can read more in the Sidecar containers
concept page.

The concept of sidecar containers is not new and there are multiple implementations of this concept.
As well as sidecar containers that you, the person defining the Pod, want to run, you can also find
that some addons modify Pods - before the Pods
start running - so that there are extra sidecar containers. The mechanisms to _inject_ those extra
sidecars are often mutating webhooks.
For example, a service mesh addon might inject a sidecar that configures mutual TLS and encryption
in transit between different Pods.

While the concept of sidecar containers is not new,
the native implementation of this feature in Kubernetes, however, is new. And as with every new feature,
adopting this feature may present certain challenges.

This tutorial explores challenges and solutions that can be experienced by end users as well as
by authors of sidecar containers.
