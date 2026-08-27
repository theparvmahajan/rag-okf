---
id: okf-structure/tasks/run-application/configure-pdb.md#think-about-how-your-application-reacts-to-disruptions
kind: section
title: Think about how your application reacts to disruptions
source: tasks/run-application/configure-pdb.md
url: https://kubernetes.io/docs/tasks/run-application/configure-pdb/
heading: Think about how your application reacts to disruptions
parent: okf-structure/tasks/run-application/configure-pdb
children: []
prev_sibling: okf-structure/tasks/run-application/configure-pdb.md#identify-an-application-to-protect
next_sibling: okf-structure/tasks/run-application/configure-pdb.md#specifying-a-poddisruptionbudget
word_count: 399
---

Decide how many instances can be down at the same time for a short period
due to a voluntary disruption.

- Stateless frontends:
  - Concern: don't reduce serving capacity by more than 10%.
    - Solution: use PDB with minAvailable 90% for example.
- Single-instance Stateful Application:
  - Concern: do not terminate this application without talking to me.
    - Possible Solution 1: Do not use a PDB and tolerate occasional downtime.
    - Possible Solution 2: Set PDB with maxUnavailable=0. Have an understanding
      (outside of Kubernetes) that the cluster operator needs to consult you before
      termination. When the cluster operator contacts you, prepare for downtime,
      and then delete the PDB to indicate readiness for disruption. Recreate afterwards.
- Multiple-instance Stateful application such as Consul, ZooKeeper, or etcd:
  - Concern: Do not reduce number of instances below quorum, otherwise writes fail.
    - Possible Solution 1: set maxUnavailable to 1 (works with varying scale of application).
    - Possible Solution 2: set minAvailable to quorum-size (e.g. 3 when scale is 5).
      (Allows more disruptions at once).
- Restartable Batch Job:
  - Concern: Job needs to complete in case of voluntary disruption.
    - Possible solution: Do not create a PDB. The Job controller will create a replacement pod.

### Rounding logic when specifying percentages

Values for `minAvailable` or `maxUnavailable` can be expressed as integers or as a percentage.

- When you specify an integer, it represents a number of Pods. For instance, if you set
  `minAvailable` to 10, then 10 Pods must always be available, even during a disruption.
- When you specify a percentage by setting the value to a string representation of a
  percentage (eg. `"50%"`), it represents a percentage of total Pods. For instance, if
  you set `minAvailable` to `"50%"`, then at least 50% of the Pods remain available
  during a disruption.

When you specify the value as a percentage, it may not map to an exact number of Pods.
For example, if you have 7 Pods and you set `minAvailable` to `"50%"`, it's not
immediately obvious whether that means 3 Pods or 4 Pods must be available. Kubernetes
rounds up to the nearest integer, so in this case, 4 Pods must be available. When you
specify the value `maxUnavailable` as a percentage, Kubernetes rounds up the number of
Pods that may be disrupted. Thereby a disruption can exceed your defined
`maxUnavailable` percentage. You can examine the
code
that controls this behavior.
