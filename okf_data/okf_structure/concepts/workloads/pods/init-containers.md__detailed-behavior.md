---
id: okf-structure/concepts/workloads/pods/init-containers.md#detailed-behavior
kind: section
title: Detailed behavior
source: concepts/workloads/pods/init-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
heading: Detailed behavior
parent: okf-structure/concepts/workloads/pods/init-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/init-containers.md#using-init-containers
next_sibling: okf-structure/concepts/workloads/pods/init-containers.md#whatsnext
word_count: 688
---

During Pod startup, the kubelet delays running init containers until the networking
and storage are ready. Then the kubelet runs the Pod's init containers in the order
they appear in the Pod's spec.

Each init container must exit successfully before
the next container starts. If a container fails to start due to the runtime or
exits with failure, it is retried according to the Pod `restartPolicy`. However,
if the Pod `restartPolicy` is set to Always, the init containers use
`restartPolicy` OnFailure.

A Pod cannot be `Ready` until all init containers have succeeded. The ports on an
init container are not aggregated under a Service. A Pod that is initializing
is in the `Pending` state but should have a condition `Initialized` set to false.

If the Pod restarts, or is restarted, all init containers
must execute again.

Changes to the init container spec are limited to the container image field.
Directly altering the `image` field of  an init container does _not_ restart the
Pod or trigger its recreation. If the Pod has yet to start, that change may
have an effect on how the Pod boots up.

For a pod template
you can typically change any field for an init container; the impact of making
that change depends on where the pod template is used.

Because init containers can be restarted, retried, or re-executed, init container
code should be idempotent. In particular, code that writes into any `emptyDir` volume
should be prepared for the possibility that an output file already exists.

Init containers have all of the fields of an app container. However, Kubernetes
prohibits `readinessProbe` from being used because init containers cannot
define readiness distinct from completion. This is enforced during validation.

Use `activeDeadlineSeconds` on the Pod to prevent init containers from failing forever.
The active deadline includes init containers.
However it is recommended to use `activeDeadlineSeconds` only if teams deploy their application
as a Job, because `activeDeadlineSeconds` has an effect even after initContainer finished.
The Pod which is already running correctly would be killed by `activeDeadlineSeconds` if you set.

The name of each app and init container in a Pod must be unique; a
validation error is thrown for any container sharing a name with another.

### Resource sharing within containers

Given the order of execution for init, sidecar and app containers, the following rules
for resource usage apply:

* The highest of any particular resource request or limit defined on all init
  containers is the *effective init request/limit*. If any resource has no
  resource limit specified this is considered as the highest limit.
* The Pod's *effective request/limit* for a resource is the higher of:
  * the sum of all app containers request/limit for a resource
  * the effective init request/limit for a resource
* Scheduling is done based on effective requests/limits, which means
  init containers can reserve resources for initialization that are not used
  during the life of the Pod.
* The QoS (quality of service) tier of the Pod's *effective QoS tier* is the
  QoS tier for init containers and app containers alike.

Quota and limits are applied based on the effective Pod request and
limit.

### Init containers and Linux cgroups {#cgroups}

On Linux, resource allocations for Pod level control groups (cgroups) are based on the effective Pod
request and limit, the same as the scheduler.

This section also present under sidecar containers page.
If you're editing this section, change both places.

### Pod restart reasons

A Pod can restart, causing re-execution of init containers, for the following
reasons:

* The Pod infrastructure container is restarted. This is uncommon and would
  have to be done by someone with root access to nodes.
* All containers in a Pod are terminated while `restartPolicy` is set to Always,
  forcing a restart, and the init container completion record has been lost due
  to garbage collection.

The Pod will not be restarted when the init container image is changed, or the
init container completion record has been lost due to garbage collection. This
applies for Kubernetes v1.20 and later. If you are using an earlier version of
Kubernetes, consult the documentation for the version you are using.
