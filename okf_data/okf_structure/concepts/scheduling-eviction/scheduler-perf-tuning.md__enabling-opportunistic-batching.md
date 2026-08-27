---
id: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#enabling-opportunistic-batching
kind: section
title: Enabling Opportunistic Batching
source: concepts/scheduling-eviction/scheduler-perf-tuning.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/scheduler-perf-tuning/
heading: Enabling Opportunistic Batching
parent: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#how-the-scheduler-iterates-over-nodes
next_sibling: okf-structure/concepts/scheduling-eviction/scheduler-perf-tuning.md#whatsnext
word_count: 261
---

When scheduling large workloads, pod definitions are typically identical and require the scheduler
to perform the same operations over and over again. The Opportunistic Batching
feature allows the scheduler to reuse the filtering and scoring results between scheduling cycles
which greatly speeds up the scheduling process.

Basically, this feature works like:
1. The scheduler schedules pod-1 and caches the scheduling result.
1. The scheduler schedules pod-2, 3, ... with the cached results.
1. The cache expires after 0.5 second. The scheduler schedules the next pod which builds a new cache.

Pods with equivalent scheduling constraints have to come to the scheduling cycle back to back. When the scheduler schedules a pod with different constraints, the cache is not used, but replaced with a new one.

We apply this batching scheduling to specific pods that:
1. Don't have inter pod affinity/anti-affinity
1. Don't have topology spread constraints
1. Don't have DRA (i.e., don't have any Resource Claims)
1. Don't request extended resources that are backed by DRA
1. Scheduled exclusively on nodes (i.e., placing more than one pod on one node invalidates the cache)

Also, to enable this feature, the scheduler configuration needs to:
1. Disable default topology spread (set empty)
1. Set `IgnorePreferredTermsOfExistingPods` of InterPodAffinityArgs
to `true` to make the batching more efficient

Note that whenever:
1. Existing pods use pod affinity constraints that match any of the scheduled pods' labels, the feature may bring no benefit
1. Custom plugins are used, they need to implement the Signature extension point

The restrictions and conditions are expected to evolve in future releases.
