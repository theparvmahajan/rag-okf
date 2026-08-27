---
id: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#create-a-container-image-create-an-image
kind: section
title: Create a container image {#create-an-image}
source: tasks/job/fine-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/fine-parallel-processing-work-queue/
heading: Create a container image {#create-an-image}
parent: okf-structure/tasks/job/fine-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#filling-the-queue-with-tasks
next_sibling: okf-structure/tasks/job/fine-parallel-processing-work-queue.md#defining-a-job
word_count: 159
---

Now you are ready to create an image that will process the work in that queue.

You're going to use a Python worker program with a Redis client to read
the messages from the message queue.

A simple Redis work queue client library is provided,
called `rediswq.py` (Download).

The "worker" program in each Pod of the Job uses the work queue
client library to get work.  Here it is:

You could also download `worker.py`,
`rediswq.py`, and
`Dockerfile` files, then build
the container image. Here's an example using Docker to do the image build:

```shell
docker build -t job-wq-2 .
```

### Push the image

For the Docker Hub, tag your app image with
your username and push to the Hub with the below commands. Replace
`<username>` with your Hub username.

```shell
docker tag job-wq-2 <username>/job-wq-2
docker push <username>/job-wq-2
```

You need to push to a public repository or configure your cluster to be able to access
your private repository.
