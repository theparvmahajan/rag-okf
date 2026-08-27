---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#testing-the-message-queue-service
kind: section
title: Testing the message queue service
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Testing the message queue service
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#starting-a-message-queue-service
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#fill-the-queue-with-tasks
word_count: 408
---

Now, we can experiment with accessing the message queue.  We will
create a temporary interactive pod, install some tools on it,
and experiment with queues.

First create a temporary interactive Pod.

```shell
# Create a temporary interactive container
kubectl run -i --tty temp --image ubuntu:22.04
```
```
Waiting for pod default/temp-loe07 to be running, status is Pending, pod ready: false
... [ previous line repeats several times .. hit return when it stops ] ...
```

Note that your pod name and command prompt will be different.

Next install the `amqp-tools` so you can work with message queues.
The next commands show what you need to run inside the interactive shell in that Pod:

```shell
apt-get update && apt-get install -y curl ca-certificates amqp-tools python3 dnsutils
```

Later, you will make a container image that includes these packages.

Next, you will check that you can discover the Service for RabbitMQ:

```
# Run these commands inside the Pod
# Note the rabbitmq-service has a DNS name, provided by Kubernetes:
nslookup rabbitmq-service
```
```
Server:        10.0.0.10
Address:    10.0.0.10#53

Name:    rabbitmq-service.default.svc.cluster.local
Address: 10.0.147.152
```
(the IP addresses will vary)

If the kube-dns addon is not set up correctly, the previous step may not work for you.
You can also find the IP address for that Service in an environment variable:

```shell
# run this check inside the Pod
env | grep RABBITMQ_SERVICE | grep HOST
```
```
RABBITMQ_SERVICE_SERVICE_HOST=10.0.147.152
```
(the IP address will vary)

Next you will verify that you can create a queue, and publish and consume messages.

```shell
# Run these commands inside the Pod
# In the next line, rabbitmq-service is the hostname where the rabbitmq-service
# can be reached.  5672 is the standard port for rabbitmq.
export BROKER_URL=amqp://guest:guest@rabbitmq-service:5672
# If you could not resolve "rabbitmq-service" in the previous step,
# then use this command instead:
BROKER_URL=amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672

# Now create a queue:

/usr/bin/amqp-declare-queue --url=$BROKER_URL -q foo -d
```
```
foo
```

Publish one message to the queue:
```shell
/usr/bin/amqp-publish --url=$BROKER_URL -r foo -p -b Hello

# And get it back.

/usr/bin/amqp-consume --url=$BROKER_URL -q foo -c 1 cat && echo 1>&2
```
```
Hello
```

In the last command, the `amqp-consume` tool took one message (`-c 1`)
from the queue, and passes that message to the standard input of an arbitrary command.
In this case, the program `cat` prints out the characters read from standard input, and
the echo adds a carriage return so the example is readable.
