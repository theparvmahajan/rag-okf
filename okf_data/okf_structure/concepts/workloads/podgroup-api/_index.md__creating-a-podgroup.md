---
id: okf-structure/concepts/workloads/podgroup-api/_index.md#creating-a-podgroup
kind: section
title: Creating a PodGroup
source: concepts/workloads/podgroup-api/_index.md
url: https://kubernetes.io/docs/concepts/workloads/podgroup-api/
heading: Creating a PodGroup
parent: okf-structure/concepts/workloads/podgroup-api/_index
children: []
prev_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#api-structure
next_sibling: okf-structure/concepts/workloads/podgroup-api/_index.md#how-it-fits-together
word_count: 96
---

A PodGroup API resource is part of the `scheduling.k8s.io/v1alpha2`
API group.
(and your cluster must have that API group enabled, as well as the `GenericWorkload`
feature gate,
before you can use this API).

The following manifest creates a PodGroup with a gang scheduling policy that requires
at least 4 Pods to be schedulable simultaneously:

```yaml
apiVersion: scheduling.k8s.io/v1alpha2
kind: PodGroup
metadata:
  name: training-worker-0
  namespace: default
spec:
  schedulingPolicy:
    gang:
      minCount: 4
```

You can inspect PodGroups in your cluster:

```shell
kubectl get podgroups
```

To see the full status including scheduling conditions:

```shell
kubectl describe podgroup training-worker-0
```
