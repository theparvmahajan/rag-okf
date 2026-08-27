---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#deleting-statefulsets
kind: section
title: Deleting StatefulSets
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Deleting StatefulSets
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#updating-statefulsets
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#pod-management-policy
word_count: 914
---

StatefulSet supports both _non-cascading_ and _cascading_ deletion. In a
non-cascading **delete**, the StatefulSet's Pods are not deleted when the
StatefulSet is deleted. In a cascading **delete**, both the StatefulSet and
its Pods are deleted.

Read Use Cascading Deletion in a Cluster
to learn about cascading deletion generally.

### Non-cascading delete

In one terminal window, watch the Pods in the StatefulSet.

```
# End this watch when there are no Pods for the StatefulSet
kubectl get pods --watch -l app=nginx
```

Use `kubectl delete` to delete the
StatefulSet. Make sure to supply the `--cascade=orphan` parameter to the
command. This parameter tells Kubernetes to only delete the StatefulSet, and to
**not** delete any of its Pods.

```shell
kubectl delete statefulset web --cascade=orphan
```
```
statefulset.apps "web" deleted
```

Get the Pods, to examine their status:

```shell
kubectl get pods -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          6m
web-1     1/1       Running   0          7m
web-2     1/1       Running   0          5m
```

Even though `web` has been deleted, all of the Pods are still Running and Ready.
Delete `web-0`:

```shell
kubectl delete pod web-0
```
```
pod "web-0" deleted
```

Get the StatefulSet's Pods:

```shell
kubectl get pods -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-1     1/1       Running   0          10m
web-2     1/1       Running   0          7m
```

As the `web` StatefulSet has been deleted, `web-0` has not been relaunched.

In one terminal, watch the StatefulSet's Pods.

```shell
# Leave this watch running until the next time you start a watch
kubectl get pods --watch -l app=nginx
```

In a second terminal, recreate the StatefulSet. Note that, unless
you deleted the `nginx` Service (which you should not have), you will see
an error indicating that the Service already exists.

```shell
kubectl apply -f https://k8s.io/examples/application/web/web.yaml
```
```
statefulset.apps/web created
service/nginx unchanged
```

Ignore the error. It only indicates that an attempt was made to create the _nginx_
headless Service even though that Service already exists.

Examine the output of the `kubectl get` command running in the first terminal.

```shell
# This should already be running
kubectl get pods --watch -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-1     1/1       Running   0          16m
web-2     1/1       Running   0          2m
NAME      READY     STATUS    RESTARTS   AGE
web-0     0/1       Pending   0          0s
web-0     0/1       Pending   0         0s
web-0     0/1       ContainerCreating   0         0s
web-0     1/1       Running   0         18s
web-2     1/1       Terminating   0         3m
web-2     0/1       Terminating   0         3m
web-2     0/1       Terminating   0         3m
web-2     0/1       Terminating   0         3m
```

When the `web` StatefulSet was recreated, it first relaunched `web-0`.
Since `web-1` was already Running and Ready, when `web-0` transitioned to
Running and Ready, it adopted this Pod. Since you recreated the StatefulSet
with `replicas` equal to 2, once `web-0` had been recreated, and once
`web-1` had been determined to already be Running and Ready, `web-2` was
terminated.

Now take another look at the contents of the `index.html` file served by the
Pods' webservers:

```shell
for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```

```
web-0
web-1
```

Even though you deleted both the StatefulSet and the `web-0` Pod, it still
serves the hostname originally entered into its `index.html` file. This is
because the StatefulSet never deletes the PersistentVolumes associated with a
Pod. When you recreated the StatefulSet and it relaunched `web-0`, its original
PersistentVolume was remounted.

### Cascading delete

In one terminal window, watch the Pods in the StatefulSet.

```shell
# Leave this running until the next page section
kubectl get pods --watch -l app=nginx
```

In another terminal, delete the StatefulSet again. This time, omit the
`--cascade=orphan` parameter.

```shell
kubectl delete statefulset web
```

```
statefulset.apps "web" deleted
```

Examine the output of the `kubectl get` command running in the first terminal,
and wait for all of the Pods to transition to Terminating.

```shell
# This should already be running
kubectl get pods --watch -l app=nginx
```

```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          11m
web-1     1/1       Running   0          27m
NAME      READY     STATUS        RESTARTS   AGE
web-0     1/1       Terminating   0          12m
web-1     1/1       Terminating   0         29m
web-0     0/1       Terminating   0         12m
web-0     0/1       Terminating   0         12m
web-0     0/1       Terminating   0         12m
web-1     0/1       Terminating   0         29m
web-1     0/1       Terminating   0         29m
web-1     0/1       Terminating   0         29m

```

As you saw in the Scaling Down section, the Pods
are terminated one at a time, with respect to the reverse order of their ordinal
indices. Before terminating a Pod, the StatefulSet controller waits for
the Pod's successor to be completely terminated.

Although a cascading delete removes a StatefulSet together with its Pods,
the cascade does **not** delete the headless Service associated with the StatefulSet.
You must delete the `nginx` Service manually.

```shell
kubectl delete service nginx
```

```
service "nginx" deleted
```

Recreate the StatefulSet and headless Service one more time:

```shell
kubectl apply -f https://k8s.io/examples/application/web/web.yaml
```

```
service/nginx created
statefulset.apps/web created
```

When all of the StatefulSet's Pods transition to Running and Ready, retrieve
the contents of their `index.html` files:

```shell
for i in 0 1; do kubectl exec -i -t "web-$i" -- curl http://localhost/; done
```

```
web-0
web-1
```

Even though you completely deleted the StatefulSet, and all of its Pods, the
Pods are recreated with their PersistentVolumes mounted, and `web-0` and
`web-1` continue to serve their hostnames.

Finally, delete the `nginx` Service...

```shell
kubectl delete service nginx
```

```
service "nginx" deleted
```

...and the `web` StatefulSet:

```shell
kubectl delete statefulset web
```

```
statefulset "web" deleted
```
