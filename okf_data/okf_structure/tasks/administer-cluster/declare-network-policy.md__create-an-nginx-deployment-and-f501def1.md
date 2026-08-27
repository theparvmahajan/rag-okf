---
id: okf-structure/tasks/administer-cluster/declare-network-policy.md#create-an-nginx-deployment-and-expose-it-via-a-service
kind: section
title: Create an `nginx` deployment and expose it via a service
source: tasks/administer-cluster/declare-network-policy.md
url: https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/
heading: Create an `nginx` deployment and expose it via a service
parent: okf-structure/tasks/administer-cluster/declare-network-policy
children: []
prev_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#prerequisites
next_sibling: okf-structure/tasks/administer-cluster/declare-network-policy.md#test-the-service-by-accessing-it-from-another-pod
word_count: 106
---

To see how Kubernetes network policy works, start off by creating an `nginx` Deployment.

```console
kubectl create deployment nginx --image=nginx
```
```none
deployment.apps/nginx created
```

Expose the Deployment through a Service called `nginx`.

```console
kubectl expose deployment nginx --port=80
```

```none
service/nginx exposed
```

The above commands create a Deployment with an nginx Pod and expose the Deployment through a Service named `nginx`. The `nginx` Pod and Deployment are found in the `default` namespace.

```console
kubectl get svc,pod
```

```none
NAME                        CLUSTER-IP    EXTERNAL-IP   PORT(S)    AGE
service/kubernetes          10.100.0.1    <none>        443/TCP    46m
service/nginx               10.100.0.16   <none>        80/TCP     33s

NAME                        READY         STATUS        RESTARTS   AGE
pod/nginx-701339712-e0qfq   1/1           Running       0          35s
```
