---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#scaling-the-number-of-replicas
kind: section
title: Scaling the number of replicas
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: Scaling the number of replicas
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#simulate-pod-and-node-failure-simulate-pod-and-node-downtime
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#cleanup
word_count: 272
---

When you use MySQL replication, you can scale your read query capacity by
adding replicas.
For a StatefulSet, you can achieve this with a single command:

```shell
kubectl scale statefulset mysql  --replicas=5
```

Watch the new Pods come up by running:

```shell
kubectl get pods -l app=mysql --watch
```

Once they're up, you should see server IDs `103` and `104` start appearing in
the `SELECT @@server_id` loop output.

You can also verify that these new servers have the data you added before they
existed:

```shell
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  mysql -h mysql-3.mysql -e "SELECT * FROM test.messages"
```

```
Waiting for pod default/mysql-client to be running, status is Pending, pod ready: false
+---------+
| message |
+---------+
| hello   |
+---------+
pod "mysql-client" deleted
```

Scaling back down is also seamless:

```shell
kubectl scale statefulset mysql --replicas=3
```

Although scaling up creates new PersistentVolumeClaims
automatically, scaling down does not automatically delete these PVCs.

This gives you the choice to keep those initialized PVCs around to make
scaling back up quicker, or to extract data before deleting them.

You can see this by running:

```shell
kubectl get pvc -l app=mysql
```

Which shows that all 5 PVCs still exist, despite having scaled the
StatefulSet down to 3:

```
NAME           STATUS    VOLUME                                     CAPACITY   ACCESSMODES   AGE
data-mysql-0   Bound     pvc-8acbf5dc-b103-11e6-93fa-42010a800002   10Gi       RWO           20m
data-mysql-1   Bound     pvc-8ad39820-b103-11e6-93fa-42010a800002   10Gi       RWO           20m
data-mysql-2   Bound     pvc-8ad69a6d-b103-11e6-93fa-42010a800002   10Gi       RWO           20m
data-mysql-3   Bound     pvc-50043c45-b1c5-11e6-93fa-42010a800002   10Gi       RWO           2m
data-mysql-4   Bound     pvc-500a9957-b1c5-11e6-93fa-42010a800002   10Gi       RWO           2m
```

If you don't intend to reuse the extra PVCs, you can delete them:

```shell
kubectl delete pvc data-mysql-3
kubectl delete pvc data-mysql-4
```
