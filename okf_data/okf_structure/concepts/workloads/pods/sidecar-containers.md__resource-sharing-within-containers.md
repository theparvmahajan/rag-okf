---
id: okf-structure/concepts/workloads/pods/sidecar-containers.md#resource-sharing-within-containers
kind: section
title: Resource sharing within containers
source: concepts/workloads/pods/sidecar-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
heading: Resource sharing within containers
parent: okf-structure/concepts/workloads/pods/sidecar-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#differences-from-init-containers
next_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#whatsnext
word_count: 207
---

This section is also present in the init containers page.
If you're editing this section, change both places.

Given the order of execution for init, sidecar and app containers, the following rules
for resource usage apply:

* The highest of any particular resource request or limit defined on all init
  containers is the *effective init request/limit*. If any resource has no
  resource limit specified this is considered as the highest limit.
* The Pod's *effective request/limit* for a resource is the sum of
pod overhead and the higher of:
  * the sum of all non-init containers(app and sidecar containers) request/limit for a
  resource
  * the effective init request/limit for a resource
* Scheduling is done based on effective requests/limits, which means
  init containers can reserve resources for initialization that are not used
  during the life of the Pod.
* The QoS (quality of service) tier of the Pod's *effective QoS tier* is the
  QoS tier for all init, sidecar and app containers alike.

Quota and limits are applied based on the effective Pod request and
limit.

### Sidecar containers and Linux cgroups {#cgroups}

On Linux, resource allocations for Pod level control groups (cgroups) are based on the effective Pod
request and limit, the same as the scheduler.
