---
id: okf-structure/tasks/run-application/scale-deployment.md#prerequisites
kind: section
title: Prerequisites
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: Prerequisites
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/scale-deployment.md#objectives
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#scaling-up-a-deployment
word_count: 66
---

You need an existing Deployment. If you do not have one, and you just want to practice,
you can create the nginx Deployment from
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
