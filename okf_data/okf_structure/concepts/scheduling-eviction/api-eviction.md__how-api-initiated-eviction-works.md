---
id: okf-structure/concepts/scheduling-eviction/api-eviction.md#how-api-initiated-eviction-works
kind: section
title: How API-initiated eviction works
source: concepts/scheduling-eviction/api-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/
heading: How API-initiated eviction works
parent: okf-structure/concepts/scheduling-eviction/api-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#calling-the-eviction-api
next_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#troubleshooting-stuck-evictions
word_count: 283
---

When you request an eviction using the API, the API server performs admission
checks and responds in one of the following ways:

* `200 OK`: the eviction is allowed, the `Eviction` subresource is created, and
  the Pod is deleted, similar to sending a `DELETE` request to the Pod URL.
* `429 Too Many Requests`: the eviction is not currently allowed because of the
  configured PodDisruptionBudget.
  You may be able to attempt the eviction again later. You might also see this
  response because of API rate limiting.
* `500 Internal Server Error`: the eviction is not allowed because there is a
  misconfiguration, like if multiple PodDisruptionBudgets reference the same Pod.

If the Pod you want to evict isn't part of a workload that has a
PodDisruptionBudget, the API server always returns `200 OK` and allows the
eviction.

If the API server allows the eviction, the Pod is deleted as follows:

1. The `Pod` resource in the API server is updated with a deletion timestamp,
   after which the API server considers the `Pod` resource to be terminated. The
   `Pod` resource is also marked with the configured grace period.
1. The kubelet on the node where the local Pod is running notices that the `Pod`
   resource is marked for termination and starts to gracefully shut down the
   local Pod.
1. While the kubelet is shutting the Pod down, the control plane removes the Pod
   from EndpointSlice
   objects. As a result, controllers no longer consider the Pod as a valid object.
1. After the grace period for the Pod expires, the kubelet forcefully terminates
   the local Pod.
1. The kubelet tells the API server to remove the `Pod` resource.
1. The API server deletes the `Pod` resource.
