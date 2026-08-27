---
id: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#tune-dns-autoscaling-parameters-tuning-autoscaling-parameters
kind: section
title: Tune DNS autoscaling parameters {#tuning-autoscaling-parameters}
source: tasks/administer-cluster/dns-horizontal-autoscaling.md
url: https://kubernetes.io/docs/tasks/administer-cluster/dns-horizontal-autoscaling/
heading: Tune DNS autoscaling parameters {#tuning-autoscaling-parameters}
parent: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling
children: []
prev_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#enable-dns-horizontal-autoscaling-enablng-dns-horizontal-autoscaling
next_sibling: okf-structure/tasks/administer-cluster/dns-horizontal-autoscaling.md#disable-dns-horizontal-autoscaling
word_count: 138
---

Verify that the kube-dns-autoscaler ConfigMap exists:

```shell
kubectl get configmap --namespace=kube-system
```

The output is similar to this:

    NAME                  DATA      AGE
    ...
    kube-dns-autoscaler   1         ...
    ...

Modify the data in the ConfigMap:

```shell
kubectl edit configmap kube-dns-autoscaler --namespace=kube-system
```

Look for this line:

```yaml
linear: '{"coresPerReplica":256,"min":1,"nodesPerReplica":16}'
```

Modify the fields according to your needs. The "min" field indicates the
minimal number of DNS backends. The actual number of backends is
calculated using this equation:

    replicas = max( ceil( cores × 1/coresPerReplica ) , ceil( nodes × 1/nodesPerReplica ) )

Note that the values of both `coresPerReplica` and `nodesPerReplica` are
floats.

The idea is that when a cluster is using nodes that have many cores,
`coresPerReplica` dominates. When a cluster is using nodes that have fewer
cores, `nodesPerReplica` dominates.

There are other supported scaling patterns. For details, see
cluster-proportional-autoscaler.
