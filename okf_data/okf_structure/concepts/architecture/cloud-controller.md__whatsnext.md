---
id: okf-structure/concepts/architecture/cloud-controller.md#whatsnext
kind: section
title: Whatsnext
source: concepts/architecture/cloud-controller.md
url: https://kubernetes.io/docs/concepts/architecture/cloud-controller/
heading: Whatsnext
parent: okf-structure/concepts/architecture/cloud-controller
children: []
prev_sibling: okf-structure/concepts/architecture/cloud-controller.md#authorization
next_sibling: null
word_count: 139
---

* Cloud Controller Manager Administration
  has instructions on running and managing the cloud controller manager.

* To upgrade a HA control plane to use the cloud controller manager, see 
  Migrate Replicated Control Plane To Use Cloud Controller Manager.

* Want to know how to implement your own cloud controller manager, or extend an existing project?

  - The cloud controller manager uses Go interfaces, specifically, `CloudProvider` interface defined in
    `cloud.go`
    from kubernetes/cloud-provider to allow
    implementations from any cloud to be plugged in.
  - The implementation of the shared controllers highlighted in this document (Node, Route, and Service),
    and some scaffolding along with the shared cloudprovider interface, is part of the Kubernetes core.
    Implementations specific to cloud providers are outside the core of Kubernetes and implement
    the `CloudProvider` interface.
  - For more information about developing plugins,
    see Developing Cloud Controller Manager.
