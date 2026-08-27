---
id: okf-structure/tasks/run-application/update-deployment-rolling.md#monitoring-rollout-progress
kind: section
title: Monitoring rollout progress
source: tasks/run-application/update-deployment-rolling.md
url: https://kubernetes.io/docs/tasks/run-application/update-deployment-rolling/
heading: Monitoring rollout progress
parent: okf-structure/tasks/run-application/update-deployment-rolling
children: []
prev_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#performing-a-rolling-update
next_sibling: okf-structure/tasks/run-application/update-deployment-rolling.md#pausing-and-resuming-a-rollout
word_count: 105
---

Use `kubectl rollout status` to watch the progress of a rolling update:

```shell
kubectl rollout status deployment/nginx-deployment
```

The output is similar to:

```
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 out of 2 new replicas have been updated...
Waiting for deployment "nginx-deployment" rollout to finish: 1 old replicas are pending termination...
deployment "nginx-deployment" successfully rolled out
```

After the rollout completes, verify the Deployment:

```shell
kubectl get deployment nginx-deployment
```

The output is similar to:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           2m
```
