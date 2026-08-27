---
id: okf-structure/tutorials/stateful-application/cassandra.md#prerequisites
kind: section
title: Prerequisites
source: tutorials/stateful-application/cassandra.md
url: https://kubernetes.io/docs/tutorials/stateful-application/cassandra/
heading: Prerequisites
parent: okf-structure/tutorials/stateful-application/cassandra
children: []
prev_sibling: okf-structure/tutorials/stateful-application/cassandra.md#objectives
next_sibling: okf-structure/tutorials/stateful-application/cassandra.md#creating-a-headless-service-for-cassandra-creating-a-cassandra-headless-service
word_count: 62
---

To complete this tutorial, you should already have a basic familiarity with
Pods,
Services, and
StatefulSets.

### Additional Minikube setup instructions

Minikube defaults to 2048MB of memory and 2 CPU.
Running Minikube with the default resource configuration results in insufficient resource
errors during this tutorial. To avoid these errors, start Minikube with the following settings:

```shell
minikube start --memory 5120 --cpus=4
```
