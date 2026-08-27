---
id: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#whatsnext
kind: section
title: Whatsnext
source: tasks/inject-data-application/downward-api-volume-expose-pod-information.md
url: https://kubernetes.io/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/
heading: Whatsnext
parent: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information
children: []
prev_sibling: okf-structure/tasks/inject-data-application/downward-api-volume-expose-pod-information.md#project-keys-to-specific-paths-and-file-permissions
next_sibling: null
word_count: 111
---

* Read the `spec`
  API definition for Pod. This includes the definition of Container (part of Pod).
* Read the list of available fields that you
  can expose using the downward API.

Read about volumes in the legacy API reference:
* Check the `Volume`
  API definition which defines a generic volume in a Pod for containers to access.
* Check the `DownwardAPIVolumeSource`
  API definition which defines a volume that contains Downward API information.
* Check the `DownwardAPIVolumeFile`
  API definition which contains references to object or resource fields for
  populating a file in the Downward API volume.
* Check the `ResourceFieldSelector`
  API definition which specifies the container resources and their output format.
