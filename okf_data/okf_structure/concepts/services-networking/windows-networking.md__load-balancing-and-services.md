---
id: okf-structure/concepts/services-networking/windows-networking.md#load-balancing-and-services
kind: section
title: Load balancing and Services
source: concepts/services-networking/windows-networking.md
url: https://kubernetes.io/docs/concepts/services-networking/windows-networking/
heading: Load balancing and Services
parent: okf-structure/concepts/services-networking/windows-networking
children: []
prev_sibling: okf-structure/concepts/services-networking/windows-networking.md#direct-server-return-dsr-dsr
next_sibling: okf-structure/concepts/services-networking/windows-networking.md#limitations
word_count: 269
---

A Kubernetes Service is an abstraction
that defines a logical set of Pods and a means to access them over a network.
In a cluster that includes Windows nodes, you can use the following types of Service:

* `NodePort`
* `ClusterIP`
* `LoadBalancer`
* `ExternalName`

Windows container networking differs in some important ways from Linux networking.
The Microsoft documentation for Windows Container Networking
provides additional details and background.

On Windows, you can use the following settings to configure Services and load
balancing behavior:

| Feature | Description | Minimum Supported Windows OS build | How to enable |
| ------- | ----------- | -------------------------- | ------------- |
| Session affinity | Ensures that connections from a particular client are passed to the same Pod each time. | Windows Server 2022 | Set `service.spec.sessionAffinity` to "ClientIP" |
| Direct Server Return (DSR) | See DSR notes above. | Windows Server 2019 | Set the following command line argument (assuming version ): ` --enable-dsr=true` |
| Preserve-Destination | Skips DNAT of service traffic, thereby preserving the virtual IP of the target service in packets reaching the backend Pod. Also disables node-node forwarding. | Windows Server, version 1903 | Set `"preserve-destination": "true"` in service annotations and enable DSR in kube-proxy. |
| IPv4/IPv6 dual-stack networking | Native IPv4-to-IPv4 in parallel with IPv6-to-IPv6 communications to, from, and within a cluster | Windows Server 2019 | See IPv4/IPv6 dual-stack |
| Client IP preservation | Ensures that source IP of incoming ingress traffic gets preserved. Also disables node-node forwarding. |  Windows Server 2019  | Set `service.spec.externalTrafficPolicy` to "Local" and enable DSR in kube-proxy |
