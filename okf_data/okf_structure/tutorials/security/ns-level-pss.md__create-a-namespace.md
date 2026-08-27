---
id: okf-structure/tutorials/security/ns-level-pss.md#create-a-namespace
kind: section
title: Create a namespace
source: tutorials/security/ns-level-pss.md
url: https://kubernetes.io/docs/tutorials/security/ns-level-pss/
heading: Create a namespace
parent: okf-structure/tutorials/security/ns-level-pss
children: []
prev_sibling: okf-structure/tutorials/security/ns-level-pss.md#create-cluster
next_sibling: okf-structure/tutorials/security/ns-level-pss.md#enable-pod-security-standards-checking-for-that-namespace
word_count: 22
---

Create a new namespace called `example`:

```shell
kubectl create ns example
```

The output is similar to this:

```
namespace/example created
```
