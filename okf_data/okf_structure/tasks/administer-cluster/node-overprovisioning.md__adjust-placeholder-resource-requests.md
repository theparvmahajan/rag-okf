---
id: okf-structure/tasks/administer-cluster/node-overprovisioning.md#adjust-placeholder-resource-requests
kind: section
title: Adjust placeholder resource requests
source: tasks/administer-cluster/node-overprovisioning.md
url: https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/
heading: Adjust placeholder resource requests
parent: okf-structure/tasks/administer-cluster/node-overprovisioning
children: []
prev_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#run-pods-that-request-node-capacity
next_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#set-the-desired-replica-count
word_count: 129
---

Configure the resource requests and limits for the placeholder pods to define the amount of overprovisioned resources you want to maintain. This reservation ensures that a specific amount of CPU and memory is kept available for new pods.

To edit the Deployment, modify the `resources` section in the Deployment manifest file
to set appropriate requests and limits. You can download that file locally and then edit it
with whichever text editor you prefer.

You can also edit the Deployment using kubectl:

```shell
kubectl edit deployment capacity-reservation
```

For example, to reserve a total of a 0.5 CPU and 1GiB of memory across 5 placeholder pods,
define the resource requests and limits for a single placeholder pod as follows:

```yaml
  resources:
    requests:
      cpu: "100m"
      memory: "200Mi"
    limits:
      cpu: "100m"
```
