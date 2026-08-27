---
id: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#introduction
kind: section
title: Scheduler Performance Tuning
source: concepts/scheduling-eviction/scheduler-perf-tuning.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
heading: null
parent: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#node-scoring-threshold-percentage-of-nodes-to-score
word_count: 250
---

kube-scheduler
is the Kubernetes default scheduler. It is responsible for placement of Pods
on Nodes in a cluster.

Nodes in a cluster that meet the scheduling requirements of a Pod are
called _feasible_ Nodes for the Pod. The scheduler finds feasible Nodes
for a Pod and then runs a set of functions to score the feasible Nodes,
picking a Node with the highest score among the feasible ones to run
the Pod. The scheduler then notifies the API server about this decision
in a process called _Binding_.

This page explains performance tuning optimizations that are relevant for
large Kubernetes clusters.

In large clusters, you can tune the scheduler's behaviour balancing
scheduling outcomes between latency (new Pods are placed quickly) and
accuracy (the scheduler rarely makes poor placement decisions).

You configure this tuning setting via kube-scheduler setting
`percentageOfNodesToScore`. This KubeSchedulerConfiguration setting determines
a threshold for scheduling nodes in your cluster.

### Setting the threshold

The `percentageOfNodesToScore` option accepts whole numeric values between 0
and 100. The value 0 is a special number which indicates that the kube-scheduler
should use its compiled-in default.
If you set `percentageOfNodesToScore` above 100, kube-scheduler acts as if you
had set a value of 100.

To change the value, edit the
kube-scheduler configuration file
and then restart the scheduler.
In many cases, the configuration file can be found at `/etc/kubernetes/config/kube-scheduler.yaml`.

After you have made this change, you can run

```bash
kubectl get pods -n kube-system | grep kube-scheduler
```

to verify that the kube-scheduler component is healthy.
