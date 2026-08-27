---
id: okf-structure/tasks/administer-cluster/node-overprovisioning.md#set-the-desired-replica-count
kind: section
title: Set the desired replica count
source: tasks/administer-cluster/node-overprovisioning.md
url: https://kubernetes.io/docs/tasks/administer-cluster/node-overprovisioning/
heading: Set the desired replica count
parent: okf-structure/tasks/administer-cluster/node-overprovisioning
children: []
prev_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#adjust-placeholder-resource-requests
next_sibling: okf-structure/tasks/administer-cluster/node-overprovisioning.md#whatsnext
word_count: 149
---

### Calculate the total reserved resources

For example, with 5 replicas each reserving 0.1 CPU and 200MiB of memory:  
Total CPU reserved: 5 × 0.1 = 0.5 (in the Pod specification, you'll write the quantity `500m`)  
Total memory reserved: 5 × 200MiB = 1GiB (in the Pod specification, you'll write `1 Gi`)  

To scale the Deployment, adjust the number of replicas based on your cluster's size and expected workload:

```shell
kubectl scale deployment capacity-reservation --replicas=5
```

Verify the scaling:

```shell
kubectl get deployment capacity-reservation
```

The output should reflect the updated number of replicas:

```none
NAME                   READY   UP-TO-DATE   AVAILABLE   AGE
capacity-reservation   5/5     5            5           2m
```

Some autoscalers, notably Karpenter,
treat preferred affinity rules as hard rules when considering node scaling.
If you use Karpenter or another node autoscaler that uses the same heuristic,
the replica count you set here  also sets a minimum node count for your cluster.
