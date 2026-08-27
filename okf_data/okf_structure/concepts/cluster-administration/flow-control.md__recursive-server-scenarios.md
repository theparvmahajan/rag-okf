---
id: okf-structure/concepts/cluster-administration/flow-control.md#recursive-server-scenarios
kind: section
title: Recursive server scenarios
source: concepts/cluster-administration/flow-control.md
url: https://kubernetes.io/docs/concepts/cluster-administration/flow-control/
heading: Recursive server scenarios
parent: okf-structure/concepts/cluster-administration/flow-control
children: []
prev_sibling: okf-structure/concepts/cluster-administration/flow-control.md#enabling-disabling-api-priority-and-fairness
next_sibling: okf-structure/concepts/cluster-administration/flow-control.md#concepts
word_count: 259
---

API Priority and Fairness must be used carefully in recursive server
scenarios. These are scenarios in which some server A, while serving
a request, issues a subsidiary request to some server B. Perhaps
server B might even make a further subsidiary call back to server
A. In situations where Priority and Fairness control is applied to
both the original request and some subsidiary ones(s), no matter how
deep in the recursion, there is a danger of priority inversions and/or
deadlocks.

One example of recursion is when the `kube-apiserver` issues an
admission webhook call to server B, and while serving that call,
server B makes a further subsidiary request back to the
`kube-apiserver`. Another example of recursion is when an `APIService`
object directs the `kube-apiserver` to delegate requests about a
certain API group to a custom external server B (this is one of the
things called "aggregation").

When the original request is known to belong to a certain priority
level, and the subsidiary controlled requests are classified to higher
priority levels, this is one possible solution. When the original
requests can belong to any priority level, the subsidiary controlled
requests have to be exempt from Priority and Fairness limitation. One
way to do that is with the objects that configure classification and
handling, discussed below. Another way is to disable Priority and
Fairness on server B entirely, using the techniques discussed above. A
third way, which is the simplest to use when server B is not
`kube-apiserver`, is to build server B with Priority and Fairness
disabled in the code.
