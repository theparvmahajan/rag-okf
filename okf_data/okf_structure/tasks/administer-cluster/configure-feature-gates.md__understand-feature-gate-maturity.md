---
id: okf-structure/tasks/administer-cluster/configure-feature-gates.md#understand-feature-gate-maturity
kind: section
title: Understand feature gate maturity
source: tasks/administer-cluster/configure-feature-gates.md
url: https://kubernetes.io/docs/tasks/administer-cluster/configure-feature-gates/
heading: Understand feature gate maturity
parent: okf-structure/tasks/administer-cluster/configure-feature-gates
children: []
prev_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/configure-feature-gates.md#identify-which-components-need-the-feature-gate
word_count: 50
---

Before enabling a feature gate, check the Feature Gates reference 
for the feature's maturity level:

- **Alpha**: Disabled by default, may be buggy. Use only in test clusters.
- **Beta**: Usually enabled by default, well-tested.
- **GA**: Always enabled by default; can sometimes be disabled for one release after GA.
