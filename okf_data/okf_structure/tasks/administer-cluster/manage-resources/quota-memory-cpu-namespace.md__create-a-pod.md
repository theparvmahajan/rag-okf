---
id: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#create-a-pod
kind: section
title: Create a Pod
source: tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md
url: https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/
heading: Create a Pod
parent: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace
children: []
prev_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#create-a-resourcequota
next_sibling: okf-structure/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace.md#attempt-to-create-a-second-pod
word_count: 149
---

Here is a manifest for an example Pod:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/admin/resource/quota-mem-cpu-pod.yaml --namespace=quota-mem-cpu-example
```

Verify that the Pod is running and that its (only) container is healthy:

```shell
kubectl get pod quota-mem-cpu-demo --namespace=quota-mem-cpu-example
```

Once again, view detailed information about the ResourceQuota:

```shell
kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example --output=yaml
```

The output shows the quota along with how much of the quota has been used.
You can see that the memory and CPU requests and limits for your Pod do not
exceed the quota.

```
status:
  hard:
    limits.cpu: "2"
    limits.memory: 2Gi
    requests.cpu: "1"
    requests.memory: 1Gi
  used:
    limits.cpu: 800m
    limits.memory: 800Mi
    requests.cpu: 400m
    requests.memory: 600Mi
```

If you have the `jq` tool, you can also query (using JSONPath)
for just the `used` values, **and** pretty-print that that of the output. For example:

```shell
kubectl get resourcequota mem-cpu-demo --namespace=quota-mem-cpu-example -o jsonpath='{ .status.used }' | jq .
```
