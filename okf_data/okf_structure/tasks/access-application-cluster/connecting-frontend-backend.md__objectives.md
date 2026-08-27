---
id: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#objectives
kind: section
title: Objectives
source: tasks/access-application-cluster/connecting-frontend-backend.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
heading: Objectives
parent: okf-structure/tasks/access-application-cluster/connecting-frontend-backend
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#introduction
next_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#prerequisites
word_count: 67
---

* Create and run a sample `hello` backend microservice using a 
  deployment object.
* Use a Service object to send traffic to the backend microservice's multiple replicas.
* Create and run a `nginx` frontend microservice, also using a Deployment object.
* Configure the frontend microservice to send traffic to the backend microservice. 
* Use a Service object of `type=LoadBalancer` to expose the frontend microservice 
  outside the cluster.
