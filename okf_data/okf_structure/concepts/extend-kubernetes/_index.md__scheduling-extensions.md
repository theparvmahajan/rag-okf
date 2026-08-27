---
id: okf-structure/concepts/extend-kubernetes/_index.md#scheduling-extensions
kind: section
title: Scheduling extensions
source: concepts/extend-kubernetes/_index.md
url: https://kubernetes.io/docs/concepts/extend-kubernetes/
heading: Scheduling extensions
parent: okf-structure/concepts/extend-kubernetes/_index
children: []
prev_sibling: okf-structure/concepts/extend-kubernetes/_index.md#infrastructure-extensions
next_sibling: okf-structure/concepts/extend-kubernetes/_index.md#whatsnext
word_count: 150
---

The scheduler is a special type of controller that watches pods, and assigns
pods to nodes. The default scheduler can be replaced entirely, while
continuing to use other Kubernetes components, or
multiple schedulers
can run at the same time.

This is a significant undertaking, and almost all Kubernetes users find they
do not need to modify the scheduler.

You can control which scheduling plugins
are active, or associate sets of plugins with different named scheduler profiles.
You can also write your own plugin that integrates with one or more of the kube-scheduler's
extension points.

Finally, the built in `kube-scheduler` component supports a
webhook
that permits a remote HTTP backend (scheduler extension) to filter and / or prioritize
the nodes that the kube-scheduler chooses for a pod.

You can only affect node filtering
and node prioritization with a scheduler extender webhook; other extension points are
not available through the webhook integration.
