---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-besteffort
kind: section
title: Create a Pod that gets assigned a QoS class of BestEffort
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: Create a Pod that gets assigned a QoS class of BestEffort
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-burstable
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-has-two-containers
word_count: 109
---

For a Pod to be given a QoS class of `BestEffort`, the Containers in the Pod must not
have any memory or CPU limits or requests.

Here is a manifest for a Pod that has one Container. The Container has no memory or CPU
limits or requests:

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod-3.yaml --namespace=qos-example
```

View detailed information about the Pod:

```shell
kubectl get pod qos-demo-3 --namespace=qos-example --output=yaml
```

The output shows that Kubernetes gave the Pod a QoS class of `BestEffort`:

```yaml
spec:
  containers:
    ...
    resources: {}
  ...
status:
  qosClass: BestEffort
```

#### Clean up {#clean-up-besteffort}

Delete your Pod:

```shell
kubectl delete pod qos-demo-3 --namespace=qos-example
```
