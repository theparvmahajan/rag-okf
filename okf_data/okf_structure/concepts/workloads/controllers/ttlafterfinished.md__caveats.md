---
id: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#caveats
kind: section
title: Caveats
source: concepts/workloads/controllers/ttlafterfinished.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished/
heading: Caveats
parent: okf-structure/concepts/workloads/controllers/ttlafterfinished
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#cleanup-for-finished-jobs
next_sibling: okf-structure/concepts/workloads/controllers/ttlafterfinished.md#whatsnext
word_count: 128
---

### Updating TTL for finished Jobs

You can modify the TTL period, e.g. `.spec.ttlSecondsAfterFinished` field of Jobs,
after the job is created or has finished. If you extend the TTL period after the
existing `ttlSecondsAfterFinished` period has expired, Kubernetes doesn't guarantee
to retain that Job, even if an update to extend the TTL returns a successful API
response.

### Time skew

Because the TTL-after-finished controller uses timestamps stored in the Kubernetes jobs to
determine whether the TTL has expired or not, this feature is sensitive to time
skew in your cluster, which may cause the control plane to clean up Job objects
at the wrong time.

Clocks aren't always correct, but the difference should be
very small. Please be aware of this risk when setting a non-zero TTL.
