---
id: okf-structure/concepts/services-networking/gateway.md#design-principles
kind: section
title: Design principles
source: concepts/services-networking/gateway.md
url: https://kubernetes.io/docs/concepts/services-networking/gateway/
heading: Design principles
parent: okf-structure/concepts/services-networking/gateway
children: []
prev_sibling: okf-structure/concepts/services-networking/gateway.md#introduction
next_sibling: okf-structure/concepts/services-networking/gateway.md#resource-model
word_count: 159
---

The following principles shaped the design and architecture of Gateway API:

* __Role-oriented:__ Gateway API kinds are modeled after organizational roles that are
  responsible for managing Kubernetes service networking:
  * __Infrastructure Provider:__ Manages infrastructure that allows multiple isolated clusters
    to serve multiple tenants, e.g. a cloud provider.
  * __Cluster Operator:__ Manages clusters and is typically concerned with policies, network
    access, application permissions, etc.
  * __Application Developer:__ Manages an application running in a cluster and is typically
    concerned with application-level configuration and Service
    composition.
* __Portable:__ Gateway API specifications are defined as custom resources
  and are supported by many implementations.
* __Expressive:__ Gateway API kinds support functionality for common traffic routing use cases
  such as header-based matching, traffic weighting, and others that were only possible in
  Ingress by using custom annotations.
* __Extensible:__ Gateway allows for custom resources to be linked at various layers of the API.
  This makes granular customization possible at the appropriate places within the API structure.
