---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#starting-a-message-queue-service
kind: section
title: Starting a message queue service
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Starting a message queue service
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#prerequisites
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#testing-the-message-queue-service
word_count: 77
---

This example uses RabbitMQ, however, you can adapt the example to use another AMQP-type message service.

In practice you could set up a message queue service once in a
cluster and reuse it for many jobs, as well as for long-running services.

Start RabbitMQ as follows:

```shell
# make a Service for the StatefulSet to use
kubectl create -f https://kubernetes.io/examples/application/job/rabbitmq/rabbitmq-service.yaml
```
```
service "rabbitmq-service" created
```

```shell
kubectl create -f https://kubernetes.io/examples/application/job/rabbitmq/rabbitmq-statefulset.yaml
```
```
statefulset "rabbitmq" created
```
