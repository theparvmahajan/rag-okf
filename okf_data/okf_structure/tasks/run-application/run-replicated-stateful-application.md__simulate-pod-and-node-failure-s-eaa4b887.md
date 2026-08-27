---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#simulate-pod-and-node-failure-simulate-pod-and-node-downtime
kind: section
title: Simulate Pod and Node failure {#simulate-pod-and-node-downtime}
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: Simulate Pod and Node failure {#simulate-pod-and-node-downtime}
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#sending-client-traffic
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#scaling-the-number-of-replicas
word_count: 570
---

To demonstrate the increased availability of reading from the pool of replicas
instead of a single server, keep the `SELECT @@server_id` loop from above
running while you force a Pod out of the Ready state.

### Break the Readiness probe

The readiness probe
for the `mysql` container runs the command `mysql -h 127.0.0.1 -e 'SELECT 1'`
to make sure the server is up and able to execute queries.

One way to force this readiness probe to fail is to break that command:

```shell
kubectl exec mysql-2 -c mysql -- mv /usr/bin/mysql /usr/bin/mysql.off
```

This reaches into the actual container's filesystem for Pod `mysql-2` and
renames the `mysql` command so the readiness probe can't find it.
After a few seconds, the Pod should report one of its containers as not Ready,
which you can check by running:

```shell
kubectl get pod mysql-2
```

Look for `1/2` in the `READY` column:

```
NAME      READY     STATUS    RESTARTS   AGE
mysql-2   1/2       Running   0          3m
```

At this point, you should see your `SELECT @@server_id` loop continue to run,
although it never reports `102` anymore.
Recall that the `init-mysql` script defined `server-id` as `100 + $ordinal`,
so server ID `102` corresponds to Pod `mysql-2`.

Now repair the Pod and it should reappear in the loop output
after a few seconds:

```shell
kubectl exec mysql-2 -c mysql -- mv /usr/bin/mysql.off /usr/bin/mysql
```

### Delete Pods

The StatefulSet also recreates Pods if they're deleted, similar to what a
ReplicaSet does for stateless Pods.

```shell
kubectl delete pod mysql-2
```

The StatefulSet controller notices that no `mysql-2` Pod exists anymore,
and creates a new one with the same name and linked to the same
PersistentVolumeClaim.
You should see server ID `102` disappear from the loop output for a while
and then return on its own.

### Drain a Node

If your Kubernetes cluster has multiple Nodes, you can simulate Node downtime
(such as when Nodes are upgraded) by issuing a
drain.

First determine which Node one of the MySQL Pods is on:

```shell
kubectl get pod mysql-2 -o wide
```

The Node name should show up in the last column:

```
NAME      READY     STATUS    RESTARTS   AGE       IP            NODE
mysql-2   2/2       Running   0          15m       10.244.5.27   kubernetes-node-9l2t
```

Then, drain the Node by running the following command, which cordons it so
no new Pods may schedule there, and then evicts any existing Pods.
Replace `<node-name>` with the name of the Node you found in the last step.

Draining a Node can impact other workloads and applications
running on the same node. Only perform the following step in a test
cluster.

```shell
# See above advice about impact on other workloads
kubectl drain <node-name> --force --delete-emptydir-data --ignore-daemonsets
```

Now you can watch as the Pod reschedules on a different Node:

```shell
kubectl get pod mysql-2 -o wide --watch
```

It should look something like this:

```
NAME      READY   STATUS          RESTARTS   AGE       IP            NODE
mysql-2   2/2     Terminating     0          15m       10.244.1.56   kubernetes-node-9l2t
[...]
mysql-2   0/2     Pending         0          0s        <none>        kubernetes-node-fjlm
mysql-2   0/2     Init:0/2        0          0s        <none>        kubernetes-node-fjlm
mysql-2   0/2     Init:1/2        0          20s       10.244.5.32   kubernetes-node-fjlm
mysql-2   0/2     PodInitializing 0          21s       10.244.5.32   kubernetes-node-fjlm
mysql-2   1/2     Running         0          22s       10.244.5.32   kubernetes-node-fjlm
mysql-2   2/2     Running         0          30s       10.244.5.32   kubernetes-node-fjlm
```

And again, you should see server ID `102` disappear from the
`SELECT @@server_id` loop output for a while and then return.

Now uncordon the Node to return it to a normal state:

```shell
kubectl uncordon <node-name>
```
