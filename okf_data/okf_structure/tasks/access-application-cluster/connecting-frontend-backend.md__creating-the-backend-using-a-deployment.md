---
id: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-backend-using-a-deployment
kind: section
title: Creating the backend using a Deployment
source: tasks/access-application-cluster/connecting-frontend-backend.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/connecting-frontend-backend/
heading: Creating the backend using a Deployment
parent: okf-structure/tasks/access-application-cluster/connecting-frontend-backend
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#prerequisites
next_sibling: okf-structure/tasks/access-application-cluster/connecting-frontend-backend.md#creating-the-hello-service-object
word_count: 132
---

The backend is a simple hello greeter microservice. Here is the configuration
file for the backend Deployment:

Create the backend Deployment:

```shell
kubectl apply -f https://k8s.io/examples/service/access/backend-deployment.yaml
```

View information about the backend Deployment:

```shell
kubectl describe deployment backend
```

The output is similar to this:

```
Name:                           backend
Namespace:                      default
CreationTimestamp:              Mon, 24 Oct 2016 14:21:02 -0700
Labels:                         app=hello
                                tier=backend
                                track=stable
Annotations:                    deployment.kubernetes.io/revision=1
Selector:                       app=hello,tier=backend,track=stable
Replicas:                       3 desired | 3 updated | 3 total | 3 available | 0 unavailable
StrategyType:                   RollingUpdate
MinReadySeconds:                0
RollingUpdateStrategy:          1 max unavailable, 1 max surge
Pod Template:
  Labels:       app=hello
                tier=backend
                track=stable
  Containers:
   hello:
    Image:              "gcr.io/google-samples/hello-go-gke:1.0"
    Port:               80/TCP
    Environment:        <none>
    Mounts:             <none>
  Volumes:              <none>
Conditions:
  Type          Status  Reason
  ----          ------  ------
  Available     True    MinimumReplicasAvailable
  Progressing   True    NewReplicaSetAvailable
OldReplicaSets:                 <none>
NewReplicaSet:                  hello-3621623197 (3/3 replicas created)
Events:
...
```
