---
id: okf-structure/tasks/administer-cluster/namespaces.md#subdividing-your-cluster-using-kubernetes-namespaces
kind: section
title: Subdividing your cluster using Kubernetes namespaces
source: tasks/administer-cluster/namespaces.md
url: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/
heading: Subdividing your cluster using Kubernetes namespaces
parent: okf-structure/tasks/administer-cluster/namespaces
children: []
prev_sibling: okf-structure/tasks/administer-cluster/namespaces.md#deleting-a-namespace
next_sibling: okf-structure/tasks/administer-cluster/namespaces.md#understanding-the-motivation-for-using-namespaces
word_count: 584
---

By default, a Kubernetes cluster will instantiate a default namespace when provisioning the
cluster to hold the default set of Pods, Services, and Deployments used by the cluster.

Assuming you have a fresh cluster, you can introspect the available namespaces by doing the following:

```shell
kubectl get namespaces
```
```console
NAME      STATUS    AGE
default   Active    13m
```

### Create new namespaces

For this exercise, you create two additional Kubernetes namespaces to hold your content.

In a scenario where an organization is using a shared Kubernetes cluster for development and
production use cases:

- The development team would like to maintain a space in the cluster where they can get a view on
  the list of Pods, Services, and Deployments they use to build and run their application.
  In this space, Kubernetes resources come and go, and the restrictions on who can or cannot modify
  resources are relaxed to enable agile development.

- The operations team would like to maintain a space in the cluster where they can enforce strict
  procedures on who can or cannot manipulate the set of Pods, Services, and Deployments that run
  the production site.

One pattern this organization could follow is to partition the Kubernetes cluster into two
namespaces: `development` and `production`. Create two new namespaces to hold your work.

Create the `development` namespace using kubectl:

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-dev.json
```

Create the `production` namespace using kubectl:

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-prod.json
```

To be sure things are right, list all of the namespaces in the cluster.

```shell
kubectl get namespaces --show-labels
```

```console
NAME          STATUS    AGE       LABELS
default       Active    32m       <none>
development   Active    29s       name=development
production    Active    23s       name=production
```

### Create pods in each namespace

A Kubernetes namespace provides the scope for Pods, Services, and Deployments in the cluster.
Users interacting with one namespace do not see the content in another namespace.
To demonstrate this, create a Deployment and Pods in the `development` namespace.

```shell
kubectl create deployment snowflake \
  --image=registry.k8s.io/serve_hostname \
  -n=development --replicas=2
```

You created a deployment whose replica size is 2 that is running the pod called `snowflake`
with a basic container that serves the hostname.

```shell
kubectl get deployment -n=development
```
```console
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
snowflake    2/2     2            2           2m
```

```shell
kubectl get pods -l app=snowflake -n=development
```
```console
NAME                         READY     STATUS    RESTARTS   AGE
snowflake-3968820950-9dgr8   1/1       Running   0          2m
snowflake-3968820950-vgc4n   1/1       Running   0          2m
```

This demonstrates that developers are able to do what they want, and they do not have to worry about
affecting content in the `production` namespace.

Switch to the `production` namespace and show how resources in one namespace are hidden from
the other. The `production` namespace should be empty, and the following commands should return nothing.

```shell
kubectl get deployment -n=production
kubectl get pods -n=production
```

Create some pods in the `production` namespace.

```shell
kubectl create deployment cattle --image=registry.k8s.io/serve_hostname -n=production
kubectl scale deployment cattle --replicas=5 -n=production

kubectl get deployment -n=production
```

```console
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
cattle       5/5     5            5           10s
```

```shell
kubectl get pods -l app=cattle -n=production
```
```console
NAME                      READY     STATUS    RESTARTS   AGE
cattle-2263376956-41xy6   1/1       Running   0          34s
cattle-2263376956-kw466   1/1       Running   0          34s
cattle-2263376956-n4v97   1/1       Running   0          34s
cattle-2263376956-p5p3i   1/1       Running   0          34s
cattle-2263376956-sxpth   1/1       Running   0          34s
```

At this point, it should be clear that the resources users create in one namespace are hidden from
the other namespace.

As the policy support in Kubernetes evolves, this scenario extends to show how you can provide different
authorization rules for each namespace.
