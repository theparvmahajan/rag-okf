---
id: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-clusterip
kind: section
title: Source IP for Services with `Type=ClusterIP`
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: Source IP for Services with `Type=ClusterIP`
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: okf-structure/tutorials/services/source-ip.md#objectives
next_sibling: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-nodeport
word_count: 352
---

Packets sent to ClusterIP from within the cluster are never source NAT'd if
you're running kube-proxy in
iptables mode,
(the default). You can query the kube-proxy mode by fetching
`http://localhost:10249/proxyMode` on the node where kube-proxy is running.

```console
kubectl get nodes
```
The output is similar to this:
```
NAME                           STATUS     ROLES    AGE     VERSION
kubernetes-node-6jst   Ready      <none>   2h      v1.13.0
kubernetes-node-cx31   Ready      <none>   2h      v1.13.0
kubernetes-node-jj1t   Ready      <none>   2h      v1.13.0
```

Get the proxy mode on one of the nodes (kube-proxy listens on port 10249):
```shell
# Run this in a shell on the node you want to query.
curl http://localhost:10249/proxyMode
```
The output is:
```
iptables
```

You can test source IP preservation by creating a Service over the source IP app:

```shell
kubectl expose deployment source-ip-app --name=clusterip --port=80 --target-port=8080
```
The output is:
```
service/clusterip exposed
```
```shell
kubectl get svc clusterip
```
The output is similar to:
```
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
clusterip    ClusterIP   10.0.170.92   <none>        80/TCP    51s
```

And hitting the `ClusterIP` from a pod in the same cluster:

```shell
kubectl run busybox -it --image=busybox:1.28 --restart=Never --rm
```
The output is similar to this:
```
Waiting for pod default/busybox to be running, status is Pending, pod ready: false
If you don't see a command prompt, try pressing enter.

```
You can then run a command inside that Pod:

```shell
# Run this inside the terminal from "kubectl run"
ip addr
```
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc noqueue
    link/ether 0a:58:0a:f4:03:08 brd ff:ff:ff:ff:ff:ff
    inet 10.244.3.8/24 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::188a:84ff:feb0:26a5/64 scope link
       valid_lft forever preferred_lft forever
```

…then use `wget` to query the local webserver
```shell
# Replace "10.0.170.92" with the IPv4 address of the Service named "clusterip"
wget -qO - 10.0.170.92
```
```
CLIENT VALUES:
client_address=10.244.3.8
command=GET
...
```
The `client_address` is always the client pod's IP address, whether the client pod and server pod are in the same node or in different nodes.
