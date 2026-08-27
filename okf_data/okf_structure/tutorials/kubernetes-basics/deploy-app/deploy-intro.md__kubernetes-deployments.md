---
id: okf-structure/tutorials/kubernetes-basics/deploy-app/deploy-intro.md#kubernetes-deployments
kind: section
title: Kubernetes Deployments
source: tutorials/kubernetes-basics/deploy-app/deploy-intro.md
url: https://kubernetes.io/docs/tutorials/kubernetes-basics/deploy-app/deploy-intro/
heading: Kubernetes Deployments
parent: okf-structure/tutorials/kubernetes-basics/deploy-app/deploy-intro
children: []
prev_sibling: okf-structure/tutorials/kubernetes-basics/deploy-app/deploy-intro.md#prerequisites
next_sibling: okf-structure/tutorials/kubernetes-basics/deploy-app/deploy-intro.md#deploying-your-first-app-on-kubernetes
word_count: 214
---

_A Deployment is responsible for creating and updating instances of your application._

This tutorial uses a container that requires the AMD64 architecture. If you are using
minikube on a computer with a different CPU architecture, you could try using minikube with
a driver that can emulate AMD64. For example, the Docker Desktop driver can do this.

Once you have a running Kubernetes cluster,
you can deploy your containerized applications on top of it. To do so, you create a
Kubernetes **Deployment**. The Deployment instructs Kubernetes how to create and
update instances of your application. Once you've created a Deployment, the Kubernetes
control plane schedules the application instances included in that Deployment to run
on individual Nodes in the cluster.

Once the application instances are created, a Kubernetes Deployment controller continuously
monitors those instances. If the Node hosting an instance goes down or is deleted,
the Deployment controller replaces the instance with an instance on another Node
in the cluster. **This provides a self-healing mechanism to address machine failure
or maintenance.**

In a pre-orchestration world, installation scripts would often be used to start
applications, but they did not allow recovery from machine failure. By both creating
your application instances and keeping them running across Nodes, Kubernetes Deployments
provide a fundamentally different approach to application management.
