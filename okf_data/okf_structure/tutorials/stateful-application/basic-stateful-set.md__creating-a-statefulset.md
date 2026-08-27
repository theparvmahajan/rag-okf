---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#creating-a-statefulset
kind: section
title: Creating a StatefulSet
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Creating a StatefulSet
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#objectives
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#pods-in-a-statefulset
word_count: 357
---

Begin by creating a StatefulSet (and the Service that it relies upon) using
the example below. It is similar to the example presented in the
StatefulSets concept.
It creates a headless Service,
`nginx`, to publish the IP addresses of Pods in the StatefulSet, `web`.

You will need to use at least two terminal windows. In the first terminal, use
`kubectl get` to watch the creation
of the StatefulSet's Pods.

```shell
# use this terminal to run commands that specify --watch
# end this watch when you are asked to start a new watch
kubectl get pods --watch -l app=nginx
```

In the second terminal, use
`kubectl apply` to create the
headless Service and StatefulSet:

```shell
kubectl apply -f https://k8s.io/examples/application/web/web.yaml
```
```
service/nginx created
statefulset.apps/web created
```

The command above creates two Pods, each running an
NGINX webserver. Get the `nginx` Service...
```shell
kubectl get service nginx
```
```
NAME      TYPE         CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
nginx     ClusterIP    None         <none>        80/TCP    12s
```
...then get the `web` StatefulSet, to verify that both were created successfully:
```shell
kubectl get statefulset web
```
```
NAME   READY   AGE
web    2/2     37s
```

### Ordered Pod creation

A StatefulSet defaults to creating its Pods in a strict order.

For a StatefulSet with _n_ replicas, when Pods are being deployed, they are
created sequentially, ordered from _{0..n-1}_. Examine the output of the
`kubectl get` command in the first terminal. Eventually, the output will
look like the example below.

```shell
# Do not start a new watch;
# this should already be running
kubectl get pods --watch -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     0/1       Pending   0          0s
web-0     0/1       Pending   0         0s
web-0     0/1       ContainerCreating   0         0s
web-0     1/1       Running   0         19s
web-1     0/1       Pending   0         0s
web-1     0/1       Pending   0         0s
web-1     0/1       ContainerCreating   0         0s
web-1     1/1       Running   0         18s
```

Notice that the `web-1` Pod is not launched until the `web-0` Pod is
_Running_ (see Pod Phase)
and _Ready_ (see `type` in Pod Conditions).

Later in this tutorial you will practice parallel startup.

To configure the integer ordinal assigned to each Pod in a StatefulSet, see
Start ordinal.
