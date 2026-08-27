---
id: okf-structure/concepts/workloads/pods/scheduling-group.md#specifying-a-scheduling-group
kind: section
title: Specifying a scheduling group
source: concepts/workloads/pods/scheduling-group.md
url: https://kubernetes.io/docs/concepts/workloads/pods/scheduling-group/
heading: Specifying a scheduling group
parent: okf-structure/concepts/workloads/pods/scheduling-group
children: []
prev_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#introduction
next_sibling: okf-structure/concepts/workloads/pods/scheduling-group.md#behavior
word_count: 70
---

When the `GenericWorkload`
feature gate is enabled,
you can set the `spec.schedulingGroup` field in your `Pod` manifest. This field establishes a link to a specific `PodGroup` object in the same namespace by name.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: worker-0
  namespace: some-ns
spec:
  schedulingGroup:
    podGroupName: training-worker-0
  containers:
  - name: ml-worker
    image: training:v1
```

The `schedulingGroup` field is immutable. Once set, a `Pod` cannot be moved to a
different `PodGroup`.
