---
id: okf-structure/tasks/administer-cluster/safely-drain-node.md#use-kubectl-drain-to-remove-a-node-from-service
kind: section
title: Use `kubectl drain` to remove a node from service
source: tasks/administer-cluster/safely-drain-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
heading: Use `kubectl drain` to remove a node from service
parent: okf-structure/tasks/administer-cluster/safely-drain-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#optional-configure-a-disruption-budget-configure-poddisruptionbudget
next_sibling: okf-structure/tasks/administer-cluster/safely-drain-node.md#draining-multiple-nodes-in-parallel
word_count: 384
---

You can use `kubectl drain` to safely evict all of your pods from a
node before you perform maintenance on the node (e.g. kernel upgrade,
hardware maintenance, etc.). Safe evictions allow the pod's containers
to gracefully terminate
and will respect the PodDisruptionBudgets you have specified.

By default `kubectl drain` ignores certain system pods on the node
that cannot be killed; see
the kubectl drain
documentation for more details.

When `kubectl drain` returns successfully, that indicates that all of
the pods (except the ones excluded as described in the previous paragraph)
have been safely evicted (respecting the desired graceful termination period,
and respecting the PodDisruptionBudget you have defined). It is then safe to
bring down the node by powering down its physical machine or, if running on a
cloud platform, deleting its virtual machine.

If any new Pods tolerate the `node.kubernetes.io/unschedulable` taint, then those Pods
might be scheduled to the node you have drained. Avoid tolerating that taint other than
for DaemonSets.

If you or another API user directly set the `nodeName`
field for a Pod (bypassing the scheduler), then the Pod is bound to the specified node
and will run there, even though you have drained that node and marked it unschedulable.

First, identify the name of the node you wish to drain. You can list all of the nodes in your cluster with

```shell
kubectl get nodes
```

Next, tell Kubernetes to drain the node:

```shell
kubectl drain --ignore-daemonsets <node name>
```

If there are pods managed by a DaemonSet, you will need to specify
`--ignore-daemonsets` with `kubectl` to successfully drain the node. The `kubectl drain` subcommand on its own does not actually drain
a node of its DaemonSet pods:
the DaemonSet controller (part of the control plane) immediately replaces missing Pods with
new equivalent Pods. The DaemonSet controller also creates Pods that ignore unschedulable
taints, which allows the new Pods to launch onto a node that you are draining.

Once it returns (without giving an error), you can power down the node
(or equivalently, if on a cloud platform, delete the virtual machine backing the node).
If you leave the node in the cluster during the maintenance operation, you need to run

```shell
kubectl uncordon <node name>
```
afterwards to tell Kubernetes that it can resume scheduling new pods onto the node.
