---
id: okf-structure/concepts/workloads/pods/init-containers.md#understanding-init-containers
kind: section
title: Understanding init containers
source: concepts/workloads/pods/init-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/
heading: Understanding init containers
parent: okf-structure/concepts/workloads/pods/init-containers
children: []
prev_sibling: okf-structure/concepts/workloads/pods/init-containers.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/init-containers.md#using-init-containers
word_count: 408
---

A Pod can have multiple containers
running apps within it, but it can also have one or more init containers, which are run
before the app containers are started.

Init containers are exactly like regular containers, except:

* Init containers always run to completion.
* Each init container must complete successfully before the next one starts.

If a Pod's init container fails, the kubelet repeatedly restarts that init container until it succeeds.
However, if the Pod has a `restartPolicy` of Never, and an init container fails during startup of that Pod, Kubernetes treats the overall Pod as failed.

To specify an init container for a Pod, add the `initContainers` field into
the Pod specification,
as an array of `container` items (similar to the app `containers` field and its contents).
See Container in the
API reference for more details.

The status of the init containers is returned in `.status.initContainerStatuses`
field as an array of the container statuses (similar to the `.status.containerStatuses`
field).

### Differences from regular containers

Init containers support all the fields and features of app containers,
including resource limits, volumes, and security settings. However, the
resource requests and limits for an init container are handled differently,
as documented in Resource sharing within containers.

Regular init containers (in other words: excluding sidecar containers) do not support the
`lifecycle`, `livenessProbe`, `readinessProbe`, or `startupProbe` fields. Init containers
must run to completion before the Pod can be ready; sidecar containers continue running
during a Pod's lifetime, and _do_ support some probes. See sidecar container
for further details about sidecar containers.

If you specify multiple init containers for a Pod, kubelet runs each init
container sequentially. Each init container must succeed before the next can run.
When all of the init containers have run to completion, kubelet initializes
the application containers for the Pod and runs them as usual.

### Differences from sidecar containers

Init containers run and complete their tasks before the main application container starts.
Unlike sidecar containers,
init containers are not continuously running alongside the main containers.

Init containers run to completion sequentially, and the main container does not start
until all the init containers have successfully completed.

init containers do not support `lifecycle`, `livenessProbe`, `readinessProbe`, or
`startupProbe` whereas sidecar containers support all these probes to control their lifecycle.

Init containers share the same resources (CPU, memory, network) with the main application
containers but do not interact directly with them. They can, however, use shared volumes
for data exchange.
