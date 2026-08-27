---
id: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md#understanding-cilium-components
kind: section
title: Understanding Cilium components
source: tasks/administer-cluster/network-policy-provider/cilium-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/network-policy-provider/cilium-network-policy/
heading: Understanding Cilium components
parent: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md#deploying-cilium-for-production-use
next_sibling: okf-structure/tasks/administer-cluster/network-policy-provider/cilium-network-policy.md#whatsnext
word_count: 73
---

Deploying a cluster with Cilium adds Pods to the `kube-system` namespace. To see
this list of Pods run:

```shell
kubectl get pods --namespace=kube-system -l k8s-app=cilium
```

You'll see a list of Pods similar to this:

```console
NAME           READY   STATUS    RESTARTS   AGE
cilium-kkdhz   1/1     Running   0          3m23s
...
```

A `cilium` Pod runs on each node in your cluster and enforces network policy
on the traffic to/from Pods on that node using Linux BPF.
