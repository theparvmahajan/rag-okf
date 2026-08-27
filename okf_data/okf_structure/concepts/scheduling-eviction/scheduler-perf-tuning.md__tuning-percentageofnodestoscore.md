---
id: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#tuning-percentageofnodestoscore
kind: section
title: Tuning percentageOfNodesToScore
source: concepts/scheduling-eviction/scheduler-perf-tuning.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
heading: Tuning percentageOfNodesToScore
parent: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#example
next_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#how-the-scheduler-iterates-over-nodes
word_count: 244
---

`percentageOfNodesToScore` must be a value between 1 and 100 with the default
value being calculated based on the cluster size. There is also a hardcoded
minimum value of 100 nodes.

In clusters with less than 100 feasible nodes, the scheduler still
checks all the nodes because there are not enough feasible nodes to stop
the scheduler's search early.

In a small cluster, if you set a low value for `percentageOfNodesToScore`, your
change will have no or little effect, for a similar reason.

If your cluster has several hundred Nodes or fewer, leave this configuration option
at its default value. Making changes is unlikely to improve the
scheduler's performance significantly.

An important detail to consider when setting this value is that when a smaller
number of nodes in a cluster are checked for feasibility, some nodes are not
sent to be scored for a given Pod. As a result, a Node which could possibly
score a higher value for running the given Pod might not even be passed to the
scoring phase. This would result in a less than ideal placement of the Pod.

You should avoid setting `percentageOfNodesToScore` very low so that kube-scheduler
does not make frequent, poor Pod placement decisions. Avoid setting the
percentage to anything below 10%, unless the scheduler's throughput is critical
for your application and the score of nodes is not important. In other words, you
prefer to run the Pod on any Node as long as it is feasible.
