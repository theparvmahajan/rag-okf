---
id: okf-structure/tasks/run-application/run-stateless-application-deployment.md#creating-and-exploring-an-nginx-deployment
kind: section
title: Creating and exploring an nginx deployment
source: tasks/run-application/run-stateless-application-deployment.md
url: https://kubernetes.io/docs/tasks/run-application/run-stateless-application-deployment/
heading: Creating and exploring an nginx deployment
parent: okf-structure/tasks/run-application/run-stateless-application-deployment
children: []
prev_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#prerequisites
next_sibling: okf-structure/tasks/run-application/run-stateless-application-deployment.md#updating-the-deployment
word_count: 211
---

You can run an application by creating a Kubernetes Deployment object, and you
can describe a Deployment in a YAML file. For example, this YAML file describes
a Deployment that runs the nginx:1.14.2 Docker image:

1. Create a Deployment based on the YAML file:

   ```shell
   kubectl apply -f https://k8s.io/examples/application/deployment.yaml
   ```

1. Display information about the Deployment:

   ```shell
   kubectl describe deployment nginx-deployment
   ```

   The output is similar to this:

   ```
   Name:     nginx-deployment
   Namespace:    default
   CreationTimestamp:  Tue, 30 Aug 2016 18:11:37 -0700
   Labels:     app=nginx
   Annotations:    deployment.kubernetes.io/revision=1
   Selector:   app=nginx
   Replicas:   2 desired | 2 updated | 2 total | 2 available | 0 unavailable
   StrategyType:   RollingUpdate
   MinReadySeconds:  0
   RollingUpdateStrategy:  1 max unavailable, 1 max surge
   Pod Template:
     Labels:       app=nginx
     Containers:
       nginx:
       Image:              nginx:1.14.2
       Port:               80/TCP
       Environment:        <none>
       Mounts:             <none>
     Volumes:              <none>
   Conditions:
     Type          Status  Reason
     ----          ------  ------
     Available     True    MinimumReplicasAvailable
     Progressing   True    NewReplicaSetAvailable
   OldReplicaSets:   <none>
   NewReplicaSet:    nginx-deployment-1771418926 (2/2 replicas created)
   No events.
   ```

1. List the Pods created by the deployment:

   ```shell
   kubectl get pods -l app=nginx
   ```

   The output is similar to this:

   ```
   NAME                                READY     STATUS    RESTARTS   AGE
   nginx-deployment-1771418926-7o5ns   1/1       Running   0          16h
   nginx-deployment-1771418926-r18az   1/1       Running   0          16h
   ```

1. Display information about a Pod:

   ```shell
   kubectl describe pod <pod-name>
   ```

   where `<pod-name>` is the name of one of your Pods.
