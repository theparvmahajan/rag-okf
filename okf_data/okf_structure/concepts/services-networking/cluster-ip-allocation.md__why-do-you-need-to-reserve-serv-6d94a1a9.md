---
id: okf-structure/concepts/services-networking/cluster-ip-allocation.md#why-do-you-need-to-reserve-service-cluster-ips
kind: section
title: Why do you need to reserve Service Cluster IPs?
source: concepts/services-networking/cluster-ip-allocation.md
url: https://kubernetes.io/docs/concepts/services-networking/cluster-ip-allocation/
heading: Why do you need to reserve Service Cluster IPs?
parent: okf-structure/concepts/services-networking/cluster-ip-allocation
children: []
prev_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#how-service-clusterips-are-allocated
next_sibling: okf-structure/concepts/services-networking/cluster-ip-allocation.md#how-can-you-avoid-service-clusterip-conflicts-avoid-clusterip-conflict
word_count: 181
---

Sometimes you may want to have Services running in well-known IP addresses, so other components and
users in the cluster can use them.

The best example is the DNS Service for the cluster. As a soft convention, some Kubernetes installers assign the 10th IP address from
the Service IP range to the DNS service. Assuming you configured your cluster with Service IP range
10.96.0.0/16 and you want your DNS Service IP to be 10.96.0.10, you'd have to create a Service like
this:

```yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    k8s-app: kube-dns
    kubernetes.io/cluster-service: "true"
    kubernetes.io/name: CoreDNS
  name: kube-dns
  namespace: kube-system
spec:
  clusterIP: 10.96.0.10
  ports:
  - name: dns
    port: 53
    protocol: UDP
    targetPort: 53
  - name: dns-tcp
    port: 53
    protocol: TCP
    targetPort: 53
  selector:
    k8s-app: kube-dns
  type: ClusterIP
```

But, as it was explained before, the IP address 10.96.0.10 has not been reserved.
If other Services are created before or in parallel with dynamic allocation, there is a chance they can allocate this IP.
Hence, you will not be able to create the DNS Service because it will fail with a conflict error.
