---
id: okf-structure/concepts/workloads/pods/static-pods.md#limitations-limitations
kind: section
title: Limitations {#limitations}
source: concepts/workloads/pods/static-pods.md
url: https://kubernetes.io/docs/concepts/workloads/pods/static-pods/
heading: Limitations {#limitations}
parent: okf-structure/concepts/workloads/pods/static-pods
children: []
prev_sibling: okf-structure/concepts/workloads/pods/static-pods.md#mirror-pods-mirror-pods
next_sibling: okf-structure/concepts/workloads/pods/static-pods.md#static-pods-vs-daemonsets-static-pods-vs-daemonsets
word_count: 25
---

The spec of a static Pod cannot refer to other API objects,
such as ServiceAccount,
ConfigMap, or
Secret.

Static Pods do not support ephemeral containers.
