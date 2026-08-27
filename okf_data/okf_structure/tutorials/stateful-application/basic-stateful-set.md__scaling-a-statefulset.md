---
id: okf-structure/tutorials/stateful-application/basic-stateful-set.md#scaling-a-statefulset
kind: section
title: Scaling a StatefulSet
source: tutorials/stateful-application/basic-stateful-set.md
url: https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/
heading: Scaling a StatefulSet
parent: okf-structure/tutorials/stateful-application/basic-stateful-set
children: []
prev_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#pods-in-a-statefulset
next_sibling: okf-structure/tutorials/stateful-application/basic-stateful-set.md#updating-statefulsets
word_count: 617
---

Scaling a StatefulSet refers to increasing or decreasing the number of replicas
(horizontal scaling).
This is accomplished by updating the `replicas` field. You can use either
`kubectl scale` or
`kubectl patch` to scale a StatefulSet.

### Scaling up

Scaling up means adding more replicas.
Provided that your app is able to distribute work across the StatefulSet, the new
larger set of Pods can perform more of that work.

In one terminal window, watch the Pods in the StatefulSet:

```shell
# If you already have a watch running, you can continue using that.
# Otherwise, start one.
# End this watch when there are 5 healthy Pods for the StatefulSet
kubectl get pods --watch -l app=nginx
```

In another terminal window, use `kubectl scale` to scale the number of replicas
to 5:

```shell
kubectl scale sts web --replicas=5
```
```
statefulset.apps/web scaled
```

Examine the output of the `kubectl get` command in the first terminal, and wait
for the three additional Pods to transition to Running and Ready.

```shell
# This should already be running
kubectl get pod --watch -l app=nginx
```
```
NAME      READY     STATUS    RESTARTS   AGE
web-0     1/1       Running   0          2h
web-1     1/1       Running   0          2h
NAME      READY     STATUS    RESTARTS   AGE
web-2     0/1       Pending   0          0s
web-2     0/1       Pending   0         0s
web-2     0/1       ContainerCreating   0         0s
web-2     1/1       Running   0         19s
web-3     0/1       Pending   0         0s
web-3     0/1       Pending   0         0s
web-3     0/1       ContainerCreating   0         0s
web-3     1/1       Running   0         18s
web-4     0/1       Pending   0         0s
web-4     0/1       Pending   0         0s
web-4     0/1       ContainerCreating   0         0s
web-4     1/1       Running   0         19s
```

The StatefulSet controller scaled the number of replicas. As with
StatefulSet creation, the StatefulSet controller
created each Pod sequentially with respect to its ordinal index, and it
waited for each Pod's predecessor to be Running and Ready before launching the
subsequent Pod.

### Scaling down

Scaling down means reducing the number of replicas. For example, you
might do this because the level of traffic to a service has decreased,
and at the current scale there are idle resources.

In one terminal, watch the StatefulSet's Pods:

```shell
# End this watch when there are only 3 Pods for the StatefulSet
kubectl get pod --watch -l app=nginx
```

In another terminal, use `kubectl patch` to scale the StatefulSet back down to
three replicas:

```shell
kubectl patch sts web -p '{"spec":{"replicas":3}}'
```
```
statefulset.apps/web patched
```

Wait for `web-4` and `web-3` to transition to Terminating.

```shell
# This should already be running
kubectl get pods --watch -l app=nginx
```
```
NAME      READY     STATUS              RESTARTS   AGE
web-0     1/1       Running             0          3h
web-1     1/1       Running             0          3h
web-2     1/1       Running             0          55s
web-3     1/1       Running             0          36s
web-4     0/1       ContainerCreating   0          18s
NAME      READY     STATUS    RESTARTS   AGE
web-4     1/1       Running   0          19s
web-4     1/1       Terminating   0         24s
web-4     1/1       Terminating   0         24s
web-3     1/1       Terminating   0         42s
web-3     1/1       Terminating   0         42s
```

### Ordered Pod termination

The control plane deleted one Pod at a time, in reverse order with respect
to its ordinal index, and it waited for each Pod to be completely shut down
before deleting the next one.

Get the StatefulSet's PersistentVolumeClaims:

```shell
kubectl get pvc -l app=nginx
```
```
NAME        STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
www-web-0   Bound     pvc-15c268c7-b507-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-1   Bound     pvc-15c79307-b507-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-2   Bound     pvc-e1125b27-b508-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-3   Bound     pvc-e1176df6-b508-11e6-932f-42010a800002   1Gi        RWO           13h
www-web-4   Bound     pvc-e11bb5f8-b508-11e6-932f-42010a800002   1Gi        RWO           13h

```

There are still five PersistentVolumeClaims and five PersistentVolumes.
When exploring a Pod's stable storage, you saw that
the PersistentVolumes mounted to the Pods of a StatefulSet are not deleted when the
StatefulSet's Pods are deleted. This is still true when Pod deletion is caused by
scaling the StatefulSet down.
