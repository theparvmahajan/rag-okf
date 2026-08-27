---
id: okf-structure/concepts/workloads/controllers/replicaset.md#working-with-replicasets
kind: section
title: Working with ReplicaSets
source: concepts/workloads/controllers/replicaset.md
url: https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/
heading: Working with ReplicaSets
parent: okf-structure/concepts/workloads/controllers/replicaset
children: []
prev_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#writing-a-replicaset-manifest
next_sibling: okf-structure/concepts/workloads/controllers/replicaset.md#alternatives-to-replicaset
word_count: 819
---

### Deleting a ReplicaSet and its Pods

To delete a ReplicaSet and all of its Pods, use
`kubectl delete`. The
Garbage collector automatically deletes all of
the dependent Pods by default.

When using the REST API or the `client-go` library, you must set `propagationPolicy` to
`Background` or `Foreground` in the `-d` option. For example:

```shell
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Foreground"}' \
  -H "Content-Type: application/json"
```

### Deleting just a ReplicaSet

You can delete a ReplicaSet without affecting any of its Pods using
`kubectl delete`
with the `--cascade=orphan` option.
When using the REST API or the `client-go` library, you must set `propagationPolicy` to `Orphan`.
For example:

```shell
kubectl proxy --port=8080
curl -X DELETE  'localhost:8080/apis/apps/v1/namespaces/default/replicasets/frontend' \
  -d '{"kind":"DeleteOptions","apiVersion":"v1","propagationPolicy":"Orphan"}' \
  -H "Content-Type: application/json"
```

Once the original is deleted, you can create a new ReplicaSet to replace it. As long
as the old and new `.spec.selector` are the same, then the new one will adopt the old Pods.
However, it will not make any effort to make existing Pods match a new, different pod template.
To update Pods to a new spec in a controlled way, use a
Deployment, as
ReplicaSets do not support a rolling update directly.

### Terminating Pods

You can enable this feature by setting the `DeploymentReplicaSetTerminatingReplicas`
feature gate
on the API server
and on the kube-controller-manager

Pods that become terminating due to deletion or scale down may take a long time to terminate, and may consume
additional resources during that period. As a result, the total number of all pods can temporarily exceed
`.spec.replicas`. Terminating pods can be tracked using the `.status.terminatingReplicas` field of the ReplicaSet.

### Isolating Pods from a ReplicaSet

You can remove Pods from a ReplicaSet by changing their labels. This technique may be used to remove Pods
from service for debugging, data recovery, etc. Pods that are removed in this way will be replaced automatically (
assuming that the number of replicas is not also changed).

### Scaling a ReplicaSet

A ReplicaSet can be easily scaled up or down by simply updating the `.spec.replicas` field. The ReplicaSet controller
ensures that a desired number of Pods with a matching label selector are available and operational.

When scaling down, the ReplicaSet controller chooses which pods to delete by sorting the available pods to
prioritize scaling down pods based on the following general algorithm:

1. Pending (and unschedulable) pods are scaled down first
1. If `controller.kubernetes.io/pod-deletion-cost` annotation is set, then
   the pod with the lower value will come first.
1. Pods on nodes with more replicas come before pods on nodes with fewer replicas.
1. If the pods' creation times differ, the pod that was created more recently
   comes before the older pod (the creation times are bucketed on an integer log scale).

If all of the above match, then selection is random.

### Pod deletion cost

Using the `controller.kubernetes.io/pod-deletion-cost`
annotation, users can set a preference regarding which pods to remove first when downscaling a ReplicaSet.

The annotation should be set on the pod, the range is [-2147483648, 2147483647]. It represents the cost of
deleting a pod compared to other pods belonging to the same ReplicaSet. Pods with lower deletion
cost are preferred to be deleted before pods with higher deletion cost.

The implicit value for this annotation for pods that don't set it is 0; negative values are permitted.
Invalid values will be rejected by the API server.

This feature is beta and enabled by default. You can disable it using the
feature gate
`PodDeletionCost` in both kube-apiserver and kube-controller-manager.

- This is honored on a best-effort basis, so it does not offer any guarantees on pod deletion order.
- Users should avoid updating the annotation frequently, such as updating it based on a metric value,
  because doing so will generate a significant number of pod updates on the apiserver.
  

#### Example Use Case

The different pods of an application could have different utilization levels. On scale down, the application
may prefer to remove the pods with lower utilization. To avoid frequently updating the pods, the application
should update `controller.kubernetes.io/pod-deletion-cost` once before issuing a scale down (setting the
annotation to a value proportional to pod utilization level). This works if the application itself controls
the down scaling; for example, the driver pod of a Spark deployment.

### ReplicaSet as a Horizontal Pod Autoscaler Target

A ReplicaSet can also be a target for
Horizontal Pod Autoscalers (HPA). That is,
a ReplicaSet can be auto-scaled by an HPA. Here is an example HPA targeting
the ReplicaSet we created in the previous example.

Saving this manifest into `hpa-rs.yaml` and submitting it to a Kubernetes cluster should
create the defined HPA that autoscales the target ReplicaSet depending on the CPU usage
of the replicated Pods.

```shell
kubectl apply -f https://k8s.io/examples/controllers/hpa-rs.yaml
```

Alternatively, you can use the `kubectl autoscale` command to accomplish the same
(and it's easier!)

```shell
kubectl autoscale rs frontend --max=10 --min=3 --cpu=50%
```
