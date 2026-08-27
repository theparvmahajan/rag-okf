---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#starting-redis
kind: section
title: Starting Redis
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Starting Redis
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#prerequisites
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#filling-the-queue-with-tasks
word_count: 73
---

For this example, for simplicity, you will start a single instance of Redis.
See the Redis Example for an example
of deploying Redis scalably and redundantly.

You could also download the following files directly:

- `redis-pod.yaml`
- `redis-service.yaml`
- `Dockerfile`
- `job.yaml`
- `rediswq.py`
- `worker.py`

To start a single instance of Redis, you need to create the redis pod and redis service:

```shell
kubectl apply -f https://k8s.io/examples/application/job/redis/redis-pod.yaml
kubectl apply -f https://k8s.io/examples/application/job/redis/redis-service.yaml
```
