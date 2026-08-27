---
id: okf-structure/tutorials/cluster-management/namespaces-walkthrough.md#create-new-namespaces
kind: section
title: Create new namespaces
source: tutorials/cluster-management/namespaces-walkthrough.md
url: https://kubernetes.io/docs/tutorials/cluster-management/namespaces-walkthrough/
heading: Create new namespaces
parent: okf-structure/tutorials/cluster-management/namespaces-walkthrough
children: []
prev_sibling: okf-structure/tutorials/cluster-management/namespaces-walkthrough.md#understand-the-default-namespace
next_sibling: okf-structure/tutorials/cluster-management/namespaces-walkthrough.md#create-pods-in-each-namespace
word_count: 241
---

For this exercise, we will create two additional Kubernetes namespaces to hold our content.

Let's imagine a scenario where an organization is using a shared Kubernetes cluster for development and production use cases.

The development team would like to maintain a space in the cluster where they can get a view on the list of Pods, Services, and Deployments
they use to build and run their application.  In this space, Kubernetes resources come and go, and the restrictions on who can or cannot modify resources
are relaxed to enable agile development.

The operations team would like to maintain a space in the cluster where they can enforce strict procedures on who can or cannot manipulate the set of
Pods, Services, and Deployments that run the production site.

One pattern this organization could follow is to partition the Kubernetes cluster into two namespaces: `development` and `production`.

Let's create two new namespaces to hold our work.

Use the file `namespace-dev.yaml` which describes a `development` namespace:

Create the `development` namespace using kubectl.

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-dev.yaml
```

Save the following contents into file `namespace-prod.yaml` which describes a `production` namespace:

And then let's create the `production` namespace using kubectl.

```shell
kubectl create -f https://k8s.io/examples/admin/namespace-prod.yaml
```

To be sure things are right, let's list all of the namespaces in our cluster.

```shell
kubectl get namespaces --show-labels
```
```
NAME          STATUS    AGE       LABELS
default       Active    32m       <none>
development   Active    29s       name=development
production    Active    23s       name=production
```
