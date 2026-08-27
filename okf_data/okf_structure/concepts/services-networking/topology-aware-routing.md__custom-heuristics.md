---
id: okf-structure/concepts/services-networking/topology-aware-routing.md#custom-heuristics
kind: section
title: Custom heuristics
source: concepts/services-networking/topology-aware-routing.md
url: https://kubernetes.io/docs/concepts/services-networking/topology-aware-routing/
heading: Custom heuristics
parent: okf-structure/concepts/services-networking/topology-aware-routing
children: []
prev_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#constraints
next_sibling: okf-structure/concepts/services-networking/topology-aware-routing.md#whatsnext
word_count: 77
---

Kubernetes is deployed in many different ways, there is no single heuristic for
allocating endpoints to zones will work for every use case. A key goal of this
feature is to enable custom heuristics to be developed if the built in heuristic
does not work for your use case. The first steps to enable custom heuristics
were included in the 1.27 release. This is a limited implementation that may not
yet cover some relevant and plausible situations.
