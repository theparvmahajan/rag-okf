---
id: okf-structure/tutorials/security/cluster-level-pss.md#introduction
kind: section
title: Apply Pod Security Standards at the Cluster Level
source: tutorials/security/cluster-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/cluster-level-pss/
heading: null
parent: okf-structure/tutorials/security/cluster-level-pss
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/security/cluster-level-pss.md#prerequisites
word_count: 97
---

This tutorial applies only for new clusters.

Pod Security is an admission controller that carries out checks against the Kubernetes
Pod Security Standards when new pods are
created. It is a feature GA'ed in v1.25.
This tutorial shows you how to enforce the `baseline` Pod Security
Standard at the cluster level which applies a standard configuration
to all namespaces in a cluster.

To apply Pod Security Standards to specific namespaces, refer to
Apply Pod Security Standards at the namespace level.

If you are running a version of Kubernetes other than v,
check the documentation for that version.
