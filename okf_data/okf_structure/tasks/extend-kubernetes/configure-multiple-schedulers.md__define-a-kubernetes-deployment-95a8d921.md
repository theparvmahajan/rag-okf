---
id: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#define-a-kubernetes-deployment-for-the-scheduler
kind: section
title: Define a Kubernetes Deployment for the scheduler
source: tasks/extend-kubernetes/configure-multiple-schedulers.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/
heading: Define a Kubernetes Deployment for the scheduler
parent: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#package-the-scheduler
next_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#run-the-second-scheduler-in-the-cluster
word_count: 222
---

Now that you have your scheduler in a container image, create a pod
configuration for it and run it in your Kubernetes cluster. But instead of creating a pod
directly in the cluster, you can use a Deployment
for this example. A Deployment manages a
Replica Set which in turn manages the pods,
thereby making the scheduler resilient to failures. Here is the deployment
config. Save it as `my-scheduler.yaml`:

In the above manifest, you use a KubeSchedulerConfiguration
to customize the behavior of your scheduler implementation. This configuration has been passed to
the `kube-scheduler` during initialization with the `--config` option. The `my-scheduler-config` ConfigMap stores the configuration file. The Pod of the`my-scheduler` Deployment mounts the `my-scheduler-config` ConfigMap as a volume.

In the aforementioned Scheduler Configuration, your scheduler implementation is represented via
a KubeSchedulerProfile.

To determine if a scheduler is responsible for scheduling a specific Pod, the `spec.schedulerName` field in a 
PodTemplate or Pod manifest must match the `schedulerName` field of the `KubeSchedulerProfile`.
All schedulers running in the cluster must have unique names.

Also, note that you create a dedicated service account `my-scheduler` and bind the ClusterRole
`system:kube-scheduler` to it so that it can acquire the same privileges as `kube-scheduler`.

Please see the
kube-scheduler documentation for
detailed description of other command line arguments and
Scheduler Configuration reference for
detailed description of other customizable `kube-scheduler` configurations.
