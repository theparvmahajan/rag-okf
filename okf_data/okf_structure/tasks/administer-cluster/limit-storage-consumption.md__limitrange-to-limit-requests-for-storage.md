---
id: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#limitrange-to-limit-requests-for-storage
kind: section
title: LimitRange to limit requests for storage
source: tasks/administer-cluster/limit-storage-consumption.md
url: https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/
heading: LimitRange to limit requests for storage
parent: okf-structure/tasks/administer-cluster/limit-storage-consumption
children: []
prev_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#scenario-limiting-storage-consumption
next_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#resourcequota-to-limit-pvc-count-and-cumulative-storage-capacity
word_count: 103
---

Adding a `LimitRange` to a namespace enforces storage request sizes to a minimum and maximum. Storage is requested
via `PersistentVolumeClaim`. The admission controller that enforces limit ranges will reject any PVC that is above or below
the values set by the admin.

In this example, a PVC requesting 10Gi of storage would be rejected because it exceeds the 2Gi max.

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: storagelimits
spec:
  limits:
  - type: PersistentVolumeClaim
    max:
      storage: 2Gi
    min:
      storage: 1Gi
```

Minimum storage requests are used when the underlying storage provider requires certain minimums. For example,
AWS EBS volumes have a 1Gi minimum requirement.
