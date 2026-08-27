---
id: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-frontend
kind: section
title: Creating the frontend
source: tasks/access-application-cluster/connecting-frontend-backend.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
heading: Creating the frontend
parent: okf-structure/tasks/access-application-cluster/connecting-frontend-backend
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-hello-service-object
next_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#interact-with-the-frontend-service
word_count: 208
---

Now that you have your backend running, you can create a frontend that is accessible 
outside the cluster, and connects to the backend by proxying requests to it.

The frontend sends requests to the backend worker Pods by using the DNS name
given to the backend Service. The DNS name is `hello`, which is the value
of the `name` field in the `examples/service/access/backend-service.yaml` 
configuration file.

The Pods in the frontend Deployment run a nginx image that is configured
to proxy requests to the `hello` backend Service. Here is the nginx configuration file:

Similar to the backend, the frontend has a Deployment and a Service. An important
difference to notice between the backend and frontend services, is that the
configuration for the frontend Service has `type: LoadBalancer`, which means that
the Service uses a load balancer provisioned by your cloud provider and will be
accessible from outside the cluster.

Create the frontend Deployment and Service:

```shell
kubectl apply -f https://k8s.io/examples/service/access/frontend-deployment.yaml
kubectl apply -f https://k8s.io/examples/service/access/frontend-service.yaml
```

The output verifies that both resources were created:

```
deployment.apps/frontend created
service/frontend created
```

The nginx configuration is baked into the
container image. A better way to do this would
be to use a
ConfigMap,
so that you can change the configuration more easily.
