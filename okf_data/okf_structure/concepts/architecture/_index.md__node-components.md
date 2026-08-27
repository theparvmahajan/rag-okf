---
id: okf-structure/concepts/architecture/_index.md#node-components
kind: section
title: Node components
source: concepts/architecture/_index.md
url: https://kubernetes.io/docs/concepts/architecture/
heading: Node components
parent: okf-structure/concepts/architecture/_index
children: []
prev_sibling: okf-structure/concepts/architecture/_index.md#control-plane-components
next_sibling: okf-structure/concepts/architecture/_index.md#addons
word_count: 58
---

Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment.

### kubelet

### kube-proxy (optional) {#kube-proxy}

If you use a network plugin that implements packet forwarding for Services
by itself, and providing equivalent behavior to kube-proxy, then you do not need to run
kube-proxy on the nodes in your cluster.

### Container runtime
