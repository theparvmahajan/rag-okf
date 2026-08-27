---
id: okf-structure/tutorials/services/source-ip.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: Prerequisites
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: okf-structure/tutorials/services/source-ip.md#introduction
next_sibling: okf-structure/tutorials/services/source-ip.md#objectives
word_count: 160
---

### Terminology

This document makes use of the following terms:

If localizing this section, link to the equivalent Wikipedia pages for
the target localization.

NAT
: Network address translation

Source NAT
: Replacing the source IP on a packet; in this page, that usually means replacing with the IP address of a node.

Destination NAT
: Replacing the destination IP on a packet; in this page, that usually means replacing with the IP address of a pod

VIP
: A virtual IP address, such as the one assigned to every Service in Kubernetes

kube-proxy
: A network daemon that orchestrates Service VIP management on every node

### Prerequisites

The examples use a small nginx webserver that echoes back the source
IP of requests it receives through an HTTP header. You can create it as follows:

The image in the following command only runs on AMD64 architectures.

```shell
kubectl create deployment source-ip-app --image=registry.k8s.io/echoserver:1.10
```
The output is:
```
deployment.apps/source-ip-app created
```
