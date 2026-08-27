---
id: okf-structure/tasks/network/extend-service-ip-ranges.md#extend-service-ip-ranges
kind: section
title: Extend Service IP Ranges
source: tasks/network/extend-service-ip-ranges.md
url: https://kubernetes.io/docs/tasks/network/extend-service-ip-ranges/
heading: Extend Service IP Ranges
parent: okf-structure/tasks/network/extend-service-ip-ranges
children: []
prev_sibling: okf-structure/tasks/network/extend-service-ip-ranges.md#prerequisites
next_sibling: okf-structure/tasks/network/extend-service-ip-ranges.md#extend-the-number-of-available-ips-for-services
word_count: 177
---

Kubernetes clusters with kube-apiservers that have enabled the `MultiCIDRServiceAllocator`
feature gate and have the
`networking.k8s.io/v1` API group active, will create a ServiceCIDR object that takes
the well-known name `kubernetes`, and that specifies an IP address range
based on the value of the `--service-cluster-ip-range` command line argument to kube-apiserver.

```sh
kubectl get servicecidr
```

```
NAME         CIDRS          AGE
kubernetes   10.96.0.0/28   17d
```

The well-known `kubernetes` Service, that exposes the kube-apiserver endpoint to the Pods, calculates
the first IP address from the default ServiceCIDR range and uses that IP address as its
cluster IP address.

```sh
kubectl get service kubernetes
```

```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   17d
```

The default Service, in this case, uses the ClusterIP 10.96.0.1, that has the corresponding IPAddress object.

```sh
kubectl get ipaddress 10.96.0.1
```

```
NAME        PARENTREF
10.96.0.1   services/default/kubernetes
```

The ServiceCIDRs are protected with finalizers,
to avoid leaving Service ClusterIPs orphans; the finalizer is only removed if there is another subnet
that contains the existing IPAddresses or there are no IPAddresses belonging to the subnet.
