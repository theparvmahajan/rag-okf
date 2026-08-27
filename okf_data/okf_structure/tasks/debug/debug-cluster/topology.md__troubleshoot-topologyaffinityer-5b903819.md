---
id: okf-structure/tasks/debug/debug-cluster/topology.md#troubleshoot-topologyaffinityerror-topologyaffinityerror
kind: section
title: Troubleshoot `TopologyAffinityError` {#TopologyAffinityError}
source: tasks/debug/debug-cluster/topology.md
url: https://kubernetes.io/docs/tasks/debug/debug-cluster/topology/
heading: Troubleshoot `TopologyAffinityError` {#TopologyAffinityError}
parent: okf-structure/tasks/debug/debug-cluster/topology
children: []
prev_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#sources-of-troubleshooting-information
next_sibling: okf-structure/tasks/debug/debug-cluster/topology.md#examine-system-logs
word_count: 88
---

This error typically occurs in the following situations:

* a node has not enough resources available to satisfy the pod's request
* the pod's request is rejected due to particular Topology Manager policy constraints

The error appears in the status of a pod:

```shell
kubectl get pods
```

```none
NAME         READY   STATUS                  RESTARTS   AGE
guaranteed   0/1     TopologyAffinityError   0          113s
```

Use `kubectl describe pod <id>` or `kubectl events` to obtain a detailed error message:

```none
Warning  TopologyAffinityError  10m   kubelet, dell8  Resources cannot be allocated with Topology locality
```
