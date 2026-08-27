---
id: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#resourcequota-to-limit-pvc-count-and-cumulative-storage-capacity
kind: section
title: ResourceQuota to limit PVC count and cumulative storage capacity
source: tasks/administer-cluster/limit-storage-consumption.md
url: https://kubernetes.io/docs/tasks/administer-cluster/limit-storage-consumption/
heading: ResourceQuota to limit PVC count and cumulative storage capacity
parent: okf-structure/tasks/administer-cluster/limit-storage-consumption
children: []
prev_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#limitrange-to-limit-requests-for-storage
next_sibling: okf-structure/tasks/administer-cluster/limit-storage-consumption.md#summary
word_count: 96
---

Admins can limit the number of PVCs in a namespace as well as the cumulative capacity of those PVCs. New PVCs that exceed
either maximum value will be rejected.

In this example, a 6th PVC in the namespace would be rejected because it exceeds the maximum count of 5. Alternatively,
a 5Gi maximum quota when combined with the 2Gi max limit above, cannot have 3 PVCs where each has 2Gi. That would be 6Gi requested
 for a namespace capped at 5Gi.

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: storagequota
spec:
  hard:
    persistentvolumeclaims: "5"
    requests.storage: "5Gi"
```
