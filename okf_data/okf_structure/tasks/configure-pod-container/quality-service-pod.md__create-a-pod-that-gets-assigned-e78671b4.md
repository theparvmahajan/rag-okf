---
id: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-burstable
kind: section
title: Create a Pod that gets assigned a QoS class of Burstable
source: tasks/configure-pod-container/quality-service-pod.md
url: https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/
heading: Create a Pod that gets assigned a QoS class of Burstable
parent: okf-structure/tasks/configure-pod-container/quality-service-pod
children: []
prev_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-guaranteed
next_sibling: okf-structure/tasks/configure-pod-container/quality-service-pod.md#create-a-pod-that-gets-assigned-a-qos-class-of-besteffort
word_count: 138
---

A Pod is given a QoS class of `Burstable` if:

* The Pod does not meet the criteria for QoS class `Guaranteed`.
* At least one Container in the Pod has a memory or CPU request or limit.

Here is a manifest for a Pod that has one Container. The Container has a memory limit of 200 MiB
and a memory request of 100 MiB.

Create the Pod:

```shell
kubectl apply -f https://k8s.io/examples/pods/qos/qos-pod-2.yaml --namespace=qos-example
```

View detailed information about the Pod:

```shell
kubectl get pod qos-demo-2 --namespace=qos-example --output=yaml
```

The output shows that Kubernetes gave the Pod a QoS class of `Burstable`:

```yaml
spec:
  containers:
  - image: nginx
    imagePullPolicy: Always
    name: qos-demo-2-ctr
    resources:
      limits:
        memory: 200Mi
      requests:
        memory: 100Mi
  ...
status:
  qosClass: Burstable
```

#### Clean up {#clean-up-burstable}

Delete your Pod:

```shell
kubectl delete pod qos-demo-2 --namespace=qos-example
```
