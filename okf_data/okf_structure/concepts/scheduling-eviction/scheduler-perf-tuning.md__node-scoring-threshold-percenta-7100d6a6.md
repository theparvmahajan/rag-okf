---
id: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#node-scoring-threshold-percentage-of-nodes-to-score
kind: section
title: Node scoring threshold {#percentage-of-nodes-to-score}
source: concepts/scheduling-eviction/scheduler-perf-tuning.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
heading: Node scoring threshold {#percentage-of-nodes-to-score}
parent: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#introduction
next_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#example
word_count: 195
---

To improve scheduling performance, the kube-scheduler can stop looking for
feasible nodes once it has found enough of them. In large clusters, this saves
time compared to a naive approach that would consider every node.

You specify a threshold for how many nodes are enough, as a whole number percentage
of all the nodes in your cluster. The kube-scheduler converts this into an
integer number of nodes. During scheduling, if the kube-scheduler has identified
enough feasible nodes to exceed the configured percentage, the kube-scheduler
stops searching for more feasible nodes and moves on to the
scoring phase.

How the scheduler iterates over Nodes
describes the process in detail.

### Default threshold

If you don't specify a threshold, Kubernetes calculates a figure using a
linear formula that yields 50% for a 100-node cluster and yields 10%
for a 5000-node cluster. The lower bound for the automatic value is 5%.

This means that the kube-scheduler always scores at least 5% of your cluster no
matter how large the cluster is, unless you have explicitly set
`percentageOfNodesToScore` to be smaller than 5.

If you want the scheduler to score all nodes in your cluster, set
`percentageOfNodesToScore` to 100.
