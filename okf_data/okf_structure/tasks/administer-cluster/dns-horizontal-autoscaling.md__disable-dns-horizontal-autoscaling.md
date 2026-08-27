---
id: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#disable-dns-horizontal-autoscaling
kind: section
title: Disable DNS horizontal autoscaling
source: tasks/administer-cluster/dns-horizontal-autoscaling.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
heading: Disable DNS horizontal autoscaling
parent: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#tune-dns-autoscaling-parameters-tuning-autoscaling-parameters
next_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#understanding-how-dns-horizontal-autoscaling-works
word_count: 191
---

There are a few options for tuning DNS horizontal autoscaling. Which option to
use depends on different conditions.

### Option 1: Scale down the kube-dns-autoscaler deployment to 0 replicas

This option works for all situations. Enter this command:

```shell
kubectl scale deployment --replicas=0 kube-dns-autoscaler --namespace=kube-system
```

The output is:

    deployment.apps/kube-dns-autoscaler scaled

Verify that the replica count is zero:

```shell
kubectl get rs --namespace=kube-system
```

The output displays 0 in the DESIRED and CURRENT columns:

    NAME                                  DESIRED   CURRENT   READY   AGE
    ...
    kube-dns-autoscaler-6b59789fc8        0         0         0       ...
    ...

### Option 2: Delete the kube-dns-autoscaler deployment

This option works if kube-dns-autoscaler is under your own control, which means
no one will re-create it:

```shell
kubectl delete deployment kube-dns-autoscaler --namespace=kube-system
```

The output is:

    deployment.apps "kube-dns-autoscaler" deleted

### Option 3: Delete the kube-dns-autoscaler manifest file from the master node

This option works if kube-dns-autoscaler is under control of the (deprecated)
Addon Manager,
and you have write access to the master node.

Sign in to the master node and delete the corresponding manifest file.
The common path for this kube-dns-autoscaler is:

    /etc/kubernetes/addons/dns-horizontal-autoscaler/dns-horizontal-autoscaler.yaml

After the manifest file is deleted, the Addon Manager will delete the
kube-dns-autoscaler Deployment.
