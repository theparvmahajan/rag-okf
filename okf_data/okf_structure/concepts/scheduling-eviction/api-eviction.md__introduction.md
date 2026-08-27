---
id: okf-structure/concepts/scheduling-eviction/api-eviction.md#introduction
kind: section
title: API-initiated Eviction
source: concepts/scheduling-eviction/api-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/
heading: null
parent: okf-structure/concepts/scheduling-eviction/api-eviction
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#calling-the-eviction-api
word_count: 67
---

You can request eviction by calling the Eviction API directly, or programmatically
using a client of the API server, like the `kubectl drain` command. This
creates an `Eviction` object, which causes the API server to terminate the Pod.

API-initiated evictions respect your configured `PodDisruptionBudgets`
and `terminationGracePeriodSeconds`.

Using the API to create an Eviction object for a Pod is like performing a
policy-controlled `DELETE` operation
on the Pod.
