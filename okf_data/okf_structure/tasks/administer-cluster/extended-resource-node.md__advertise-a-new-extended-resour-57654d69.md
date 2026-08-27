---
id: okf-structure/tasks/administer-cluster/extended-resource-node.md#advertise-a-new-extended-resource-on-one-of-your-nodes
kind: section
title: Advertise a new extended resource on one of your Nodes
source: tasks/administer-cluster/extended-resource-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/
heading: Advertise a new extended resource on one of your Nodes
parent: okf-structure/tasks/administer-cluster/extended-resource-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/extended-resource-node.md#get-the-names-of-your-nodes
next_sibling: okf-structure/tasks/administer-cluster/extended-resource-node.md#discussion
word_count: 259
---

To advertise a new extended resource on a Node, send an HTTP PATCH request to
the Kubernetes API server. For example, suppose one of your Nodes has four dongles
attached. Here's an example of a PATCH request that advertises four dongle resources
for your Node.

```
PATCH /api/v1/nodes/<your-node-name>/status HTTP/1.1
Accept: application/json
Content-Type: application/json-patch+json
Host: k8s-master:8080

[
  {
    "op": "add",
    "path": "/status/capacity/example.com~1dongle",
    "value": "4"
  }
]
```

Note that Kubernetes does not need to know what a dongle is or what a dongle is for.
The preceding PATCH request tells Kubernetes that your Node has four things that
you call dongles.

Start a proxy, so that you can easily send requests to the Kubernetes API server:

```shell
kubectl proxy
```

In another command window, send the HTTP PATCH request.
Replace `<your-node-name>` with the name of your Node:

```shell
curl --header "Content-Type: application/json-patch+json" \
  --request PATCH \
  --data '[{"op": "add", "path": "/status/capacity/example.com~1dongle", "value": "4"}]' \
  http://localhost:8001/api/v1/nodes/<your-node-name>/status
```

In the preceding request, `~1` is the encoding for the character / in
the patch path. The operation path value in JSON-Patch is interpreted as a
JSON-Pointer. For more details, see
IETF RFC 6901, section 3.

The output shows that the Node has a capacity of 4 dongles:

```
"capacity": {
  "cpu": "2",
  "memory": "2049008Ki",
  "example.com/dongle": "4",
```

Describe your Node:

```
kubectl describe node <your-node-name>
```

Once again, the output shows the dongle resource:

```yaml
Capacity:
  cpu: 2
  memory: 2049008Ki
  example.com/dongle: 4
```

Now, application developers can create Pods that request a certain
number of dongles. See
Assign Extended Resources to a Container.
