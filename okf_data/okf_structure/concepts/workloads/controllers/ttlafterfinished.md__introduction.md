---
id: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#introduction
kind: section
title: Automatic Cleanup for Finished Jobs
source: concepts/workloads/controllers/ttlafterfinished.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/
heading: null
parent: okf-structure/concepts/workloads/controllers/ttlafterfinished
children: []
prev_sibling: null
next_sibling: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#cleanup-for-finished-jobs
word_count: 52
---

When your Job has finished, it's useful to keep that Job in the API (and not immediately delete the Job)
so that you can tell whether the Job succeeded or failed.

Kubernetes' TTL-after-finished controller provides a
TTL (time to live) mechanism to limit the lifetime of Job objects that
have finished execution.
