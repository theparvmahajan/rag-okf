---
id: okf-structure/tasks/administer-cluster/declare-network-policy.md#test-the-service-by-accessing-it-from-another-pod
kind: section
title: Test the service by accessing it from another Pod
source: tasks/administer-cluster/declare-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/
heading: Test the service by accessing it from another Pod
parent: okf-structure/tasks/administer-cluster/declare-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#create-an-nginx-deployment-and-expose-it-via-a-service
next_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#limit-access-to-the-nginx-service
word_count: 61
---

You should be able to access the new `nginx` service from other Pods. To access the `nginx` Service from another Pod in the `default` namespace, start a busybox container:

```console
kubectl run busybox --rm -ti --image=busybox -- /bin/sh
```

In your shell, run the following command:

```shell
wget --spider --timeout=1 nginx
```

```none
Connecting to nginx (10.100.0.16:80)
remote file exists
```
