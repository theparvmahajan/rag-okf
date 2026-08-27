---
id: okf-structure/concepts/workloads/pods/downward-api.md#introduction
kind: section
title: Downward API
source: concepts/workloads/pods/downward-api.md
url: https://kubernetes.io/docs/concepts/workloads/pods/downward-api/
heading: null
parent: okf-structure/concepts/workloads/pods/downward-api
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/pods/downward-api.md#available-fields
word_count: 142
---

It is sometimes useful for a container to have information about itself, without
being overly coupled to Kubernetes. The _downward API_ allows containers to consume
information about themselves or the cluster without using the Kubernetes client
or API server.

An example is an existing application that assumes a particular well-known
environment variable holds a unique identifier. One possibility is to wrap the
application, but that is tedious and error-prone, and it violates the goal of low
coupling. A better option would be to use the Pod's name as an identifier, and
inject the Pod's name into the well-known environment variable.

In Kubernetes, there are two ways to expose Pod and container fields to a running container:

* as environment variables
* as files in a `downwardAPI` volume

Together, these two ways of exposing Pod and container fields are called the
_downward API_.
