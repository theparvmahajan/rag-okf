---
id: okf-structure/concepts/services-networking/dns-pod-service.md#services
kind: section
title: Services
source: concepts/services-networking/dns-pod-service.md
url: https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/
heading: Services
parent: okf-structure/concepts/services-networking/dns-pod-service
children: []
prev_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#introduction
next_sibling: okf-structure/concepts/services-networking/dns-pod-service.md#pods
word_count: 177
---

### A/AAAA records

"Normal" (not headless) Services are assigned DNS A and/or AAAA records,
depending on the IP family or families of the Service, with a name of the form
`my-svc.my-namespace.svc.cluster-domain.example`. This resolves to the cluster IP
of the Service.

Headless Services
(without a cluster IP) are also assigned DNS A and/or AAAA records,
with a name of the form `my-svc.my-namespace.svc.cluster-domain.example`. Unlike normal
Services, this resolves to the set of IPs of all of the Pods selected by the Service.
Clients are expected to consume the set or else use standard round-robin
selection from the set.

### SRV records

SRV Records are created for named ports that are part of normal or headless
services.

- For each named port, the SRV record has the form
  `_port-name._port-protocol.my-svc.my-namespace.svc.cluster-domain.example`.
- For a regular Service, this resolves to the port number and the domain name:
  `my-svc.my-namespace.svc.cluster-domain.example`.
- For a headless Service, this resolves to multiple answers, one for each Pod
  that is backing the Service, and contains the port number and the domain name of the Pod
  of the form `hostname.my-svc.my-namespace.svc.cluster-domain.example`.
