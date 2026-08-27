---
id: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#introduction
kind: section
title: Expose Pod Information to Containers Through Environment Variables
source: tasks/inject-data-application/environment-variable-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/environment-variable-expose-pod-information/
heading: null
parent: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information
children: []
prev_sibling: null
next_sibling: okf-structure/tasks/inject-data-application/environment-variable-expose-pod-information.md#prerequisites
word_count: 111
---

This page shows how a Pod can use environment variables to expose information
about itself to containers running in the Pod, using the _downward API_.
You can use environment variables to expose Pod fields, container fields, or both.

In Kubernetes, there are two ways to expose Pod and container fields to a running container:

* _Environment variables_, as explained in this task
* Volume files

Together, these two ways of exposing Pod and container fields are called the
downward API.

As Services are the primary mode of communication between containerized applications managed by Kubernetes, 
it is helpful to be able to discover them at runtime. 

Read more about accessing Services here.
