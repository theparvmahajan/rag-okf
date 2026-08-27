---
id: okf-structure/tutorials/security/cluster-level-pss.md#whatsnext
kind: section
title: Whatsnext
source: tutorials/security/cluster-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/cluster-level-pss/
heading: Whatsnext
parent: okf-structure/tutorials/security/cluster-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/cluster-level-pss.md#clean-up
next_sibling: null
word_count: 90
---

- Run a
  shell script
  to perform all the preceding steps at once:
  1. Create a Pod Security Standards based cluster level Configuration
  2. Create a file to let API server consume this configuration
  3. Create a cluster that creates an API server with this configuration
  4. Set kubectl context to this new cluster
  5. Create a minimal pod yaml file
  6. Apply this file to create a Pod in the new cluster
- Pod Security Admission
- Pod Security Standards
- Apply Pod Security Standards at the namespace level
