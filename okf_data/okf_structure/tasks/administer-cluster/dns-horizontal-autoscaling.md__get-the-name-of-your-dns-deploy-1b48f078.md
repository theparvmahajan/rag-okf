---
id: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#get-the-name-of-your-dns-deployment-find-scaling-target
kind: section
title: Get the name of your DNS Deployment {#find-scaling-target}
source: tasks/administer-cluster/dns-horizontal-autoscaling.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
heading: Get the name of your DNS Deployment {#find-scaling-target}
parent: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#determine-whether-dns-horizontal-autoscaling-is-already-enabled-determining-whether-dns-horizontal-autoscaling-is-already-enabled
next_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#enable-dns-horizontal-autoscaling-enablng-dns-horizontal-autoscaling
word_count: 124
---

List the DNS deployments in your cluster in the kube-system namespace:

```shell
kubectl get deployment -l k8s-app=kube-dns --namespace=kube-system
```

The output is similar to this:

    NAME      READY   UP-TO-DATE   AVAILABLE   AGE
    ...
    coredns   2/2     2            2           ...
    ...

If you don't see a Deployment for DNS services, you can also look for it by name:

```shell
kubectl get deployment --namespace=kube-system
```

and look for a deployment named `coredns` or `kube-dns`.

Your scale target is

    Deployment/<your-deployment-name>

where `<your-deployment-name>` is the name of your DNS Deployment. For example, if
the name of your Deployment for DNS is coredns, your scale target is Deployment/coredns.

CoreDNS is the default DNS service for Kubernetes. CoreDNS sets the label
`k8s-app=kube-dns` so that it can work in clusters that originally used
kube-dns.
