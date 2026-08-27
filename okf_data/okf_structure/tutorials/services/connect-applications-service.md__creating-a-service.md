---
id: okf-structure/tutorials/services/connect-applications-service.md#creating-a-service
kind: section
title: Creating a Service
source: tutorials/services/connect-applications-service.md
url: https://kubernetes.io/docs/tutorials/services/connect-applications-service/
heading: Creating a Service
parent: okf-structure/tutorials/services/connect-applications-service
children: []
prev_sibling: okf-structure/tutorials/services/connect-applications-service.md#exposing-pods-to-the-cluster
next_sibling: okf-structure/tutorials/services/connect-applications-service.md#accessing-the-service
word_count: 468
---

So we have pods running nginx in a flat, cluster wide, address space. In theory,
you could talk to these pods directly, but what happens when a node dies? The pods
die with it, and the ReplicaSet inside the Deployment will create new ones, with different IPs. This is
the problem a Service solves.

A Kubernetes Service is an abstraction which defines a logical set of Pods running
somewhere in your cluster, that all provide the same functionality. When created,
each Service is assigned a unique IP address (also called clusterIP). This address
is tied to the lifespan of the Service, and will not change while the Service is alive.
Pods can be configured to talk to the Service, and know that communication to the
Service will be automatically load-balanced out to some pod that is a member of the Service.

You can create a Service for your 2 nginx replicas with `kubectl expose`:

```shell
kubectl expose deployment/my-nginx
```
```
service/my-nginx exposed
```

This is equivalent to `kubectl apply -f` in the following yaml:

This specification will create a Service which targets TCP port 80 on any Pod
with the `run: my-nginx` label, and expose it on an abstracted Service port
(`targetPort`: is the port the container accepts traffic on, `port`: is the
abstracted Service port, which can be any port other pods use to access the
Service).
View Service
API object to see the list of supported fields in service definition.
Check your Service:

```shell
kubectl get svc my-nginx
```
```
NAME       TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)   AGE
my-nginx   ClusterIP   10.0.162.149   <none>        80/TCP    21s
```

As mentioned previously, a Service is backed by a group of Pods. These Pods are
exposed through
EndpointSlices.
The Service's selector will be evaluated continuously and the results will be POSTed
to an EndpointSlice that is connected to the Service using
labels.
When a Pod dies, it is automatically removed from the EndpointSlices that contain it 
as an endpoint. New Pods that match the Service's selector will automatically get added
to an EndpointSlice for that Service.
Check the endpoints, and note that the IPs are the same as the Pods created in
the first step:

```shell
kubectl describe svc my-nginx
```
```
Name:                my-nginx
Namespace:           default
Labels:              run=my-nginx
Annotations:         <none>
Selector:            run=my-nginx
Type:                ClusterIP
IP Family Policy:    SingleStack
IP Families:         IPv4
IP:                  10.0.162.149
IPs:                 10.0.162.149
Port:                <unset> 80/TCP
TargetPort:          80/TCP
Endpoints:           10.244.2.5:80,10.244.3.4:80
Session Affinity:    None
Events:              <none>
```
```shell
kubectl get endpointslices -l kubernetes.io/service-name=my-nginx
```
```
NAME             ADDRESSTYPE   PORTS   ENDPOINTS               AGE
my-nginx-7vzhx   IPv4          80      10.244.2.5,10.244.3.4   21s
```

You should now be able to curl the nginx Service on `<CLUSTER-IP>:<PORT>` from
any node in your cluster. Note that the Service IP is completely virtual, it
never hits the wire. If you're curious about how this works you can read more
about the service proxy.
