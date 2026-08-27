---
id: okf-structure/tutorials/security/ns-level-pss.md#whatsnext
kind: section
title: Whatsnext
source: tutorials/security/ns-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/ns-level-pss/
heading: Whatsnext
parent: okf-structure/tutorials/security/ns-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/ns-level-pss.md#clean-up
next_sibling: null
word_count: 72
---

- Run a
  shell script
  to perform all the preceding steps all at once.

  1. Create kind cluster
  2. Create new namespace
  3. Apply `baseline` Pod Security Standard in `enforce` mode while applying
     `restricted` Pod Security Standard also in `warn` and `audit` mode.
  4. Create a new pod with the following pod security standards applied

- Pod Security Admission
- Pod Security Standards
- Apply Pod Security Standards at the cluster level
