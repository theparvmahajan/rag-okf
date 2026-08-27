---
id: okf-structure/tutorials/security/cluster-level-pss.md#clean-up
kind: section
title: Clean up
source: tutorials/security/cluster-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/cluster-level-pss/
heading: Clean up
parent: okf-structure/tutorials/security/cluster-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/cluster-level-pss.md#set-modes-versions-and-standards
next_sibling: okf-structure/tutorials/security/cluster-level-pss.md#whatsnext
word_count: 27
---

Now delete the clusters which you created above by running the following command:

```shell
kind delete cluster --name psa-with-cluster-pss
```
```shell
kind delete cluster --name psa-wo-cluster-pss
```
