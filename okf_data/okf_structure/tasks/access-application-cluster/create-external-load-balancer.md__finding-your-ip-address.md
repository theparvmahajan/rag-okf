---
id: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#finding-your-ip-address
kind: section
title: Finding your IP address
source: tasks/access-application-cluster/create-external-load-balancer.md
url: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
heading: Finding your IP address
parent: okf-structure/tasks/access-application-cluster/create-external-load-balancer
children: []
prev_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#create-a-service
next_sibling: okf-structure/tasks/access-application-cluster/create-external-load-balancer.md#preserving-the-client-source-ip
word_count: 107
---

You can find the IP address created for your service by getting the service
information through `kubectl`:

```bash
kubectl describe services example-service
```

which should produce output similar to:

```
Name:                     example-service
Namespace:                default
Labels:                   app=example
Annotations:              <none>
Selector:                 app=example
Type:                     LoadBalancer
IP Families:              <none>
IP:                       10.3.22.96
IPs:                      10.3.22.96
LoadBalancer Ingress:     192.0.2.89
Port:                     <unset>  8765/TCP
TargetPort:               9376/TCP
NodePort:                 <unset>  30593/TCP
Endpoints:                172.17.0.3:9376
Session Affinity:         None
External Traffic Policy:  Cluster
Events:                   <none>
```

The load balancer's IP address is listed next to `LoadBalancer Ingress`.

If you are running your service on Minikube, you can find the assigned IP address and port with:

```bash
minikube service example-service --url
```
