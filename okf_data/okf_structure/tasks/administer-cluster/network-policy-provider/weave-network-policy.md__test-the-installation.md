---
id: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy.md#test-the-installation
kind: section
title: Test the installation
source: tasks/administer-cluster/network-policy-provider/weave-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/weave-network-policy/
heading: Test the installation
parent: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy.md#install-the-weave-net-addon
next_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/weave-network-policy.md#whatsnext
word_count: 84
---

Verify that the weave works.

Enter the following command:

```shell
kubectl get pods -n kube-system -o wide
```

The output is similar to this:

```
NAME                                    READY     STATUS    RESTARTS   AGE       IP              NODE
weave-net-1t1qg                         2/2       Running   0          9d        192.168.2.10    worknode3
weave-net-231d7                         2/2       Running   1          7d        10.2.0.17       worknodegpu
weave-net-7nmwt                         2/2       Running   3          9d        192.168.2.131   masternode
weave-net-pmw8w                         2/2       Running   0          9d        192.168.2.216   worknode2
```

Each Node has a weave Pod, and all Pods are `Running` and `2/2 READY`. (`2/2` means that each Pod has `weave` and `weave-npc`.)
