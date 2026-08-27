---
id: okf-structure/concepts/workloads/pods/sidecar-containers.md#introduction
kind: section
title: Sidecar Containers
source: concepts/workloads/pods/sidecar-containers.md
url: https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/
heading: null
parent: okf-structure/concepts/workloads/pods/sidecar-containers
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/sidecar-containers.md#sidecar-containers-in-kubernetes-pod-sidecar-containers
word_count: 93
---

Sidecar containers are the secondary containers that run along with the main
application container within the same Pod.
These containers are used to enhance or to extend the functionality of the primary _app
container_ by providing additional services, or functionality such as logging, monitoring,
security, or data synchronization, without directly altering the primary application code.

Typically, you only have one app container in a Pod. For example, if you have a web
application that requires a local webserver, the local webserver is a sidecar and the
web application itself is the app container.
