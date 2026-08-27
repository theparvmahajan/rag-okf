---
id: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#introduction
kind: section
title: Expose Pod Information to Containers Through Files
source: tasks/inject-data-application/downward-api-volume-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/
heading: null
parent: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#prerequisites
word_count: 74
---

This page shows how a Pod can use a
`downwardAPI` volume,
to expose information about itself to containers running in the Pod.
A `downwardAPI` volume can expose Pod fields and container fields.

In Kubernetes, there are two ways to expose Pod and container fields to a running container:

* Environment variables
* Volume files, as explained in this task

Together, these two ways of exposing Pod and container fields are called the
_downward API_.
