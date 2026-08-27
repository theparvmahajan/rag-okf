---
id: okf-structure/tutorials/stateful-application/cassandra.md#creating-a-headless-service-for-cassandra-creating-a-cassandra-headless-service
kind: section
title: Creating a headless Service for Cassandra {#creating-a-cassandra-headless-service}
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Creating a headless Service for Cassandra {#creating-a-cassandra-headless-service}
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#prerequisites
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#using-a-statefulset-to-create-a-cassandra-ring
word_count: 100
---

In Kubernetes, a Service describes a set of
Pods that perform the same task.

The following Service is used for DNS lookups between Cassandra Pods and clients within your cluster:

Create a Service to track all Cassandra StatefulSet members from the `cassandra-service.yaml` file:

```shell
kubectl apply -f https://k8s.io/examples/application/cassandra/cassandra-service.yaml
```

### Validating (optional) {#validating}

Get the Cassandra Service.

```shell
kubectl get svc cassandra
```

The response is

```
NAME        TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
cassandra   ClusterIP   None         <none>        9042/TCP   45s
```

If you don't see a Service named `cassandra`, that means creation failed. Read
Debug Services
for help troubleshooting common issues.
