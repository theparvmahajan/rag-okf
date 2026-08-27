---
id: okf-structure/concepts/cluster-administration/swap-memory-management.md#observability-for-swap-use
kind: section
title: Observability for swap use
source: concepts/cluster-administration/swap-memory-management.md
url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
heading: Observability for swap use
parent: okf-structure/concepts/cluster-administration/swap-memory-management
children: []
prev_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#how-does-it-work
next_sibling: okf-structure/concepts/cluster-administration/swap-memory-management.md#risks-and-caveats
word_count: 518
---

### Node and container level metric statistics

Kubelet now collects node and container level metric statistics,
which can be accessed at the `/metrics/resource` (which is used mainly by monitoring
tools like Prometheus) and `/stats/summary` (which is used mainly by Autoscalers) kubelet HTTP endpoints.
This allows clients who can directly request the kubelet to
monitor swap usage and remaining swap memory when using `LimitedSwap`.
Additionally, a `machine_swap_bytes` metric has been added to cadvisor to show
the total physical swap capacity of the machine.
See this page for more info.

For example, these `/metrics/resource` are supported:
- `node_swap_usage_bytes`: Current swap usage of the node in bytes.
- `container_swap_usage_bytes`: Current amount of the container swap usage in bytes.
- `container_swap_limit_bytes`: Current amount of the container swap limit in bytes.

### Using `kubectl top --show-swap`

Querying metrics is valuable, but somewhat cumbersome, as these metrics
are designed to be used by software rather than humans.
In order to consume this data in a more user-friendly way,
the `kubectl top` command has been extended to support swap metrics, using the `--show-swap` flag.

In order to receive information about swap usage on nodes, `kubectl top nodes --show-swap` can be used:
```shell
kubectl top nodes --show-swap
```

This will result in an output similar to:
```
NAME    CPU(cores)   CPU(%)   MEMORY(bytes)   MEMORY(%)   SWAP(bytes)    SWAP(%)       
node1   1m           10%      2Mi             10%         1Mi            0%   
node2   5m           10%      6Mi             10%         2Mi            0%   
node3   3m           10%      4Mi             10%         <unknown>      <unknown>   
```

In order to receive information about swap usage by pods, `kubectl top pods --show-swap` can be used:
```shell
kubectl top pod -n kube-system --show-swap
```

This will result in an output similar to:
```
NAME                                      CPU(cores)   MEMORY(bytes)   SWAP(bytes)
coredns-58d5bc5cdb-5nbk4                  2m           19Mi            0Mi
coredns-58d5bc5cdb-jsh26                  3m           37Mi            0Mi
etcd-node01                               51m          143Mi           5Mi
kube-apiserver-node01                     98m          824Mi           16Mi
kube-controller-manager-node01            20m          135Mi           9Mi
kube-proxy-ffgs2                          1m           24Mi            0Mi
kube-proxy-fhvwx                          1m           39Mi            0Mi
kube-scheduler-node01                     13m          69Mi            0Mi
metrics-server-8598789fdb-d2kcj           5m           26Mi            0Mi   
```

### Nodes to report swap capacity as part of node status

A new node status field is now added, `node.status.nodeInfo.swap.capacity`, to report the swap capacity of a node.

As an example, the following command can be used to retrieve the swap capacity of the nodes in a cluster:
```shell
kubectl get nodes -o go-template='{{range .items}}{{.metadata.name}}: {{if .status.nodeInfo.swap.capacity}}{{.status.nodeInfo.swap.capacity}}{{else}}<unknown>{{end}}{{"\n"}}{{end}}'
```

This will result in an output similar to:
```
node1: 21474836480
node2: 42949664768
node3: <unknown>
```

The `<unknown>` value indicates that the `.status.nodeInfo.swap.capacity` field is not set for that Node.
This probably means that the node does not have swap provisioned, or less likely,
that the kubelet is not able to determine the swap capacity of the node.

### Swap discovery using Node Feature Discovery (NFD) {#node-feature-discovery}

Node Feature Discovery
is a Kubernetes addon for detecting hardware features and configuration.
It can be utilized to discover which nodes are provisioned with swap.

As an example, to figure out which nodes are provisioned with swap,
use the following command:
```shell
kubectl get nodes -o jsonpath='{range .items[?(@.metadata.labels.feature\.node\.kubernetes\.io/memory-swap)]}{.metadata.name}{"\t"}{.metadata.labels.feature\.node\.kubernetes\.io/memory-swap}{"\n"}{end}'
```

This will result in an output similar to:
```
k8s-worker1: true
k8s-worker2: true
k8s-worker3: false
```

In this example, swap is provisioned on nodes `k8s-worker1` and `k8s-worker2`, but not on `k8s-worker3`.
