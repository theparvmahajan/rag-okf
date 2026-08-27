---
id: okf-structure/tasks/run-application/scale-deployment.md#scaling-up-a-deployment
kind: section
title: Scaling up a Deployment
source: tasks/run-application/scale-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/scale-deployment/
heading: Scaling up a Deployment
parent: okf-structure/tasks/run-application/scale-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/scale-deployment.md#prerequisites
next_sibling: okf-structure/tasks/run-application/scale-deployment.md#scaling-down-a-deployment
word_count: 155
---

There are several different ways you can change the replica count for an
existing Deployment.

### Scaling up using `kubectl scale`

Use `kubectl scale` to set the replica count:

```shell
kubectl scale deployment/nginx-deployment --replicas=4
```

The output is similar to:

```
deployment.apps/nginx-deployment scaled
```

Verify that the Deployment has four Pods:

```shell
kubectl get deployment nginx-deployment
```

The output is similar to:

```
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   4/4     4            4           1m
```

### Declarative scaling using `kubectl apply`

Instead of running an imperative command, you can update the manifest file and
apply it. This approach fits well with version-controlled configuration
workflows.

Save the current Deployment configuration to a local file:

```shell
kubectl get deployment nginx-deployment -o yaml > /tmp/nginx-deployment.yaml
```

Edit `/tmp/nginx-deployment.yaml` and change `.spec.replicas` to `4`.

Before applying, compare your local changes against the cluster state:

```shell
kubectl diff -f /tmp/nginx-deployment.yaml
```

Apply the edited manifest:

```shell
kubectl apply -f /tmp/nginx-deployment.yaml
```
