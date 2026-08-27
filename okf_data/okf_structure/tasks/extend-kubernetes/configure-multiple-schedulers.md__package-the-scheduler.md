---
id: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#package-the-scheduler
kind: section
title: Package the scheduler
source: tasks/extend-kubernetes/configure-multiple-schedulers.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/
heading: Package the scheduler
parent: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#prerequisites
next_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#define-a-kubernetes-deployment-for-the-scheduler
word_count: 143
---

Package your scheduler binary into a container image. For the purposes of this example,
you can use the default scheduler (kube-scheduler) as your second scheduler.
Clone the Kubernetes source code from GitHub
and build the source.

```shell
git clone https://github.com/kubernetes/kubernetes.git
cd kubernetes
make
```

Create a container image containing the kube-scheduler binary. Here is the `Dockerfile`
to build the image:

```docker
FROM busybox
ADD ./_output/local/bin/linux/amd64/kube-scheduler /usr/local/bin/kube-scheduler
```

Save the file as `Dockerfile`, build the image and push it to a registry. This example
pushes the image to
Google Container Registry (GCR).
For more details, please read the GCR
documentation. Alternatively
you can also use the docker hub. For more details
refer to the docker hub documentation.

```shell
docker build -t gcr.io/my-gcp-project/my-kube-scheduler:1.0 .     # The image name and the repository
gcloud docker -- push gcr.io/my-gcp-project/my-kube-scheduler:1.0 # used in here is just an example
```
