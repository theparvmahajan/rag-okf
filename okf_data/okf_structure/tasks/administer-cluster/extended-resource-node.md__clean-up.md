---
id: okf-structure/tasks/administer-cluster/extended-resource-node.md#clean-up
kind: section
title: Clean up
source: tasks/administer-cluster/extended-resource-node.md
url: https://kubernetes.io/docs/tasks/administer-cluster/extended-resource-node/
heading: Clean up
parent: okf-structure/tasks/administer-cluster/extended-resource-node
children: []
prev_sibling: okf-structure/tasks/administer-cluster/extended-resource-node.md#discussion
next_sibling: okf-structure/tasks/administer-cluster/extended-resource-node.md#whatsnext
word_count: 108
---

Here is a PATCH request that removes the dongle advertisement from a Node.

```
PATCH /api/v1/nodes/<your-node-name>/status HTTP/1.1
Accept: application/json
Content-Type: application/json-patch+json
Host: k8s-master:8080

[
  {
    "op": "remove",
    "path": "/status/capacity/example.com~1dongle",
  }
]
```

Start a proxy, so that you can easily send requests to the Kubernetes API server:

```shell
kubectl proxy
```

In another command window, send the HTTP PATCH request.
Replace `<your-node-name>` with the name of your Node:

```shell
curl --header "Content-Type: application/json-patch+json" \
  --request PATCH \
  --data '[{"op": "remove", "path": "/status/capacity/example.com~1dongle"}]' \
  http://localhost:8001/api/v1/nodes/<your-node-name>/status
```

Verify that the dongle advertisement has been removed:

```
kubectl describe node <your-node-name> | grep dongle
```

(you should not see any output)
