---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#pausing-and-resuming-a-rollout
kind: section
title: Pausing and resuming a rollout
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Pausing and resuming a rollout
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#monitoring-rollout-progress
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#configuring-rolling-update-strategy
word_count: 120
---

You can pause a rollout to inspect a partial update or to batch multiple changes
into a single rollout.

### Pausing a rollout

```shell
kubectl rollout pause deployment/nginx-deployment
```

The output is similar to:

```
deployment.apps/nginx-deployment paused
```

### Making additional changes while paused

While the rollout is paused, you can make additional changes. These changes do
not trigger a new rollout until you resume:

```shell
kubectl set image deployment/nginx-deployment nginx=nginx:1.17.0
```

You can make multiple changes to a paused Deployment. Kubernetes applies all
changes together when you resume the rollout.

### Resuming a rollout

```shell
kubectl rollout resume deployment/nginx-deployment
```

The output is similar to:

```
deployment.apps/nginx-deployment resumed
```

Verify the rollout completes:

```shell
kubectl rollout status deployment/nginx-deployment
```
