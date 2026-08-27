---
id: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace.md#create-a-resourcequota
kind: section
title: Create a ResourceQuota
source: tasks/administer-cluster/manage-resources/quota-pod-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-pod-namespace/
heading: Create a ResourceQuota
parent: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace.md#create-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-pod-namespace.md#clean-up
word_count: 226
---

Here is an example manifest for a ResourceQuota:

Create the ResourceQuota:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-pod.yaml --namespace=quota-pod-example
```

View detailed information about the ResourceQuota:

```shell
kubectl get resourcequota pod-demo --namespace=quota-pod-example --output=yaml
```

The output shows that the namespace has a quota of two Pods, and that currently there are
no Pods; that is, none of the quota is used.

```yaml
spec:
  hard:
    pods: "2"
status:
  hard:
    pods: "2"
  used:
    pods: "0"
```

Here is an example manifest for a deployment:

In that manifest, `replicas: 3` tells Kubernetes to attempt to create three new Pods, all
running the same application.

Create the Deployment:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-pod-deployment.yaml --namespace=quota-pod-example
```

View detailed information about the Deployment:

```shell
kubectl get deployment pod-quota-demo --namespace=quota-pod-example --output=yaml
```

The output shows that even though the Deployment specifies three replicas, only two
Pods were created because of the quota you defined earlier:

```yaml
spec:
  ...
  replicas: 3
...
status:
  availableReplicas: 2
...
lastUpdateTime: 2021-04-02T20:57:05Z
    message: 'unable to create pods: pods "pod-quota-demo-1650323038-" is forbidden:
      exceeded quota: pod-demo, requested: pods=1, used: pods=2, limited: pods=2'
```

### Choice of resource

In this task you have defined a ResourceQuota that limited the total number of Pods, but
you could also limit the total number of other kinds of object. For example, you
might decide to limit how many CronJobs
that can live in a single namespace.
