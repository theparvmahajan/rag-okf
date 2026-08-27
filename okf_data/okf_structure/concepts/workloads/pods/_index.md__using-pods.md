---
id: okf-structure/concepts/workloads/pods/_index.md#using-pods
kind: section
title: Using Pods
source: concepts/workloads/pods/_index.md
url: https://kubernetes.io/docs/concepts/workloads/pods/
heading: Using Pods
parent: okf-structure/concepts/workloads/pods/_index
children: []
prev_sibling: okf-structure/concepts/workloads/pods/_index.md#what-is-a-pod
next_sibling: okf-structure/concepts/workloads/pods/_index.md#working-with-pods
word_count: 201
---

The following is an example of a Pod which consists of a container running the image `nginx:1.14.2`.

To create the Pod shown above, run the following command:
```shell
kubectl apply -f https://k8s.io/examples/pods/simple-pod.yaml
```

Pods are generally not created directly and are created using workload resources.
See Working with Pods for more information on how Pods are used
with workload resources.

### Workload resources for managing pods

Usually you don't need to create Pods directly, even singleton Pods. Instead, create them using workload resources such as Deployment or Job.
If your Pods need to track state, consider the
StatefulSet resource.

Each Pod is meant to run a single instance of a given application. If you want to
scale your application horizontally (to provide more overall resources by running
more instances), you should use multiple Pods, one for each instance. In
Kubernetes, this is typically referred to as _replication_.
Replicated Pods are usually created and managed as a group by a workload resource
and its controller.

See Pods and controllers for more information on how
Kubernetes uses workload resources, and their controllers, to implement application
scaling and auto-healing.

Pods natively provide two kinds of shared resources for their constituent containers:
networking and storage.
