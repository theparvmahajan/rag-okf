---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#prerequisites
kind: section
title: Prerequisites
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Prerequisites
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#objectives
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#performing-a-rolling-update
word_count: 58
---

You need an existing Deployment. If you do not have one, create the nginx
Deployment from
Run a Stateless Application Using a Deployment:

```shell
kubectl apply -f https://k8s.io/examples/application/deployment.yaml
```

Verify the Deployment runs two Pods:

```shell
kubectl get deployment nginx-deployment
```

The output is similar to:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           10s
```
