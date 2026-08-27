---
id: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-nodeport
kind: section
title: Source IP for Services with `Type=NodePort`
source: tutorials/services/source-ip.md
url: https://kubernetes.io/docs/tutorials/services/source-ip/
heading: Source IP for Services with `Type=NodePort`
parent: okf-structure/tutorials/services/source-ip
children: []
prev_sibling: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-clusterip
next_sibling: okf-structure/tutorials/services/source-ip.md#source-ip-for-services-with-type-loadbalancer
word_count: 395
---

Packets sent to Services with
`Type=NodePort`
are source NAT'd by default. You can test this by creating a `NodePort` Service:

```shell
kubectl expose deployment source-ip-app --name=nodeport --port=80 --target-port=8080 --type=NodePort
```
The output is:
```
service/nodeport exposed
```

```shell
NODEPORT=$(kubectl get -o jsonpath="{.spec.ports[0].nodePort}" services nodeport)
NODES=$(kubectl get nodes -o jsonpath='{ $.items[*].status.addresses[?(@.type=="InternalIP")].address }')
```

If you're running on a cloud provider, you may need to open up a firewall-rule
for the `nodes:nodeport` reported above.
Now you can try reaching the Service from outside the cluster through the node
port allocated above.

```shell
for node in $NODES; do curl -s $node:$NODEPORT | grep -i client_address; done
```
The output is similar to:
```
client_address=10.180.1.1
client_address=10.240.0.5
client_address=10.240.0.3
```

Note that these are not the correct client IPs, they're cluster internal IPs. This is what happens:

* Client sends packet to `node2:nodePort`
* `node2` replaces the source IP address (SNAT) in the packet with its own IP address
* `node2` replaces the destination IP on the packet with the pod IP
* packet is routed to node 1, and then to the endpoint
* the pod's reply is routed back to node2
* the pod's reply is sent back to the client

Visually:

To avoid this, Kubernetes has a feature to
preserve the client source IP.
If you set `service.spec.externalTrafficPolicy` to the value `Local`,
kube-proxy only proxies proxy requests to local endpoints, and does not
forward traffic to other nodes. This approach preserves the original
source IP address. If there are no local endpoints, packets sent to the
node are dropped, so you can rely on the correct source-ip in any packet
processing rules you might apply a packet that make it through to the
endpoint.

Set the `service.spec.externalTrafficPolicy` field as follows:

```shell
kubectl patch svc nodeport -p '{"spec":{"externalTrafficPolicy":"Local"}}'
```
The output is:
```
service/nodeport patched
```

Now, re-run the test:

```shell
for node in $NODES; do curl --connect-timeout 1 -s $node:$NODEPORT | grep -i client_address; done
```
The output is similar to:
```
client_address=198.51.100.79
```

Note that you only got one reply, with the *right* client IP, from the one node on which the endpoint pod
is running.

This is what happens:

* client sends packet to `node2:nodePort`, which doesn't have any endpoints
* packet is dropped
* client sends packet to `node1:nodePort`, which *does* have endpoints
* node1 routes packet to endpoint with the correct source IP

Visually:
