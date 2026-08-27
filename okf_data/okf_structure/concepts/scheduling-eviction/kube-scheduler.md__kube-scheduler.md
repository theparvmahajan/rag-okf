---
id: okf-structure/concepts/scheduling-eviction/kube-scheduler.md#kube-scheduler
kind: section
title: kube-scheduler
source: concepts/scheduling-eviction/kube-scheduler.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/
heading: kube-scheduler
parent: okf-structure/concepts/scheduling-eviction/kube-scheduler
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/kube-scheduler.md#scheduling-overview-scheduling
next_sibling: okf-structure/concepts/scheduling-eviction/kube-scheduler.md#whatsnext
word_count: 435
---

kube-scheduler
is the default scheduler for Kubernetes and runs as part of the
control plane.
kube-scheduler is designed so that, if you want and need to, you can
write your own scheduling component and use that instead.

Kube-scheduler selects an optimal node to run newly created or not yet
scheduled (unscheduled) pods. Since containers in pods - and pods themselves -
can have different requirements, the scheduler filters out any nodes that
don't meet a Pod's specific scheduling needs. Alternatively, the API lets
you specify a node for a Pod when you create it, but this is unusual
and is only done in special cases.

In a cluster, Nodes that meet the scheduling requirements for a Pod
are called _feasible_ nodes. If none of the nodes are suitable, the pod
remains unscheduled until the scheduler is able to place it.

The scheduler finds feasible Nodes for a Pod and then runs a set of
functions to score the feasible Nodes and picks a Node with the highest
score among the feasible ones to run the Pod. The scheduler then notifies
the API server about this decision in a process called _binding_.

Factors that need to be taken into account for scheduling decisions include
individual and collective resource requirements, hardware / software /
policy constraints, affinity and anti-affinity specifications, data
locality, inter-workload interference, and so on.

### Node selection in kube-scheduler {#kube-scheduler-implementation}

kube-scheduler selects a node for the pod in a 2-step operation:

1. Filtering
1. Scoring

The _filtering_ step finds the set of Nodes where it's feasible to
schedule the Pod. For example, the PodFitsResources filter checks whether a
candidate Node has enough available resources to meet a Pod's specific
resource requests. After this step, the node list contains any suitable
Nodes; often, there will be more than one. If the list is empty, that
Pod isn't (yet) schedulable.

In the _scoring_ step, the scheduler ranks the remaining nodes to choose
the most suitable Pod placement. The scheduler assigns a score to each Node
that survived filtering, basing this score on the active scoring rules.

Finally, kube-scheduler assigns the Pod to the Node with the highest ranking.
If there is more than one node with equal scores, kube-scheduler selects
one of these at random.

There are two supported ways to configure the filtering and scoring behavior
of the scheduler:

1. Scheduling Policies allow you to configure _Predicates_ for filtering and _Priorities_ for scoring.
1. Scheduling Profiles allow you to configure Plugins that implement different scheduling stages, including: `QueueSort`, `Filter`, `Score`, `Bind`, `Reserve`, `Permit`, and others. You can also configure the kube-scheduler to run different profiles.
