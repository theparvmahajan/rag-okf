---
id: okf-structure/tasks/administer-cluster/declare-network-policy.md#define-access-label-and-test-again
kind: section
title: Define access label and test again
source: tasks/administer-cluster/declare-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/
heading: Define access label and test again
parent: okf-structure/tasks/administer-cluster/declare-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#test-access-to-the-service-when-access-label-is-not-defined
next_sibling: null
word_count: 48
---

You can create a Pod with the correct labels to see that the request is allowed:

```console
kubectl run busybox --rm -ti --labels="access=true" --image=busybox -- /bin/sh
```

In your shell, run the command:

```shell
wget --spider --timeout=1 nginx
```

```none
Connecting to nginx (10.100.0.16:80)
remote file exists
```
