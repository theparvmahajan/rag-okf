---
id: okf-structure/tasks/run-application/scale-deployment.md#scaling-down-a-deployment
kind: section
title: Scaling down a Deployment
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: Scaling down a Deployment
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/scale-deployment.md#scaling-up-a-deployment
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#scaling-to-zero
word_count: 65
---

To reduce the number of Pods, set `--replicas` to a lower value:

```shell
kubectl scale deployment/nginx-deployment --replicas=2
```

Kubernetes gracefully terminates the excess Pods, respecting each Pod's
`terminationGracePeriodSeconds` setting.

Verify that the Deployment has two Pods:

```shell
kubectl get pods -l app=nginx
```

The output is similar to:

```
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-66b6c48dd5-7gl6h   1/1     Running   0          2m
nginx-deployment-66b6c48dd5-v8mkd   1/1     Running   0          2m
```
