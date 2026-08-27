---
id: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#create-a-container-image
kind: section
title: Create a container image
source: tasks/job/coarse-parallel-processing-work-queue.md
url: https://kubernetes.io/docs/tasks/job/coarse-parallel-processing-work-queue/
heading: Create a container image
parent: okf-structure/tasks/job/coarse-parallel-processing-work-queue
children: []
prev_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#fill-the-queue-with-tasks
next_sibling: okf-structure/tasks/job/coarse-parallel-processing-work-queue.md#defining-a-job
word_count: 135
---

Now you are ready to create an image that you will run as a Job.

The job will use the `amqp-consume` utility to read the message
from the queue and run the actual work.  Here is a very simple
example program:

Give the script execution permission:

```shell
chmod +x worker.py
```

Now, build an image. Make a temporary directory, change to it,
download the Dockerfile,
and worker.py.  In either case,
build the image with this command:

```shell
docker build -t job-wq-1 .
```

For the Docker Hub, tag your app image with
your username and push to the Hub with the below commands. Replace
`<username>` with your Hub username.

```shell
docker tag job-wq-1 <username>/job-wq-1
docker push <username>/job-wq-1
```

If you are using an alternative container image registry, tag the
image and push it there instead.
