---
id: okf-structure/tutorials/services/connect-applications-service.md#the-kubernetes-model-for-connecting-containers
kind: section
title: The Kubernetes model for connecting containers
source: tutorials/services/connect-applications-service.md
url: https://kubernetes.io/docs/tutorials/services/connect-applications-service/
heading: The Kubernetes model for connecting containers
parent: okf-structure/tutorials/services/connect-applications-service
children: []
prev_sibling: null
next_sibling: okf-structure/tutorials/services/connect-applications-service.md#exposing-pods-to-the-cluster
word_count: 116
---

Now that you have a continuously running, replicated application you can expose it on a network.

Kubernetes assumes that pods can communicate with other pods, regardless of which host they land on.
Kubernetes gives every pod its own cluster-private IP address, so you do not need to explicitly
create links between pods or map container ports to host ports. This means that containers within
a Pod can all reach each other's ports on localhost, and all pods in a cluster can see each other
without NAT. The rest of this document elaborates on how you can run reliable services on such a
networking model.

This tutorial uses a simple nginx web server to demonstrate the concept.
