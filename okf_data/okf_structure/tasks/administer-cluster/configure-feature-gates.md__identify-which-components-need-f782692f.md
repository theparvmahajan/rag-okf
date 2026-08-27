---
id: okf-structure/tasks/administer-cluster/configure-feature-gates.md#identify-which-components-need-the-feature-gate
kind: section
title: Identify which components need the feature gate
source: tasks/administer-cluster/configure-feature-gates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/
heading: Identify which components need the feature gate
parent: okf-structure/tasks/administer-cluster/configure-feature-gates
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#understand-feature-gate-maturity
next_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#configuration
word_count: 74
---

Different feature gates affect different Kubernetes components:

- Some features require enabling the gate on **multiple components** (e.g., API server and controller manager)
- Other features only need the gate on a **single component** (e.g., only kubelet)

The Feature Gates reference 
typically indicates which components are affected by each gate. All Kubernetes components 
share the same feature gate definitions, so all gates appear in help output, but only 
relevant gates affect each component's behavior.
