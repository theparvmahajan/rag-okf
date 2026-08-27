---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-guaranteed
kind: section
title: Create a Pod that gets assigned a QoS class of Guaranteed
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: Create a Pod that gets assigned a QoS class of Guaranteed
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-namespace
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-burstable
word_count: 283
---

For a Pod to be given a QoS class of `Guaranteed`:

* Every Container in the Pod must have a memory limit and a memory request.
* For every Container in the Pod, the memory limit must equal the memory request.
* Every Container in the Pod must have a CPU limit and a CPU request.
* For every Container in the Pod, the CPU limit must equal the CPU request.

These restrictions apply to init containers and app containers equally.
Ephemeral containers
cannot define resources so these restrictions do not apply.

Here is a manifest for a Pod that has one Container. The Container has a memory limit and a
memory request, both equal to 200 MiB. The Container has a CPU limit and a CPU request, both equal to 700 milliCPU:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod.yaml --namespace=qos-example
```

View detailed information about the Pod:

```shell
kubectl get pod qos-demo --namespace=qos-example --output=yaml
```

The output shows that Kubernetes gave the Pod a QoS class of `Guaranteed`. The output also
verifies that the Pod Container has a memory request that matches its memory limit, and it has
a CPU request that matches its CPU limit.

```yaml
spec:
  containers:
    ...
    resources:
      limits:
        cpu: 700m
        memory: 200Mi
      requests:
        cpu: 700m
        memory: 200Mi
    ...
status:
  qosClass: Guaranteed
```

If a Container specifies its own memory limit, but does not specify a memory request, Kubernetes
automatically assigns a memory request that matches the limit. Similarly, if a Container specifies its own
CPU limit, but does not specify a CPU request, Kubernetes automatically assigns a CPU request that matches
the limit.

#### Clean up {#clean-up-guaranteed}

Delete your Pod:

```shell
kubectl delete pod qos-demo --namespace=qos-example
```
