---
id: okf-structure/tutorials/stateless-application/guestbook.md#start-up-the-redis-database
kind: section
title: Start up the Redis Database
source: tutorials/stateless-application/guestbook.md
url: https://kubernetes.io/docs/tutorials/stateless-application/guestbook/
heading: Start up the Redis Database
parent: okf-structure/tutorials/stateless-application/guestbook
children: []
prev_sibling: okf-structure/tutorials/stateless-application/guestbook.md#prerequisites
next_sibling: okf-structure/tutorials/stateless-application/guestbook.md#set-up-and-expose-the-guestbook-frontend
word_count: 474
---

The guestbook application uses Redis to store its data.

### Creating the Redis Deployment

The manifest file, included below, specifies a Deployment controller that runs a single replica Redis Pod.

1. Launch a terminal window in the directory you downloaded the manifest files.
1. Apply the Redis Deployment from the `redis-leader-deployment.yaml` file:

   

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-deployment.yaml
   ```

1. Query the list of Pods to verify that the Redis Pod is running:

   ```shell
   kubectl get pods
   ```

   The response should be similar to this:

   ```
   NAME                           READY   STATUS    RESTARTS   AGE
   redis-leader-fb76b4755-xjr2n   1/1     Running   0          13s
   ```

1. Run the following command to view the logs from the Redis leader Pod:

   ```shell
   kubectl logs -f deployment/redis-leader
   ```

### Creating the Redis leader Service

The guestbook application needs to communicate to the Redis to write its data.
You need to apply a Service to
proxy the traffic to the Redis Pod. A Service defines a policy to access the
Pods.

1. Apply the Redis Service from the following `redis-leader-service.yaml` file:

   

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-leader-service.yaml
   ```

1. Query the list of Services to verify that the Redis Service is running:

   ```shell
   kubectl get service
   ```

   The response should be similar to this:

   ```
   NAME           TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
   kubernetes     ClusterIP   10.0.0.1     <none>        443/TCP    1m
   redis-leader   ClusterIP   10.103.78.24 <none>        6379/TCP   16s
   ```

This manifest file creates a Service named `redis-leader` with a set of labels
that match the labels previously defined, so the Service routes network
traffic to the Redis Pod.

### Set up Redis followers

Although the Redis leader is a single Pod, you can make it highly available
and meet traffic demands by adding a few Redis followers, or replicas.

1. Apply the Redis Deployment from the following `redis-follower-deployment.yaml` file:

   

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-deployment.yaml
   ```

1. Verify that the two Redis follower replicas are running by querying the list of Pods:

   ```shell
   kubectl get pods
   ```

   The response should be similar to this:

   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   redis-follower-dddfbdcc9-82sfr   1/1     Running   0          37s
   redis-follower-dddfbdcc9-qrt5k   1/1     Running   0          38s
   redis-leader-fb76b4755-xjr2n     1/1     Running   0          11m
   ```

### Creating the Redis follower service

The guestbook application needs to communicate with the Redis followers to
read data. To make the Redis followers discoverable, you must set up another
Service.

1. Apply the Redis Service from the following `redis-follower-service.yaml` file:

   

   ```shell
   kubectl apply -f https://k8s.io/examples/application/guestbook/redis-follower-service.yaml
   ```

1. Query the list of Services to verify that the Redis Service is running:

   ```shell
   kubectl get service
   ```

   The response should be similar to this:

   ```
   NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
   kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP    3d19h
   redis-follower   ClusterIP   10.110.162.42   <none>        6379/TCP   9s
   redis-leader     ClusterIP   10.103.78.24    <none>        6379/TCP   6m10s
   ```

This manifest file creates a Service named `redis-follower` with a set of
labels that match the labels previously defined, so the Service routes network
traffic to the Redis Pod.
