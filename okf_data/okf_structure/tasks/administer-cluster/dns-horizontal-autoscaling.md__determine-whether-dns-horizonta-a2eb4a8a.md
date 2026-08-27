---
id: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#determine-whether-dns-horizontal-autoscaling-is-already-enabled-determining-whether-dns-horizontal-autoscaling-is-already-enabled
kind: section
title: Determine whether DNS horizontal autoscaling is already enabled {#determining-whether-dns-horizontal-autoscaling-is-already-enabled}
source: tasks/administer-cluster/dns-horizontal-autoscaling.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
heading: Determine whether DNS horizontal autoscaling is already enabled {#determining-whether-dns-horizontal-autoscaling-is-already-enabled}
parent: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#get-the-name-of-your-dns-deployment-find-scaling-target
word_count: 55
---

List the Deployments
in your cluster in the kube-system namespace:

```shell
kubectl get deployment --namespace=kube-system
```

The output is similar to this:

    NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
    ...
    kube-dns-autoscaler    1/1     1            1           ...
    ...

If you see "kube-dns-autoscaler" in the output, DNS horizontal autoscaling is
already enabled, and you can skip to
Tuning autoscaling parameters.
