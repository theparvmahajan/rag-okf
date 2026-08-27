---
id: okf-structure/tasks/administer-cluster/declare-network-policy.md#test-access-to-the-service-when-access-label-is-not-defined
kind: section
title: Test access to the service when access label is not defined
source: tasks/administer-cluster/declare-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/
heading: Test access to the service when access label is not defined
parent: okf-structure/tasks/administer-cluster/declare-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#assign-the-policy-to-the-service
next_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#define-access-label-and-test-again
word_count: 51
---

When you attempt to access the `nginx` Service from a Pod without the correct labels, the request times out:

```console
kubectl run busybox --rm -ti --image=busybox -- /bin/sh
```

In your shell, run the command:

```shell
wget --spider --timeout=1 nginx
```

```none
Connecting to nginx (10.100.0.16:80)
wget: download timed out
```
