---
id: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-hello-service-object
kind: section
title: Creating the `hello` Service object
source: tasks/access-application-cluster/connecting-frontend-backend.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
heading: Creating the `hello` Service object
parent: okf-structure/tasks/access-application-cluster/connecting-frontend-backend
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-backend-using-a-deployment
next_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-frontend
word_count: 126
---

The key to sending requests from a frontend to a backend is the backend
Service. A Service creates a persistent IP address and DNS name entry
so that the backend microservice can always be reached. A Service uses
selectors to find
the Pods that it routes traffic to.

First, explore the Service configuration file:

In the configuration file, you can see that the Service, named `hello` routes 
traffic to Pods that have the labels `app: hello` and `tier: backend`.

Create the backend Service:

```shell
kubectl apply -f https://k8s.io/examples/service/access/backend-service.yaml
```

At this point, you have a `backend` Deployment running three replicas of your `hello`
application, and you have a Service that can route traffic to them. However, this 
service is neither available nor resolvable outside the cluster.
