---
id: okf-structure/tutorials/security/ns-level-pss.md#introduction
kind: section
title: Apply Pod Security Standards at the Namespace Level
source: tutorials/security/ns-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/ns-level-pss/
heading: null
parent: okf-structure/tutorials/security/ns-level-pss
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/security/ns-level-pss.md#prerequisites
word_count: 74
---

This tutorial applies only for new clusters.

Pod Security Admission is an admission controller that applies 
Pod Security Standards 
when pods are created.  It is a feature GA'ed in v1.25.
In this tutorial, you will enforce the `baseline` Pod Security Standard,
one namespace at a time.

You can also apply Pod Security Standards to multiple namespaces at once at the cluster
level. For instructions, refer to
Apply Pod Security Standards at the cluster level.
