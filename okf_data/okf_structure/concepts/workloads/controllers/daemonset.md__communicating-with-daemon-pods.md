---
id: okf-structure/concepts/workloads/controllers/daemonset.md#communicating-with-daemon-pods
kind: section
title: Communicating with Daemon Pods
source: concepts/workloads/controllers/daemonset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/
heading: Communicating with Daemon Pods
parent: okf-structure/concepts/workloads/controllers/daemonset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#how-daemon-pods-are-scheduled
next_sibling: okf-structure/concepts/workloads/controllers/daemonset.md#updating-a-daemonset
word_count: 133
---

Some possible patterns for communicating with Pods in a DaemonSet are:

- **Push**: Pods in the DaemonSet are configured to send updates to another service, such
  as a stats database.  They do not have clients.
- **NodeIP and Known Port**: Pods in the DaemonSet can use a `hostPort`, so that the pods
  are reachable via the node IPs.
  Clients know the list of node IPs somehow, and know the port by convention.
- **DNS**: Create a headless service
  with the same pod selector, and then discover DaemonSets using the `endpoints`
  resource or retrieve multiple A records from DNS.
- **Service**: Create a service with the same Pod selector, and use the service to reach a
  daemon on a random node. Use Service Internal Traffic Policy
  to limit to pods on the same node.
