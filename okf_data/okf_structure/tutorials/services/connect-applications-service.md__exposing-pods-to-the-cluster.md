---
id: okf-structure/tutorials/services/connect-applications-service.md#exposing-pods-to-the-cluster
kind: section
title: Exposing pods to the cluster
source: tutorials/services/connect-applications-service.md
url: https://kubernetes.io/docs/tutorials/services/connect-applications-service/
heading: Exposing pods to the cluster
parent: okf-structure/tutorials/services/connect-applications-service
children: []
prev_sibling: okf-structure/tutorials/services/connect-applications-service.md#the-kubernetes-model-for-connecting-containers
next_sibling: okf-structure/tutorials/services/connect-applications-service.md#creating-a-service
word_count: 237
---

We did this in a previous example, but let's do it once again and focus on the networking perspective.
Create an nginx Pod, and note that it has a container port specification:

This makes it accessible from any node in your cluster. Check the nodes the Pod is running on:

```shell
kubectl apply -f ./run-my-nginx.yaml
kubectl get pods -l run=my-nginx -o wide
```
```
NAME                        READY     STATUS    RESTARTS   AGE       IP            NODE
my-nginx-3800858182-jr4a2   1/1       Running   0          13s       10.244.3.4    kubernetes-minion-905m
my-nginx-3800858182-kna2y   1/1       Running   0          13s       10.244.2.5    kubernetes-minion-ljyd
```

Check your pods' IPs:

```shell
kubectl get pods -l run=my-nginx -o custom-columns=POD_IP:.status.podIPs
    POD_IP
    [map[ip:10.244.3.4]]
    [map[ip:10.244.2.5]]
```

You should be able to ssh into any node in your cluster and use a tool such as `curl`
to make queries against both IPs. Note that the containers are *not* using port 80 on
the node, nor are there any special NAT rules to route traffic to the pod. This means
you can run multiple nginx pods on the same node all using the same `containerPort`,
and access them from any other pod or node in your cluster using the assigned IP
address for the pod. If you want to arrange for a specific port on the host
Node to be forwarded to backing Pods, you can - but the networking model should
mean that you do not need to do so.

You can read more about the
Kubernetes Networking Model
if you're curious.
