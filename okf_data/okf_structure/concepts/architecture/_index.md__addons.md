---
id: okf-structure/concepts/architecture/_index.md#addons
kind: section
title: Addons
source: concepts/architecture/_index.md
url: https://kubernetes.io/docs/concepts/architecture/
heading: Addons
parent: okf-structure/concepts/architecture/_index
children: []
prev_sibling: okf-structure/concepts/architecture/_index.md#node-components
next_sibling: okf-structure/concepts/architecture/_index.md#architecture-variations
word_count: 215
---

Addons use Kubernetes resources (daemonset,
deployment, etc) to implement cluster features.
Because these are providing cluster-level features, namespaced resources for
addons belong within the `kube-system` namespace.

Selected addons are described below; for an extended list of available addons,
please see Addons.

### DNS

While the other addons are not strictly required, all Kubernetes clusters should have
cluster DNS, as many examples rely on it.

Cluster DNS is a DNS server, in addition to the other DNS server(s) in your environment,
which serves DNS records for Kubernetes services.

Containers started by Kubernetes automatically include this DNS server in their DNS searches.

### Web UI (Dashboard)

Dashboard is a general purpose,
web-based UI for Kubernetes clusters. It allows users to manage and troubleshoot applications
running in the cluster, as well as the cluster itself.

### Container resource monitoring

Container Resource Monitoring
records generic time-series metrics about containers in a central database, and provides a UI for browsing that data.

### Cluster-level Logging

A cluster-level logging mechanism is responsible
for saving container logs to a central log store with a search/browsing interface.

### Network plugins

Network plugins
are software components that implement the container network interface (CNI) specification.
They are responsible for allocating IP addresses to pods and enabling them to communicate
with each other within the cluster.
