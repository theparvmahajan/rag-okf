---
id: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#use-kompose
kind: section
title: Use Kompose
source: tasks/configure-pod-container/translate-compose-kubernetes.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/translate-compose-kubernetes/
heading: Use Kompose
parent: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#install-kompose
next_sibling: okf-structure/tasks/configure-pod-container/translate-compose-kubernetes.md#user-guide
word_count: 309
---

In a few steps, we'll take you from Docker Compose to Kubernetes. All
you need is an existing `docker-compose.yml` file.

1. Go to the directory containing your `docker-compose.yml` file. If you don't have one, test using this one.

   ```yaml

   services:

     redis-leader:
       container_name: redis-leader
       image: redis
       ports:
         - "6379"

     redis-replica:
       container_name: redis-replica
       image: redis
       ports:
         - "6379"
       command: redis-server --replicaof redis-leader 6379 --dir /tmp

     web:
       container_name: web
       image: quay.io/kompose/web
       ports:
         - "8080:8080"
       environment:
         - GET_HOSTS_FROM=dns
       labels:
         kompose.service.type: LoadBalancer
   ```

2. To convert the `docker-compose.yml` file to files that you can use with
   `kubectl`, run `kompose convert` and then `kubectl apply -f <output file>`.

   ```bash
   kompose convert
   ```

   The output is similar to:

   ```none
   INFO Kubernetes file "redis-leader-service.yaml" created
   INFO Kubernetes file "redis-replica-service.yaml" created
   INFO Kubernetes file "web-tcp-service.yaml" created
   INFO Kubernetes file "redis-leader-deployment.yaml" created
   INFO Kubernetes file "redis-replica-deployment.yaml" created
   INFO Kubernetes file "web-deployment.yaml" created
   ```

   ```bash
    kubectl apply -f web-tcp-service.yaml,redis-leader-service.yaml,redis-replica-service.yaml,web-deployment.yaml,redis-leader-deployment.yaml,redis-replica-deployment.yaml
   ```

   The output is similar to:

   ```none
   deployment.apps/redis-leader created
   deployment.apps/redis-replica created
   deployment.apps/web created
   service/redis-leader created
   service/redis-replica created
   service/web-tcp created
   ```

    Your deployments are running in Kubernetes.

3. Access your application.

   If you're already using `minikube` for your development process:

   ```bash
   minikube service web-tcp
   ```

   Otherwise, let's look up what IP your service is using!

   ```sh
   kubectl describe svc web-tcp
   ```

   ```none
    Name:                     web-tcp
    Namespace:                default
    Labels:                   io.kompose.service=web-tcp
    Annotations:              kompose.cmd: kompose convert
                              kompose.service.type: LoadBalancer
                              kompose.version: 1.33.0 (3ce457399)
    Selector:                 io.kompose.service=web
    Type:                     LoadBalancer
    IP Family Policy:         SingleStack
    IP Families:              IPv4
    IP:                       10.102.30.3
    IPs:                      10.102.30.3
    Port:                     8080  8080/TCP
    TargetPort:               8080/TCP
    NodePort:                 8080  31624/TCP
    Endpoints:                10.244.0.5:8080
    Session Affinity:         None
    External Traffic Policy:  Cluster
    Events:                   <none>
   ```

   If you're using a cloud provider, your IP will be listed next to `LoadBalancer Ingress`.

   ```sh
   curl http://192.0.2.89
   ```
   
4. Clean-up.

   After you are finished testing out the example application deployment, simply run the following command in your shell to delete the
   resources used.
   
   ```sh
   kubectl delete -f web-tcp-service.yaml,redis-leader-service.yaml,redis-replica-service.yaml,web-deployment.yaml,redis-leader-deployment.yaml,redis-replica-deployment.yaml
   ```
