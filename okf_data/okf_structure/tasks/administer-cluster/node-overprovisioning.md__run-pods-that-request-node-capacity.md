---
id: okf-structure/tasks/administer-cluster/node-overprovisioning.md#run-pods-that-request-node-capacity
kind: section
title: Run Pods that request node capacity
source: tasks/administer-cluster/node-overprovisioning.md
url: https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/
heading: Run Pods that request node capacity
parent: okf-structure/tasks/administer-cluster/node-overprovisioning
children: []
prev_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#create-a-priorityclass
next_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#adjust-placeholder-resource-requests
word_count: 52
---

Review the sample manifest:

### Pick a namespace for the placeholder pods

You should select, or create, a namespace
that the placeholder Pods will go into.

### Create the placeholder deployment

Create a Deployment based on that manifest:

```shell
# Change the namespace name "example"
kubectl --namespace example apply -f https://k8s.io/examples/deployments/deployment-with-capacity-reservation.yaml
```
