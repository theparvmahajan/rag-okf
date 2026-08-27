---
id: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#pre-scheduled-pods
kind: section
title: Pre-scheduled Pods
source: concepts/scheduling-eviction/dynamic-resource-allocation.md
url: https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/
heading: Pre-scheduled Pods
parent: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation
children: []
prev_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#observability-of-dynamic-resources-observability-dynamic-resources
next_sibling: okf-structure/concepts/scheduling-eviction/dynamic-resource-allocation.md#limitations
word_count: 225
---

When you - or another API client - create a Pod with `spec.nodeName` already set, the scheduler gets bypassed.
If some ResourceClaim needed by that Pod does not exist yet, is not allocated
or not reserved for the Pod, then the kubelet will fail to run the Pod and
re-check periodically because those requirements might still get fulfilled later.

Such a situation can also arise when support for dynamic resource allocation
was not enabled in the scheduler at the time when the Pod got scheduled
(version skew, configuration, feature gate, etc.). kube-controller-manager
detects this and tries to make the Pod runnable by reserving the required
ResourceClaims. However, this only works if those were allocated by
the scheduler for some other pod.

It is better to avoid bypassing the scheduler because a Pod that is assigned to a node
blocks normal resources (RAM, CPU) that then cannot be used for other Pods
while the Pod is stuck. To make a Pod run on a specific node while still going
through the normal scheduling flow, create the Pod with a node selector that
exactly matches the desired node:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-with-cats
spec:
  nodeSelector:
    kubernetes.io/hostname: name-of-the-intended-node
  ...
```

You may also be able to mutate the incoming Pod, at admission time, to unset
the `.spec.nodeName` field and to use a node selector instead.
