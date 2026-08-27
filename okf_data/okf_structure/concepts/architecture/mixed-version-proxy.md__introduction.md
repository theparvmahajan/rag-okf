---
id: okf-structure/concepts/architecture/mixed-version-proxy.md#introduction
kind: section
title: Mixed Version Proxy
source: concepts/architecture/mixed-version-proxy.md
url: https://kubernetes.io/docs/concepts/architecture/mixed-version-proxy/
heading: null
parent: okf-structure/concepts/architecture/mixed-version-proxy
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/architecture/mixed-version-proxy.md#enabling-peer-aggregated-discovery-and-mixed-version-proxy
word_count: 151
---

Kubernetes  includes a beta feature that lets an
API Server
proxy resource requests to other _peer_ API servers. It also lets clients get 
a holistic view of resources served across the entire cluster through discovery.
This is useful when there are multiple
API servers running different versions of Kubernetes in one cluster
(for example, during a long-lived rollout to a new release of Kubernetes).

This enables cluster administrators to configure highly available clusters that can be upgraded
more safely, by :

1. ensuring that controllers relying on discovery to show a comprehensive list of resources
for important tasks always get the complete view of all resources. We call this complete cluster-wide 
discovery _Peer-aggregated discovery_.
1. directing resource requests (made during the upgrade) to the correct kube-apiserver.
This proxying prevents users from seeing unexpected 404 Not Found errors that stem
from the upgrade process. This mechanism is called the _Mixed Version Proxy_.
