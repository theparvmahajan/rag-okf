---
id: okf-structure/tasks/run-application/run-replicated-stateful-application.md#sending-client-traffic
kind: section
title: Sending client traffic
source: tasks/run-application/run-replicated-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-replicated-stateful-application/
heading: Sending client traffic
parent: okf-structure/tasks/run-application/run-replicated-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#understanding-stateful-pod-initialization
next_sibling: okf-structure/tasks/run-application/run-replicated-stateful-application.md#simulate-pod-and-node-failure-simulate-pod-and-node-downtime
word_count: 258
---

You can send test queries to the primary MySQL server (hostname `mysql-0.mysql`)
by running a temporary container with the `mysql:5.7` image and running the
`mysql` client binary.

```shell
kubectl run mysql-client --image=mysql:5.7 -i --rm --restart=Never --\
  mysql -h mysql-0.mysql <<EOF
CREATE DATABASE test;
CREATE TABLE test.messages (message VARCHAR(250));
INSERT INTO test.messages VALUES ('hello');
EOF
```

Use the hostname `mysql-read` to send test queries to any server that reports
being Ready:

```shell
kubectl run mysql-client --image=mysql:5.7 -i -t --rm --restart=Never --\
  mysql -h mysql-read -e "SELECT * FROM test.messages"
```

You should get output like this:

```
Waiting for pod default/mysql-client to be running, status is Pending, pod ready: false
+---------+
| message |
+---------+
| hello   |
+---------+
pod "mysql-client" deleted
```

To demonstrate that the `mysql-read` Service distributes connections across
servers, you can run `SELECT @@server_id` in a loop:

```shell
kubectl run mysql-client-loop --image=mysql:5.7 -i -t --rm --restart=Never --\
  bash -ic "while sleep 1; do mysql -h mysql-read -e 'SELECT @@server_id,NOW()'; done"
```

You should see the reported `@@server_id` change randomly, because a different
endpoint might be selected upon each connection attempt:

```
+-------------+---------------------+
| @@server_id | NOW()               |
+-------------+---------------------+
|         100 | 2006-01-02 15:04:05 |
+-------------+---------------------+
+-------------+---------------------+
| @@server_id | NOW()               |
+-------------+---------------------+
|         102 | 2006-01-02 15:04:06 |
+-------------+---------------------+
+-------------+---------------------+
| @@server_id | NOW()               |
+-------------+---------------------+
|         101 | 2006-01-02 15:04:07 |
+-------------+---------------------+
```

You can press **Ctrl+C** when you want to stop the loop, but it's useful to keep
it running in another window so you can see the effects of the following steps.
