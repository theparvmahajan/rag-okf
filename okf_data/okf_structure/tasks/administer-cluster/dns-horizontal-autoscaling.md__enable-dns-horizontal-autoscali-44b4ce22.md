---
id: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#enable-dns-horizontal-autoscaling-enablng-dns-horizontal-autoscaling
kind: section
title: Enable DNS horizontal autoscaling {#enablng-dns-horizontal-autoscaling}
source: tasks/administer-cluster/dns-horizontal-autoscaling.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
heading: Enable DNS horizontal autoscaling {#enablng-dns-horizontal-autoscaling}
parent: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#get-the-name-of-your-dns-deployment-find-scaling-target
next_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#tune-dns-autoscaling-parameters-tuning-autoscaling-parameters
word_count: 76
---

In this section, you create a new Deployment. The Pods in the Deployment run a
container based on the `cluster-proportional-autoscaler-amd64` image.

Create a file named `dns-horizontal-autoscaler.yaml` with this content:

In the file, replace `<SCALE_TARGET>` with your scale target.

Go to the directory that contains your configuration file, and enter this
command to create the Deployment:

```shell
kubectl apply -f dns-horizontal-autoscaler.yaml
```

The output of a successful command is:

    deployment.apps/kube-dns-autoscaler created

DNS horizontal autoscaling is now enabled.
