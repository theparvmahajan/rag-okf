---
id: okf-structure/concepts/cluster-administration/dra.md#dra-driver-deployment-and-maintenance
kind: section
title: DRA driver deployment and maintenance
source: concepts/cluster-administration/dra.md
url: https://kubernetes.io/docs/concepts/cluster-administration/dra/
heading: DRA driver deployment and maintenance
parent: okf-structure/concepts/cluster-administration/dra
children: []
prev_sibling: okf-structure/concepts/cluster-administration/dra.md#separate-permissions-to-dra-related-apis
next_sibling: okf-structure/concepts/cluster-administration/dra.md#monitor-and-tune-components-for-higher-load-especially-in-high-scale-environments
word_count: 428
---

DRA drivers are third-party applications that run on each node of your cluster
to interface with the hardware of that node and Kubernetes' native DRA
components. The installation procedure depends on the driver you choose, but is
likely deployed as a DaemonSet to all or a selection of the nodes (using node
selectors or similar mechanisms) in your cluster.

### Use drivers with seamless upgrade if available

DRA drivers implement the `kubeletplugin` package
interface.
Your driver may support _seamless upgrades_ by implementing a property of this
interface that allows two versions of the same DRA driver to coexist for a short
time. This is only available for kubelet versions 1.33 and above and may not be
supported by your driver for heterogeneous clusters with attached nodes running
older versions of Kubernetes - check your driver's documentation to be sure.

If seamless upgrades are available for your situation, consider using it to
minimize scheduling delays when your driver updates.

If you cannot use seamless upgrades, during driver downtime for upgrades you may
observe that:
* Pods cannot start unless the claims they depend on were already prepared for
  use.
* Cleanup after the last pod which used a claim gets delayed until the driver is
  available again. The pod is not marked as terminated. This prevents reusing
  the resources used by the pod for other pods.
* Running pods will continue to run.

### Confirm your DRA driver exposes a liveness probe and utilize it

Your DRA driver likely implements a gRPC socket for healthchecks as part of DRA
driver good practices. The easiest way to utilize this grpc socket is to
configure it as a liveness probe for the DaemonSet deploying your DRA driver.
Your driver's documentation or deployment tooling may already include this, but
if you are building your configuration separately or not running your DRA driver
as a Kubernetes pod, be sure that your orchestration tooling restarts the DRA
driver on failed healthchecks to this grpc socket. Doing so will minimize any
accidental downtime of the DRA driver and give it more opportunities to self
heal, reducing scheduling delays or troubleshooting time.

### When draining a node, drain the DRA driver as late as possible

The DRA driver is responsible for unpreparing any devices that were allocated to
Pods, and if the DRA driver is drained before Pods with claims have been deleted, it will not be
able to finalize its cleanup. If you implement custom drain logic for nodes,
consider checking that there are no allocated/reserved ResourceClaim or
ResourceClaimTemplates before terminating the DRA driver itself.
