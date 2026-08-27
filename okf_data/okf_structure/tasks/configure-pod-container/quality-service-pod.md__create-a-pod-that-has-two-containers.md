---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-has-two-containers
kind: section
title: Create a Pod that has two Containers
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: Create a Pod that has two Containers
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-besteffort
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#retrieve-the-qos-class-for-a-pod
word_count: 119
---

Here is a manifest for a Pod that has two Containers. One container specifies a memory
request of 200 MiB. The other Container does not specify any requests or limits.

Notice that this Pod meets the criteria for QoS class `Burstable`. That is, it does not meet the
criteria for QoS class `Guaranteed`, and one of its Containers has a memory request.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod-4.yaml --namespace=qos-example
```

View detailed information about the Pod:

```shell
kubectl get pod qos-demo-4 --namespace=qos-example --output=yaml
```

The output shows that Kubernetes gave the Pod a QoS class of `Burstable`:

```yaml
spec:
  containers:
    ...
    name: qos-demo-4-ctr-1
    resources:
      requests:
        memory: 200Mi
    ...
    name: qos-demo-4-ctr-2
    resources: {}
    ...
status:
  qosClass: Burstable
```
