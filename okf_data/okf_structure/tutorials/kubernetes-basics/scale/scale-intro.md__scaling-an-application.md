---
id: okf-structure/tutorials/kubernetes-basics/scale/scale-intro.md#scaling-an-application
kind: section
title: Scaling an application
source: tutorials/kubernetes-basics/scale/scale-intro.md
url: https://kubernetes.io/docs/tutorials/kubernetes-basics/scale/scale-intro/
heading: Scaling an application
parent: okf-structure/tutorials/kubernetes-basics/scale/scale-intro
children: []
prev_sibling: okf-structure/tutorials/kubernetes-basics/scale/scale-intro.md#prerequisites
next_sibling: okf-structure/tutorials/kubernetes-basics/scale/scale-intro.md#scaling-overview
word_count: 173
---

_You can create from the start a Deployment with multiple instances using the --replicas
parameter for the kubectl create deployment command._

Previously we created a Deployment,
and then exposed it publicly via a Service.
The Deployment created only one Pod for running our application. When traffic increases,
we will need to scale the application to keep up with user demand.

If you haven't worked through the earlier sections, start from
Using minikube to create a cluster.

_Scaling_ is accomplished by changing the number of replicas in a Deployment.

If you are trying this after the
previous section, then you
may have deleted the service you created, or have created a Service of `type: NodePort`.
In this section, it is assumed that a service with `type: LoadBalancer` is created
for the kubernetes-bootcamp Deployment.

If you have _not_ deleted the Service created in
the previous section,
first delete that Service and then run the following command to create a new Service
with its `type` set to `LoadBalancer`:

```shell
kubectl expose deployment/kubernetes-bootcamp --type="LoadBalancer" --port 8080
```
