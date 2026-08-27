---
id: okf-structure/tasks/run-application/scale-deployment.md#scaling-to-zero
kind: section
title: Scaling to zero
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: Scaling to zero
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/scale-deployment.md#scaling-down-a-deployment
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#other-ways-to-change-the-replica-count
word_count: 107
---

You can scale a Deployment to zero to temporarily suspend the workload without
deleting the Deployment itself:

```shell
kubectl scale deployment/nginx-deployment --replicas=0
```

Verify that no Pods are running:

```shell
kubectl get deployment nginx-deployment
```

The output is similar to:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   0/0     0            0           5m
```

Scaling to zero removes all Pods but preserves the Deployment and its
ReplicaSet. Scale back up at any time by setting `--replicas` to a positive
number.

Common use cases for scaling to zero include:

- Temporarily suspending a workload to save resources
- Debugging or maintenance windows
- Cost control in development or staging environments
