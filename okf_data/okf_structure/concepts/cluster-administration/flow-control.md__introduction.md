---
id: okf-structure/concepts/cluster-administration/flow-control.md#introduction
kind: section
title: API Priority and Fairness
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: null
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#enabling-disabling-api-priority-and-fairness
word_count: 244
---

Controlling the behavior of the Kubernetes API server in an overload situation
is a key task for cluster administrators. The kube-apiserver has some controls available
(i.e. the `--max-requests-inflight` and `--max-mutating-requests-inflight`
command-line flags) to limit the amount of outstanding work that will be
accepted, preventing a flood of inbound requests from overloading and
potentially crashing the API server, but these flags are not enough to ensure
that the most important requests get through in a period of high traffic.

The API Priority and Fairness feature (APF) is an alternative that improves upon
aforementioned max-inflight limitations. APF classifies
and isolates requests in a more fine-grained way. It also introduces
a limited amount of queuing, so that no requests are rejected in cases
of very brief bursts. Requests are dispatched from queues using a
fair queuing technique so that, for example, a poorly-behaved
controller need not
starve others (even at the same priority level).

This feature is designed to work well with standard controllers, which
use informers and react to failures of API requests with exponential
back-off, and other clients that also work this way.

Some requests classified as "long-running"—such as remote
command execution or log tailing—are not subject to the API
Priority and Fairness filter. This is also true for the
`--max-requests-inflight` flag without the API Priority and Fairness
feature enabled. API Priority and Fairness _does_ apply to **watch**
requests. When API Priority and Fairness is disabled, **watch** requests
are not subject to the `--max-requests-inflight` limit.
