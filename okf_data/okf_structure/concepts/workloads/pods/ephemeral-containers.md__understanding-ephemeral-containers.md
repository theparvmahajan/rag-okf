---
id: okf-structure/concepts/workloads/pods/ephemeral-containers.md#understanding-ephemeral-containers
kind: section
title: Understanding ephemeral containers
source: concepts/workloads/pods/ephemeral-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
heading: Understanding ephemeral containers
parent: okf-structure/concepts/workloads/pods/ephemeral-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/ephemeral-containers.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/ephemeral-containers.md#uses-for-ephemeral-containers
word_count: 241
---

Pods are the fundamental building
block of Kubernetes applications. Since Pods are intended to be disposable and
replaceable, you cannot add a container to a Pod once it has been created.
Instead, you usually delete and replace Pods in a controlled fashion using
deployments.

Sometimes it's necessary to inspect the state of an existing Pod, however, for
example to troubleshoot a hard-to-reproduce bug. In these cases you can run
an ephemeral container in an existing Pod to inspect its state and run
arbitrary commands.

### What is an ephemeral container?

Ephemeral containers differ from other containers in that they lack guarantees
for resources or execution, and they will never be automatically restarted, so
they are not appropriate for building applications.  Ephemeral containers are
described using the same `ContainerSpec` as regular containers, but many fields
are incompatible and disallowed for ephemeral containers.

- Ephemeral containers may not have ports, so fields such as `ports`,
  `livenessProbe`, `readinessProbe` are disallowed.
- Pod resource allocations are immutable, so setting `resources` is disallowed.
- For a complete list of allowed fields, see the EphemeralContainer reference
  documentation.

Ephemeral containers are created using a special `ephemeralcontainers` handler
in the API rather than by adding them directly to `pod.spec`, so it's not
possible to add an ephemeral container using `kubectl edit`.

Like regular containers, you may not change or remove an ephemeral container
after you have added it to a Pod.

Ephemeral containers are not supported by static pods.
