---
id: okf-structure/concepts/workloads/pods/disruptions.md#how-to-perform-disruptive-actions-on-your-cluster
kind: section
title: How to perform Disruptive Actions on your Cluster
source: concepts/workloads/pods/disruptions.md
url: https://kubernetes.io/docs/concepts/workloads/pods/disruptions/
heading: How to perform Disruptive Actions on your Cluster
parent: okf-structure/concepts/workloads/pods/disruptions
children: []
prev_sibling: okf-structure/concepts/workloads/pods/disruptions.md#separating-cluster-owner-and-application-owner-roles
next_sibling: okf-structure/concepts/workloads/pods/disruptions.md#whatsnext
word_count: 112
---

If you are a Cluster Administrator, and you need to perform a disruptive action on all
the nodes in your cluster, such as a node or system software upgrade, here are some options:

- Accept downtime during the upgrade.
- Failover to another complete replica cluster.
   -  No downtime, but may be costly both for the duplicated nodes
     and for human effort to orchestrate the switchover.
- Write disruption tolerant applications and use PDBs.
   - No downtime.
   - Minimal resource duplication.
   - Allows more automation of cluster administration.
   - Writing disruption-tolerant applications is tricky, but the work to tolerate voluntary
     disruptions largely overlaps with work to support autoscaling and tolerating
     involuntary disruptions.
