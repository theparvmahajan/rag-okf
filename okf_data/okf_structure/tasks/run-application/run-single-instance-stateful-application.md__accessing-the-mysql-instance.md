---
id: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#accessing-the-mysql-instance
kind: section
title: Accessing the MySQL instance
source: tasks/run-application/run-single-instance-stateful-application.md
url: https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/
heading: Accessing the MySQL instance
parent: okf-structure/tasks/run-application/run-single-instance-stateful-application
children: []
prev_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#deploy-mysql
next_sibling: okf-structure/tasks/run-application/run-single-instance-stateful-application.md#updating
word_count: 141
---

The preceding YAML file creates a service that
allows other Pods in the cluster to access the database. The Service option
`clusterIP: None` lets the Service DNS name resolve directly to the
Pod's IP address. This is optimal when you have only one Pod
behind a Service and you don't intend to increase the number of Pods.

Run a MySQL client to connect to the server:

```shell
kubectl run -it --rm --image=mysql:9 --restart=Never mysql-client -- mysql -h mysql -ppassword
```

This command creates a new Pod in the cluster running a MySQL client
and connects it to the server through the Service. If it connects, you
know your stateful MySQL database is up and running.

```
Waiting for pod default/mysql-client-274442439-zyp6i to be running, status is Pending, pod ready: false
If you don't see a command prompt, try pressing enter.

mysql>
```
