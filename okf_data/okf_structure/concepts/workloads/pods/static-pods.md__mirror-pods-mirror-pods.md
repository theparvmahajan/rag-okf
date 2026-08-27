---
id: okf-structure/concepts/workloads/pods/static-pods.md#mirror-pods-mirror-pods
kind: section
title: Mirror Pods {#mirror-pods}
source: concepts/workloads/pods/static-pods.md
url: https://kubernetes.io/docs/concepts/workloads/pods/static-pods/
heading: Mirror Pods {#mirror-pods}
parent: okf-structure/concepts/workloads/pods/static-pods
children: []
prev_sibling: okf-structure/concepts/workloads/pods/static-pods.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/static-pods.md#limitations-limitations
word_count: 104
---

The kubelet automatically tries to create a
mirror Pod
on the Kubernetes API server for each static Pod.
This means that the Pods running on a node are visible on the API server,
but cannot be controlled from there.
The Pod names will be suffixed with the node hostname with a leading hyphen.

The kubelet propagates labels
from the static Pod to the mirror Pod. You can use those labels as normal via
selectors.

If you try to use `kubectl` to delete the mirror Pod from the API server,
the kubelet _does not_ remove the static Pod. The kubelet will recreate
the mirror Pod.
