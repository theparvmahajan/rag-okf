---
id: okf-structure/tasks/administer-cluster/node-overprovisioning.md#create-a-priorityclass
kind: section
title: Create a PriorityClass
source: tasks/administer-cluster/node-overprovisioning.md
url: https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/
heading: Create a PriorityClass
parent: okf-structure/tasks/administer-cluster/node-overprovisioning
children: []
prev_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#run-pods-that-request-node-capacity
word_count: 101
---

Begin by defining a PriorityClass for the placeholder Pods. First, create a PriorityClass with a
negative priority value, that you will shortly assign to the placeholder pods.
Later, you will set up a Deployment that uses this PriorityClass

Then create the PriorityClass:

```shell
kubectl apply -f https://k8s.io/examples/priorityclass/low-priority-class.yaml
```

You will next define a Deployment that uses the negative-priority PriorityClass and runs a minimal container.
When you add this to your cluster, Kubernetes runs those placeholder pods to reserve capacity. Any time there
is a capacity shortage, the control plane will pick one these placeholder pods as the first candidate to
preempt.
