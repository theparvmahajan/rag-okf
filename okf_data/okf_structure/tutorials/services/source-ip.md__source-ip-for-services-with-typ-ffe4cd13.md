---
id: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-loadbalancer
kind: section
title: Source IP for Services with `Type=LoadBalancer`
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: Source IP for Services with `Type=LoadBalancer`
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-nodeport
next_sibling: okf-structure/tutorials/services/source-ip.md#cross-platform-support
word_count: 422
---

Packets sent to Services with
`Type=LoadBalancer`
are source NAT'd by default, because all schedulable Kubernetes nodes in the
`Ready` state are eligible for load-balanced traffic. So if packets arrive
at a node without an endpoint, the system proxies it to a node *with* an
endpoint, replacing the source IP on the packet with the IP of the node (as
described in the previous section).

You can test this by exposing the source-ip-app through a load balancer:

```shell
kubectl expose deployment source-ip-app --name=loadbalancer --port=80 --target-port=8080 --type=LoadBalancer
```
The output is:
```
service/loadbalancer exposed
```

Print out the IP addresses of the Service:
```console
kubectl get svc loadbalancer
```
The output is similar to this:
```
NAME           TYPE           CLUSTER-IP    EXTERNAL-IP       PORT(S)   AGE
loadbalancer   LoadBalancer   10.0.65.118   203.0.113.140     80/TCP    5m
```

Next, send a request to this Service's external-ip:

```shell
curl 203.0.113.140
```
The output is similar to this:
```
CLIENT VALUES:
client_address=10.240.0.5
...
```

However, if you're running on Google Kubernetes Engine/GCE, setting the same `service.spec.externalTrafficPolicy`
field to `Local` forces nodes *without* Service endpoints to remove
themselves from the list of nodes eligible for loadbalanced traffic by
deliberately failing health checks.

Visually:

Source IP with externalTrafficPolicy

You can test this by setting the annotation:

```shell
kubectl patch svc loadbalancer -p '{"spec":{"externalTrafficPolicy":"Local"}}'
```

You should immediately see the `service.spec.healthCheckNodePort` field allocated
by Kubernetes:

```shell
kubectl get svc loadbalancer -o yaml | grep -i healthCheckNodePort
```
The output is similar to this:
```yaml
  healthCheckNodePort: 32122
```

The `service.spec.healthCheckNodePort` field points to a port on every node
serving the health check at `/healthz`. You can test this:

```shell
kubectl get pod -o wide -l app=source-ip-app
```
The output is similar to this:
```
NAME                            READY     STATUS    RESTARTS   AGE       IP             NODE
source-ip-app-826191075-qehz4   1/1       Running   0          20h       10.180.1.136   kubernetes-node-6jst
```

Use `curl` to fetch the `/healthz` endpoint on various nodes:
```shell
# Run this locally on a node you choose
curl localhost:32122/healthz
```
```
1 Service Endpoints found
```

On a different node you might get a different result:
```shell
# Run this locally on a node you choose
curl localhost:32122/healthz
```
```
No Service Endpoints Found
```

A controller running on the
control plane is
responsible for allocating the cloud load balancer. The same controller also
allocates HTTP health checks pointing to this port/path on each node. Wait
about 10 seconds for the 2 nodes without endpoints to fail health checks,
then use `curl` to query the IPv4 address of the load balancer:

```shell
curl 203.0.113.140
```
The output is similar to this:
```
CLIENT VALUES:
client_address=198.51.100.79
...
```
