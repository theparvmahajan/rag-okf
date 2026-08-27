---
id: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#specify-schedulers-for-pods
kind: section
title: Specify schedulers for pods
source: tasks/extend-kubernetes/configure-multiple-schedulers.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/
heading: Specify schedulers for pods
parent: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#run-the-second-scheduler-in-the-cluster
next_sibling: null
word_count: 382
---

Now that your second scheduler is running, create some pods, and direct them
to be scheduled by either the default scheduler or the one you deployed.
In order to schedule a given pod using a specific scheduler, specify the name of the
scheduler in that pod spec. Let's look at three examples.

- Pod spec without any scheduler name

  

  When no scheduler name is supplied, the pod is automatically scheduled using the
  default-scheduler.

  Save this file as `pod1.yaml` and submit it to the Kubernetes cluster.

  ```shell
  kubectl create -f pod1.yaml
  ```

- Pod spec with `default-scheduler`

  

  A scheduler is specified by supplying the scheduler name as a value to `spec.schedulerName`. In this case, we supply the name of the
  default scheduler which is `default-scheduler`.

  Save this file as `pod2.yaml` and submit it to the Kubernetes cluster.

  ```shell
  kubectl create -f pod2.yaml
  ```

- Pod spec with `my-scheduler`

  

  In this case, we specify that this pod should be scheduled using the scheduler that we
  deployed - `my-scheduler`. Note that the value of `spec.schedulerName` should match the name supplied for the scheduler
  in the `schedulerName` field of the mapping `KubeSchedulerProfile`.

  Save this file as `pod3.yaml` and submit it to the Kubernetes cluster.

  ```shell
  kubectl create -f pod3.yaml
  ```

  Verify that all three pods are running.

  ```shell
  kubectl get pods
  ```

### Verifying that the pods were scheduled using the desired schedulers

In order to make it easier to work through these examples, we did not verify that the
pods were actually scheduled using the desired schedulers. We can verify that by
changing the order of pod and deployment config submissions above. If we submit all the
pod configs to a Kubernetes cluster before submitting the scheduler deployment config,
we see that the pod `annotation-second-scheduler` remains in "Pending" state forever
while the other two pods get scheduled. Once we submit the scheduler deployment config
and our new scheduler starts running, the `annotation-second-scheduler` pod gets
scheduled as well.

Alternatively, you can look at the "Scheduled" entries in the event logs to
verify that the pods were scheduled by the desired schedulers.

```shell
kubectl get events
```
You can also use a custom scheduler configuration
or a custom container image for the cluster's main scheduler by modifying its static pod manifest
on the relevant control plane nodes.
