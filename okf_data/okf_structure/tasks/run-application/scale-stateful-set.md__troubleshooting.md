---
id: okf-structure/tasks/run-application/scale-stateful-set.md#troubleshooting
kind: section
title: Troubleshooting
source: tasks/run-application/scale-stateful-set.md
url: https://kubernetes.io/docs/tasks/run-application/scale-stateful-set/
heading: Troubleshooting
parent: okf-structure/tasks/run-application/scale-stateful-set
children: []
prev_sibling: okf-structure/tasks/run-application/scale-stateful-set.md#scaling-statefulsets
next_sibling: okf-structure/tasks/run-application/scale-stateful-set.md#whatsnext
word_count: 196
---

### Scaling down does not work right

You cannot scale down a StatefulSet when any of the stateful Pods it manages is
unhealthy. Scaling down only takes place after those stateful Pods become running and ready.

If spec.replicas > 1, Kubernetes cannot determine the reason for an unhealthy Pod.
It might be the result of a permanent fault or of a transient fault. A transient
fault can be caused by a restart required by upgrading or maintenance.

If the Pod is unhealthy due to a permanent fault, scaling
without correcting the fault may lead to a state where the StatefulSet membership
drops below a certain minimum number of replicas that are needed to function
correctly. This may cause your StatefulSet to become unavailable.

If the Pod is unhealthy due to a transient fault and the Pod might become available again,
the transient error may interfere with your scale-up or scale-down operation. Some distributed
databases have issues when nodes join and leave at the same time. It is better
to reason about scaling operations at the application level in these cases, and
perform scaling only when you are sure that your stateful application cluster is
completely healthy.
