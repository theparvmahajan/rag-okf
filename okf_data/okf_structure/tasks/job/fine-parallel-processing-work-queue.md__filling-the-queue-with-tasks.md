---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#filling-the-queue-with-tasks
kind: section
title: Filling the queue with tasks
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Filling the queue with tasks
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#starting-redis
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#create-a-container-image-create-an-image
word_count: 197
---

Now let's fill the queue with some "tasks".  In this example, the tasks are strings to be
printed.

Start a temporary interactive pod for running the Redis CLI.

```shell
kubectl run -i --tty temp --image redis --command "/bin/sh"
```
```
Waiting for pod default/redis2-c7h78 to be running, status is Pending, pod ready: false
Hit enter for command prompt
```

Now hit enter, start the Redis CLI, and create a list with some work items in it.

```shell
redis-cli -h redis
```
```console
redis:6379> rpush job2 "apple"
(integer) 1
redis:6379> rpush job2 "banana"
(integer) 2
redis:6379> rpush job2 "cherry"
(integer) 3
redis:6379> rpush job2 "date"
(integer) 4
redis:6379> rpush job2 "fig"
(integer) 5
redis:6379> rpush job2 "grape"
(integer) 6
redis:6379> rpush job2 "lemon"
(integer) 7
redis:6379> rpush job2 "melon"
(integer) 8
redis:6379> rpush job2 "orange"
(integer) 9
redis:6379> lrange job2 0 -1
1) "apple"
2) "banana"
3) "cherry"
4) "date"
5) "fig"
6) "grape"
7) "lemon"
8) "melon"
9) "orange"
```

So, the list with key `job2` will be the work queue.

Note: if you do not have Kube DNS setup correctly, you may need to change
the first step of the above block to `redis-cli -h $REDIS_SERVICE_HOST`.
