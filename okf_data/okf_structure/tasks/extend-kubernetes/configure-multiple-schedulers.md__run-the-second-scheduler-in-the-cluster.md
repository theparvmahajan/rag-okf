---
id: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#run-the-second-scheduler-in-the-cluster
kind: section
title: Run the second scheduler in the cluster
source: tasks/extend-kubernetes/configure-multiple-schedulers.md
url: https://kubernetes.io/docs/tasks/extend-kubernetes/configure-multiple-schedulers/
heading: Run the second scheduler in the cluster
parent: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers
children: []
prev_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#define-a-kubernetes-deployment-for-the-scheduler
next_sibling: okf-structure/tasks/extend-kubernetes/configure-multiple-schedulers.md#specify-schedulers-for-pods
word_count: 177
---

In order to run your scheduler in a Kubernetes cluster, create the deployment
specified in the config above in a Kubernetes cluster:

```shell
kubectl create -f my-scheduler.yaml
```

Verify that the scheduler pod is running:

```shell
kubectl get pods --namespace=kube-system
```

```
NAME                                           READY     STATUS    RESTARTS   AGE
....
my-scheduler-lnf4s-4744f                       1/1       Running   0          2m
...
```

You should see a "Running" my-scheduler pod, in addition to the default kube-scheduler
pod in this list.

### Enable leader election

To run multiple-scheduler with leader election enabled, you must do the following:

Update the following fields for the KubeSchedulerConfiguration in the `my-scheduler-config` ConfigMap in your YAML file:

* `leaderElection.leaderElect` to `true`
* `leaderElection.resourceNamespace` to `<lock-object-namespace>`
* `leaderElection.resourceName` to `<lock-object-name>`

The control plane creates the lock objects for you, but the namespace must already exist.
You can use the `kube-system` namespace.

If RBAC is enabled on your cluster, you must update the `system:kube-scheduler` cluster role.
Add your scheduler name to the resourceNames of the rule applied for `endpoints` and `leases` resources, as in the following example:

```shell
kubectl edit clusterrole system:kube-scheduler
```
