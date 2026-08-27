---
id: okf-structure/concepts/services-networking/ingress.md#terminology
kind: section
title: Terminology
source: concepts/services-networking/ingress.md
url: https://kubernetes.io/docs/concepts/services-networking/ingress/
heading: Terminology
parent: okf-structure/concepts/services-networking/ingress
children: []
prev_sibling: okf-structure/concepts/services-networking/ingress.md#introduction
next_sibling: okf-structure/concepts/services-networking/ingress.md#what-is-ingress
word_count: 133
---

For clarity, this guide defines the following terms:

* Node: A worker machine in Kubernetes, part of a cluster.
* Cluster: A set of Nodes that run containerized applications managed by Kubernetes.
  For this example, and in most common Kubernetes deployments, nodes in the cluster
  are not part of the public internet.
* Edge router: A router that enforces the firewall policy for your cluster. This
  could be a gateway managed by a cloud provider or a physical piece of hardware.
* Cluster network: A set of links, logical or physical, that facilitate communication
  within a cluster according to the Kubernetes networking model.
* Service: A Kubernetes service that identifies
  a set of Pods using label selectors.
  Unless mentioned otherwise, Services are assumed to have virtual IPs only routable within the cluster network.
