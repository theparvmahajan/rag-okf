---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#fill-the-queue-with-tasks
kind: section
title: Fill the queue with tasks
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Fill the queue with tasks
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#testing-the-message-queue-service
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#create-a-container-image
word_count: 213
---

Now, fill the queue with some simulated tasks.  In this example, the tasks are strings to be
printed.

In a practice, the content of the messages might be:

- names of files to that need to be processed
- extra flags to the program
- ranges of keys in a database table
- configuration parameters to a simulation
- frame numbers of a scene to be rendered

If there is large data that is needed in a read-only mode by all pods
of the Job, you typically put that in a shared file system like NFS and mount
that readonly on all the pods, or write the program in the pod so that it can natively read
data from a cluster file system (for example: HDFS).

For this example, you will create the queue and fill it using the AMQP command line tools.
In practice, you might write a program to fill the queue using an AMQP client library.

```shell
# Run this on your computer, not in the Pod
/usr/bin/amqp-declare-queue --url=$BROKER_URL -q job1  -d
```
```
job1
```
Add items to the queue:
```shell
for f in apple banana cherry date fig grape lemon melon
do
  /usr/bin/amqp-publish --url=$BROKER_URL -r job1 -p -b $f
done
```

You added 8 messages to the queue.
