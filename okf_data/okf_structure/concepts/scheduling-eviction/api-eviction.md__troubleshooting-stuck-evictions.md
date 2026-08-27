---
id: okf-structure/concepts/scheduling-eviction/api-eviction.md#troubleshooting-stuck-evictions
kind: section
title: Troubleshooting stuck evictions
source: concepts/scheduling-eviction/api-eviction.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/
heading: Troubleshooting stuck evictions
parent: okf-structure/concepts/scheduling-eviction/api-eviction
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#how-api-initiated-eviction-works
next_sibling: okf-structure/concepts/scheduling-eviction/api-eviction.md#whatsnext
word_count: 115
---

In some cases, your applications may enter a broken state, where the Eviction
API will only return `429` or `500` responses until you intervene. This can
happen if, for example, a ReplicaSet creates pods for your application but new
pods do not enter a `Ready` state. You may also notice this behavior in cases
where the last evicted Pod had a long termination grace period.

If you notice stuck evictions, try one of the following solutions:

* Abort or pause the automated operation causing the issue. Investigate the stuck
  application before you restart the operation.
* Wait a while, then directly delete the Pod from your cluster control plane
  instead of using the Eviction API.
